"""Menus et donnees statiques de la Course d'elytres : sous-menu (fenetre + texte), avancement de choc contre un mur,
tag de type de degats. (Le branchement dans les menus existants est fait par wire_elyrace.py.)
Python stdlib uniquement (compatible 3.8).
"""
import json

import game as G

GO_TRIGGER = 'trigger mg.go set %d' % G.GAME_ID
TITLE = "🪽 Course d'élytres"
RACES = [  # (libelle, id de jeu, couleur, infobulle)
    ("🏜 Canyon du Couchant", G.GAME_ID, 'gold',
     "Parcours 1 (Far West, ~1000 blocs) : slalom entre cheminées de fée, arches, viaduc ferroviaire, gorge en S, crête, ville fantôme. "
     "%d anneaux, 3 anneaux d'or, 4 points de reprise, 3 cœurs." % G.RING_N),
]


def sub_lines():
    out = ['# Sous-menu 🪽 Course d\'élytres (@s = joueur) — fenêtre, sinon menu texte',
           'execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]',
           'execute unless entity @s[tag=mg.admin] run return 0',
           'scoreboard players set $dlg mg.st 0',
           'execute store success score $dlg mg.st run dialog show @s mg:sub_elyrace',
           'execute if score $dlg mg.st matches 1 run return 0',
           'tellraw @s [{"text":"\\n🪽 Course d\'élytres — choisis un parcours","color":"aqua","bold":true}]']
    for label, gid, col, tip in RACES:
        out.append('tellraw @s ["",{"text":" [%s]","color":"%s","click_event":{"action":"run_command","command":"trigger mg.go set %d"},'
                   '"hover_event":{"action":"show_text","value":"%s"}}]' % (label, col, gid, tip.replace('"', '\\"')))
    out.append('tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]')
    return out


def dialog_json():
    def act(label, col, tip, cmd, bold=False):
        lab = {"text": label, "color": col}
        if bold:
            lab["bold"] = True
        a = {"label": [lab]}
        if tip:
            a["tooltip"] = [{"text": tip, "color": "gray"}]
        a["action"] = {"type": "minecraft:run_command", "command": cmd}
        return a
    return {
        "type": "minecraft:multi_action",
        "title": {"text": TITLE, "color": "aqua", "bold": True},
        "pause": False,
        "can_close_with_escape": True,
        "body": [{"type": "minecraft:plain_message", "contents": [
            {"text": "Plane avec tes élytres à travers des anneaux : choisis le parcours.", "color": "gray"}]}],
        "columns": 2,
        "exit_action": {"label": [{"text": "Fermer", "color": "gray"}]},
        "actions": [act(l, c, t, 'trigger mg.go set %d' % g, True) for l, g, c, t in RACES]
                   + [act("« Retour au menu", "yellow", None, "trigger mg.menu")],
    }


def advancement_json():
    return {"criteria": {"hit": {"trigger": "minecraft:entity_hurt_player", "conditions": {
        "damage": {"type": {"tags": [{"id": "mg:elyrace_wall", "expected": True}]}}}}},
            "rewards": {"function": "mg:elyrace/wall_adv"}}


def damage_tag_json():
    return {"values": ["minecraft:fly_into_wall"]}


def dumps(d):
    return json.dumps(d, ensure_ascii=False, indent=2) + '\n'
