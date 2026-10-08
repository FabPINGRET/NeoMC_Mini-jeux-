"""Menus et donnees statiques de la Course d'elytres : sous-menu (fenetre + texte), avancement de choc contre un mur,
tag de type de degats. (Le branchement dans les menus existants est fait par wire_elyrace.py.)
Python stdlib uniquement (compatible 3.8).
"""
import json

import game as G

TITLE = "🪽 Course élytres"      # titre court, identique a SHORT_TITLE de tools/variantes/gen_variants.py (qui le reecrit sinon)
RANDOM_TIP = "Un parcours tiré au hasard parmi ceux qui sont construits."
BACK_OPT = 42                     # mg.opt de la categorie « Courses et vol » (menu en arbre de gen_variants.py)


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


def sub_lines(specs):
    out = ['# Sous-menu 🪽 Course d\'élytres (@s = joueur) — fenêtre, sinon menu texte',
           'execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]',
           'execute unless entity @s[tag=mg.admin] run return 0',
           'scoreboard players set $dlg mg.st 0',
           'execute store success score $dlg mg.st run dialog show @s mg:sub_elyrace',
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
        out.append('tellraw @s ' + json.dumps([""] + parts, ensure_ascii=False, separators=(',', ':')))
    out.append('tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set %d"}}]' % BACK_OPT)
    return out


def dialog_json(specs):
    """Fenetre du sous-menu, sous sa forme finale (celle que gen_variants.py laisse inchangee : titre court, cartes etoilees,
    retour vers la categorie « Courses et vol »)."""
    def act(label, tip, cmd):
        a = {"label": label}
        if tip:
            a["tooltip"] = [{"text": tip, "color": "gray"}]
        a["action"] = {"type": "minecraft:run_command", "command": cmd}
        return a
    buttons = []
    for name, stars, gid, col, icon, tip in races(specs):
        label = [{"text": name, "color": col}] if stars is None else star_label(name, stars, col)
        buttons.append(act(label, tip, 'trigger mg.go set %d' % gid))
    return {
        "type": "minecraft:multi_action",
        "title": {"text": TITLE, "color": "aqua", "bold": True},
        "pause": False,
        "can_close_with_escape": True,
        "body": [{"type": "minecraft:plain_message", "contents": [
            {"text": "Plane avec tes élytres à travers des anneaux : choisis le parcours.", "color": "gray"}]}],
        "columns": 2,
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
