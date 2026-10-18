"""⚽ Terrain de foot : administration (importé par gen_foot.py, jamais lancé seul) - coupure, compteurs, boutons, mg.opt 84 et 85.

Même mécanique que gen_sit.py (admin_toggle / admin_stats, add_buttons / chat_line recopiés : gen_sit.py s'exécute à l'import).
- mg.opt 84 : coupe / rétablit le terrain ($ftoff mg.st = 1 : coupé, absent : actif). Couper : plus de balle, joueurs du terrain renvoyés au
  spawn, équipes quittées, puits refermé (margelle pleine) et panneaux retirés. Rétablir : puits rouvert, panneaux reposés.
- mg.opt 85 : compteurs d'usage (objectif mg.ftn : $but buts, $eq choix d'équipe, $ent entrées sur le terrain) et score en cours.
- Boutons dans dialog/lobby_events.json (avant « trigger mg.menu ») et lignes de lobby/ev/menu_chat (après la dernière du menu texte).
  gen_events.py réécrit ces deux fichiers : le relancer impose de relancer gen_foot.py (et gen_sit.py) ensuite.
"""
import json
import os

import common as C
import foot_build as FB

OPT_TOGGLE, OPT_STATS = 84, 85
TIP_TOGGLE = 'Active ou coupe le terrain de foot souterrain du spawn (actif par défaut)'
TIP_STATS = 'Affiche les compteurs d\'usage du foot (buts, équipes, entrées) et le score en cours'
COUNTERS = [('$but', '⚽ Buts'), ('$eq', '🔴🔵 Choix d\'équipe'), ('$ent', '🚪 Entrées')]
CHAT_LAST = ('🎄 Déco Noël', 'red', 74, 'Pose ou retire le décor de Noël du spawn (réversible)')    # dernier EV_BTN de gen_events.py


def act(label, color, opt, tip):
    return {'label': [{'text': label, 'color': color, 'bold': True}], 'tooltip': [{'text': tip, 'color': 'gray'}],
            'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.opt set {opt}'}}


def add_buttons(path, buttons, before=None):
    """Insère les boutons absents (clé : leur commande) dans une fenêtre, avant le bouton de commande « before » (sinon à la fin) ;
    l'infobulle des boutons déjà présents est alignée sur celle d'ici."""
    p = os.path.join(C.D, 'dialog', path)
    d = json.load(open(p, encoding='utf-8'))
    have = {a['action'].get('command'): a for a in d['actions']}
    new = [b for b in buttons if b['action']['command'] not in have]
    stale = [(have[b['action']['command']], b) for b in buttons if b['action']['command'] in have
             and have[b['action']['command']].get('tooltip') != b['tooltip']]
    for old, b in stale:
        old['tooltip'] = b['tooltip']
    if not new and not stale:
        return
    i = next((i for i, a in enumerate(d['actions']) if a['action'].get('command') == before), len(d['actions']))
    d['actions'][i:i] = new
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


def chat_line(t, c, o, tip):
    return ('tellraw @s ["",' + C.js({'text': ' [' + t + ']', 'color': c, 'click_event': {'action': 'run_command', 'command': f'trigger mg.opt set {o}'},
                                      'hover_event': {'action': 'show_text', 'value': tip}}) + ']')


def write():
    w, js = C.w, C.js
    w('foot/admin_toggle', ['# Admin (@s) : coupe / rétablit le terrain de foot ($ftoff mg.st = 1 : coupé, absent : actif)',
                            'execute store success score #ftw mg.st if score $ftoff mg.st matches 1',
                            'execute if score #ftw mg.st matches 1 run scoreboard players reset $ftoff mg.st',
                            'execute if score #ftw mg.st matches 1 run function mg:foot/hole_open',
                            'execute if score #ftw mg.st matches 1 run return run tellraw @s ' + js({'text': '⚽ Terrain de foot : activé.', 'color': 'green'}),
                            'scoreboard players set $ftoff mg.st 1',
                            f'kill {FB.BALLS}',
                            f'execute as @a[{FB.FOOT_ZONE}] run function mg:foot/leave',
                            'execute as @a run function mg:foot/cleanup', 'tag @a remove mg.ftin',
                            'function mg:foot/hole_close',
                            'tellraw @s ' + js({'text': '⚽ Terrain de foot : désactivé (joueurs renvoyés au spawn, trou refermé).', 'color': 'red'})])
    w('foot/admin_stats', ['# Admin (@s) : compteurs d\'usage du terrain de foot (objectif mg.ftn) et score en cours (mg.ft)'] +
      [f'execute unless score {n} mg.ftn matches 0.. run scoreboard players set {n} mg.ftn 0' for n, _ in COUNTERS] +
      ['execute if score $ftoff mg.st matches 1 run tellraw @s ' + js({'text': '⚽ Terrain de foot : désactivé', 'color': 'red'}),
       'execute unless score $ftoff mg.st matches 1 run tellraw @s ' + js({'text': '⚽ Terrain de foot : activé', 'color': 'green'}),
       'tellraw @s ' + js([{'text': 'Usage : ', 'color': 'gray'}] + sum([[
           {'text': ('' if i == 0 else ' · ') + lab + ' ', 'color': 'white'},
           {'score': {'name': n, 'objective': 'mg.ftn'}, 'color': 'yellow'}] for i, (n, lab) in enumerate(COUNTERS)], [])),
       'tellraw @s ' + js([{'text': 'Score en cours : ', 'color': 'gray'}, {'text': 'Rouges ', 'color': 'red'},
                           {'score': {'name': '$ftr', 'objective': 'mg.ft'}, 'color': 'red'}, {'text': ' – ', 'color': 'gray'},
                           {'score': {'name': '$ftb', 'objective': 'mg.ft'}, 'color': 'blue'}, {'text': ' Bleus · buts libres ', 'color': 'gray'},
                           {'score': {'name': '$ftg', 'objective': 'mg.ft'}, 'color': 'yellow'}])])


def wire():
    """Boutons du menu des événements (fenêtre et menu texte) et lignes de core/opt."""
    add_buttons('lobby_events.json', [act('⚽ Foot on/off', 'green', OPT_TOGGLE, TIP_TOGGLE), act('⚽ Stats foot', 'aqua', OPT_STATS, TIP_STATS)],
                before='trigger mg.menu')
    C.patch('lobby/ev/menu_chat', chat_line(*CHAT_LAST), [chat_line('⚽ Foot on/off', 'green', OPT_TOGGLE, TIP_TOGGLE),
                                                         chat_line('⚽ Stats foot', 'aqua', OPT_STATS, TIP_STATS)])
    reset = 'scoreboard players reset @s mg.opt'
    for line in [f'execute if score @s mg.opt matches {OPT_TOGGLE}..{OPT_STATS} unless entity @s[tag=mg.admin] run tellraw @s '
                 '{"text":"⚠ Réservé aux admins.","color":"red"}',
                 f'execute if score @s mg.opt matches {OPT_TOGGLE} if entity @s[tag=mg.admin] run function mg:foot/admin_toggle',
                 f'execute if score @s mg.opt matches {OPT_STATS} if entity @s[tag=mg.admin] run function mg:foot/admin_stats']:
        C.patch('core/opt', reset, [line], where='before')
