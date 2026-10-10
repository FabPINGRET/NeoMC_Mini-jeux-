"""Menus et donnees statiques de la Course d'elytres : sous-menu (fenetre + texte), avancement de choc contre un mur,
tag de type de degats. (Le branchement dans les menus existants est fait par wire_elyrace.py.)
Python stdlib uniquement (compatible 3.8).
"""
import json

import game as G

TITLE = "🪽 Course élytres"      # titre court, identique a SHORT_TITLE de tools/variantes/gen_variants.py (qui le reecrit sinon)
RANDOM_TIP = "Un parcours tiré au hasard parmi ceux qui sont construits."
BACK_OPT = 42                     # mg.opt de la categorie « Courses et vol » (menu en arbre de gen_variants.py)

# Valeurs de /trigger mg.xs (contre-la-montre solo, ouvert a tous) : 10 + NUM = solo sur le parcours NUM. Aucune etiquette de ces boutons
# ne commence par « : gen_variants.py (is_back) retire de sub_elyrace tout bouton dont le libelle commence ainsi.
SOLO_MENU, SOLO_QUIT, SOLO_RECORDS, SOLO_STOP, SOLO_RANDOM = 1, 2, 3, 4, 10     # SOLO_STOP : un admin arrete tous les solos (pas de bouton)
SOLO_RETRY = 5          # [Rejouer] du message d'arrivee (phase 4 du solo) : relance le meme parcours, sans repasser par le lobby
SOLO_LOBBY = 6          # [Retour au lobby] du meme message : arret silencieux en phase 4 seulement (un vieux lien du chat n'abandonne pas une tentative suivante)
SOLO_TIP = "Contre-la-montre : seul en piste, ton meilleur temps est enregistré. Te met en pause pendant le solo ; 30 s d'attente entre deux solos."
SOLO_BACK_MENU = 'trigger mg.menu set 1'      # retour de la fenetre solo : menu principal (admin) ou fenetre de vote (non-admin)


def solo_value(spec):
    return SOLO_RANDOM + spec.NUM


# Id de lancement (mg.go) d'un parcours = ID_BASE + NUM (81 = Canyon du Couchant, 82 = Pic Blanc). Les ids 67..80 sont pris (TNT Tag,
# Bedwars, Elytra, Quakecraft sniper) et 100..196 sont les variantes ; mg:core/request convertit 81.. en $xc = id - ID_BASE puis
# $game = 66 (66 = au hasard).
ID_BASE = 80


def route_id(spec):
    return ID_BASE + spec.NUM


def star_label(name, n, col):
    """Libelle d'une carte : nom puis difficulte (★ pleines, ☆ vides sur 4), meme forme que gen_variants.star_label (a garder identique :
    gen_variants reecrit tout bouton `trigger mg.go set <id>` de NATIVE, et doit retrouver ce que ce module produit)."""
    return [{"text": name + " ", "color": col}, {"text": "★" * n, "color": "gold"}, {"text": "☆" * (4 - n), "color": "dark_gray"}]


def races(specs):
    """Boutons du menu : (nom, etoiles ou None, id de jeu, couleur, icone, infobulle)."""
    out = [("🎲 Au hasard", None, G.GAME_ID, 'light_purple', '', RANDOM_TIP)]
    for s in specs:
        out.append((s.NAME, s.STARS, route_id(s), s.COLOR, s.ICON, "%s %d anneaux, %d anneaux d'or, %d points de reprise, %d cœurs."
                    % (s.TIP, len(s.RINGS), len(s.GOLDS), len(s.CPS), G.HEARTS)))
    return out


def rate_call(name, macro):
    """Ouverture d'une fenetre sous sa forme finale : gen_rating.py (point fixe, comme dialog_json) remplace tout `dialog show @s mg:X`
    par `function mg:rate/d/X`, avec `with storage mg:rate lab` si la fenetre porte les notes des joueurs (macro, 1re ligne en `$`)."""
    return 'function mg:rate/d/%s' % name + (' with storage mg:rate lab' if macro else '')


def sub_lines(specs):
    out = ['# Sous-menu 🪽 Course d\'élytres (@s = joueur) — fenêtre, sinon menu texte',
           'execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]',
           'execute unless entity @s[tag=mg.admin] run return 0',
           'scoreboard players set $dlg mg.st 0',
           'execute store success score $dlg mg.st run ' + rate_call('sub_elyrace', True),
           'execute if score $dlg mg.st matches 1 run return 0',
           'tellraw @s [{"text":"\\n🪽 Course d\'élytres — choisis un parcours","color":"aqua","bold":true}]']
    for name, stars, gid, col, icon, tip in races(specs):
        click = {"action": "run_command", "command": "trigger mg.go set %d" % gid}
        hover = {"action": "show_text", "value": tip}
        if stars is None:
            parts = [{"text": " [%s]" % name, "color": col, "click_event": click, "hover_event": hover}]
        else:
            parts = [{"text": " [%s %s " % (icon, name), "color": col, "click_event": click, "hover_event": hover},
                     {"text": "★" * stars, "color": "gold"}, {"text": "☆" * (4 - stars) + "]", "color": "dark_gray"}]
        out.append(tell(parts))
    out += solo_text_lines(specs)
    out.append('tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set %d"}}]' % BACK_OPT)
    return out


def tell(parts):
    return 'tellraw @s ' + json.dumps([""] + parts, ensure_ascii=False, separators=(',', ':'))


def solo_text_lines(specs):
    """Menu texte du contre-la-montre solo : un bouton par parcours (et au hasard), puis les records."""
    out = ['tellraw @s [{"text":"\\n⏱ Contre-la-montre solo (ouvert à tous : /trigger mg.xs)","color":"aqua","bold":true}]']
    for label, stars, val, col, tip in solo_races(specs):
        click = {"action": "run_command", "command": "trigger mg.xs set %d" % val}
        hover = {"action": "show_text", "value": tip}
        parts = [{"text": " [%s" % label + ("]" if stars is None else " "), "color": col, "click_event": click, "hover_event": hover}]
        if stars is not None:
            parts += [{"text": "★" * stars, "color": "gold"}, {"text": "☆" * (4 - stars) + "]", "color": "dark_gray"}]
        out.append(tell(parts))
    out.append(tell([{"text": " [📊 Records]", "color": "gold", "click_event": {"action": "run_command", "command": "trigger mg.xs set %d" % SOLO_RECORDS},
                      "hover_event": {"action": "show_text", "value": "Tes meilleurs temps et les records du serveur."}}]))
    return out


def solo_races(specs):
    """Boutons solo : (libelle, etoiles ou None, valeur de mg.xs, couleur, infobulle)."""
    out = [("⏱ Au hasard", None, SOLO_RANDOM, 'light_purple', SOLO_TIP)]
    out += [("⏱ " + s.NAME, s.STARS, solo_value(s), s.COLOR, SOLO_TIP) for s in specs]
    return out


def act(label, tip, cmd):
    a = {"label": label}
    if tip:
        a["tooltip"] = [{"text": tip, "color": "gray"}]
    a["action"] = {"type": "minecraft:run_command", "command": cmd}
    return a


def solo_buttons(specs):
    """Boutons de la fenetre : un par parcours (et au hasard), puis les records."""
    out = []
    for label, stars, val, col, tip in solo_races(specs):
        out.append(act([{"text": label, "color": col}] if stars is None else star_label(label, stars, col), tip, 'trigger mg.xs set %d' % val))
    return out + [act([{"text": "📊 Records", "color": "gold"}], "Tes meilleurs temps et les records du serveur.", 'trigger mg.xs set %d' % SOLO_RECORDS)]


def solo_dialog_json(specs):
    """Fenetre du contre-la-montre solo, ouverte a tous (trigger mg.xs) : le retour mene au menu principal ou, pour un non-admin, a la fenetre de vote."""
    return {
        "type": "minecraft:multi_action",
        "title": {"text": "⏱ Contre-la-montre", "color": "aqua", "bold": True},
        "pause": False,
        "can_close_with_escape": True,
        "body": [{"type": "minecraft:plain_message", "contents": [
            {"text": "Seul en piste, avec ton meilleur temps et un record du serveur par parcours. Le solo te met en pause (désactiver la pause l'arrête) et se joue même pendant une partie, sauf une course d'élytres de groupe. 30 s d'attente entre deux solos.", "color": "gray"}]}],
        "columns": 2,
        "exit_action": {"label": [{"text": "Fermer", "color": "gray"}]},
        "actions": solo_buttons(specs) + [act([{"text": "« Retour", "color": "yellow"}], None, SOLO_BACK_MENU)],
    }


def dialog_json(specs):
    """Fenetre du sous-menu, sous sa forme finale (celle que gen_variants.py laisse inchangee : titre court, cartes etoilees,
    retour vers la categorie « Courses et vol »). Une rangee de lancement de groupe, une rangee de solo, puis les records."""
    buttons = []
    for name, stars, gid, col, icon, tip in races(specs):
        label = [{"text": name, "color": col}] if stars is None else star_label(name, stars, col)
        buttons.append(act(label, tip, 'trigger mg.go set %d' % gid))
    buttons += solo_buttons(specs)
    return {
        "type": "minecraft:multi_action",
        "title": {"text": TITLE, "color": "aqua", "bold": True},
        "pause": False,
        "can_close_with_escape": True,
        "body": [{"type": "minecraft:plain_message", "contents": [
            {"text": "Plane avec tes élytres à travers des anneaux : choisis le parcours.", "color": "gray"}]}],
        "columns": 1 + len(specs),
        "exit_action": {"label": [{"text": "Fermer", "color": "gray"}]},
        "actions": buttons + [act([{"text": "« Retour", "color": "yellow"}], None, "trigger mg.opt set %d" % BACK_OPT)],
    }


def advancement_json():
    return {"criteria": {"hit": {"trigger": "minecraft:entity_hurt_player", "conditions": {
        "damage": {"type": {"tags": [{"id": "mg:elyrace_wall", "expected": True}]}}}}},
            "rewards": {"function": "mg:elyrace/wall_adv"}}


def damage_tag_json():
    return {"values": ["minecraft:fly_into_wall"]}


def dumps(d):
    return json.dumps(d, ensure_ascii=False, indent=2) + '\n'
