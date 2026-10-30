"""État de la carte « Scourge of the Floaty Isles » (scoreboard, équipes, bossbars, storage, schedules) -> install / uninstall de floaty.

    st = fl_state.build(dossier_carte, auteur, trampolines)   # State(install, uninstall, counts, sched_missing, players) : rien n'est écrit

Sources (lecture seule, <carte>/data/) : minecraft/scoreboard.dat (objectifs, équipes, scores), minecraft/custom_boss_events.dat
(bossbars), minecraft/scheduled_events.dat (schedules en attente, avec <carte>/level.dat pour l'heure du monde) et command_storage_*.dat
(storage de commandes, n'importe où sous data/). Un fichier absent = section vide.
- install (floaty:install) : gardée par `data storage mg:floaty installed` (ne s'exécute qu'une fois). Crée objectifs (critère +
  displayName, rendertype s'il n'est pas « integer »), équipes (options, SANS membres), scores, bossbars (propriétés, SANS joueurs),
  storage et schedules en attente. Aucun `scoreboard objectives setdisplay` : l'affichage est global au serveur.
- uninstall (floaty:uninstall, appelé par mg:desinstaller) : `schedule clear` de CHAQUE trampoline de la carte (elle peut les replanifier
  en jeu) AVANT la garde, donc même si floaty n'est pas installé ; puis sans effet si floaty n'est pas installé (même garde, à l'envers) ;
  sinon l'inverse exact (bossbars, équipes, objectifs — leurs scores partent avec —, clés de storage, puis le drapeau installed).
NOTE POUR L3 : personne n'appelle install ici. L3 doit l'appeler (une fois, à l'activation de la dimension ; la garde le rend inoffensif
  s'il est rappelé). Rejouer l'état = `function floaty:uninstall` puis `function floaty:install`. Les schedules en attente de la carte
  repartent à l'appel d'install, avec le délai qu'il restait à la carte (au moins 1 tick), pas à la date d'origine.
Valeurs par défaut : les codecs 26.x n'écrivent pas une valeur égale à son défaut, et ce défaut est celui des commandes de création
(`team add`, `bossbar add`, `scoreboard objectives add`) ; une propriété absente n'a donc rien à émettre, sauf deux cas où le défaut
n'est PAS une commande : Score absent = 0 (installé : l'entrée du score doit exister) et Visible absent = false (toujours émis).
Scores : seuls les FAUX joueurs (#x, $x, constantes « 20 », noms de variables) sont installés. Écartés et comptés :
- vrais joueurs : `auteur` et tout membre non-UUID d'une équipe de la carte (la carte y range ses testeurs) ; un nom comme « Time » ou
  « grove_eye » est un faux joueur, on ne peut pas le deviner au motif, d'où cette règle explicite ;
- UUID : entités (mobs) du monde d'origine, qui n'existent pas dans le nouveau ;
- noms inutilisables dans une commande (espace, @, *), valeurs non entières et scores d'un objectif non déclaré.
Schedules : seuls ceux dont la fonction a un trampoline (fonction planifiée par la carte elle-même : floaty:sched/...) sont reproduits ;
les autres, et les rappels qui ne sont pas une fonction, sont comptés (sched_missing liste les fonctions sans trampoline).
Storage : un storage de l'espace de noms mg est écarté (il écraserait un storage du pack).
"""
import re
from collections import namedtuple
from pathlib import Path

import fl_nbt
import mcfn

State = namedtuple('State', 'install uninstall counts sched_missing players')    # players : noms des vrais joueurs dont un score est écarté
GUARD = 'mg:floaty installed'
_NAME = re.compile(r'[A-Za-z0-9_.+-]+')
_CRITERIA = re.compile(r'[A-Za-z0-9_.:+-]+')
_RLOC = re.compile(r'[a-z0-9_.-]+:[a-z0-9_./-]+')
_WORD = re.compile(r'[A-Za-z0-9_]+')                        # mot de commande : chiffres admis (style notched_6), majuscules admises
_PATH_KEY = re.compile(r'[A-Za-z0-9_]+')                    # clé nue d'un chemin NBT (le « . » y sépare les niveaux : on le met entre guillemets)
_UUID = re.compile(r'[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}')
_STYLES = {'bold', 'italic', 'underlined', 'strikethrough', 'obfuscated'}
_TEAM_BOOL = (('AllowFriendlyFire', 'friendlyFire'), ('SeeFriendlyInvisibles', 'seeFriendlyInvisibles'))
_TEAM_WORD = (('TeamColor', 'color'), ('NameTagVisibility', 'nametagVisibility'),
              ('DeathMessageVisibility', 'deathMessageVisibility'), ('CollisionRule', 'collisionRule'))
_TEAM_TEXT = (('MemberNamePrefix', 'prefix'), ('MemberNameSuffix', 'suffix'))
_COUNTERS = ('objectives_invalid', 'teams_invalid', 'options_invalid', 'scores_players', 'scores_uuid', 'scores_invalid',
             'bossbars_invalid', 'bossbar_props_invalid', 'sched_events', 'sched_other', 'sched_missing')


def component(v):
    """Composant de texte NBT -> JSON : les styles (bold...) sont des bytes en NBT (1b) et des booléens en JSON."""
    if isinstance(v, dict):
        return {k: bool(x) if k in _STYLES else component(x) for k, x in v.items()}
    if isinstance(v, list):
        return [component(x) for x in v]
    return v


def _int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def read(map_dir):
    """-> (data de scoreboard.dat, bossbars {id: propriétés}, storages {'ns:clé': (texte SNBT, clés de premier niveau)}, storages écartés [ns:clé])."""
    d = Path(map_dir) / 'data'
    sb = d / 'minecraft' / 'scoreboard.dat'
    bb = d / 'minecraft' / 'custom_boss_events.dat'
    board = fl_nbt.load(sb).get('data', {}) if sb.exists() else {}
    bars = fl_nbt.load(bb).get('data', {}) if bb.exists() else {}
    storages, skipped = {}, []
    for p in sorted(d.rglob('command_storage_*.dat')) if d.is_dir() else []:
        ns = p.stem[len('command_storage_'):]
        for key, val in sorted(fl_nbt.load(p, snbt=True).get('data', {}).get('contents', {}).items()):
            sid = f'{ns}:{key}'
            if ns == 'mg' or not _RLOC.fullmatch(sid) or not isinstance(val, dict):
                skipped.append(sid)
            else:
                storages[sid] = (fl_nbt.snbt(val), list(val))
    return board, bars, storages, skipped


def _path(key):
    """Clé de premier niveau -> chemin NBT (entre guillemets si elle n'est pas un simple mot)."""
    return key if _PATH_KEY.fullmatch(key) else mcfn.js(key)


def _word(v):
    return isinstance(v, str) and _WORD.fullmatch(v) is not None


def _objectives(board, c):
    out, lines = [], []
    for o in sorted(board.get('Objectives', []), key=lambda o: o.get('Name', '')):
        name, crit = o.get('Name', ''), o.get('CriteriaName', 'dummy')
        if not _NAME.fullmatch(name) or not _CRITERIA.fullmatch(crit):
            c['objectives_invalid'] += 1
            continue
        title = mcfn.js(component(o.get('DisplayName', name)))
        lines.append(f'scoreboard objectives add {name} {crit} {title}')
        render = o.get('RenderType', 'integer')
        if not _word(render):
            c['options_invalid'] += 1
        elif render != 'integer':
            lines.append(f'scoreboard objectives modify {name} rendertype {render}')
        out.append(name)
    return out, lines


def _teams(board, c):
    out, lines = [], []
    for t in sorted(board.get('Teams', []), key=lambda t: t.get('Name', '')):
        name = t.get('Name', '')
        if not _NAME.fullmatch(name):
            c['teams_invalid'] += 1
            continue
        lines.append(f'team add {name} {mcfn.js(component(t.get("DisplayName", name)))}')
        lines += [f'team modify {name} {opt} {"true" if t[key] else "false"}' for key, opt in _TEAM_BOOL if key in t]
        for key, opt in _TEAM_WORD:
            if key not in t:
                continue
            if _word(t[key]):
                lines.append(f'team modify {name} {opt} {t[key]}')
            else:
                c['options_invalid'] += 1
        lines += [f'team modify {name} {opt} {mcfn.js(component(t[key]))}' for key, opt in _TEAM_TEXT if key in t]
        out.append(name)
    return out, lines


def _scores(board, objectives, real, c, players):
    """players (set) reçoit les noms des vrais joueurs écartés (scores_players compte les entrées, un nom peut en avoir plusieurs)."""
    lines = []
    for s in sorted(board.get('PlayerScores', []), key=lambda s: (s.get('Objective', ''), s.get('Name', ''))):
        who, obj, score = s.get('Name', ''), s.get('Objective', ''), s.get('Score', 0)     # Score absent = 0 (défaut du codec)
        if who in real:
            c['scores_players'] += 1
            players.add(who)
        elif _UUID.fullmatch(who):
            c['scores_uuid'] += 1
        elif obj not in objectives or not who or who[0] in '@*' or re.search(r'\s', who) or not _int(score):
            c['scores_invalid'] += 1
        else:
            lines.append(f'scoreboard players set {who} {obj} {score}')
    return lines


def _bossbars(bars, c):
    out, lines = [], []
    for bid, b in sorted(bars.items()):
        if not _RLOC.fullmatch(bid):
            c['bossbars_invalid'] += 1
            continue
        lines.append(f'bossbar add {bid} {mcfn.js(component(b.get("Name", bid)))}')
        for key, opt in (('Color', 'color'), ('Overlay', 'style')):
            if key in b:
                if _word(b[key]):
                    lines.append(f'bossbar set {bid} {opt} {b[key]}')
                else:
                    c['bossbar_props_invalid'] += 1
        for key, opt, low in (('Max', 'max', 1), ('Value', 'value', 0)):                  # max avant value
            if key in b:
                if _int(b[key]) and b[key] >= low:
                    lines.append(f'bossbar set {bid} {opt} {b[key]}')
                else:
                    c['bossbar_props_invalid'] += 1
        lines.append(f'bossbar set {bid} visible {"true" if b.get("Visible", False) else "false"}')    # absent = false (la commande add crée visible)
        out.append(bid)
    return out, lines


def _events(map_dir, c):
    """[(fonction, délai en ticks)] des schedules en attente de la carte. trigger_time est une date de jeu absolue : délai = trigger_time -
    Time de level.dat, au moins 1 (sans Time lisible : 1). Un rappel qui n'est pas une fonction (ou illisible) est compté dans sched_other."""
    p = Path(map_dir) / 'data' / 'minecraft' / 'scheduled_events.dat'
    if not p.exists():
        return []
    lvl = Path(map_dir) / 'level.dat'
    root = fl_nbt.load(lvl) if lvl.exists() else {}
    now = root.get('Data', root).get('Time')                  # level.dat : racine « Data » (comme fl_nbt.spawn)
    out = []
    for e in fl_nbt.load(p).get('data', {}).get('events', []):
        cb, at = e.get('callback') or {}, e.get('trigger_time')
        fid = cb.get('id')
        if cb.get('type') != 'minecraft:function' or not isinstance(fid, str) or not _RLOC.fullmatch(fid) or not _int(at):
            c['sched_other'] += 1
            continue
        out.append((fid, max(1, at - now) if _int(now) else 1))
    return sorted(out, key=lambda e: (e[1], e[0]))


def _schedules(events, trampolines, c):
    """-> (lignes d'install, fonctions sans trampoline). trampolines = {fonction: id du trampoline}."""
    install, missing = [], set()
    for fn, delay in events:
        c['sched_events'] += 1
        if fn not in trampolines:
            missing.add(fn)
            continue
        install.append(f'schedule function {trampolines[fn]} {delay}t replace')
    c['sched_missing'] = sum(1 for fn, _ in events if fn in missing)
    return install, sorted(missing)


def build(map_dir, author, trampolines=None):
    """Lit la carte et renvoie State(install, uninstall, counts, sched_missing, players) (voir l'en-tête pour les règles).
    players : noms triés des vrais joueurs dont un score est écarté.
    trampolines : {fonction planifiée par la carte : id de son trampoline} (st.sched de fl_rewrite) ; sans, aucun schedule n'est reproduit."""
    board, bars, storages, skipped = read(map_dir)
    c = dict.fromkeys(_COUNTERS, 0)
    real = {author} | {p for t in board.get('Teams', []) for p in t.get('Players', []) if not _UUID.fullmatch(p)}
    objectives, obj_lines = _objectives(board, c)
    teams, team_lines = _teams(board, c)
    players = set()
    score_lines = _scores(board, set(objectives), real, c, players)
    bossbars, bar_lines = _bossbars(bars, c)
    trampolines = trampolines or {}
    sched_lines, missing = _schedules(_events(map_dir, c), trampolines, c)
    clear_lines = [f'schedule clear {t}' for t in sorted(trampolines.values())]       # TOUS les trampolines : la carte peut les replanifier en jeu
    players = sorted(players)
    c.update(objectives=len(objectives), teams=len(teams), scores=len(score_lines), bossbars=len(bossbars),
             storage=len(storages), storage_skipped=len(skipped), sched_installed=len(sched_lines))
    install = ['# Installation de l\'état de la carte Scourge (généré par tools/floaty/gen_floaty.py : ne pas éditer) — une seule fois',
               f'execute if data storage {GUARD} run return 0', f'data modify storage {GUARD} set value 1b'] + obj_lines + team_lines + \
              score_lines + bar_lines + [f'data merge storage {sid} {txt}' for sid, (txt, _) in storages.items()] + sched_lines
    uninstall = ['# Désinstallation de l\'état de la carte Scourge (généré par tools/floaty/gen_floaty.py : ne pas éditer) ; appelé par mg:desinstaller '
                 '(schedule clear AVANT la garde)'] + clear_lines + \
                [f'execute unless data storage {GUARD} run return 0'] + \
                [f'bossbar remove {b}' for b in bossbars] + [f'team remove {t}' for t in teams] + \
                [f'scoreboard objectives remove {o}' for o in objectives] + [f'data remove storage {sid} {_path(k)}' for sid, (_, ks) in storages.items() for k in ks] + \
                [f'data remove storage {GUARD}']
    return State(install, uninstall, c, missing, players)
