"""Commandes cliquables (`run_command`) des panneaux `sign` / `hanging_sign` d'un chunk lu par fl_nbt (fonctions pures, lecture seule ;
les blocs de commande, minecarts et panneaux sont les holders de count_outside).

    fl_signs.sign_commands(be, 'sign')                 # ([(étiquette, commande)], vus) : « sign[front,2] », « hanging_sign[back,0] »...
    fl_signs.sign_slots(be, 'sign')                    # emplacements des messages (pour la réécriture, fl_terrain_rw)
    fl_signs.message_events(msg)                       # (JSON décodé ou None, [(événement, clé de la commande)]) d'un message
    fl_signs.count_outside(root, tokens, holders)      # occurrences de chaque token hors des holders (livre, coffre, spawner...)

Le format n'est PAS choisi d'après la DataVersion (snapshots, DataVersion absente, outils externes) : on cherche les deux événements,
`click_event{action:"run_command", command:"..."}` (1.21.5+, composant NBT) et `clickEvent{action:"run_command", value:"..."}` (JSON), dans
tout composant (`extra`, `with`... : récursif), et toute chaîne qui commence par `{`, `[` ou `"` est essayée comme JSON (avant 1.21.5 un
message est une chaîne JSON). Emplacements : front_text / back_text `.messages[*]` (+ `filtered_messages` s'il est présent), ou `Text1` à
`Text4` avant la 1.20 (étiquette « sign[text,N] »). Un `filtered_messages` n'ajoute une trouvaille que si sa commande diffère de celle de
`messages` à la même ligne (« sign[front,N,filtered] »), mais ses commandes sont comptées dans `vus`.
`vus` = nombre de commandes extraites (doublons de filtered compris) + les `run_command` que ces commandes contiennent elles-mêmes (un
clickEvent dans un tellraw) : si le panneau contient plus de `run_command` que cela, il a été mal lu (JSON invalide, type inattendu) :
l'appelant le signale. Jamais fatal.
"""
import json

SIGN_IDS = frozenset(('sign', 'hanging_sign'))
RUN = 'run_command'
_EVENTS = (('click_event', 'command'), ('clickEvent', 'value'))      # (clé de l'événement, clé de la commande) : NBT 1.21.5+, JSON
# Noms de blocs et de biomes du chunk (palettes, ticks planifiés) : jamais des objets ni des entités ; ignorés à la racine du chunk (ou de
# `Level`, ancien format) seulement : une clé du même nom plus bas (NBT d'un objet, d'une entité) reste examinée
_SKIP = frozenset(('sections', 'Sections', 'block_ticks', 'fluid_ticks', 'TileTicks', 'LiquidTicks', 'palette', 'Palette'))


def kind_of(e):
    """Dict d'un block entity / d'une entité / d'un objet -> son id sans `minecraft:`, en minuscules ('' si ce n'est pas un dict)."""
    return str(e.get('id', '')).removeprefix('minecraft:').lower() if isinstance(e, dict) else ''


def _clicks(node, out):
    """Composant (NBT, ou JSON décodé) -> out : (événement, clé de sa commande) de chaque événement run_command, sous-composants
    compris (extra, with...) ; la commande est ev[clé]."""
    if isinstance(node, list):
        for x in node:
            _clicks(x, out)
    elif isinstance(node, dict):
        for key, field in _EVENTS:
            ev = node.get(key)
            if isinstance(ev, dict) and ev.get('action') == RUN and isinstance(ev.get(field), str):
                out.append((ev, field))
        for k, v in node.items():
            if k not in ('click_event', 'clickEvent'):
                _clicks(v, out)


def message_events(msg):
    """Un message de panneau (composant NBT, ou chaîne JSON) -> (objet JSON décodé, [(événement, clé de sa commande)]). L'objet n'est
    donné que pour une chaîne JSON (à ré-encoder après modification des événements) ; None pour un composant NBT (ses événements
    sont dans l'arbre du chunk), pour une chaîne qui n'est pas du JSON (un texte) ou pour un JSON invalide (aucun événement)."""
    out = []
    if not isinstance(msg, str):
        _clicks(msg, out)
        return None, out
    text = msg.lstrip()
    if text[:1] not in ('{', '[', '"'):
        return None, out
    try:
        obj = json.loads(text)
        _clicks(obj, out)
    except (ValueError, RecursionError):
        return None, out
    return obj, out


def _message(msg):
    return [ev[field] for ev, field in message_events(msg)[1]]


def sign_slots(be, kind):
    """Block entity de panneau (kind : 'sign' ou 'hanging_sign') -> (étiquette, message, conteneur, clé, filtered) de chaque emplacement
    de message, dans l'ordre de lecture ; le message est conteneur[clé] (liste + indice, ou block entity + « TextN »)."""
    for face in ('front', 'back'):
        text = be.get(face + '_text')
        if not isinstance(text, dict):
            continue
        filtered = text.get('filtered_messages')
        for i, msg in enumerate(text.get('messages') or []):
            yield f'{kind}[{face},{i}]', msg, text['messages'], i, False
            if isinstance(filtered, list) and i < len(filtered):
                yield f'{kind}[{face},{i},filtered]', filtered[i], filtered, i, True
    for i in range(4):
        yield f'{kind}[text,{i}]', be.get(f'Text{i + 1}'), be, f'Text{i + 1}', False


def sign_commands(be, kind):
    """Block entity de panneau (kind : 'sign' ou 'hanging_sign') -> ([(étiquette, commande)], nombre de commandes vues)."""
    out, seen, last = [], 0, []
    for label, msg, _, _, filtered in sign_slots(be, kind):
        cmds = _message(msg)
        seen += len(cmds) + sum(c.count(RUN) for c in cmds)
        out += [(label, c) for c in cmds if not (filtered and c in last)]       # filtered : seulement si différent de `messages`
        if not filtered:
            last = cmds
    return out, seen


def _count(node, tokens, holders, counts, rider=False, top=0):
    """rider : `node` est (ou contient, si liste) un passager d'un porteur qui a `Pos` (ou qui est lui-même un passager) : une entité
    même sans `Pos`. top : 2 = `node` est la racine du chunk, 1 = son `Level` (seuls endroits où _SKIP s'applique : un `Level` dans
    `Level` n'en est plus un), 0 sinon."""
    if isinstance(node, str):
        for i, t in enumerate(tokens):
            counts[i] += node.count(t)
    elif isinstance(node, list):
        for x in node:
            if isinstance(x, (str, list, dict)):
                _count(x, tokens, holders, counts, rider)
    elif isinstance(node, dict):
        if kind_of(node) in holders and (rider or 'x' in node or 'Pos' in node):
            return
        for k, v in node.items():
            if not (top and k in _SKIP) and isinstance(v, (str, list, dict)):
                _count(v, tokens, holders, counts, k == 'Passengers' and (rider or 'Pos' in node), int(top == 2 and k == 'Level'))


def count_outside(node, tokens, holders):
    """Arbre NBT -> [occurrences de chaque token] dans les chaînes HORS des holders (block entity ou entité, donc avec `x` ou `Pos`, dont
    l'id est dans `holders` : blocs de commande, minecarts, panneaux : déjà analysés ; un passager `Passengers` d'un porteur qui a `Pos`
    n'en a pas toujours) et hors palettes / ticks planifiés de la racine (_SKIP : noms de blocs). Un panneau en tant qu'OBJET d'un coffre
    n'a ni `x` ni `Pos` : il reste compté. Un livre, un coffre, un spawner (SpawnData : son passager sans `Pos` n'est pas un holder), un
    falling_block (TileEntityData)... qui en porte un est à vérifier.
    Faux positifs acceptés de `sans_bloc` : un `block_display` / `item_display` (BlockState) ou un enderman (`carriedBlockState`) dont le
    bloc est un command_block : un avertissement de plus, jamais un trou."""
    counts = [0] * len(tokens)
    _count(node, tokens, holders, counts, top=2)
    return counts
