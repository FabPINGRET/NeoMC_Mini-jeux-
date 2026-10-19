"""🎣 Pêche à l'étang : socle, canne, garde et entretien (importé par gen_fish.py, fish_game.py et fish_admin.py, jamais lancé seul).

Un socle de bois (SOCLE, sur la berge de l'étang du spawn : POND de gen_lobby.py) porte une zone cliquable (interaction, tags mg.lfs et mg.lfi)
et un panneau (text_display, tag mg.lfs, sans mg.lby : lobby/deco tuerait tout ce qui le porte). Clic droit : prend la canne, ou la range si
le joueur l'a déjà. La pêche reste ouverte toute l'année (l'étang ne gèle pas sous le thème Noël : gen_themes.py).
- Canne : fishing_rod incassable marquée (custom_data mg_rod), rangée en hotbar.7 (ou donnée si le slot est pris). Rien de pêché ne reste dans
  l'inventaire (le spawn est en aventure) : la prise est virtuelle, tirée par fish_game.py (advancement mg:lobby_fish -> lobby/fish/catch).
- Garde (lobby/fish/keep, sans message) : overworld, pêche pas coupée par un admin, dans le spawn, ni spectateur ni occupé ailleurs (BUSY de
  sit_item.py, la même liste que sit et emotes) et à moins de FISH_R blocs du centre de l'étang. Qui ne la garde pas perd la canne.
- Toutes les 2 s (core/tick, $lan mg.t = 30) : lobby/fish/second tue les cannes jetées au sol, purge les conteneurs du spawn et du Hall
  (SI.containers : liste relue dans les constructions, jamais écrite à la main), retire la canne à qui ne la garde pas, reporte la stat
  vanilla mg.lfu dans $use (mg.lfn), et refait les deux entités du socle s'il en manque.
- lobby/fish/after (core/tick, tant qu'un joueur porte mg.lfc ou qu'un marqueur mg.lfm reste : joueur déconnecté) : le tick suivant une prise, tue les objets de la ligne (à moins de 1,5 du
  marqueur mg.lfm posé à l'hameçon) et les orbes d'XP (à moins de 2 du joueur) : la fonction #minecraft:tick passe AVANT l'avancement des
  entités, ces objets n'ont donc pas encore bougé. Pas de récompense en XP : la barre d'XP affiche le rang.
- lobby/fish/build (core/tick : bloc du socle absent) pose le bloc puis les entités. Fichiers : lobby/fish/* ; advancements mg:lobby_fish_take
  (clic sur le socle) et mg:lobby_fish (hameçon remonté avec un objet ; accroché à une entité, le contexte du trigger n'est plus l'hameçon : écarté par `entity`).
Tags : mg.lfs (entités du socle), mg.lfi (zone cliquable), mg.lfc (joueur qui vient de pêcher), mg.lfm (marqueur à l'hameçon), mg.lfx (marqueur
de la prise en cours, voir fish_game.py). Objectifs : mg.lfb (record en cm), mg.lfn (compteurs), mg.lfu (stat used:fishing_rod). C.D / C.F sont
ceux de gen_fish.py (C.init déjà appelé).
"""
import json
import os

import common as C
import sit_item as SI
from foot_build import TF
from theme_world import LOBBY_BOX

# bloc du socle (berge est de l'étang, à 7 blocs de son centre) : sol (y 63) plein, colonne y 64..66 libre ; HORS des boîtes d'eau de
# theme_water.boxes (x 22..35, z -35..-22 autour de l'étang : water_fix n'y tolère aucune zone modifiée ailleurs, et fish/build en est une)
SOCLE = (36, 64, -27)
POND_C = '30.5 64 -29.5'                 # centre de l'étang (POND = (30, -30, 6.6) de gen_lobby.py), pieds des joueurs
FISH_R = 12                              # rayon de garde de la canne autour du centre de l'étang
SLOT = 'hotbar.7'                        # le spawn n'utilise que hotbar.0..4 ; hotbar.8 est l'objet emotes
PRED = '*[minecraft:custom_data~{mg_rod:1b}]'
ROD = ('minecraft:fishing_rod[custom_data={mg_rod:1b},unbreakable={},'
       'custom_name=[{"text":"🎣 Canne du spawn","color":"aqua","bold":true,"italic":false}],'
       'lore=[[{"text":"Lance ta ligne dans l\'étang : les prises sont virtuelles","color":"gray","italic":false}]]]')
POS = ' '.join(map(str, SOCLE))
LOG = 'minecraft:spruce_log'
PURGE = 'Items[{components:{"minecraft:custom_data":{mg_rod:1b}}}]'
KEEP_SEL = f'@s[{LOBBY_BOX},' + ','.join(f'tag=!{t}' for t in SI.BUSY) + ',gamemode=!spectator]'
DROPPED = f'execute as @e[type=minecraft:item] if items entity @s contents {PRED} run kill @s'


def adv(name, data):
    os.makedirs(os.path.join(C.D, 'advancement'), exist_ok=True)
    with open(os.path.join(C.D, 'advancement', name + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def bar(text, color):
    return 'title @s actionbar ' + C.js({'text': text, 'color': color})


def write(containers):
    """Écrit lobby/fish/{take, keep, second, purge, build, entities, after} et les advancements ; containers = SI.containers()."""
    w, js = C.w, C.js
    w('lobby/fish/take', ['# @s : a cliqué sur le socle de la canne (advancement mg:lobby_fish_take) : prend la canne, ou la range s\'il l\'a déjà',
                          'advancement revoke @s only mg:lobby_fish_take',
                          'execute if score $lfoff mg.st matches 1 run return run ' + bar('🎣 Pêche désactivée par un admin.', 'red'),
                          'execute unless function mg:lobby/fish/keep run return run ' + bar('🎣 Pas possible ici (au spawn, hors activité).', 'red'),
                          '# canne déjà dans l\'inventaire : on la range',
                          f'execute store result score #lfi mg.st run clear @s {PRED} 0',
                          f'execute if score #lfi mg.st matches 1.. run clear @s {PRED}',
                          'execute if score #lfi mg.st matches 1.. run ' + bar('🎣 Canne rangée.', 'gray'),
                          'execute if score #lfi mg.st matches 1.. run return 0',
                          'scoreboard players add $rod mg.lfn 1',
                          f'execute if items entity @s {SLOT} * run give @s {ROD}',
                          f'execute unless items entity @s {SLOT} * run item replace entity @s {SLOT} with {ROD}',
                          bar('🎣 Canne en main : lance-la dans l\'étang.', 'aqua')])
    w('lobby/fish/keep', ['# @s : garde la canne ? Retourne 1 ou 0, sans message (à la position de @s)',
                          'execute at @s unless dimension minecraft:overworld run return 0',
                          'execute if score $lfoff mg.st matches 1 run return 0',
                          f'execute unless entity {KEEP_SEL} run return 0',
                          f'execute positioned {POND_C} unless entity @s[distance=..{FISH_R}] run return 0',
                          'return 1'])
    w('lobby/fish/second', ['# Toutes les 2 s (core/tick : $lan mg.t = 30, chunk du socle chargé) : cannes, stat de lancers, entités du socle',
                            DROPPED,
                            'function mg:lobby/fish/purge',
                            f'execute as @a unless function mg:lobby/fish/keep run clear @s {PRED}',
                            '# lancers : stat vanilla used:fishing_rod (lancer et remontée comptent chacun), reportée dans $use (seulement pour qui passe keep), remise à zéro pour tous',
                            'execute as @a[scores={mg.lfu=1..}] if function mg:lobby/fish/keep run scoreboard players operation $use mg.lfn += @s mg.lfu',
                            'scoreboard players set @a[scores={mg.lfu=1..}] mg.lfu 0',
                            '# socle : deux entités (zone cliquable et panneau), refaites s\'il en manque ; coupé par un admin : plus rien',
                            'execute if score $lfoff mg.st matches 1 run return 0',
                            'execute store result score #lfe mg.st if entity @e[tag=mg.lfs]',
                            f'execute unless score #lfe mg.st matches 2 if block {POS} {LOG} run function mg:lobby/fish/entities'])
    w('lobby/fish/purge', ['# Retire la canne des conteneurs du spawn et du Hall (généré : liste relue dans les fonctions de construction)'] +
      [f'execute in minecraft:overworld if loaded {x} {y} {z} run data remove block {x} {y} {z} {PURGE}' for x, y, z in containers])
    w('lobby/fish/build', ['# 🎣 Socle de la canne (généré par tools/lobby/gen_fish.py) : le bloc, puis ses entités',
                           f'setblock {POS} {LOG}', 'function mg:lobby/fish/entities'])
    x, y, z = SOCLE
    w('lobby/fish/entities', ['# Zone cliquable et panneau du socle (tag mg.lfs, sans mg.lby) : les anciens sont retirés',
                              'kill @e[tag=mg.lfs]',
                              f'summon minecraft:interaction {x + 0.5} {y} {z + 0.5} {{Tags:["mg.lfs","mg.lfi"],width:1.05f,height:1.05f,response:1b}}',
                              f'summon minecraft:text_display {x + 0.5} {y + 1.6} {z + 0.5} {{Tags:["mg.lfs"],billboard:"center",background:0,'
                              'text:' + js([{'text': '🎣 Pêche à l\'étang', 'color': 'aqua', 'bold': True},
                                            {'text': '\nclic droit : prendre ou ranger la canne', 'color': 'gray'}]) + ',' + TF.format(s=1.2) + '}'])
    w('lobby/fish/after', ['# Chaque tick tant qu\'un joueur porte mg.lfc ou qu\'un marqueur mg.lfm reste (core/tick) : le tick suivant une prise, objets de la ligne et orbes d\'XP tués',
                           'execute as @e[type=minecraft:marker,tag=mg.lfm] at @s run kill @e[type=minecraft:item,distance=..1.5]',
                           'execute as @a[tag=mg.lfc] at @s run kill @e[type=minecraft:experience_orb,distance=..2]',
                           'kill @e[type=minecraft:marker,tag=mg.lfm]', 'tag @a remove mg.lfc'])
    adv('lobby_fish_take', {'criteria': {'use': {'trigger': 'minecraft:player_interacted_with_entity', 'conditions': {'entity': [{
        'condition': 'minecraft:entity_properties', 'entity': 'this',
        'predicate': {'minecraft:entity_type': 'minecraft:interaction', 'minecraft:nbt': '{Tags:["mg.lfi"]}'}}]}}},
        'rewards': {'function': 'mg:lobby/fish/take'}})
    adv('lobby_fish', {'criteria': {'catch': {'trigger': 'minecraft:fishing_rod_hooked', 'conditions': {
        'rod': {'predicates': {'minecraft:custom_data': '{mg_rod:1b}'}}, 'item': {'count': {'min': 1}},
        # hameçon accroché à une entité (objet au sol, mob) : le contexte du trigger est cette entité, pas l'hameçon : on exige l'hameçon
        'entity': [{'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'minecraft:entity_type': 'minecraft:fishing_bobber'}}]}}},
        'rewards': {'function': 'mg:lobby/fish/catch'}})
