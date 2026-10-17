"""Votes par carte (au choix : le jeu, ou une carte précise) : fonctions vote/map_*, fenêtres, crochets dans vote/*,
boutons « Voter pour une carte », « Exclure Zinedine » et « Défier en duel ».

Jamais lancé seul : gen_variants.py appelle run() après var_stars.run() (LAB lit les libellés étoilés des menus).
"""
import json
import os
import re

import var_common as VC
from var_common import act, js, load_dialog, patch, save_dialog, w
from var_data import COMBAT, FLOOR_MODES, SET, VARIANTS


# ============================================================ votes par carte (au choix : le jeu, ou une carte précise)
# mg.vote = 1000 + id de lancement → vote pour cette carte (compte aussi pour son jeu) ; 91 = menu des cartes ;
# 900 + n = cartes du jeu n. Au lancement, le jeu le plus voté (votes jeu + cartes) gagne, puis sa carte la plus votée.
def dialog_labels():
    out = {}
    for f in sorted(os.listdir(os.path.join(VC.D, 'dialog'))):
        d = json.load(open(os.path.join(VC.D, 'dialog', f), encoding='utf-8'))
        for a in d.get('actions', []) or []:
            mm = re.match(r'trigger mg\.go set (\d+)$', a.get('action', {}).get('command', ''))
            if mm and int(mm.group(1)) < 100:
                lab = ''.join(x.get('text', '') for x in a['label']) if isinstance(a['label'], list) else a['label']
                out.setdefault(int(mm.group(1)), lab.strip())
    return out


LAB = {}   # libellés des cartes d'origine (id < 100) : remplis par run(), après la réécriture des étoiles
VBYID = {v['id']: v for v in VARIANTS}
# (n° de vote du jeu, joueur fictif du compteur, nom, couleur, ids des cartes)
VG = [
    (1, 'Spleef', '❄ Spleef', 'aqua', [1] + [v['id'] for v in FLOOR_MODES[0]['vars']]),
    (2, 'TNT-Run', '✷ TNT Run', 'red', [2] + [v['id'] for v in FLOOR_MODES[1]['vars']]),
    (8, 'Splegg', '❍ Splegg', 'yellow', [20, 21] + [v['id'] for v in FLOOR_MODES[2]['vars']]),
    (9, 'Sumo', '✊ Sumo', 'gold', [22, 24]),
    (13, 'Enclumes', '⚓ Pluie d\'Enclumes', 'gray', [29, 42]),
    (3, 'PvP', '⚔ Arène PvP', 'yellow', [3, 44, 47, 50] + [v['id'] for v in COMBAT[0]['vars']]),
    (4, 'PvP-classes', '⚔ PvP classes', 'gold', [13, 45, 48, 51]),
    (17, 'One-in-Chamber', '➶ One in the Chamber', 'gold', [26, 52, 53] + [v['id'] for v in COMBAT[1]['vars']]),
    (15, 'Quakecraft', '⚡ Quakecraft', 'aqua', [31, 32, 33, 34, 35, 43, 46, 49, 79, 80] + [v['id'] for v in COMBAT[2]['vars']]),
    (11, 'TNT-Tag', '✹ TNT Tag', 'red', [67, 68, 69, 70] + [v['id'] for v in COMBAT[3]['vars']]),
    (5, 'Bedwars', '⚑ Bedwars', 'light_purple', [71, 72, 73, 74]),
    (6, 'Sheep-War', '☁ Sheep War', 'white', [5, 7, 14, 15, 16, 17, 18, 19]),
    (16, 'Paintball', '▓ Paintball', 'gold', [36, 54, 55]),
    (7, 'Mob-Arena', '☠ Mob Arena', 'dark_green', [6, 8, 9, 10, 11, 12, 37, 38, 39, 40, 41]),
    (10, 'Dropper', '⬇ The Dropper', 'aqua', [23, 25, 64, 65, 228]),
    (21, 'Elytra', '🪽 Élytra', 'aqua', [75, 76, 77]),
]


def map_name(i):
    if i in VBYID:
        v = VBYID[i]
        return f'✦ {v["map"]["name"]} ' + '★' * v['dif'] + '☆' * (4 - v['dif'])
    return LAB.get(i, str(i))


def run():
    LAB.clear()
    LAB.update(dialog_labels())

    L = ['# Votes par carte : compteurs #vm<id> (mg.st), ajoutés au total du jeu (mg.vb). Appelé par vote/refresh. Généré.']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L += [f'execute store result score #vm{i} mg.st if entity @a[scores={{mg.vc={1000 + i}}}]',
                  f'execute if score #vm{i} mg.st matches 1.. run scoreboard players operation {fake} mg.vb += #vm{i} mg.st']
    w('vote/map_refresh', L)

    L = ['# @s vote pour une carte (mg.vote = 1000 + id). Généré.',
         'scoreboard players operation @s mg.vc = @s mg.vote', 'function mg:vote/refresh',
         'execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 1 1.4']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L.append(f'execute if score @s mg.vote matches {1000 + i} run tellraw @s ' + js([
                {'text': '☑ Tu votes pour : ', 'color': 'gray'}, {'text': name, 'color': col, 'bold': True},
                {'text': ' — carte ', 'color': 'gray'}, {'text': map_name(i), 'color': 'white'},
                {'text': ' (', 'color': 'gray'}, {'score': {'name': fake, 'objective': 'mg.vb'}, 'color': 'gold'},
                {'text': ' vote(s) pour ce jeu)', 'color': 'gray'}]))
            L.append(f'execute if score @s mg.vote matches {1000 + i} run tellraw @a[tag=mg.admin] ' + js([
                {'text': '☑ ', 'color': 'green'}, {'selector': '@s', 'color': 'yellow'}, {'text': ' vote pour ', 'color': 'gray'},
                {'text': f'{name} — {map_name(i)}', 'color': col}]))
    w('vote/map_choose', L)

    L = ['# Le jeu $vwin a gagné : sa carte la plus votée (égalité : au hasard) remplace la carte par défaut (@s = admin). Généré.',
         'scoreboard players set $vmm mg.st 0']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L.append(f'execute if score $vwin mg.st matches {n} run scoreboard players operation $vmm mg.st > #vm{i} mg.st')
    L += ['execute if score $vmm mg.st matches 0 run return 0', 'scoreboard players set $vmc mg.st 0']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L.append(f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st run scoreboard players add $vmc mg.st 1')
    L += ['execute store result score $vmk mg.st run random value 0..9999', 'scoreboard players operation $vmk mg.st %= $vmc mg.st',
          'scoreboard players add $vmk mg.st 1']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L += [f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st run scoreboard players remove $vmk mg.st 1',
                  f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st if score $vmk mg.st matches 0 run scoreboard players set @s mg.go {i}',
                  f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st if score $vmk mg.st matches 0 run tellraw @a ' + js([
                      {'text': '☑ Carte la plus votée : ', 'color': 'gray'}, {'text': map_name(i), 'color': col, 'bold': True},
                      {'text': ' (', 'color': 'gray'}, {'score': {'name': f'#vm{i}', 'objective': 'mg.st'}, 'color': 'gold'}, {'text': ' vote(s))', 'color': 'gray'}])]
    w('vote/map_pick', L)

    L = ['# Détail des votes par carte (@s), après vote/show. Généré.']
    for n, fake, name, col, ids in VG:
        for i in ids:
            L.append(f'execute if score #vm{i} mg.st matches 1.. run tellraw @s ' + js([
                {'text': '    ↳ carte ', 'color': 'dark_gray'}, {'text': f'{name} — {map_name(i)}', 'color': col},
                {'text': ' : ', 'color': 'gray'}, {'score': {'name': f'#vm{i}', 'objective': 'mg.st'}, 'color': 'gold'}]))
    w('vote/map_show', L)

    # menus de vote par carte
    acts = []
    for n, fake, name, col, ids in VG:
        acts.append(act(f'{name} ▸', col, f'trigger mg.vote set {900 + n}', f'{len(ids)} cartes'))
    acts.append(act('« Retour aux votes', 'yellow', 'trigger mg.vote set 97'))
    save_dialog('vote_maps', {'type': 'minecraft:multi_action', 'title': {'text': '🗺 VOTE : une carte précise', 'color': 'green', 'bold': True},
                              'pause': False, 'can_close_with_escape': True,
                              'body': [{'type': 'minecraft:plain_message', 'contents': [
                                  {'text': 'Choisis un jeu puis la carte. Ton vote compte pour le jeu ; si le jeu gagne, sa carte la plus votée est jouée.', 'color': 'gray'}]}],
                              'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': acts})
    OPENL = ['# Menus de vote par carte (@s = joueur, mg.vote = 91 ou 900 + n). Généré.',
             'execute if score @s mg.vote matches 91 run function mg:vote/map_menu {d:"vote_maps",n:0}']
    for n, fake, name, col, ids in VG:
        acts = [act(f'🎲 {name} (carte au hasard)', col, f'trigger mg.vote set {n}', 'Vote pour le jeu, sans choisir la carte')]
        for i in ids:
            tip = None
            if i in VBYID:
                v = VBYID[i]
                tip = f'Variante : carte {v["map"]["src"]} ({v["map"]["desc"]}) · réglages : {SET[v["mode"]["key"]][v["dif"] - 1]}'
            acts.append(act(map_name(i), 'gold' if i in VBYID else 'white', f'trigger mg.vote set {1000 + i}', tip))
        acts.append(act('« Autres jeux', 'yellow', 'trigger mg.vote set 91'))
        save_dialog(f'vote_m{n}', {'type': 'minecraft:multi_action', 'title': {'text': f'🗺 VOTE : {name}', 'color': col, 'bold': True},
                                   'pause': False, 'can_close_with_escape': True,
                                   'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Vote pour une carte : cartes d’origine puis ✦ variantes ; ★ facile → ★★★★ difficile.', 'color': 'gray'}]}],
                                   'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': acts})
        OPENL.append(f'execute if score @s mg.vote matches {900 + n} run function mg:vote/map_menu {{d:"vote_m{n}",n:{n}}}')
        C = [f'# Repli chat : cartes de {name} (@s). Généré.',
             'tellraw @s ' + js([{'text': f'\n🗺 VOTE : {name} ', 'color': col, 'bold': True}, {'text': '(clique une carte)', 'color': 'gray'}])]
        for i in ids:
            C.append('tellraw @s ' + js(['', {'text': f' [{map_name(i)}]', 'color': 'gold' if i in VBYID else 'white',
                                              'click_event': {'action': 'run_command', 'command': f'trigger mg.vote set {1000 + i}'}}]))
        w(f'vote/map_chat_{n}', C)
    w('vote/map_open', OPENL)
    w('vote/map_menu', ['# Macro : ouvre la fenêtre $(d), sinon le menu chat des cartes du jeu $(n). Généré.',
                        'scoreboard players set $dlg mg.st 0',
                        '$execute store success score $dlg mg.st run dialog show @s mg:$(d)',
                        'execute if score $dlg mg.st matches 1 run return 0',
                        '$execute if score $dlg mg.st matches 0 run function mg:vote/map_chat {n:$(n)}'])
    w('vote/map_chat', ['# Macro : repli chat des cartes du jeu $(n) (0 = liste des jeux). Généré.', '$function mg:vote/map_chat_$(n)'])
    C = ['# Repli chat : liste des jeux pour voter une carte (@s). Généré.',
         'tellraw @s ' + js([{'text': '\n🗺 VOTE : une carte précise ', 'color': 'green', 'bold': True}, {'text': '(choisis le jeu)', 'color': 'gray'}])]
    for n, fake, name, col, ids in VG:
        C.append('tellraw @s ' + js(['', {'text': f' [{name} ▸]', 'color': col, 'click_event': {'action': 'run_command', 'command': f'trigger mg.vote set {900 + n}'}}]))
    w('vote/map_chat_0', C)

    # crochets
    patch('vote/cast', 'execute if score @s mg.vote matches 1..21 run function mg:vote/choose', [
        'execute if score @s mg.vote matches 1001..1199 run function mg:vote/map_choose',
        'execute if score @s mg.vote matches 91 run function mg:vote/map_open',
        'execute if score @s mg.vote matches 901..921 run function mg:vote/map_open'])
    patch('vote/refresh', 'function mg:vote/sidebar', ['function mg:vote/map_refresh'], where='before')
    patch('vote/launch', 'function mg:core/go', ['function mg:vote/map_pick'], where='before')
    p = os.path.join(VC.F, 'vote/show.mcfunction')
    if 'function mg:vote/map_show' not in open(p, encoding='utf-8').read():
        with open(p, 'a', encoding='utf-8', newline='\n') as f:
            f.write('\nfunction mg:vote/map_show\n')
    VBTN = act('🗺 Voter pour une carte ▸', 'green', 'trigger mg.vote set 91', 'Choisis la carte précise (cartes d’origine et variantes ★)', True)
    for name in ('vote', 'vote_pvp'):
        d = load_dialog(name)
        if not any(a.get('action', {}).get('command') == 'trigger mg.vote set 91' for a in d['actions']):
            d['actions'].insert(0, VBTN)
            save_dialog(name, d)
    # 🚫 « Exclure Zinedine » (running gag) : aussi dans le menu des joueurs (fenêtre de vote) et son menu texte
    ZBTN = act('🚫 Exclure Zinedine', 'red', 'trigger mg.opt set 49', 'Exclut Zinedine du serveur (définitivement, cette fois)')
    d = load_dialog('vote')
    if not any(a.get('action', {}).get('command') == 'trigger mg.opt set 49' for a in d['actions']):
        d['actions'].append(ZBTN)
        save_dialog('vote', d)
    patch('vote/chat', 'tellraw @s [{"text":"\\n☑ VOTE : quel jeu veux-tu jouer ? ","color":"green","bold":true},{"text":"(clique)","color":"gray"}]',
          ['tellraw @s ' + js(['', {'text': ' [🚫 Exclure Zinedine]', 'color': 'red',
                                    'click_event': {'action': 'run_command', 'command': 'trigger mg.opt set 49'}}])])
    patch('vote/chat', 'tellraw @s [{"text":"\\n☑ VOTE : quel jeu veux-tu jouer ? ","color":"green","bold":true},{"text":"(clique)","color":"gray"}]',
          ['tellraw @s ' + js(['', {'text': ' [🗺 Voter pour une carte précise ▸]', 'color': 'green', 'bold': True,
                                    'click_event': {'action': 'run_command', 'command': 'trigger mg.vote set 91'}}])])
    # ⚔ « Défier en duel » : dans la fenêtre de vote des joueurs (les admins l'ouvrent par « 👁 Voir le menu joueur », opt 66),
    # pas dans vote_pvp : simple sous-menu du vote PvP, on y arrive depuis vote
    DUEL_TIP = 'Sniper 1v1 : tête = élimination, corps = 2 touches, premier à 3 manches'
    DBTN = act('⚔ Défier en duel', 'red', 'trigger mg.duel set 1', DUEL_TIP)
    d = load_dialog('vote')
    if not any(a.get('action', {}).get('command') == 'trigger mg.duel set 1' for a in d['actions']):
        pl = [i for i, a in enumerate(d['actions']) if a.get('action', {}).get('command') == 'trigger mg.pl set 1']
        d['actions'].insert(pl[0] if pl else len(d['actions']), DBTN)   # avant les boutons de plot, sinon en fin de liste
        save_dialog('vote', d)
    # patch() pose « après l'ancre » : placé après les deux précédents, ce crochet s'affiche en premier (ligne duel avant carte et Zinedine)
    # idempotence sur la commande (pas sur le texte de la ligne) : changer libellé ou tooltip plus tard ne dupliquera pas la ligne
    if 'trigger mg.duel set 1' not in open(os.path.join(VC.F, 'vote/chat.mcfunction'), encoding='utf-8').read():
        patch('vote/chat', 'tellraw @s [{"text":"\\n☑ VOTE : quel jeu veux-tu jouer ? ","color":"green","bold":true},{"text":"(clique)","color":"gray"}]',
              ['tellraw @s ' + js(['', {'text': ' [⚔ Défier en duel]', 'color': 'red',
                                        'click_event': {'action': 'run_command', 'command': 'trigger mg.duel set 1'},
                                        'hover_event': {'action': 'show_text', 'value': DUEL_TIP}}])])
