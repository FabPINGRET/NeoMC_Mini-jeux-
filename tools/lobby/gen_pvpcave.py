"""⚔ Arène PvP souterraine du spawn : petit trou dans la place (entre le buffet et le centre) → mini-lobby des classes
dans la roche → arène PvP simple en dessous. Pour se taper dessus en attendant que tout le monde soit là.

    python tools/lobby/gen_pvpcave.py .        (depuis la racine du dépôt ; idempotent)

- Trou 2×2 en (13..14, 12..13) dans la place → chute (sans dégâts au lobby) dans le mini-lobby (y 55..58).
- Mini-lobby : 4 socles de classe (Guerrier, Archer, Tank, Assassin) + socle « retour au spawn ».
  Marcher sur un socle = kit de la classe + téléportation dans l'arène (point au hasard), point de réapparition dans l'arène.
- Arène (x −11..37, y 43..51, z −9..33, 49×43) : sol plat, piliers, petits murets, 4 tremplins en slime, pièces bonus qui apparaissent.
- Monnaie 💰 (mg.pco, gardée d'une fois sur l'autre) : +10 par kill, bonus de série (3, 5, 10 kills), pièces ramassées (+5).
- Boutique (émeraude de la barre, clic droit) : pomme d'or, pomme d'or enchantée (très chère), potions de soin / dégâts /
  force / vitesse / régénération, chien de garde, flèches, perle de l'Ender, totem, épée en diamant.
- Retour au spawn (boussole de la barre, clic droit) : 5 s sans bouger de l'arène ni prendre de coup, sinon annulé.
- Une partie qui démarre retire les joueurs de l'arène (kit, chiens) ; mg:core/reset_player fait aussi le ménage.
Tout est reconstruit si le bloc témoin (pierre de magnétite cachée) disparaît.
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
A = os.path.join(R, 'data/mg/advancement')

HOLE = (13, 12)                          # coin nord-ouest du trou 2×2
ROOM = (7, 55, 6, 19, 58, 18)            # intérieur du mini-lobby (sol en y 54)
AR = (-11, 43, -9, 37, 51, 33)           # intérieur de l'arène (sol en y 42), agrandie (49×43)
SENT = (13, 53, 5)                       # bloc témoin (dans la coque, invisible)
ZONE = 'x=-12,y=40,z=-10,dx=51,dy=20,dz=45'  # tout le souterrain (y 40..60)
SPAWNS = [(-8, -6), (34, -6), (-8, 30), (34, 30), (13, -6), (13, 30), (-8, 12), (34, 12), (2, 2), (24, 2), (2, 22), (24, 22)]
PADS = [  # n, nom, couleur, bloc, x, z, description
    (1, 'Guerrier', 'white', 'iron_block', 8, 7, 'Épée en fer, bouclier, armure en fer'),
    (2, 'Archer', 'green', 'emerald_block', 16, 7, 'Arc Puissance II, 48 flèches, armure en mailles'),
    (3, 'Tank', 'aqua', 'diamond_block', 8, 15, 'Hache, bouclier, armure lourde, +4 cœurs, lent'),
    (4, 'Assassin', 'dark_gray', 'coal_block', 16, 15, 'Épée en fer Tranchant II, rapide, 2 perles'),
]
HOME_PAD = (12, 16)                      # socle « retour au spawn » (3×3)
UNB = 'unbreakable={}'
KITS = {
    1: ['item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={}]',
        'item replace entity @s weapon.offhand with minecraft:shield[unbreakable={}]',
        'item replace entity @s armor.head with minecraft:iron_helmet[unbreakable={}]',
        'item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={}]',
        'item replace entity @s armor.legs with minecraft:iron_leggings[unbreakable={}]',
        'item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]'],
    2: ['item replace entity @s hotbar.0 with minecraft:stone_sword[unbreakable={}]',
        'item replace entity @s hotbar.1 with minecraft:bow[unbreakable={},enchantments={power:2,punch:1}]',
        'item replace entity @s hotbar.2 with minecraft:arrow 48',
        'item replace entity @s armor.head with minecraft:chainmail_helmet[unbreakable={}]',
        'item replace entity @s armor.chest with minecraft:chainmail_chestplate[unbreakable={}]',
        'item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={}]',
        'item replace entity @s armor.feet with minecraft:chainmail_boots[unbreakable={}]'],
    3: ['item replace entity @s hotbar.0 with minecraft:iron_axe[unbreakable={}]',
        'item replace entity @s weapon.offhand with minecraft:shield[unbreakable={}]',
        'item replace entity @s armor.head with minecraft:diamond_helmet[unbreakable={}]',
        'item replace entity @s armor.chest with minecraft:diamond_chestplate[unbreakable={}]',
        'item replace entity @s armor.legs with minecraft:iron_leggings[unbreakable={}]',
        'item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]',
        'effect give @s minecraft:health_boost infinite 1 true', 'effect give @s minecraft:slowness infinite 0 true'],
    4: ['item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},enchantments={sharpness:2}]',
        'item replace entity @s hotbar.1 with minecraft:ender_pearl 2',
        'item replace entity @s armor.head with minecraft:leather_helmet[unbreakable={},dyed_color=1118481]',
        'item replace entity @s armor.chest with minecraft:leather_chestplate[unbreakable={},dyed_color=1118481]',
        'item replace entity @s armor.legs with minecraft:leather_leggings[unbreakable={},dyed_color=1118481]',
        'item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={},dyed_color=1118481]',
        'effect give @s minecraft:speed infinite 1 true'],
}
CONS = 'consumable={consume_seconds:0.05f,animation:"none",sound:"minecraft:ui.button.click",has_consume_particles:false}'
SHOP_ITEM = ('minecraft:emerald[custom_data={pvpc_shop:1b},enchantment_glint_override=true,' + CONS +
             ',custom_name=[{"text":"💰 Boutique","color":"green","bold":true,"italic":false}],'
             'lore=[[{"text":"Clic droit : acheter des bonus avec tes pièces","color":"gray","italic":false}]]]')
HOME_ITEM = ('minecraft:recovery_compass[custom_data={pvpc_home:1b},' + CONS +
             ',custom_name=[{"text":"🏠 Retour au spawn","color":"yellow","bold":true,"italic":false}],'
             'lore=[[{"text":"Clic droit : 5 s sans prendre de coup","color":"gray","italic":false}]]]')
POT = lambda typ, contents, name, col: (f'minecraft:{typ}[potion_contents={contents},'
                                        f'custom_name=[{{"text":"{name}","color":"{col}","italic":false}}]]')
SHOP = [  # n, libellé, couleur, prix, commandes (@s = acheteur)
    (1, '🍎 Pomme d\'or', 'gold', 30, ['give @s minecraft:golden_apple']),
    (2, '✨ Pomme d\'or enchantée', 'light_purple', 250, ['give @s minecraft:enchanted_golden_apple']),
    (3, '❤ Potion de soin (jetable)', 'red', 20,
     ['give @s ' + POT('splash_potion', '{potion:"minecraft:strong_healing"}', 'Potion de soin', 'red')]),
    (4, '☠ Potion de dégâts (jetable)', 'dark_purple', 35,
     ['give @s ' + POT('splash_potion', '{potion:"minecraft:strong_harming"}', 'Potion de dégâts', 'dark_purple')]),
    (5, '🐺 Chien de garde', 'white', 60, ['function mg:pvpc/dog']),
    (6, '➶ Flèches ×16', 'gray', 10, ['give @s minecraft:arrow 16']),
    (7, '⚡ Potion de vitesse (1 min 30)', 'aqua', 25,
     ['give @s ' + POT('potion', '{potion:"minecraft:swiftness"}', 'Potion de vitesse', 'aqua')]),
    (8, '💪 Potion de force (1 min 30)', 'dark_red', 50,
     ['give @s ' + POT('potion', '{potion:"minecraft:strength"}', 'Potion de force', 'dark_red')]),
    (9, '♥ Potion de régénération (45 s)', 'light_purple', 40,
     ['give @s ' + POT('potion', '{potion:"minecraft:regeneration"}', 'Potion de régénération', 'light_purple')]),
    (10, '🟣 Perle de l\'Ender', 'dark_aqua', 40, ['give @s minecraft:ender_pearl']),
    (11, '🗿 Totem d\'immortalité', 'yellow', 200, ['give @s minecraft:totem_of_undying']),
    (12, '🗡 Épée en diamant', 'aqua', 120, ['give @s minecraft:diamond_sword[unbreakable={}]']),
]
written = []


def w(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    written.append(p)


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def patch(rel, anchor, lines, where='after', drop_prefix=None):
    """Insère `lines` à côté de la ligne `anchor` (idempotent ; `drop_prefix` retire d'abord les anciennes versions)."""
    p = os.path.join(F, rel + '.mcfunction')
    t = open(p, encoding='utf-8').read().split('\n')
    if drop_prefix:
        t = [l for l in t if not l.startswith(drop_prefix)]
    if all(l in t for l in lines):
        open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(t))
        return
    t = [l for l in t if l not in lines]
    idx = [i for i, l in enumerate(t) if l == anchor]
    if len(idx) != 1:
        raise SystemExit(f'{rel} : ancre {anchor!r} trouvée {len(idx)} fois')
    i = idx[0] + (1 if where == 'after' else 0)
    t[i:i] = lines
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(t))


hx, hz = HOLE
rx1, ry1, rz1, rx2, ry2, rz2 = ROOM
ax1, ay1, az1, ax2, ay2, az2 = AR

# ------------------------------------------------------------------ construction
B = ['# ⚔ Arène PvP souterraine : mini-lobby des classes + arène (généré par tools/lobby/gen_pvpcave.py)',
     'kill @e[tag=mg.pvpcd]', 'kill @e[type=minecraft:item,tag=mg.pvpcoin]',
     # arène : coque, intérieur, sol
     f'fill {ax1 - 1} {ay1 - 2} {az1 - 1} {ax2 + 1} {ay2 + 1} {az2 + 1} minecraft:deepslate_bricks',
     f'fill {ax1} {ay1} {az1} {ax2} {ay2} {az2} minecraft:air',
     f'fill {ax1} {ay1 - 1} {az1} {ax2} {ay1 - 1} {az2} minecraft:polished_andesite',
     f'fill {ax1 + 1} {ay1 - 1} {az1 + 1} {ax2 - 1} {ay1 - 1} {az2 - 1} minecraft:stone_bricks',
     f'fill {ax1 + 3} {ay1 - 1} {az1 + 3} {ax2 - 3} {ay1 - 1} {az2 - 3} minecraft:smooth_stone',
     f'fill 11 {ay1 - 1} 10 15 {ay1 - 1} 14 minecraft:polished_deepslate',
     f'fill 12 {ay1 - 1} 11 14 {ay1 - 1} 13 minecraft:chiseled_stone_bricks',
     # bas des murs et plafond décorés
     f'fill {ax1} {ay1} {az1} {ax2} {ay1} {az1} minecraft:mossy_stone_bricks', f'fill {ax1} {ay1} {az2} {ax2} {ay1} {az2} minecraft:mossy_stone_bricks',
     f'fill {ax1} {ay1} {az1} {ax1} {ay1} {az2} minecraft:mossy_stone_bricks', f'fill {ax2} {ay1} {az1} {ax2} {ay1} {az2} minecraft:mossy_stone_bricks',
     f'fill {ax1 + 1} {ay1} {az1 + 1} {ax2 - 1} {ay1} {az2 - 1} minecraft:air']
# piliers 2×2 sur toute la hauteur
for (px, pz) in ((6, 6), (19, 6), (6, 17), (19, 17), (-3, -1), (28, -1), (-3, 24), (28, 24), (12, -4), (12, 28)):
    B += [f'fill {px} {ay1} {pz} {px + 1} {ay2} {pz + 1} minecraft:stone_bricks',
          f'fill {px} {ay1} {pz} {px + 1} {ay1} {pz + 1} minecraft:chiseled_stone_bricks',
          f'setblock {px} {ay2} {pz - 1} minecraft:lantern[hanging=true]']
# petits murets (1 bloc, on saute par-dessus) et bosse centrale
B += [f'fill 11 {ay1} 5 15 {ay1} 5 minecraft:mossy_stone_bricks', f'fill 11 {ay1} 19 15 {ay1} 19 minecraft:mossy_stone_bricks',
      f'fill 4 {ay1} 10 4 {ay1} 14 minecraft:mossy_stone_bricks', f'fill 22 {ay1} 10 22 {ay1} 14 minecraft:mossy_stone_bricks',
      f'fill -7 {ay1} 4 -7 {ay1} 8 minecraft:mossy_stone_bricks', f'fill 33 {ay1} 16 33 {ay1} 20 minecraft:mossy_stone_bricks',
      f'fill 3 {ay1} -5 7 {ay1} -5 minecraft:mossy_stone_bricks', f'fill 19 {ay1} 29 23 {ay1} 29 minecraft:mossy_stone_bricks',
      f'fill 25 {ay1} -6 25 {ay1} -3 minecraft:cobblestone_wall', f'fill 1 {ay1} 27 1 {ay1} 30 minecraft:cobblestone_wall',
      # buttes basses (1 bloc) aux quatre coins
      f'fill -9 {ay1} 25 -5 {ay1} 31 minecraft:smooth_stone_slab[type=bottom]', f'fill 31 {ay1} -7 35 {ay1} -1 minecraft:smooth_stone_slab[type=bottom]',
      f'fill 12 {ay1} 11 14 {ay1} 13 minecraft:smooth_stone_slab[type=bottom]', f'setblock 13 {ay1} 12 minecraft:chiseled_stone_bricks',
      f'fill 9 {ay1} 21 9 {ay1} 22 minecraft:cobblestone_wall', f'fill 17 {ay1} 2 17 {ay1} 3 minecraft:cobblestone_wall',
      # tremplins (slime) dans deux coins
      f'setblock 3 {ay1 - 1} 7 minecraft:slime_block', f'setblock 23 {ay1 - 1} 17 minecraft:slime_block',
      f'setblock -6 {ay1 - 1} -4 minecraft:slime_block', f'setblock 32 {ay1 - 1} 28 minecraft:slime_block',
      # lumière : lanternes de mer au plafond
      ] + [f'setblock {x} {ay2 + 1} {z} minecraft:sea_lantern' for x in range(ax1 + 3, ax2, 6) for z in range(az1 + 3, az2, 6)] + [
      f'setblock {x} {ay1 + 3} {z} minecraft:glowstone' for (x, z) in [(ax1 - 1, k) for k in range(az1 + 4, az2, 8)] + [(ax2 + 1, k) for k in range(az1 + 4, az2, 8)] + [(k, az1 - 1) for k in range(ax1 + 4, ax2, 8)] + [(k, az2 + 1) for k in range(ax1 + 4, ax2, 8)]]
# mini-lobby : coque, sol, plafond, puits
B += [f'fill {rx1 - 1} {ry1 - 2} {rz1 - 1} {rx2 + 1} {ry2 + 1} {rz2 + 1} minecraft:deepslate_bricks',
      f'fill {rx1} {ry1} {rz1} {rx2} {ry2} {rz2} minecraft:air',
      f'fill {rx1} {ry1 - 1} {rz1} {rx2} {ry1 - 1} {rz2} minecraft:deepslate_tiles',
      f'fill {rx1 + 1} {ry1 - 1} {rz1 + 1} {rx2 - 1} {ry1 - 1} {rz2 - 1} minecraft:polished_deepslate',
      f'fill {rx1} {ry2 + 1} {rz1} {rx2} {ry2 + 1} {rz2} minecraft:polished_deepslate',
      f'setblock {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone',
      ] + [f'setblock {x} {ry2 + 1} {z} minecraft:shroomlight' for x in (9, 13, 17) for z in (8, 16)] + [
      f'fill {hx} {ry2 + 1} {hz} {hx + 1} 63 {hz + 1} minecraft:air',
      f'fill {hx} {ry1 - 1} {hz} {hx + 1} {ry1 - 1} {hz + 1} minecraft:hay_block',
      # entrée en surface : margelle en briques noires, piquets avec lanternes, 2×2 ouvert
      f'fill {hx - 1} 64 {hz - 1} {hx + 2} 66 {hz + 2} minecraft:air',
      f'fill {hx - 1} 63 {hz - 1} {hx + 2} 63 {hz + 2} minecraft:polished_blackstone_bricks',
      f'fill {hx} 63 {hz} {hx + 1} 63 {hz + 1} minecraft:air',
      f'fill {hx - 1} 59 {hz - 1} {hx + 2} 62 {hz + 2} minecraft:deepslate_bricks',
      f'fill {hx} 59 {hz} {hx + 1} 62 {hz + 1} minecraft:air']
for (dx, dz) in ((-1, -1), (2, -1), (-1, 2), (2, 2)):
    B += [f'setblock {hx + dx} 64 {hz + dz} minecraft:polished_blackstone_wall', f'setblock {hx + dx} 65 {hz + dz} minecraft:lantern']
B.append(f'summon minecraft:text_display {hx + 1} 66.6 {hz + 1} {{Tags:["mg.pvpcd","mg.lby"],billboard:"center",background:0,'
         f'text:[{{"text":"⚔ Arène PvP","color":"red","bold":true}},{{"text":"\\nsaute dans le trou ↓","color":"gray"}}],'
         'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}')
# socles de classe + retour
TF = 'transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[{s}f,{s}f,{s}f]}}'
for (n, nm, col, blk, x, z, desc) in PADS:
    B += [f'fill {x} {ry1 - 1} {z} {x + 2} {ry1 - 1} {z + 2} minecraft:{blk}',
          f'summon minecraft:text_display {x + 1.5} {ry1 + 1.6} {z + 1.5} {{Tags:["mg.pvpcd"],billboard:"center",background:1342177280,'
          f'text:[{{"text":"{nm}","color":"{col}","bold":true}},{{"text":"\\n{desc}","color":"gray"}}],' + TF.format(s=0.8) + '}']
px_, pz_ = HOME_PAD
B += [f'fill {px_} {ry1 - 1} {pz_} {px_ + 2} {ry1 - 1} {pz_ + 2} minecraft:gold_block',
      f'summon minecraft:text_display {px_ + 1.5} {ry1 + 1.6} {pz_ + 1.5} {{Tags:["mg.pvpcd"],billboard:"center",background:1342177280,'
      'text:[{"text":"🏠 Retour au spawn","color":"yellow","bold":true}],' + TF.format(s=0.8) + '}',
      f'summon minecraft:text_display 13.5 {ry1 + 2.2} {rz1 + 0.1} {{Tags:["mg.pvpcd"],billboard:"fixed",Rotation:[0f,0f],background:1342177280,line_width:260,'
      'text:[{"text":"⚔ ARÈNE PVP","color":"red","bold":true},'
      '{"text":"\\nMarche sur un socle pour choisir ta classe et descendre dans l\'arène.","color":"white"},'
      '{"text":"\\n💰 +10 pièces par kill, bonus de série à 3, 5 et 10 kills, pièces à ramasser dans l\'arène.","color":"gold"},'
      '{"text":"\\nÉmeraude = boutique · Boussole = retour au spawn (5 s sans prendre de coup).","color":"gray"}],' + TF.format(s=0.75) + '}']
for (x, z) in SPAWNS:
    B.append(f'summon minecraft:marker {x}.5 {ay1} {z}.5 {{Tags:["mg.pvpcd","mg.pvpsp"]}}')
B.append('data modify storage mg:lobby pvpc2 set value 1b')
w('pvpc/build', B)
w('pvpc/build_start', ['# Charge la zone puis construit (2 s plus tard)', 'forceload add -12 -10 38 34', 'schedule function mg:pvpc/build_go 2s'])
w('pvpc/build_go', ['function mg:pvpc/build', 'forceload remove -12 -10 38 34', 'function mg:core/forceloads',
                    'tellraw @a[tag=mg.admin] {"text":"⚔ Arène PvP souterraine construite (trou entre le buffet et le centre du spawn).","color":"gold"}'])

# ------------------------------------------------------------------ entrée / sortie
pad_lines = []
for (n, nm, col, blk, x, z, desc) in PADS:
    w(f'pvpc/class_{n}', [f'# @s choisit la classe {nm} : kit, puis arène',
                          'scoreboard players set @s mg.pcl ' + str(n), 'function mg:pvpc/equip', 'function mg:pvpc/to_arena',
                          f'tellraw @s [{{"text":"⚔ Classe ","color":"gray"}},{{"text":"{nm}","color":"{col}","bold":true}},'
                          '{"text":" — bonne chance ! ","color":"gray"},{"text":"(émeraude = boutique, boussole = retour)","color":"dark_gray"}]'])
    pad_lines.append(f'execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.pvpc,x={x},y={ry1},z={z},dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/class_{n}')
w('pvpc/equip', ['# @s : kit de sa classe (mg.pcl) + boutique + retour (+ menu)', 'clear @s', 'effect clear @s', 'function mg:core/attr_reset'] +
  [f'execute if score @s mg.pcl matches {n} run function mg:pvpc/kit_{n}' for n in KITS] +
  ['function mg:pvpc/items', 'function mg:core/give_menu', 'function mg:core/heal'])
for n, lines in KITS.items():
    w(f'pvpc/kit_{n}', [f'# Kit de la classe {n}'] + lines)
w('pvpc/items', ['# @s : émeraude (boutique) et boussole (retour) dans la barre',
                 f'item replace entity @s hotbar.7 with {SHOP_ITEM}', f'item replace entity @s hotbar.8 with {HOME_ITEM}'])
w('pvpc/to_arena', ['# @s : dans l\'arène, à un point au hasard (réapparition au même endroit)',
                    'execute unless score @s mg.pvid matches 1.. run scoreboard players add $pvidn mg.st 1',
                    'execute unless score @s mg.pvid matches 1.. run scoreboard players operation @s mg.pvid = $pvidn mg.st',
                    'tag @s add mg.pvpc', 'scoreboard players set @s mg.pks 0', 'scoreboard players set @s mg.phc 0',
                    'scoreboard players set @s mg.deaths 0', 'scoreboard players reset @s mg.pkc',
                    'execute unless score @s mg.pco matches 0.. run scoreboard players set @s mg.pco 0',
                    'scoreboard players enable @s mg.pshop',
                    'execute at @e[type=minecraft:marker,tag=mg.pvpsp,sort=random,limit=1] run tp @s ~ ~ ~ facing 13.5 44 12.5',
                    'execute at @s run spawnpoint @s ~ ~ ~', 'effect give @s minecraft:resistance 3 4 true',
                    'execute at @s run playsound minecraft:item.armor.equip_netherite master @s ~ ~ ~ 1 1'])
w('pvpc/cleanup', ['# @s quitte l\'arène (appelé aussi par mg:core/reset_player et au départ d\'une partie) : tag, retour, chiens',
                   'execute unless entity @s[tag=mg.pvpc] run return 0',
                   'tag @s remove mg.pvpc', 'scoreboard players set @s mg.phc 0',
                   'scoreboard players operation $p mg.st = @s mg.pvid',
                   'execute as @e[type=minecraft:wolf,tag=mg.pdog] if score @s mg.pvid = $p mg.st run tp @s ~ -300 ~',
                   'spawnpoint @s 0 64 0'])
w('pvpc/leave', ['# @s remonte au spawn', 'function mg:pvpc/cleanup', 'function mg:core/reset_player',
                 'tellraw @s {"text":"🏠 Retour au spawn. Tes pièces sont gardées pour la prochaine fois.","color":"yellow"}'])

# ------------------------------------------------------------------ jeu
w('pvpc/tick', ['# ⚔ Arène PvP souterraine — tick (seulement si quelqu\'un est dessous ou y est inscrit)'] + pad_lines +
  [f'execute as @a[tag=!mg.play,tag=!mg.out,x={px_},y={ry1},z={pz_},dx=2.99,dy=1.5,dz=2.99] run function mg:pvpc/leave',
   # une partie a démarré : ses joueurs ne sont plus dans l'arène
   'execute as @a[tag=mg.pvpc,tag=mg.play] run function mg:pvpc/cleanup',
   'execute as @a[tag=mg.pvpc,scores={mg.pkc=1..}] run function mg:pvpc/kill',
   'execute as @a[tag=mg.pvpc,scores={mg.deaths=1..}] run function mg:pvpc/died',
   'execute as @a[tag=mg.pvpc,scores={mg.pshop=1..}] run function mg:pvpc/buy',
   'execute as @a[tag=mg.pvpc,scores={mg.phc=1..}] run function mg:pvpc/home_tick',
   # sorti de la zone autrement (tp, menu…) : plus inscrit
   f'execute as @a[tag=mg.pvpc] unless entity @s[{ZONE}] run function mg:pvpc/cleanup',
   # pièces ramassées
   'execute as @a[tag=mg.pvpc] if items entity @s container.* minecraft:gold_nugget[custom_data~{pvpc_coin:1b}] run function mg:pvpc/coins_picked',
   'scoreboard players add $pvt mg.st 1',
   'execute if score $pvt mg.st matches 20.. run function mg:pvpc/second'])
w('pvpc/second', ['scoreboard players set $pvt mg.st 0',
                  'execute as @a[tag=mg.pvpc,scores={mg.phc=0}] run title @s actionbar [{"text":"💰 ","color":"gold"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow","bold":true},'
                  '{"text":" pièces   ","color":"gold"},{"text":"🔥 série ","color":"red"},{"score":{"name":"@s","objective":"mg.pks"},"color":"red","bold":true}]',
                  # chiens dont le maître n'est plus là
                  'execute as @e[type=minecraft:wolf,tag=mg.pdog] run function mg:pvpc/dog_check',
                  # pièces bonus : une toutes les 15 s s'il y a au moins 2 joueurs, 4 au sol au maximum
                  'scoreboard players add $pvc mg.st 1',
                  'execute if score $pvc mg.st matches 15.. run function mg:pvpc/coin_spawn'])
w('pvpc/coin_spawn', ['scoreboard players set $pvc mg.st 0',
                      'execute store result score $n mg.st if entity @a[tag=mg.pvpc]', 'execute if score $n mg.st matches ..1 run return 0',
                      'execute store result score $n mg.st if entity @e[type=minecraft:item,tag=mg.pvpcoin]', 'execute if score $n mg.st matches 4.. run return 0',
                      'execute store result score $cx mg.st run random value -9..35', 'execute store result score $cz mg.st run random value -7..31',
                      'execute store result storage mg:pvpc p.x int 1 run scoreboard players get $cx mg.st',
                      'execute store result storage mg:pvpc p.z int 1 run scoreboard players get $cz mg.st',
                      'function mg:pvpc/coin_at with storage mg:pvpc p'])
w('pvpc/coin_at', ['# Pile de pièces (+5) en $(x) $(z) ; si le point est dans un pilier, rien cette fois',
                   f'$execute unless block $(x) {ay1} $(z) minecraft:air run return 0',
                   f'$summon minecraft:item $(x).5 {ay1 + 0.2} $(z).5 {{Tags:["mg.keep","mg.pvpcoin"],PickupDelay:10s,Age:-32768s,'
                   'Item:{id:"minecraft:gold_nugget",count:5,components:{"minecraft:custom_data":{pvpc_coin:1b},'
                   '"minecraft:custom_name":{"text":"Pièces","color":"gold","italic":false}}}}',
                   f'$particle minecraft:wax_on $(x).5 {ay1 + 0.6} $(z).5 0.3 0.3 0.3 0 12'])
w('pvpc/coins_picked', ['# @s a ramassé des pièces : 1 pépite = 1 pièce',
                        'execute store result score $n mg.st run clear @s minecraft:gold_nugget[custom_data~{pvpc_coin:1b}]',
                        'scoreboard players operation @s mg.pco += $n mg.st',
                        'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.4',
                        'title @s actionbar [{"text":"💰 +","color":"gold"},{"score":{"name":"$n","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pièces","color":"gold"}]'])
w('pvpc/kill', ['# @s a fait un ou plusieurs kills : +10 pièces chacun, série, petit soin',
                'scoreboard players operation $k mg.st = @s mg.pkc', 'scoreboard players reset @s mg.pkc',
                'scoreboard players operation @s mg.pks += $k mg.st',
                'scoreboard players operation $g mg.st = $k mg.st', 'scoreboard players set #10 mg.st 10',
                'scoreboard players operation $g mg.st *= #10 mg.st', 'scoreboard players operation @s mg.pco += $g mg.st',
                'effect give @s minecraft:regeneration 3 1 true',
                'playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.7 1.6',
                'title @s actionbar [{"text":"⚔ Kill ! ","color":"red","bold":true},{"text":"+","color":"gold"},{"score":{"name":"$g","objective":"mg.st"},"color":"yellow"},{"text":" 💰","color":"gold"}]',
                'execute if score @s mg.pks matches 3 run function mg:pvpc/streak {n:3,b:15,t:"est en série"}',
                'execute if score @s mg.pks matches 5 run function mg:pvpc/streak {n:5,b:30,t:"est déchaîné"}',
                'execute if score @s mg.pks matches 10 run function mg:pvpc/streak {n:10,b:80,t:"est IMBATTABLE"}'])
w('pvpc/streak', ['# Bonus de série (@s, macro : n kills, b pièces, t texte)',
                  '$scoreboard players add @s mg.pco $(b)',
                  '$tellraw @a[tag=mg.pvpc] [{"text":"🔥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" $(t) ($(n) kills d\'affilée) : +$(b) 💰","color":"red"}]',
                  'execute as @a[tag=mg.pvpc] at @s run playsound minecraft:entity.blaze.shoot master @s ~ ~ ~ 0.6 1.4'])
w('pvpc/died', ['# @s est mort dans l\'arène : série perdue, réapparaît dans l\'arène protégé 3 s, kit de classe rendu',
                'scoreboard players set @s mg.deaths 0', 'scoreboard players set @s mg.pks 0', 'scoreboard players set @s mg.phc 0',
                'function mg:pvpc/equip', 'effect give @s minecraft:resistance 3 4 true'])
w('pvpc/dog', ['# @s achète un chien de garde (2 au maximum)',
               'scoreboard players operation $p mg.st = @s mg.pvid', 'scoreboard players set $n mg.st 0',
               'execute as @e[type=minecraft:wolf,tag=mg.pdog] if score @s mg.pvid = $p mg.st run scoreboard players add $n mg.st 1',
               'execute if score $n mg.st matches 2.. run scoreboard players add @s mg.pco 60',
               'execute if score $n mg.st matches 2.. run return run tellraw @s {"text":"🐺 Tu as déjà 2 chiens (remboursé).","color":"red"}',
               'execute at @s run summon minecraft:wolf ~ ~ ~ {Tags:["mg.pdog","mg.mob","mg.pdogn"],PersistenceRequired:1b,CollarColor:14b,'
               'attributes:[{id:"minecraft:max_health",base:30d},{id:"minecraft:attack_damage",base:5d}],Health:30f}',
               'data modify entity @e[type=minecraft:wolf,tag=mg.pdogn,limit=1] Owner set from entity @s UUID',
               'scoreboard players operation @e[type=minecraft:wolf,tag=mg.pdogn,limit=1] mg.pvid = @s mg.pvid',
               'tag @e[type=minecraft:wolf,tag=mg.pdogn] remove mg.pdogn',
               'execute at @s run playsound minecraft:entity.wolf.ambient master @a ~ ~ ~ 1 1'])
w('pvpc/dog_check', ['# @s = chien : disparaît si son maître n\'est plus dans l\'arène',
                     'scoreboard players operation $p mg.st = @s mg.pvid', 'scoreboard players set $f mg.st 0',
                     'execute as @a[tag=mg.pvpc] if score @s mg.pvid = $p mg.st run scoreboard players set $f mg.st 1',
                     'execute if score $f mg.st matches 0 run tp @s ~ -300 ~'])

# ------------------------------------------------------------------ boutique
shop_actions = [{'label': [{'text': f'{lbl} — {price} 💰', 'color': col}],
                 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.pshop set {n}'}} for n, lbl, col, price, _ in SHOP]
dlg = {'type': 'minecraft:multi_action', 'title': {'text': '💰 Boutique de l\'arène', 'color': 'gold', 'bold': True},
       'pause': False, 'can_close_with_escape': True,
       'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Tu as ', 'color': 'gray'}, {'text': 'PIECES', 'color': 'yellow', 'bold': True},
                                                                  {'text': ' pièces. +10 par kill, bonus de série, pièces à ramasser.', 'color': 'gray'}]}],
       'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': shop_actions}
w('pvpc/shop', ['# @s ouvre la boutique (fenêtre avec son solde)', 'scoreboard players enable @s mg.pshop',
                'execute store result storage mg:pvpc s.c int 1 run scoreboard players get @s mg.pco',
                'function mg:pvpc/shop_show with storage mg:pvpc s'])
w('pvpc/shop_show', ['$dialog show @s ' + js(dlg).replace('"PIECES"', '"$(c)"')])
buy = ['# @s achète l\'article mg.pshop', 'scoreboard players operation $b mg.st = @s mg.pshop', 'scoreboard players reset @s mg.pshop',
       'scoreboard players enable @s mg.pshop']
for n, lbl, col, price, cmds in SHOP:
    buy.append(f'execute if score $b mg.st matches {n} run return run function mg:pvpc/buy_{n}')
    w(f'pvpc/buy_{n}', [f'# Achat : {lbl} ({price} 💰)',
                        f'execute unless score @s mg.pco matches {price}.. run return run tellraw @s [{{"text":"💰 Pas assez de pièces pour ","color":"red"}},'
                        f'{{"text":"{lbl}","color":"{col}"}},{{"text":" ({price}).","color":"red"}}]',
                        f'scoreboard players remove @s mg.pco {price}'] + cmds +
      [f'tellraw @s [{{"text":"✔ Acheté : ","color":"green"}},{{"text":"{lbl}","color":"{col}"}},{{"text":" — reste ","color":"gray"}},'
       '{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]',
       'execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2'])
w('pvpc/buy', buy)

# ------------------------------------------------------------------ objets de la barre (clic droit = consommation)
for key, fn in (('shop', 'pvpc/shop_adv'), ('home', 'pvpc/home_adv')):
    os.makedirs(A, exist_ok=True)
    with open(os.path.join(A, f'pvpc_{key}.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'criteria': {'use': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {'predicates': {
            'minecraft:custom_data': f'{{pvpc_{key}:1b}}'}}}}}, 'rewards': {'function': f'mg:{fn}'}}, f, ensure_ascii=False, indent=2)
        f.write('\n')
w('pvpc/shop_adv', ['advancement revoke @s only mg:pvpc_shop', f'item replace entity @s hotbar.7 with {SHOP_ITEM}',
                    'execute if entity @s[tag=mg.pvpc] run function mg:pvpc/shop'])
w('pvpc/home_adv', ['advancement revoke @s only mg:pvpc_home', f'item replace entity @s hotbar.8 with {HOME_ITEM}',
                    'execute unless entity @s[tag=mg.pvpc] run return 0',
                    'execute if score @s mg.phc matches 1.. run return 0',
                    'scoreboard players set @s mg.phc 100', 'scoreboard players set @s mg.pdt 0',
                    'tellraw @s {"text":"🏠 Retour au spawn dans 5 s… ne prends pas de coup !","color":"yellow"}'])
w('pvpc/home_tick', ['# @s attend son retour (5 s) : un coup reçu annule',
                     'execute if score @s mg.pdt matches 1.. run scoreboard players set @s mg.phc 0',
                     'execute if score @s mg.pdt matches 1.. run return run title @s actionbar {"text":"✖ Retour annulé : tu as pris un coup !","color":"red","bold":true}',
                     'scoreboard players remove @s mg.phc 1',
                     'scoreboard players operation $s mg.st = @s mg.phc', 'scoreboard players add $s mg.st 19', 'scoreboard players set #20 mg.st 20',
                     'scoreboard players operation $s mg.st /= #20 mg.st',
                     'title @s actionbar [{"text":"🏠 Retour au spawn dans ","color":"yellow"},{"score":{"name":"$s","objective":"mg.st"},"color":"gold","bold":true},{"text":" s","color":"yellow"}]',
                     'execute if score @s mg.phc matches 0 run function mg:pvpc/leave'])

# ------------------------------------------------------------------ branchements
OBJ = [('mg.pco', 'dummy {"text":"💰 Pièces (arène PvP)","color":"gold"}'), ('mg.pkc', 'playerKillCount'), ('mg.pks', 'dummy'),
       ('mg.phc', 'dummy'), ('mg.pdt', 'minecraft.custom:minecraft.damage_taken'), ('mg.pshop', 'trigger'), ('mg.pvid', 'dummy'),
       ('mg.pcl', 'dummy')]
patch('core/load', 'scoreboard objectives add mg.bw trigger', drop_prefix='execute if score $setup mg.st matches 1 unless data storage mg:lobby pvpc1 ', lines=[f'scoreboard objectives add {o} {c}' for o, c in OBJ] + [
    'execute if score $setup mg.st matches 1 unless data storage mg:lobby pvpc2 run schedule function mg:pvpc/build_start 22s'])
patch('desinstaller', 'scoreboard objectives remove mg.bw', [f'scoreboard objectives remove {o}' for o, _ in OBJ] + [
    'schedule clear mg:pvpc/build_start', 'schedule clear mg:pvpc/build_go', 'kill @e[tag=mg.pvpcd]', 'kill @e[type=minecraft:wolf,tag=mg.pdog]',
    'kill @e[type=minecraft:item,tag=mg.pvpcoin]', 'data remove storage mg:lobby pvpc1', 'data remove storage mg:lobby pvpc2', 'data remove storage mg:pvpc p', 'data remove storage mg:pvpc s'])
_tp = os.path.join(F, 'core/tick.mcfunction')   # anciennes lignes (zone de la petite arène)
_tl = open(_tp, encoding='utf-8').read().split('\n')
open(_tp, 'w', encoding='utf-8', newline='\n').write('\n'.join(l for l in _tl if 'x=0,y=40,z=0,dx=27,dy=20,dz=25' not in l))
patch('core/tick', 'execute as @a[scores={mg.cs=1..},tag=!mg.surv] run function mg:core/menu_use', [
    f'execute if score $setup mg.st matches 1 if entity @a[{ZONE}] run function mg:pvpc/tick',
    f'execute if score $setup mg.st matches 1 unless entity @a[{ZONE}] if entity @a[tag=mg.pvpc] run function mg:pvpc/tick',
    f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 if loaded {SENT[0]} {SENT[1]} {SENT[2]} unless block {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone run function mg:pvpc/build'])
patch('core/reset_player', 'tag @s remove mg.play', ['function mg:pvpc/cleanup'], where='before')
print('Arène PvP souterraine OK :', len(written), 'fichiers')
