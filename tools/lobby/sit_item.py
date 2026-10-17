"""🎉 Objet « Emotes » de la barre (importé par gen_sit.py, jamais lancé seul) : clic droit = fenêtre mg:lobby_emotes.

Une pomme de terre empoisonnée habillée en éclat d'améthyste (item_model ; custom_data mg_emote ; sans sa nourriture ni son poison :
!minecraft:food, et notre consumable remplace celui d'origine, sans on_consume_effects) rangée en hotbar.8, donnée au spawn à qui ne
l'a pas et retirée à qui ne doit pas l'avoir. Aucune recette n'utilise cette base (un vrai éclat d'améthyste se craft : table du spawn).
- Garde (lobby/sit/item_keep, sans message) : dans le spawn, overworld, ni spectateur ni occupé ailleurs (BUSY de gen_sit.py), assis et
  emotes pas coupés par un admin. Contrairement à sit/ok, le ragoût (mini-moi, lapin) et les élytres (parcours, libres) le GARDENT :
  KEEP_BUSY les retire de BUSY ; le clic passe quand même par sit/can, qui affiche alors le refus habituel.
- Clic = consommation (modèle pvpc : advancement mg:lobby_emote -> lobby/sit/item_adv). L'objet n'est PAS remis dans le même tick (le
  serveur croit le slot inchangé : objet fantôme) : mg.lsg marque le joueur, mg.lsw saute un tick, item_tick rend l'objet au suivant.
- Toutes les 2 s (core/tick, $lan mg.t = 30) : item_second retire l'objet aux joueurs qui ne le gardent pas, tue les objets jetés au sol,
  purge les conteneurs du spawn (item_purge), et passe item_check aux autres (hors créatif) : 1 objet = rien ; 2 ou plus = les
  surplus sont retirés ; 0 = hotbar.8 si libre, sinon give.
- item_purge : un `data remove block` par conteneur (tonneaux, coffres, fours, hoppers, shulkers...) du spawn et du Hall, liste relue
  dans theme_world.W et hall/build.mcfunction (sit_bench.scan), jamais écrite à la main, gardé par `if loaded` : le joueur ne peut pas
  y mettre l'objet pour le multiplier (item_check ne compte que son inventaire).
Tags : mg.lsg (objet consommé, à rendre), mg.lsw (attente d'un tick). Compteur $itm (mg.lsn). Fichiers : lobby/sit/item_* ; advancement
mg:lobby_emote (écrit ici). C.D / C.F sont ceux de gen_sit.py (C.init déjà appelé).
"""
import json
import os

import common as C
import sit_bench as SB
from theme_world import LOBBY_BOX

PRED = '*[minecraft:custom_data~{mg_emote:1b}]'
CONS = 'consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:ui.button.click",has_consume_particles:false}'   # = gen_pvpcave.py
ITEM = ('minecraft:poisonous_potato[!minecraft:food,item_model="minecraft:amethyst_shard",custom_data={mg_emote:1b},max_stack_size=1,'
        'enchantment_glint_override=true,' + CONS +
        ',custom_name=[{"text":"🎉 Emotes","color":"light_purple","bold":true,"italic":false}],'
        'lore=[[{"text":"Clic droit : ouvrir les emotes","color":"gray","italic":false}]]]')
SLOT = 'hotbar.8'                        # le spawn n'utilise que hotbar.0..4 ; seule l'arène PvP (occupée : objet retiré) prend 7 et 8
KEEP_FREE = ['mg.thbun', 'mg.thmini', 'mg.ely', 'mg.elyf']        # états du BUSY de gen_sit.py où l'objet reste en main
DROPPED = f'execute as @e[type=minecraft:item] if items entity @s contents {PRED} run kill @s'
TICK_LINE = 'execute if entity @a[tag=mg.lsg] run function mg:lobby/sit/item_tick'
SECOND_LINE = 'execute if score $lan mg.t matches 30 run function mg:lobby/sit/item_second'
# conteneurs (blocs à NBT Items) où l'objet pourrait être rangé
CONTAINERS = {'barrel', 'chest', 'trapped_chest', 'hopper', 'dispenser', 'dropper', 'furnace', 'blast_furnace', 'smoker',
              'brewing_stand', 'crafter'}
PURGE = 'Items[{components:{"minecraft:custom_data":{mg_emote:1b}}}]'


def is_container(blk):
    name = blk.split('[')[0].split('{')[0].removeprefix('minecraft:')
    return name in CONTAINERS or name.endswith('shulker_box')


def containers():
    """Conteneurs du spawn et du Hall (triés) : theme_world.W et hall/build.mcfunction."""
    spawn, hall = SB.scan(is_container)
    return sorted(spawn | hall)


def write(busy):
    """Écrit les fonctions lobby/sit/item_* et l'advancement mg:lobby_emote ; busy = BUSY de gen_sit.py."""
    w = C.w
    assert set(KEEP_FREE) <= set(busy), set(KEEP_FREE) - set(busy)
    keep_busy = [t for t in busy if t not in KEEP_FREE]
    keep_sel = f'@s[{LOBBY_BOX},' + ','.join(f'tag=!{t}' for t in keep_busy) + ',gamemode=!spectator]'
    cl = containers()
    print('Conteneurs purgés :', len(cl))
    w('lobby/sit/item_keep', ['# @s : garde l\'objet 🎉 Emotes ? Retourne 1 ou 0, sans message (≠ sit/ok : ragoût et élytres le gardent)',
                              '# tourne sans « at @s » (core/tick) : la dimension se lit à la position du joueur',
                              'execute at @s unless dimension minecraft:overworld run return 0',
                              'execute if score $sitoff mg.st matches 1 run return 0',
                              f'execute unless entity {keep_sel} run return 0',
                              'return 1'])
    w('lobby/sit/item_check', ['# @s : exactement un objet 🎉 Emotes dans l\'inventaire (en rend un s\'il manque, retire les surplus)',
                               f'execute store result score #lsi mg.st run clear @s {PRED} 0',
                               'execute if score #lsi mg.st matches 1 run return 0',
                               f'execute if score #lsi mg.st matches 2.. run clear @s {PRED}',
                               f'execute unless items entity @s {SLOT} * run return run item replace entity @s {SLOT} with {ITEM}',
                               f'give @s {ITEM}'])
    w('lobby/sit/item_second', ['# Toutes les 2 s (core/tick) : l\'objet 🎉 Emotes est retiré à qui ne le garde pas, rendu à qui l\'a perdu',
                                DROPPED,
                                'function mg:lobby/sit/item_purge',
                                f'execute as @a unless function mg:lobby/sit/item_keep run clear @s {PRED}',
                                'execute as @a[tag=!mg.lsg,gamemode=!creative] if function mg:lobby/sit/item_keep run function mg:lobby/sit/item_check'])
    w('lobby/sit/item_purge', ['# Retire l\'objet 🎉 Emotes des conteneurs du spawn et du Hall (généré : liste relue dans les fonctions de construction)'] +
      [f'execute in minecraft:overworld if loaded {x} {y} {z} run data remove block {x} {y} {z} {PURGE}' for x, y, z in cl])
    # NB : ne PAS remettre l'objet dans le tick du clic (objet fantôme) : item_tick le rend deux ticks plus tard.
    w('lobby/sit/item_adv', ['# @s : a consommé l\'objet 🎉 Emotes (clic droit) : fenêtre des emotes si possible ; l\'objet est rendu par item_tick',
                             'advancement revoke @s only mg:lobby_emote',
                             'tag @s add mg.lsg',
                             'tag @s add mg.lsw',
                             'execute unless function mg:lobby/sit/can run return 0',
                             'scoreboard players add $itm mg.lsn 1',
                             'function mg:lobby/sit/menu'])
    w('lobby/sit/item_tick', ['# Appelé chaque tick (core/tick) tant qu\'un joueur porte mg.lsg : mg.lsw fait attendre un tick avant de rendre l\'objet',
                              'execute as @a[tag=mg.lsg,tag=!mg.lsw] run function mg:lobby/sit/item_back',
                              'tag @a[tag=mg.lsw] remove mg.lsw'])
    w('lobby/sit/item_back', ['# @s : l\'objet consommé lui est rendu (s\'il le garde encore)',
                              'tag @s remove mg.lsg',
                              'execute if function mg:lobby/sit/item_keep run function mg:lobby/sit/item_check'])
    os.makedirs(os.path.join(C.D, 'advancement'), exist_ok=True)
    with open(os.path.join(C.D, 'advancement', 'lobby_emote.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'criteria': {'use': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {'predicates': {
            'minecraft:custom_data': '{mg_emote:1b}'}}}}}, 'rewards': {'function': 'mg:lobby/sit/item_adv'}}, f, ensure_ascii=False, indent=2)
        f.write('\n')


def wire(untag):
    """Câblage (une ligne par patch) : à appeler après les patchs de core/request, core/tick et desinstaller de gen_sit.py ; untag = sa ligne UNTAG."""
    C.patch('core/request', 'execute as @a[tag=mg.play,tag=mg.sit] run function mg:lobby/sit/stand',
            [f'clear @a[tag=mg.play] {PRED}'])
    C.patch('core/tick', 'execute if entity @a[tag=mg.sit] run function mg:lobby/sit/tick', [TICK_LINE, SECOND_LINE], where='before')
    C.patch('desinstaller', untag, [f'clear @a {PRED}', DROPPED, 'function mg:lobby/sit/item_purge', 'advancement revoke @a only mg:lobby_emote',
                                    'tag @a remove mg.lsg', 'tag @a remove mg.lsw'])
