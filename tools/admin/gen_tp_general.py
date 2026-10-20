"""TP général (admin) : envoie tous les joueurs disponibles vers un monde (survie, Neo GTA… extensible).

    python tools/admin/gen_tp_general.py .      (depuis la racine du dépôt ; idempotent ; AVANT tools/duel/gen_duel.py,
    qui ajoute une ligne à tpg/lobby, réécrit en entier ici)

Menu principal → « 🌍 TP général (admin) ▸ » (mg.opt 62) → fenêtre mg:tp_general → une destination (mg.opt 63..) :
survie, Neo GTA, Terra Nova, Ombrelune, ou retour de tous au lobby (sortie des activités secondaires avant de lancer un mini-jeu).
Ids : 63..65 (survie, GTA, lobby), 75 (Terra Nova) et 88 (Ombrelune) : 59 et 61 fusionneraient la plage 62..65 sur laquelle gen_events.py et theme_core.py s'ancrent.
Joueurs concernés : tous sauf ceux d'une partie en cours (mg.play / mg.out) et de la Mini Party (mg.mpp).
Pour ajouter une destination : une entrée dans DEST + sa fonction tpg/<clé>.
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
OPEN_OPT = 62
FREE = 'tag=!mg.play,tag=!mg.out,tag=!mg.mpp'

# clé, libellé, couleur, info-bulle, mg.opt, lignes de la fonction tpg/<clé>
DEST = [
    ('survie', '🌲 Tout le monde → Survie', 'green', 'Les joueurs à Neo GTA, Terra Nova ou Ombrelune en sortent d\'abord (tout est sauvegardé)', 63, [
        '# TP général → survie (@s = admin)',
        f'execute as @a[{FREE},tag=mg.gtw] run function mg:gta/leave',
        f'execute as @a[{FREE},tag=mg.tvw] run function mg:terra/leave',
        f'execute as @a[{FREE},tag=mg.olw] run function mg:ombre/leave',
        f'execute as @a[{FREE},tag=!mg.surv] run function mg:survie/enter',
        'tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde en survie.","color":"gray"}]']),
    ('gta', '🚓 Tout le monde → Neo GTA', 'gold', 'Les joueurs en survie ou sur leur plot en sortent d\'abord (tout est sauvegardé)', 64, [
        '# TP général → Neo GTA (@s = admin)',
        'execute unless data storage mg:gta built run return run function mg:gta/not_ready',
        f'execute as @a[{FREE},tag=mg.surv,tag=!mg.gtw] run function mg:survie/leave',
        f'execute as @a[{FREE},tag=mg.inplot] run function mg:plot/leave',
        f'execute as @a[{FREE},tag=!mg.gtw,tag=!mg.dl] run function mg:gta/enter',
        'tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde à Neo GTA.","color":"gray"}]']),
    ('terra', '🦖 Tout le monde → Terra Nova', 'dark_green', 'Les joueurs en survie, à Neo GTA ou sur leur plot en sortent d\'abord (tout est sauvegardé)', 75, [
        '# TP général → Terra Nova (@s = admin)',
        'execute unless data storage mg:terra built run return run function mg:terra/not_ready',
        f'execute as @a[{FREE},tag=mg.surv,tag=!mg.tvw] run function mg:survie/leave',
        f'execute as @a[{FREE},tag=mg.inplot] run function mg:plot/leave',
        f'execute as @a[{FREE},tag=!mg.tvw,tag=!mg.dl] run function mg:terra/enter',
        'tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde à Terra Nova.","color":"gray"}]']),
    ('ombre', '🌙 Tout le monde → Ombrelune', 'light_purple', 'Les joueurs en survie, à Neo GTA, à Terra Nova ou sur leur plot en sortent d\'abord (tout est sauvegardé)', 88, [
        '# TP général → Ombrelune (@s = admin)',
        'execute unless data storage mg:ombre built run return run function mg:ombre/not_ready',
        f'execute as @a[{FREE},tag=mg.surv,tag=!mg.olw] run function mg:survie/leave',
        f'execute as @a[{FREE},tag=mg.inplot] run function mg:plot/leave',
        f'execute as @a[{FREE},tag=!mg.olw,tag=!mg.dl] run function mg:ombre/enter',
        'tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a envoyé tout le monde à Ombrelune.","color":"gray"}]']),
    ('lobby', '🏠 Tout le monde → Lobby', 'yellow', 'Sort tout le monde de la survie, de Neo GTA, de Terra Nova, d\'Ombrelune, des plots, du kart, du parkour, des élytra et de la montagne russe : prêt pour lancer un mini-jeu', 65, [
        '# TP général → lobby (@s = admin) : chacun quitte proprement son activité (sauvegardes comprises), puis remise à zéro au spawn',
        f'execute as @a[{FREE},tag=mg.gtw] run function mg:gta/leave',
        f'execute as @a[{FREE},tag=mg.tvw] run function mg:terra/leave',
        f'execute as @a[{FREE},tag=mg.olw] run function mg:ombre/leave',
        f'execute as @a[{FREE},tag=mg.surv,tag=!mg.gtw] run function mg:survie/leave',
        f'execute as @a[{FREE},tag=mg.inplot] run function mg:plot/leave',
        f'execute as @a[{FREE},tag=mg.visit] run function mg:plot/leave',
        f'execute as @a[{FREE},tag=mg.lk] run function mg:lobkart/leave',
        f'execute as @a[{FREE},tag=mg.pkr] run function mg:parkour/quit',
        f'execute as @a[{FREE},tag=mg.ely] run function mg:elytra/stop_quiet',
        f'execute as @a[{FREE},tag=mg.elyf] run function mg:elytra/free_stop',
        f'execute as @a[{FREE}] if predicate mg:coaster_riding run ride @s dismount',
        f'execute as @a[{FREE}] run function mg:core/reset_player',
        'tellraw @a [{"text":"🌍 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a ramené tout le monde au lobby.","color":"gray"}]']),
]


def w(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def act(label, col, cmd, tip=None):
    a = {'label': [{'text': label, 'color': col}], 'action': {'type': 'minecraft:run_command', 'command': cmd}}
    if tip:
        a['tooltip'] = [{'text': tip, 'color': 'gray'}]
    return a


dialog = {'type': 'minecraft:multi_action', 'title': {'text': '🌍 TP général', 'color': 'gold', 'bold': True},
          'pause': False, 'can_close_with_escape': True,
          'body': [{'type': 'minecraft:plain_message', 'contents': [
              {'text': 'Envoie tous les joueurs (hors partie en cours) vers un monde.', 'color': 'gray'}]}],
          'columns': 1, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]},
          'actions': [act(l, c, f'trigger mg.opt set {o}', t) for _, l, c, t, o, _ in DEST] +
                     [act('« Retour au menu', 'yellow', 'trigger mg.menu')]}
os.makedirs(os.path.join(R, 'data/mg/dialog'), exist_ok=True)
with open(os.path.join(R, 'data/mg/dialog/tp_general.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(dialog, f, ensure_ascii=False, indent=2)
    f.write('\n')

w('tpg/open', ['# Fenêtre du TP général (@s = admin), sinon liens dans le chat',
               'scoreboard players set $dlg mg.st 0',
               'execute store success score $dlg mg.st run dialog show @s mg:tp_general',
               'execute unless score $dlg mg.st matches 1 run tellraw @s ' + json.dumps(
                   [{'text': '🌍 TP général : ', 'color': 'gold', 'bold': True}] +
                   [{'text': f'[{l}] ', 'color': c, 'bold': False, 'click_event': {'action': 'run_command', 'command': f'trigger mg.opt set {o}'}}
                    for _, l, c, _, o, _ in DEST], ensure_ascii=False)])
for k, _, _, _, _, lines in DEST:
    w(f'tpg/{k}', lines)
OPTS = sorted({OPEN_OPT} | {o for *_, o, _ in DEST})
RANGES = []
for o in OPTS:
    if RANGES and o == RANGES[-1][1] + 1:
        RANGES[-1][1] = o
    else:
        RANGES.append([o, o])
w('tpg/run', ['# mg.opt 62.. : TP général (@s = joueur)',
              f'execute unless entity @s[tag=mg.admin] run return run tellraw @s {{"text":"⚠ Réservé aux admins.","color":"red"}}',
              f'execute if score @s mg.opt matches {OPEN_OPT} run return run function mg:tpg/open'] +
  [f'execute if score @s mg.opt matches {o} run function mg:tpg/{k}' for k, _, _, _, o, _ in DEST])

# branchement dans core/opt (avant la remise à zéro finale)
p = os.path.join(F, 'core/opt.mcfunction')
t = open(p, encoding='utf-8').read().split('\n')
new_lines = [f'execute if score @s mg.opt matches {a}..{b} run function mg:tpg/run' if a != b else f'execute if score @s mg.opt matches {a} run function mg:tpg/run'
             for a, b in RANGES]
t = [l for l in t if not (l.startswith('execute if score @s mg.opt matches ') and l.endswith(' run function mg:tpg/run'))]
i = t.index('scoreboard players reset @s mg.opt')
t[i:i] = new_lines
open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(t))
print('TP général OK :', ', '.join(k for k, *_ in DEST))

# Les notes des joueurs remplacent les étoiles dans les menus : à refaire après chaque régénération des menus
import runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rating', 'gen_rating.py'), run_name='__main__')
