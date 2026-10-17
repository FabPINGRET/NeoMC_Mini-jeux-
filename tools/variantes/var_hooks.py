"""Crochets « [variantes] » dans les fichiers des jeux existants (idempotents : patch / replace de var_common),
et tag de blocs traversés par le rayon du Quake.

Jamais lancé seul : gen_variants.py appelle run() après var_common.init().
"""
import os

import var_common as VC
from var_common import js, patch, replace, wjson
from var_data import VARIANTS

# ============================================================ crochets dans les fichiers existants (idempotents)
MARK = '[variantes]'

VR = 'execute if score $ar mg.st matches 1.. run return run function mg:var/'


def run():
    # tag de blocs traversés par le rayon du Quake
    wjson(os.path.join(VC.D, 'tags/block/ray_pass.json'), {'values': [
        '#minecraft:air', 'minecraft:short_grass', 'minecraft:tall_grass', 'minecraft:fern', 'minecraft:large_fern',
        '#minecraft:small_flowers', 'minecraft:dead_bush', '#minecraft:wool_carpets', 'minecraft:moss_carpet',
        'minecraft:water', 'minecraft:snow', 'minecraft:vine', 'minecraft:light', 'minecraft:sugar_cane',
        {'id': 'minecraft:short_dry_grass', 'required': False}, {'id': 'minecraft:tall_dry_grass', 'required': False},
        {'id': 'minecraft:bush', 'required': False}, {'id': 'minecraft:leaf_litter', 'required': False}]})

    # core
    patch('core/request', 'scoreboard players reset @s mg.go', [
        f'# {MARK} ids 100..196 : carte d\'un autre jeu + difficulté ($ar, $dif) ; $ar = 0 → carte native',
        'scoreboard players set $ar mg.st 0',
        'scoreboard players set $dif mg.st 2',
        'execute if score $game mg.st matches 100..196 run function mg:var/remap'])
    patch('core/request', '# Préparation de l\'arène + téléportation', [
        f'# {MARK} annonce de la variante puis $game = jeu réel',
        'execute if score $ar mg.st matches 1.. run function mg:var/start'], where='before')
    if 'matches 100..196' not in open(os.path.join(VC.F, 'core/go.mcfunction'), encoding='utf-8').read():
        replace('core/go', 'execute unless score @s mg.go matches 1..78 run return run scoreboard players reset @s mg.go',
                'execute unless score @s mg.go matches 1..78 unless score @s mg.go matches 100..196 run return run scoreboard players reset @s mg.go')
    patch('core/forceloads', 'function mg:tnttag/map/fl', [f'# {MARK} sols des variantes (z 24300)', 'function mg:var/fl'])
    patch('core/opt', 'execute if score @s mg.opt matches 1 run function mg:core/opt_spec', [
        'execute if score @s mg.opt matches 32..39 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins.","color":"red"}',
        'execute if score @s mg.opt matches 32..39 if entity @s[tag=mg.admin] run function mg:var/menu/open'], where='before')

    # PvP
    patch('pvp/prepare', '# Arène PvP — préparation', [VR + 'mode/pvp_prepare'])
    replace('pvp/tick', 'execute as @a[tag=mg.play,scores={mg.t=..55}] run function mg:core/eliminate',
            'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..55}] run function mg:core/eliminate\n'
            f'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate')
    patch('pvp/go', 'tellraw @a[tag=mg.play] [{"text":"⚔ Chacun pour soi : dernier survivant = gagnant !","color":"yellow"}]',
          ['execute if score $ar mg.st matches 1.. run function mg:var/mode/pvp_go'])

    # One in the Chamber
    patch('oitc/prepare', '# One in the Chamber — préparation (centre 0 ~ 5800)', [VR + 'mode/oitc_prepare'])
    replace('oitc/death', 'execute if score $om mg.st matches 0 run spreadplayers 0 5800 5 10 under 90 false @s',
            'execute if score $ar mg.st matches 1.. run function mg:var/spread_one\n'
            'execute if score $ar mg.st matches 0 if score $om mg.st matches 0 run spreadplayers 0 5800 5 10 under 90 false @s')
    replace('oitc/death', 'execute if score $om mg.st matches 1 run spreadplayers',
            'execute if score $ar mg.st matches 0 if score $om mg.st matches 1 run spreadplayers')
    replace('oitc/death', 'execute if score $om mg.st matches 2 run spreadplayers',
            'execute if score $ar mg.st matches 0 if score $om mg.st matches 2 run spreadplayers')
    replace('oitc/tick', 'execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:oitc/death',
            'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..70}] run function mg:oitc/death\n'
            'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:oitc/death')
    replace('oitc/tick', 'execute if score $os mg.st matches 600.. run function mg:oitc/special_timer',
            'execute if score $os mg.st >= $osi mg.st run function mg:oitc/special_timer')
    replace('oitc/tick', 'execute if score $state mg.st matches 2 as @a[tag=mg.play,scores={mg.ok=10..},limit=1] run function mg:core/win_player',
            'execute if score $state mg.st matches 2 as @a[tag=mg.play] if score @s mg.ok >= $og mg.st run return run function mg:core/win_player')
    patch('oitc/go', 'scoreboard players set $og mg.st 10', ['scoreboard players set $osi mg.st 600',
                                                              'execute if score $ar mg.st matches 1.. run function mg:var/mode/oitc_go'])
    replace('oitc/kill_reward', '{"text":" / 10  ","color":"gray"}',
            '{"text":" / ","color":"gray"},{"score":{"name":"$og","objective":"mg.st"},"color":"gray"},{"text":"  ","color":"gray"}')

    # Quakecraft
    patch('quake/prepare', '# Quakecraft — préparation (carte $qm : 0 néon, 1 volcan XL, 2 jungle XL, 3 désert, 4 glacier mini)',
          ['scoreboard players set $qcd mg.st 22', VR + 'mode/quake_prepare'])
    patch('quake/spread_one', '# Quakecraft — placement aléatoire selon la carte (@s)', [VR + 'spread_one'])
    replace('quake/tick', 'execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:quake/respawn',
            'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..70}] run function mg:quake/respawn\n'
            'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:quake/respawn')
    replace('quake/shoot', 'scoreboard players set @s mg.cd 22', 'scoreboard players operation @s mg.cd = $qcd mg.st')
    replace('quake/ray', 'execute unless block ~ ~ ~ #minecraft:air run return run', 'execute unless block ~ ~ ~ #mg:ray_pass run return run')

    # TNT Tag
    patch('tnttag/prepare', 'tag @a remove mg.bomb', [VR + 'mode/tnttag_prepare'])
    patch('tnttag/go', 'scoreboard players set $mx mg.st 600', ['scoreboard players set $ttb mg.st 200',
                                                                 'execute if score $ar mg.st matches 1.. run function mg:var/mode/tnttag_go'])
    replace('tnttag/new_round', 'scoreboard players add $tt mg.st 200', 'scoreboard players operation $tt mg.st += $ttb mg.st')

    # Spleef
    patch('spleef/prepare', '# Spleef — préparation (appelé au lancement)', [VR + 'mode/spleef_prepare'])
    patch('spleef/go', 'scoreboard players set $sk mg.st 800', ['execute if score $ar mg.st matches 1.. run function mg:var/mode/spleef_go'])
    patch('spleef/shrink', '# Spleef — l\'arène rétrécit (appelé toutes les 12 s après les 40 premières secondes)', [VR + 'floor/shrink'])
    patch('spleef/top_check', 'scoreboard players set $tfn mg.st 0', [VR + 'floor/top_check'], where='before')

    # TNT Run
    patch('tntrun/prepare', '# TNT Run — préparation', [VR + 'mode/tntrun_prepare'])
    replace('tntrun/tick', 'execute as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate',
            'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate\n'
            'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate')
    patch('tntrun/decay', '# (un bloc piétiné disparaît entre 9 et 18 ticks plus tard, jamais instantanément)', [VR + 'floor/decay'])

    # Splegg
    patch('splegg/prepare', '# Splegg — préparation (centre 0 ~ 4200) ; $sg = 1 → version XXL', [VR + 'mode/splegg_prepare'])
    patch('splegg/shoot', 'scoreboard players set $rs mg.st 160', ['execute if score $ar mg.st matches 1.. run scoreboard players operation $rs mg.st = $vrs mg.st'])
    patch('splegg/hit', 'execute if score $sg mg.st matches 1 run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:snow_block',
          ['execute if score $ar mg.st matches 1.. if score $vcr mg.st matches 1 run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:snow_block'])
    patch('splegg/top_check', 'scoreboard players set $tfn mg.st 0', [VR + 'floor/top_check'], where='before')

    # désinstallation
    patch('desinstaller', 'forceload remove all', ['data remove storage mg:var a'])

    # menu texte : bouton Variantes
    patch('core/menu_chat', 'tellraw @s ["",{"text":" [🪽 Élytra ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 31"},"hover_event":{"action":"show_text","value":"Course d\'anneaux, course + combat, survie en vol"}}]',
          ['tellraw @s ' + js(['', {'text': f' [★ Variantes ({len(VARIANTS)}) ▸]', 'color': 'gold',
                                    'click_event': {'action': 'run_command', 'command': 'trigger mg.opt set 32'},
                                    'hover_event': {'action': 'show_text', 'value': 'Chaque mode sur les cartes des autres jeux, de ★ à ★★★★'}}])])
