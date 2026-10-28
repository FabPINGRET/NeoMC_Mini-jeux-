"""⛏ Filon : mode « long » persistant façon skyblock (monde des mini-jeux, x 0 / z 46000), par saisons.

    python tools/arcade/gen_filon.py .     (après gen_ombrelune.py ; puis tools/lobby/gen_sidebar.py . et tools/variantes/gen_variants.py .)

Principe
- Une île flottante (rayon 30) avec, au centre, UN chunk de mine (x 0..15, z 46000..46015, y 40..99) : pierre en haut, deepslate en bas,
  minerais posés au hasard (place feature : vrais filons) + jackpots (blocs d'or brut, débris antiques, coffres enfouis, géodes).
  Le chunk se régénère toutes les 45 min (alerte 1 min avant) ; certaines régénérations sont « exceptionnelles » (rumeur annoncée).
- Mode aventure : la pioche ne casse que les blocs de la mine (can_break #mg:filon_mine) → impossible de construire ou d'abîmer l'île.
  Minage rapide : pioche en fer Efficacité II + Hâte I dès le départ, vision nocturne, pas de dégâts de chute (on saute dans la mine).
- On vend au 💰 Comptoir (tout l'inventaire vendable d'un coup) : le 📈 cours de chaque minerai change toutes les 15 min (50 à 180 %).
  Points = solde (magasin) ; points gagnés à la vente = classement de la saison (tableau à droite, mg.fns).
- 🛒 Magasin : pioche (diamant, netherite), Efficacité, Fortune, Hâte, épée, armure, steaks, pomme d'or, dynamite.
- 🪢 Corde de remontée (case 9) : retour à la surface, recharge 120 s.
- ⚔ PvP seulement DANS la mine : 3 min après chaque régénération + une phase de 3 min au hasard entre deux (annoncée 30 s avant).
  Ailleurs, jamais (équipe sans tir ami ; en surface pendant le PvP : résistance + faiblesse). Tué en PvP : la moitié de ce que tu
  n'as pas vendu passe au tueur.
- Persistant : niveaux, solde et sac (minerais non vendus) gardés d'une visite à l'autre. Saison : tout repart de zéro
  (automatique toutes les 960 régénérations, ou /function mg:filon/season_end) ; le classement précédent reste dans mg.fnl.
Entrée : menu Échap → « ⛏ Aller au Filon » (trigger mg.sv 9). Sortie : panneau « Retour au lobby » de l'île ou menu Échap.
Admin : /function mg:filon/regen_now (régénère), mg:filon/pvp_now (phase PvP), mg:filon/season_end, mg:filon/build_start (île).
"""
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import shutil
shutil.rmtree(os.path.join(C.F, 'filon'), ignore_errors=True)
w, js = C.w, C.js
P = 'filon'
VERSION = 1                                # île (re)construite si mg:filon built ≠ VERSION
Z0 = 46000                                 # chunk de mine : x 0..15, z Z0..Z0+15 (aligné sur la grille des chunks)
YT, YB = 99, 40                            # couche du haut / du bas de la mine (fond en bedrock à YB - 1)
CX, CZ = 8, Z0 + 8                         # centre de l'île
R = 30                                     # rayon de l'île
SPAWN = (8.5, 100, Z0 - 8.5)               # place nord, face à la mine
PIT = f'x=0,y={YB - 1},z={Z0},dx=15,dy={YT - YB + 1},dz=15'          # volume de la mine (PvP, corde)
PLAZA = f'x=-4,y=97,z={Z0 - 24},dx=24,dy=10,dz=20'                   # place (comptoir, magasin) : achats et ventes
AREA = f'x=-60,y=0,z={Z0 - 70},dx=136,dy=200,dz=136'
FL = f'{CX - R - 8} {CZ - R - 8} {CX + R + 8} {CZ + R + 8}'          # chargement forcé pendant la session
REGEN_S, PVP_S, MKT_S, ROPE_S, SEASON_N = 2700, 180, 900, 120, 960
TXT = lambda t, c='gray', **k: dict(text=t, color=c, **k)
rnd = random.Random(4600)

# ---------------------------------------------------------------- blocs de la mine, objets vendables
MINE_BLOCKS = ['stone', 'deepslate', 'cobblestone', 'cobbled_deepslate', 'andesite', 'diorite', 'granite', 'tuff', 'gravel', 'calcite', 'smooth_basalt',
               'coal_ore', 'deepslate_coal_ore', 'iron_ore', 'deepslate_iron_ore', 'copper_ore', 'deepslate_copper_ore', 'gold_ore', 'deepslate_gold_ore',
               'redstone_ore', 'deepslate_redstone_ore', 'lapis_ore', 'deepslate_lapis_ore', 'diamond_ore', 'deepslate_diamond_ore',
               'emerald_ore', 'deepslate_emerald_ore', 'amethyst_block', 'budding_amethyst', 'amethyst_cluster', 'large_amethyst_bud',
               'medium_amethyst_bud', 'small_amethyst_bud', 'raw_gold_block', 'raw_iron_block', 'ancient_debris']
LUCKY = 'minecraft:gold_nugget[custom_data={fn_lucky:1b},item_name={"text":"🍀 Pépite de chance","color":"gold"},enchantment_glint_override=true]'
LUCKY_Q = 'minecraft:gold_nugget[minecraft:custom_data~{fn_lucky:1b}]'
# (id pour clear/give, prix de base, nom, montré au tableau du marché, variation min..max en %)
SELL = [('cobblestone', 1, 'Pierre', 0, 60, 150), ('cobbled_deepslate', 1, 'Deepslate', 0, 60, 150), ('andesite', 1, 'Andésite', 0, 60, 150),
        ('diorite', 1, 'Diorite', 0, 60, 150), ('granite', 1, 'Granite', 0, 60, 150), ('tuff', 1, 'Tuf', 0, 60, 150), ('gravel', 1, 'Gravier', 0, 60, 150),
        ('flint', 3, 'Silex', 0, 60, 150), ('calcite', 2, 'Calcite', 0, 60, 150), ('smooth_basalt', 2, 'Basalte', 0, 60, 150),
        ('coal', 4, 'Charbon', 1, 50, 170), ('raw_copper', 3, 'Cuivre brut', 1, 50, 170), ('raw_iron', 7, 'Fer brut', 1, 50, 170),
        ('raw_gold', 14, 'Or brut', 1, 50, 170), ('redstone', 2, 'Redstone', 1, 50, 170), ('lapis_lazuli', 3, 'Lapis', 1, 50, 170),
        ('diamond', 50, 'Diamant', 1, 50, 180), ('emerald', 70, 'Émeraude', 1, 50, 180), ('amethyst_shard', 6, 'Éclat d\'améthyste', 1, 50, 170),
        ('amethyst_block', 10, 'Bloc d\'améthyste', 0, 50, 170), ('raw_gold_block', 140, 'Bloc d\'or brut', 1, 50, 180),
        ('raw_iron_block', 70, 'Bloc de fer brut', 0, 50, 180), ('ancient_debris', 300, 'Débris antique', 1, 50, 180),
        (LUCKY_Q, 500, '🍀 Pépite de chance', 1, 50, 180)]
NS = len(SELL)
GIVE_ID = {LUCKY_Q: LUCKY}
iid = lambda s: s if s.startswith('minecraft:') else 'minecraft:' + s

os.makedirs(os.path.join(C.D, 'tags', 'block'), exist_ok=True)
with open(os.path.join(C.D, 'tags', 'block', 'filon_mine.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': ['minecraft:' + b for b in MINE_BLOCKS]}, f, indent=2)
    f.write('\n')
CB = 'can_break={blocks:"#mg:filon_mine"}'

# ---------------------------------------------------------------- équipement (niveaux gardés : mg.fnpk, fnef, fnfo, fnha, fnsw, fnar)
PICK = {1: ('iron_pickaxe', 'fer'), 2: ('diamond_pickaxe', 'diamant'), 3: ('netherite_pickaxe', 'netherite')}
SWORD = {0: ('wooden_sword', 'bois'), 1: ('stone_sword', 'pierre'), 2: ('iron_sword', 'fer'), 3: ('diamond_sword', 'diamant'), 4: ('netherite_sword', 'netherite')}
ARMOR = {1: ('leather', 'cuir'), 2: ('chainmail', 'mailles'), 3: ('iron', 'fer'), 4: ('diamond', 'diamant')}
ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'}
# boutique : (n° trigger, objectif, {niveau actuel: (prix, libellé du niveau suivant)}, libellé si max)
SHOP = [(1, 'mg.fnpk', {1: (400, '⛏ Pioche en diamant'), 2: (1500, '⛏ Pioche en netherite')}, '⛏ Pioche : niveau max'),
        (2, 'mg.fnef', {2: (150, '⚡ Efficacité III'), 3: (350, '⚡ Efficacité IV'), 4: (800, '⚡ Efficacité V')}, '⚡ Efficacité : max'),
        (3, 'mg.fnfo', {0: (300, '🍀 Fortune I'), 1: (900, '🍀 Fortune II'), 2: (2500, '🍀 Fortune III')}, '🍀 Fortune : max'),
        (4, 'mg.fnha', {0: (500, '💨 Hâte II'), 1: (1500, '💨 Hâte III')}, '💨 Hâte : max'),
        (5, 'mg.fnsw', {0: (60, '🗡 Épée en pierre'), 1: (200, '🗡 Épée en fer'), 2: (600, '🗡 Épée en diamant'), 3: (1500, '🗡 Épée en netherite')}, '🗡 Épée : max'),
        (6, 'mg.fnar', {0: (80, '🛡 Armure en cuir'), 1: (250, '🛡 Armure en mailles'), 2: (600, '🛡 Armure en fer'), 3: (1500, '🛡 Armure en diamant')}, '🛡 Armure : max')]
ITEMS = [(7, 20, '🥩 8 steaks', 'minecraft:cooked_beef 8'), (8, 120, '🍎 Pomme d\'or', 'minecraft:golden_apple 1'),
         (9, 150, '🧨 Dynamite', 'DYN')]
DYN = ('minecraft:warped_fungus_on_a_stick[!max_damage,max_stack_size=16,custom_data={fn:1b,fn_dyn:1b},item_model="minecraft:tnt",'
       'item_name={"text":"🧨 Dynamite","color":"red"},lore=[{"text":"Clic droit dans la mine (sous la surface) : explose 2 s plus tard","color":"gray","italic":false}]]')
ROPE = ('minecraft:warped_fungus_on_a_stick[custom_data={fn:1b,fn_rope:1b},unbreakable={},item_model="minecraft:lead",'
        'item_name={"text":"🪢 Corde de remontée","color":"gold"},lore=[{"text":"Clic droit dans la mine : retour à la surface (recharge 120 s)","color":"gray","italic":false}]]')
DEF = [('mg.fnpk', 1), ('mg.fnef', 2), ('mg.fnfo', 0), ('mg.fnha', 0), ('mg.fnsw', 0), ('mg.fnar', 0), ('mg.fnp', 0), ('mg.fncd', 0)] + \
      [(f'mg.fb{i}', 0) for i in range(NS)]

kit = ['# @s : équipement selon ses niveaux (les objets du Filon portent custom_data fn)', 'clear @s *[minecraft:custom_data~{fn:1b}]']
for pk, (pid, _) in PICK.items():
    for ef in range(2, 6):
        for fo in range(0, 4):
            ench = f'efficiency:{ef}' + (f',fortune:{fo}' if fo else '')
            kit.append(f'execute if score @s mg.fnpk matches {pk} if score @s mg.fnef matches {ef} if score @s mg.fnfo matches {fo} run item replace entity @s hotbar.0 with '
                       f'minecraft:{pid}[{CB},enchantments={{{ench}}},unbreakable={{}},custom_data={{fn:1b}}]')
for sw, (sid, _) in SWORD.items():
    kit.append(f'execute if score @s mg.fnsw matches {sw} run item replace entity @s hotbar.1 with minecraft:{sid}[unbreakable={{}},custom_data={{fn:1b}}]')
for ar, (aid, _) in ARMOR.items():
    for slot, piece in (('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings'), ('feet', 'boots')):
        kit.append(f'execute if score @s mg.fnar matches {ar} run item replace entity @s armor.{slot} with minecraft:{aid}_{piece}[unbreakable={{}},custom_data={{fn:1b}}]')
kit.append(f'item replace entity @s hotbar.8 with {ROPE}')
w(f'{P}/kit', kit)

# île, entités, régénération (fn_world.py) ; marché, vente, magasin, PvP (fn_eco.py) : mêmes globals
for _part in ('fn_world.py', 'fn_eco.py'):
    exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), _part), encoding='utf-8').read())

# ---------------------------------------------------------------- horloge globale (même sans joueur), session, boucles
w(f'{P}/clock', ['# Chaque seconde (toujours) : cycle de 45 min, cours du marché, PvP, annonces',
                 'scoreboard players add $fnt mg.st 1',
                 f'execute if score $fnt mg.st matches {REGEN_S}.. if score $fnw mg.st matches 1 if score $fnok mg.st matches 1 run function mg:{P}/regen',
                 f'execute if score $fnt mg.st matches {REGEN_S}.. run function mg:{P}/cycle_idle',
                 'scoreboard players operation #m mg.st = $fnt mg.st', f'scoreboard players operation #m mg.st %= #fnmk mg.st',
                 f'execute if score #m mg.st matches 0 run function mg:{P}/market',
                 'execute unless score $fnw mg.st matches 1 run return 0',
                 f'function mg:{P}/pvp_check',
                 f'execute if score $fnt mg.st matches {REGEN_S - 60} run tellraw @a[tag=mg.fnw] {{"text":"⛏ Le filon se régénère dans 1 minute (les mineurs remonteront tout seuls).","color":"gold"}}',
                 'scoreboard players operation #pa mg.st = $fnpr mg.st', 'scoreboard players remove #pa mg.st 30',
                 'execute if score $fnt mg.st = #pa mg.st run tellraw @a[tag=mg.fnw] {"text":"⚔ Attention : PvP dans la mine dans 30 secondes !","color":"red"}',
                 'execute if score $fnt mg.st = #pa mg.st as @a[tag=mg.fnw] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8',
                 f'function mg:{P}/second'])
w(f'{P}/cycle_idle', ['# 45 min écoulées sans joueur : la régénération attend le prochain mineur', 'scoreboard players set $fnt mg.st 0',
                      'scoreboard players set $fnpend mg.st 1', 'scoreboard players set $fnrp mg.st 0',
                      'execute store result score $fnpr mg.st run random value 900..2100'])
w(f'{P}/lobby_tick', ['# Chaque tick (monde des mini-jeux) : horloge du Filon, session', 'execute unless score $setup mg.st matches 1 run return 0',
                      'scoreboard players add $fnq mg.st 1', f'execute if score $fnq mg.st matches 20.. run function mg:{P}/clock',
                      'execute if score $fnq mg.st matches 20.. run scoreboard players set $fnq mg.st 0',
                      f'execute unless score $fnw mg.st matches 1 if entity @a[tag=mg.fnw] run function mg:{P}/session_start',
                      f'execute if score $fnw mg.st matches 1 unless entity @a[tag=mg.fnw] run function mg:{P}/session_end',
                      f'execute if score $fnw mg.st matches 1 run function mg:{P}/tick'])
w(f'{P}/session_start', ['# Premier mineur : île chargée ; construite si besoin, régénération en attente faite', 'scoreboard players set $fnw mg.st 1',
                         'scoreboard players set $fnok mg.st 0', f'forceload add {FL}', f'schedule function mg:{P}/session_ready 40t'])
w(f'{P}/session_ready', ['execute unless score $fnw mg.st matches 1 run return 0',
                         f'execute unless loaded {CX - R} {YT} {CZ - R} run return run schedule function mg:{P}/session_ready 20t',
                         f'execute unless loaded {CX + R} {YT} {CZ + R} run return run schedule function mg:{P}/session_ready 20t',
                         f'execute unless data storage mg:filon {{built:{VERSION}}} run function mg:{P}/build',
                         f'execute unless entity @e[type=minecraft:text_display,tag=mg.fnboard,{AREA}] run function mg:{P}/ents',
                         'scoreboard players set $fnok mg.st 1', f'function mg:{P}/board',
                         f'execute if score $fnpend mg.st matches 1 run function mg:{P}/regen'])
w(f'{P}/session_end', ['# Plus personne : zone déchargée', 'scoreboard players set $fnw mg.st 0', 'scoreboard players set $fnok mg.st 0',
                       f'schedule clear mg:{P}/session_ready', f'forceload remove {FL}', 'bossbar set mg:filon players'])
w(f'{P}/build_start', ['# (Re)construit l\'île (zone chargée le temps de la construction) : au chargement si besoin, ou par un admin',
                       'scoreboard players set $fnb mg.st 1', f'execute in minecraft:overworld run forceload add {FL}', f'schedule function mg:{P}/build_wait 40t'])
w(f'{P}/build_wait', [f'execute unless loaded {CX - R} {YT} {CZ - R} run return run schedule function mg:{P}/build_wait 20t',
                      f'execute unless loaded {CX + R} {YT} {CZ + R} run return run schedule function mg:{P}/build_wait 20t',
                      'scoreboard players set $fnb mg.st 0', f'function mg:{P}/build', f'function mg:{P}/regen', 'scoreboard players set $fnrp mg.st 0',
                      f'execute unless score $fnw mg.st matches 1 run forceload remove {FL}'])
w(f'{P}/build', ['# Île + entités + chunk de mine neuf', f'function mg:{P}/island', f'function mg:{P}/ents', f'function mg:{P}/board',
                 f'data modify storage mg:filon built set value {VERSION}', 'scoreboard players set $fnpend mg.st 1',
                 'tellraw @a[tag=mg.admin] {"text":"[Filon] Île construite.","color":"gray"}'])
w(f'{P}/regen_now', ['# Admin : régénère le chunk maintenant', f'execute if score $fnok mg.st matches 1 run function mg:{P}/regen',
                     f'execute unless score $fnok mg.st matches 1 run scoreboard players set $fnpend mg.st 1'])

TK = ['# Chaque tick (joueurs présents) : clics, triggers, objets, morts, sécurité',
      f'execute as @e[type=minecraft:interaction,tag=mg.fni,{AREA}] if data entity @s interaction run function mg:{P}/click',
      'scoreboard players enable @a[tag=mg.fnw] mg.fnt',
      f'execute as @a[tag=mg.fnw,scores={{mg.fnt=1..}}] run function mg:{P}/cmd',
      f'execute as @a[tag=mg.fnw,scores={{mg.fnu=1..}}] run function mg:{P}/use',
      f'execute as @a[tag=mg.fnw,scores={{mg.fnd=1..}}] run function mg:{P}/died',
      'scoreboard players reset @a[tag=mg.fnw] mg.fnk',
      '# dans la mine ou en surface',
      'tag @a[tag=mg.fnw] remove mg.fnin', f'tag @a[tag=mg.fnw,{PIT}] add mg.fnin',
      f'execute as @a[tag=mg.fnw,tag=!mg.fnin] at @s if entity @s[y=-64,dy={YT - 4 + 64}] run function mg:{P}/to_surface',
      f'execute as @a[tag=mg.fnw] at @s unless entity @s[{AREA}] run function mg:{P}/to_surface',
      'execute if score $fnpvp mg.st matches 1 run team leave @a[tag=mg.fnw,tag=mg.fnin]',
      'execute if score $fnpvp mg.st matches 1 run team join mg_fn @a[tag=mg.fnw,tag=!mg.fnin]']
w(f'{P}/tick', TK)
w(f'{P}/click', ['# @s = interaction cliquée sur l\'île', 'execute on target run tag @s add mg.fnby', 'data remove entity @s interaction',
                 f'execute if entity @s[tag=mg.fni_sell] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:{P}/sell',
                 f'execute if entity @s[tag=mg.fni_shop] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:{P}/shop',
                 f'execute if entity @s[tag=mg.fni_mkt] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:{P}/market_show',
                 f'execute if entity @s[tag=mg.fni_exit] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:{P}/leave',
                 'tag @a remove mg.fnby'])
w(f'{P}/effects', ['# @s : hâte selon son niveau, vision nocturne (rafraîchies chaque seconde)'] +
  [f'execute if score @s mg.fnha matches {h} run effect give @s minecraft:haste 3 {h} true' for h in range(3)] +
  ['effect give @s minecraft:night_vision 15 0 true'])
w(f'{P}/second', ['# Chaque seconde (joueurs présents) : effets, recharges, barre, PvP en surface',
                  f'execute as @a[tag=mg.fnw] run function mg:{P}/effects',
                  'scoreboard players remove @a[tag=mg.fnw,scores={mg.fncd=1..}] mg.fncd 1',
                  '# coincé dans la roche (reconnecté après une régénération) : remonté',
                  f'execute as @a[tag=mg.fnw,tag=mg.fnin] at @s if block ~ ~ ~ #mg:filon_mine if block ~ ~1 ~ #mg:filon_mine run function mg:{P}/to_surface',
                  'execute if score $fnpvp mg.st matches 1 run effect give @a[tag=mg.fnw,tag=!mg.fnin] minecraft:resistance 2 4 true',
                  'execute if score $fnpvp mg.st matches 1 run effect give @a[tag=mg.fnw,tag=!mg.fnin] minecraft:weakness 2 255 true',
                  'bossbar set mg:filon players @a[tag=mg.fnw]',
                  'execute store result bossbar mg:filon value run scoreboard players get $fnt mg.st',
                  'scoreboard players set #r mg.st 2700', 'scoreboard players operation #r mg.st -= $fnt mg.st', 'scoreboard players operation #r mg.st /= #fn60 mg.st',
                  'execute if score $fnpvp mg.st matches 1 run bossbar set mg:filon color red',
                  'execute if score $fnpvp mg.st matches 1 run bossbar set mg:filon name [{"text":"⚔ PvP dans la mine","color":"red","bold":true},{"text":" — régénération dans ","color":"gray","bold":false},{"score":{"name":"#r","objective":"mg.st"},"color":"yellow","bold":false},{"text":" min","color":"gray","bold":false}]',
                  'execute unless score $fnpvp mg.st matches 1 run bossbar set mg:filon color yellow',
                  'execute unless score $fnpvp mg.st matches 1 run bossbar set mg:filon name [{"text":"⛏ Filon","color":"gold","bold":true},{"text":" — régénération dans ","color":"gray","bold":false},{"score":{"name":"#r","objective":"mg.st"},"color":"yellow","bold":false},{"text":" min","color":"gray","bold":false}]',
                  '# (objets au sol : disparition naturelle au bout de 5 min)'])
CONSTS.append('scoreboard players set #fn60 mg.st 60')
CONSTS.append(f'scoreboard players set #fnmk mg.st {MKT_S}')
w(f'{P}/consts', ['# Constantes, cours de départ, équipe et barre du Filon (chargement)'] + CONSTS)

# ---------------------------------------------------------------- entrée / sortie / saison
BAG_SAVE = ['# @s : son sac (objets vendables pas encore vendus) mis de côté dans ses scores']
BAG_LOAD = ['# @s : son sac rendu']
for i, (iid_, *_) in enumerate(SELL):
    BAG_SAVE.append(f'execute store result score @s mg.fb{i} run clear @s {iid(iid_)}')
    BAG_LOAD += [f'execute if score @s mg.fb{i} matches 1.. store result storage mg:filon g.n int 1 run scoreboard players get @s mg.fb{i}',
                 f'execute if score @s mg.fb{i} matches 1.. run data modify storage mg:filon g.i set value \'{GIVE_ID.get(iid_, iid(iid_))}\'',
                 f'execute if score @s mg.fb{i} matches 1.. run function mg:{P}/give_n with storage mg:filon g', f'scoreboard players set @s mg.fb{i} 0']
w(f'{P}/bag_save', BAG_SAVE)
w(f'{P}/bag_load', BAG_LOAD)
w(f'{P}/give_n', ['$give @s $(i) $(n)'])
w(f'{P}/join', ['# @s : scores par défaut (première visite ou nouvelle saison)',
                f'execute unless score @s mg.fnsea = $fnsea mg.st run function mg:{P}/fresh'] +
  [f'execute unless score @s {o} matches -2147483648.. run scoreboard players set @s {o} {v}' for o, v in DEF] +
  ['scoreboard players reset @s mg.fnd', 'scoreboard players reset @s mg.fnk', 'scoreboard players reset @s mg.fnu', 'scoreboard players reset @s mg.fnt'])
w(f'{P}/fresh', ['# Nouvelle saison pour @s : tout repart de zéro (+ de quoi manger)'] + [f'scoreboard players set @s {o} {v}' for o, v in DEF] +
  ['scoreboard players operation @s mg.fnsea = $fnsea mg.st', 'tag @s add mg.fnnew'])
w(f'{P}/enter', ['# @s entre au Filon (contexte : monde des mini-jeux)',
                 'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : le Filon sera accessible après.","color":"red"}',
                 'function mg:lobkart/leave', 'function mg:parkour/quit', 'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
                 'tag @s add mg.surv', 'tag @s add mg.fnw',
                 'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc', 'execute if score $state mg.st matches 0 run function mg:vote/refresh',
                 'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
                 'attribute @s minecraft:fall_damage_multiplier base set 0', f'function mg:{P}/join', 'function mg:core/heal', 'team join mg_fn @s',
                 f'spawnpoint @s {math.floor(SPAWN[0])} {SPAWN[1]} {math.floor(SPAWN[2])}', f'tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]} 0 0',
                 f'function mg:{P}/kit', f'function mg:{P}/bag_load',
                 'execute if entity @s[tag=mg.fnnew] run give @s minecraft:bread 16', 'tag @s remove mg.fnnew',
                 f'function mg:{P}/effects',
                 'title @s times 10 60 20', 'title @s title {"text":"⛏ FILON","color":"gold","bold":true}',
                 'title @s subtitle {"text":"Un chunk, de la chance, et des pioches","color":"gray"}',
                 'tellraw @s ' + js([TXT('⛏ FILON', 'gold', bold=True), TXT(' : saute dans le chunk au centre de l\'île et mine. Vends au ', 'yellow'),
                                     TXT('💰 Comptoir', 'gold'), TXT(' (le cours change toutes les 15 min), améliore-toi au ', 'yellow'), TXT('🛒 Magasin', 'aqua'), TXT('.', 'yellow')]),
                 'tellraw @s ' + js([TXT(' ⏳ Régénération du chunk toutes les 45 min — ', 'gray'), TXT('⚔ PvP seulement dans la mine, pendant les phases annoncées', 'red'),
                                     TXT(' (tué : la moitié de ton sac part au tueur).', 'gray')]),
                 'tellraw @s ' + js([TXT(' 🪢 Corde (case 9) : remonter (recharge 120 s). Ta progression est gardée jusqu\'à la fin de la saison.', 'gray')]),
                 'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6'])
w(f'{P}/leave', ['# @s retourne au lobby (contexte : monde des mini-jeux) : sac mis de côté', 'execute unless entity @s[tag=mg.fnw] run return 0',
                 f'function mg:{P}/bag_save', 'tag @s remove mg.fnw', 'tag @s remove mg.surv', 'tag @s remove mg.fnin', 'team leave @s',
                 'bossbar set mg:filon players @a[tag=mg.fnw]', 'effect clear @s', 'function mg:core/reset_player',
                 'attribute @s minecraft:fall_damage_multiplier base set 0',
                 'tellraw @s [{"text":"⌂ Retour au lobby. Ta progression reste au Filon (solde ","color":"gold"},{"score":{"name":"@s","objective":"mg.fnp"},"color":"yellow"},{"text":" pts, saison ","color":"gold"},{"score":{"name":"@s","objective":"mg.fns"},"color":"yellow"},{"text":" pts).","color":"gold"}]'])
w(f'{P}/menu_go', ['# @s : « Aller au Filon » (menu Échap, trigger mg.sv 9)',
                   'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup","color":"red"}',
                   'execute if entity @s[tag=mg.fnw] run return run tellraw @s {"text":"Tu es déjà au Filon.","color":"gray"}',
                   'execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : le Filon sera accessible après.","color":"red"}',
                   'execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : le Filon sera accessible après.","color":"red"}',
                   'execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]',
                   f'execute unless data storage mg:filon {{built:{VERSION}}} unless score $fnb mg.st matches 1 run function mg:{P}/build_start',
                   f'execute unless data storage mg:filon {{built:{VERSION}}} run return run tellraw @s {{"text":"🚧 Le Filon se prépare (île en construction) : réessaie dans quelques secondes.","color":"yellow"}}',
                   'execute if entity @s[tag=mg.surv] run function mg:survie/leave', f'execute in minecraft:overworld run function mg:{P}/enter'])
w(f'{P}/season_end', ['# Fin de saison : classement gardé dans mg.fnl, tout le monde repart de zéro à sa prochaine visite',
                      'tellraw @a {"text":"⛏ Fin de la saison du Filon ! Le classement repart à zéro (l\'ancien reste visible : /scoreboard objectives setdisplay sidebar mg.fnl).","color":"gold","bold":true}',
                      f'execute as @a[tag=mg.fnw] in minecraft:overworld run function mg:{P}/leave',
                      'scoreboard players reset * mg.fnl', 'scoreboard players operation * mg.fnl = * mg.fns', 'scoreboard players reset * mg.fns',
                      'scoreboard players add $fnsea mg.st 1', 'scoreboard players set $fnsc mg.st 0'])

# ---------------------------------------------------------------- câblage dans le datapack
C.patch('core/tick', 'function mg:ombre/lobby_tick', [f'function mg:{P}/lobby_tick'])
C.patch('survie/leave', 'execute if entity @s[tag=mg.olw] run return run function mg:ombre/leave',
        [f'execute if entity @s[tag=mg.fnw] run return run function mg:{P}/leave'])
C.patch('survie/cmd', 'execute if score @s mg.sv matches 8 run function mg:ombre/menu_go', [f'execute if score @s mg.sv matches 9 run function mg:{P}/menu_go'])
_cmd = C.lines_of('survie/cmd')
if '8 = Ombrelune,' in _cmd[0] and 'Filon' not in _cmd[0]:
    _cmd[0] = _cmd[0].replace('8 = Ombrelune,', '8 = Ombrelune, 9 = Filon,')
    C.w('survie/cmd', _cmd[:-1] if _cmd[-1] == '' else _cmd)
_pa = C.lines_of('core/pull_all')
_pa = [l.replace('tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw] add mg.pulls', 'tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw,tag=!mg.fnw] add mg.pulls') for l in _pa]
if 'tag @a[tag=mg.fnw] add mg.pullf' not in _pa:
    i = _pa.index('tag @a[tag=mg.olw] add mg.pullo')
    _pa[i + 1:i + 1] = ['tag @a[tag=mg.fnw] add mg.pullf']
    i = _pa.index('tag @a[tag=mg.spectate] remove mg.pullo')
    _pa[i + 1:i + 1] = ['tag @a[tag=mg.spectate] remove mg.pullf']
    j = _pa.index('execute as @a[tag=mg.pullo] in minecraft:overworld run function mg:ombre/leave')
    _pa[j + 1:j + 1] = [f'execute as @a[tag=mg.pullf] in minecraft:overworld run function mg:{P}/leave']
C.w('core/pull_all', _pa[:-1] if _pa[-1] == '' else _pa)
C.patch('core/optout', 'execute if entity @s[tag=mg.pullo] in minecraft:overworld run function mg:ombre/enter',
        [f'execute if entity @s[tag=mg.pullf] in minecraft:overworld run function mg:{P}/enter'])
C.patch('core/optout', 'tag @s remove mg.pullo', ['tag @s remove mg.pullf'])
C.patch('core/request', 'tag @a remove mg.pullo', ['tag @a remove mg.pullf'])
# survie/tick : un mineur du Filon est dans le monde des mini-jeux sans être un joueur de survie égaré ; ses objets au sol sont gardés
C._fn.replace('survie/tick', 'execute as @a[tag=mg.surv] at @s if dimension minecraft:overworld run function mg:survie/from_overworld',
              'execute as @a[tag=mg.surv,tag=!mg.fnw] at @s if dimension minecraft:overworld run function mg:survie/from_overworld')
C._fn.replace('survie/tick', 'tag=!mg.olw,tag=!mg.svg2,', 'tag=!mg.olw,tag=!mg.fnw,tag=!mg.svg2,')
C.patch('survie/tick', 'execute in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:item,distance=0..,tag=!mg.keep]',
        [f'execute if score $fnw mg.st matches 1 in minecraft:overworld run tag @e[type=minecraft:item,{AREA}] add mg.keep'], where='before')
FN_LOAD = ['# Filon : constantes, cours, équipe, barre ; pas de zone chargée hors session ; île construite une fois (~1 s)', f'function mg:{P}/consts',
           'scoreboard players set $fnw mg.st 0', 'scoreboard players set $fnok mg.st 0', 'scoreboard players set $fnb mg.st 0',
           f'execute if score $setup mg.st matches 1 unless data storage mg:filon {{built:{VERSION}}} run schedule function mg:{P}/build_start 45s']
C.drop_lines('core/load', FN_LOAD)
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', FN_LOAD, where='after')
OBJ = sorted({o for o, _ in DEF} | {'mg.fns', 'mg.fnl', 'mg.fnsea'})
C.objectives([(o, 'dummy') for o in OBJ if o not in ('mg.fns', 'mg.fnl')] +
             [('mg.fns', 'dummy {"text":"⛏ Filon — saison","color":"gold","bold":true}'), ('mg.fnl', 'dummy {"text":"⛏ Filon — saison passée","color":"gold"}'),
              ('mg.fnu', 'minecraft.used:minecraft.warped_fungus_on_a_stick'), ('mg.fnd', 'deathCount'), ('mg.fnk', 'playerKillCount'), ('mg.fnt', 'trigger')])
FN_UNINST = [f'execute as @a[tag=mg.fnw] in minecraft:overworld run function mg:{P}/leave', f'execute in minecraft:overworld run kill @e[tag=mg.fne]',
             f'execute in minecraft:overworld run forceload remove {FL}', 'team remove mg_fn', 'bossbar remove mg:filon',
             f'schedule clear mg:{P}/session_ready', f'schedule clear mg:{P}/build_start', f'schedule clear mg:{P}/build_wait', f'schedule clear mg:{P}/season_end', 'data remove storage mg:filon built']
C.drop_lines('desinstaller', FN_UNINST)
C.patch('desinstaller', 'execute as @a[tag=mg.olw] in minecraft:overworld run function mg:ombre/leave', FN_UNINST)
# menu Échap : « ⛏ Aller au Filon » (après Ombrelune)
_mp = os.path.join(C.D, 'dialog', 'main_menu.json')
_m = json.load(open(_mp, encoding='utf-8'))
if not any(a['action'].get('command') == 'trigger mg.sv set 9' for a in _m['actions']):
    i = next(i for i, a in enumerate(_m['actions']) if a['action'].get('command') == 'trigger mg.sv set 8')
    _m['actions'].insert(i + 1, {'label': [{'text': '⛏ Aller au Filon', 'color': 'gold', 'bold': True}],
                                 'tooltip': [{'text': 'Une île, un chunk à miner, un marché qui bouge : vends, améliore-toi, gagne la saison (progression gardée)', 'color': 'gray'}],
                                 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.sv set 9'}})
    with open(_mp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(_m, f, ensure_ascii=False, indent=2)
        f.write('\n')
print(f'Filon OK : île {len(ISL)} commandes, régénération {len(RG)} commandes, {NS} objets vendables')
