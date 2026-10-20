# Neo GTA, véhicules (carrosserie DSP / H), liasses de billets, interface (HUD) : exécuté par gen_gta.py (exec) à sa place d'origine.
# Utilise : CARS, DIM, G, HELI_AT, HX, js, TR, w, Z

# ---------------------------------------------------------------- véhicules : morceaux de carrosserie (block_display liés par mg.gvid)
def DSP(kind, blk, tx, ty, tz, sx, sy, sz, body=False, extra=''):
    tags = f'"mg.gta","mg.gvd","mg.gvn","{kind}"' + (',"mg.gvb"' if body else '')
    return (f'summon minecraft:block_display ~ ~ ~ {{Tags:[{tags}],block_state:{{Name:"minecraft:{blk}"}},teleport_duration:1,'
            f'{TR % (tx, ty, tz, sx, sy, sz)}{extra}}}')


for (n, body, roof, name, spd) in CARS:
    def D(*a, **k): return DSP('mg.gcard', *a, **k)
    L = [f'# Voiture n° {n} : {name} (cheval invisible rapetissé : on est assis dans l\'habitacle)', 'scoreboard players add $gvid mg.st 1',
         'summon minecraft:horse ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcarh","mg.gvn","mg.npc"],Tame:1b,Silent:1b,PersistenceRequired:1b,Health:40f,'
         'equipment:{saddle:{id:"minecraft:saddle",count:1}},drop_chances:{saddle:0f},'
         f'CustomName:{js({"text": name, "color": "yellow"})},CustomNameVisible:0b,'
         'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
         f'attributes:[{{id:"minecraft:movement_speed",base:{spd}}},{{id:"minecraft:jump_strength",base:0.0}},{{id:"minecraft:step_height",base:1.1}},'
         '{id:"minecraft:max_health",base:40},{id:"minecraft:scale",base:0.55}]}',
         D(body, -0.95, 0.05, -1.7, 1.9, 0.75, 3.4, body=True),           # caisse
         D(roof, -0.8, 0.8, -0.9, 1.6, 0.65, 1.7),                         # habitacle
         D('black_concrete', -1.0, 0.0, -1.25, 0.25, 0.45, 0.6), D('black_concrete', 0.75, 0.0, -1.25, 0.25, 0.45, 0.6),   # roues
         D('black_concrete', -1.0, 0.0, 0.85, 0.25, 0.45, 0.6), D('black_concrete', 0.75, 0.0, 0.85, 0.25, 0.45, 0.6),
         D('sea_lantern', -0.8, 0.35, 1.68, 0.35, 0.2, 0.05), D('sea_lantern', 0.45, 0.35, 1.68, 0.35, 0.2, 0.05),       # phares
         D('redstone_block', -0.8, 0.35, -1.73, 0.35, 0.2, 0.05), D('redstone_block', 0.45, 0.35, -1.73, 0.35, 0.2, 0.05),
         D('light_gray_concrete', -0.9, 0.1, 1.7, 1.8, 0.15, 0.1)]                                                          # pare-chocs
    if 'Taxi' in name:
        L.append(D('yellow_concrete', -0.3, 1.45, -0.3, 0.6, 0.2, 0.6))
    if 'police' in name:
        L += [D('blue_stained_glass', -0.55, 1.45, -0.2, 0.5, 0.2, 0.4), D('red_stained_glass', 0.05, 1.45, -0.2, 0.5, 0.2, 0.4)]
    if n == 8:
        L.append(D(body, -0.95, 0.8, -1.7, 1.9, 0.9, 1.9))
    L += ['summon minecraft:interaction ~ ~ ~ {Tags:["mg.gta","mg.gcint","mg.gvn"],width:2.4f,height:1.7f,response:1b}', 'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
    w(f'gta/car/spawn_{n}', L)
w('gta/car_random', ['# Une voiture au hasard à ce carrefour (remplace une voiture détruite)',
                     f'execute store result score $gr mg.st run random value 1..{len(CARS)}'] +
  [f'execute if score $gr mg.st matches {n} positioned ~2 ~ ~ run function mg:gta/car/spawn_{n}' for (n, *_) in CARS])
w('gta/car_sync', ['# @s : cheval d\'une voiture. La carrosserie suit ; lancée (> 0,2 bloc/tick), elle renverse ce qu\'elle percute',
                   'scoreboard players operation $gv mg.st = @s mg.gvid',
                   'execute unless predicate mg:has_passenger as @e[type=minecraft:interaction,tag=mg.gcint] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if predicate mg:has_passenger positioned ~ ~-6 ~ as @e[type=minecraft:interaction,tag=mg.gcint] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute store result score $gx mg.st run data get entity @s Pos[0] 100',
                   'execute store result score $gz mg.st run data get entity @s Pos[2] 100',
                   'scoreboard players operation $gdx mg.st = $gx mg.st', 'scoreboard players operation $gdx mg.st -= @s mg.gpx',
                   'scoreboard players operation $gdz mg.st = $gz mg.st', 'scoreboard players operation $gdz mg.st -= @s mg.gpz',
                   'scoreboard players operation @s mg.gpx = $gx mg.st', 'scoreboard players operation @s mg.gpz = $gz mg.st',
                   'scoreboard players operation $gdx mg.st *= $gdx mg.st', 'scoreboard players operation $gdz mg.st *= $gdz mg.st',
                   'scoreboard players operation $gdx mg.st += $gdz mg.st',
                   # carrosserie : légèrement en avance selon la vitesse (le conducteur voit son cheval bouger sans délai)
                   'execute unless score $gdx mg.st matches 100..100000 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 100..899 positioned ^ ^ ^0.3 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 900..1599 positioned ^ ^ ^0.6 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 1600..100000 positioned ^ ^ ^0.9 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 400..100000 on passengers run function mg:gta/car_ram',
                   'execute if score $gdx mg.st matches 400..100000 run particle minecraft:smoke ^ ^0.3 ^-1.8 0.1 0.05 0.1 0.01 1',
                   'execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 0 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3',
                   'execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 10 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3'])
w('gta/vd_follow', ['# @s : morceau de carrosserie, colle au véhicule (position et cap du contexte)', 'tp @s ~ ~ ~ ~ 0', 'tag @s add mg.gok'])
w('gta/car_int', ['# @s (zone cliquable d\'une voiture) : le joueur qui a cliqué monte au volant', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                  'execute on target run function mg:gta/car_mount', 'data remove entity @s interaction', 'data remove entity @s attack'])
w('gta/car_mount', ['# @s (joueur) : monte dans la voiture $gv (si personne ne la conduit)',
                    'execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gv mg.st run tag @s add mg.gmnt',
                    'ride @s mount @e[type=minecraft:horse,tag=mg.gmnt,limit=1]', 'tag @e remove mg.gmnt'])
w('gta/car_ram', ['# @s : conducteur d\'une voiture lancée : renverse (6 dégâts) ce qui est juste devant',
                  'tag @s add mg.grd',
                  'execute on vehicle rotated as @s positioned ^ ^ ^1.8 as @e[tag=mg.gtg,tag=!mg.grd,tag=!mg.gcarh,distance=..1.5] run damage @s 6 minecraft:player_attack by @a[tag=mg.grd,limit=1]',
                  'tag @s remove mg.grd'])
w('gta/wreck', ['# @s : caisse d\'un véhicule détruit (son cheval ou son ghast est mort) : explosion',
                'function mg:bomber/boom/r2',
                'execute as @e[tag=mg.gtg,distance=..3.5] run damage @s 8 minecraft:explosion',
                'particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~1 ~ 1.2 0.8 1.2 0.1 50 force',
                'particle minecraft:large_smoke ~ ~1.5 ~ 1 1 1 0.05 40 force', 'particle minecraft:lava ~ ~1 ~ 1 0.5 1 0 15 force',
                'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.7'])

# hélicos : happy ghast invisible rapetissé (siège à ~2 blocs), modèle autour du pilote
SH = 2.0


def H(blk, tx, ty, tz, sx, sy, sz, body=False):
    return DSP('mg.ghbody', blk, tx, SH + ty, tz, sx, sy, sz, body=body)


HELI = ['# Hélico : happy ghast invisible et rapetissé, carrosserie de couleur $(c), rotors qui tournent', 'scoreboard players add $gvid mg.st 1',
        'summon minecraft:happy_ghast ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.ghel","mg.gvn","mg.npc"],PersistenceRequired:1b,Health:60f,'
        'equipment:{body:{id:"minecraft:black_harness",count:1}},drop_chances:{body:0f},'
        f'CustomName:{js({"text": "🚁 Hélico", "color": "aqua", "bold": True})},CustomNameVisible:0b,'
        'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
        'attributes:[{id:"minecraft:flying_speed",base:0.12},{id:"minecraft:movement_speed",base:0.12},{id:"minecraft:max_health",base:60},{id:"minecraft:scale",base:0.5}]}']
HELI += ['$' + H('$(c)', -0.9, -0.6, -1.4, 1.8, 1.5, 2.8, body=True),                       # fuselage
         H('light_blue_stained_glass', -0.8, -0.5, 1.4, 1.6, 1.25, 0.9),                    # cockpit
         '$' + H('$(c)', -0.7, 0.75, 1.0, 1.4, 0.15, 0.8),                                    # toit avant
         '$' + H('$(c)', -0.2, 0.1, -5.2, 0.4, 0.4, 3.8),                                     # poutre de queue
         '$' + H('$(c)', -0.06, 0.3, -5.3, 0.12, 1.1, 0.6),                                   # dérive
         H('gray_concrete', 0.1, 0.35, -5.35, 0.06, 1.0, 0.22), H('gray_concrete', 0.1, 0.74, -5.74, 0.06, 0.22, 1.0),   # rotor de queue
         H('gray_concrete', -1.0, -1.25, -1.3, 0.12, 0.12, 3.0), H('gray_concrete', 0.88, -1.25, -1.3, 0.12, 0.12, 3.0),  # patins
         H('gray_concrete', -0.95, -1.15, -0.8, 0.08, 0.55, 0.08), H('gray_concrete', 0.87, -1.15, -0.8, 0.08, 0.55, 0.08),
         H('gray_concrete', -0.95, -1.15, 0.8, 0.08, 0.55, 0.08), H('gray_concrete', 0.87, -1.15, 0.8, 0.08, 0.55, 0.08),
         H('gray_concrete', -0.1, 0.9, -0.1, 0.2, 0.4, 0.2),                                # mât
         H('sea_lantern', -0.1, -0.7, 1.6, 0.2, 0.1, 0.2),                                  # phare
         DSP('mg.ghrot', 'black_concrete', -4.5, SH + 1.3, -0.15, 9, 0.08, 0.3),            # pales du rotor principal
         DSP('mg.ghrot', 'black_concrete', -0.15, SH + 1.3, -4.5, 0.3, 0.08, 9),
         DSP('mg.ghrot', 'gray_concrete', -0.3, SH + 1.25, -0.3, 0.6, 0.2, 0.6),
         'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
w('gta/heli_spawn', HELI)
w('gta/heli_random', ['# Un hélico de remplacement sur une des hélisurfaces (contexte : dimension mg:gta)',
                      f'execute store result score $gr mg.st run random value 0..{len(HELI_AT) - 1}'] +
  [f'execute if score $gr mg.st matches {i} in {DIM} positioned {x} 66 {Z + z} unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] '
   f'run function mg:gta/heli_spawn {{c:"{col}"}}' for i, (x, z, col) in enumerate(HELI_AT)])
w('gta/heli_park', ['# @s : hélico ou avion sans pilote, il reste sur place', 'tag @s add mg.gpark',
                    'attribute @s minecraft:flying_speed modifier add mg:park -1 add_multiplied_total', 'data merge entity @s {Motion:[0d,0d,0d]}'])
w('gta/heli_unpark', ['# @s : un pilote est monté, il peut voler', 'tag @s remove mg.gpark', 'attribute @s minecraft:flying_speed modifier remove mg:park'])
w('gta/heli_sync', ['# @s : hélico. La carrosserie suit, les rotors tournent (plus vite avec un pilote)',
                    'scoreboard players operation $gv mg.st = @s mg.gvid',
                    'execute on passengers run tag @s add mg.gpil',
                    'execute unless entity @a[tag=mg.gpil] unless entity @s[tag=mg.gpark] run function mg:gta/heli_park',
                    'execute if entity @a[tag=mg.gpil] if entity @s[tag=mg.gpark] run function mg:gta/heli_unpark',
                    'execute as @e[type=minecraft:block_display,tag=mg.ghbody] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                    'execute if entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_fast',
                    'execute unless entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_slow',
                    'execute if entity @a[tag=mg.gpil] run particle minecraft:cloud ~ ~-0.3 ~ 1.5 0.1 1.5 0.02 2',
                    'execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 0 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5',
                    'execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 10 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5',
                    'tag @a remove mg.gpil'])
w('gta/rotor_fast', ['tp @s ~ ~ ~ ~45 0', 'tag @s add mg.gok'])
w('gta/rotor_slow', ['tp @s ~ ~ ~ ~6 0', 'tag @s add mg.gok'])

# ---------------------------------------------------------------- liasses de billets, interface
w('gta/cash_new', ['# Une liasse de billets ici, montant $gcv (score mg.gpc de l\'objet)',
                   'execute if score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew","mg.gbill"],'
                   'item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"mg:cash"}},teleport_duration:1,billboard:"vertical",'
                   f'Glowing:1b,glow_color_override:5635925,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
                   'execute unless score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew"],'
                   f'item:{{id:"minecraft:emerald_block",count:1}},teleport_duration:1,Glowing:1b,glow_color_override:5635925,{TR % (0, 0, 0, 0.6, 0.45, 0.6)}}}',
                   'scoreboard players operation @e[type=minecraft:item_display,tag=mg.gcnew] mg.gpc = $gcv mg.st',
                   'tag @e[tag=mg.gcnew] remove mg.gcnew',
                   'particle minecraft:happy_villager ~ ~0.3 ~ 0.4 0.4 0.4 0 10'])
w('gta/cash_spawn', ['# Une valise de billets (+75 $) sur ce trottoir', 'scoreboard players set $gcv mg.st 75',
                     'execute positioned ~ ~0.8 ~ run function mg:gta/cash_new',
                     'tellraw @a[tag=mg.gtw] {"text":"💰 Une valise de billets est apparue quelque part en ville !","color":"green"}'])
w('gta/cash_take', ['# @s : liasse ramassée par le joueur le plus proche (montant mg.gpc)', 'scoreboard players operation $gcv mg.st = @s mg.gpc',
                    'execute as @p[tag=mg.gtw] run function mg:gta/cash_gain',
                    'execute at @s run playsound minecraft:entity.player.levelup player @a ~ ~ ~ 0.8 1.4', 'kill @s'])
w('gta/cash_gain', ['# @s ramasse $gcv dollars', 'scoreboard players operation @s mg.gta += $gcv mg.st', 'scoreboard players set @s mg.gal 40',
                    'title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},'
                    '{"text":" $ ","color":"green","bold":true},{"text":"billets ramassés","color":"gray"}]'])
MONEY_RP = [{'text': '$', 'font': 'mg:gta_cash'}, {'score': {'name': '@s', 'objective': 'mg.gta'}, 'font': 'mg:gta_cash'}]
MONEY_PL = [{'text': '$ ', 'color': 'green', 'bold': True}, {'score': {'name': '@s', 'objective': 'mg.gta'}, 'color': 'green', 'bold': True}]
GAP = {'text': '      ', 'color': 'gray'}


def hud_lines(money):
    L = []
    for n, g in G.GUNS.items():
        L.append(f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] unless score @s mg.grl matches 1.. run return run title @s actionbar ' +
                 js([{'text': '🔫 ' + g[0] + '  ', 'color': g[8]}, {'score': {'name': '@s', 'objective': f'mg.g{n}'}, 'color': 'white', 'bold': True},
                     {'text': f' / {2 * g[4]}', 'color': 'gray'}, GAP] + money))
    L.append('execute if score @s mg.grl matches 1.. run return run title @s actionbar ' + js([{'text': '⟳ Rechargement…', 'color': 'yellow'}, GAP] + money))
    L.append('execute if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run return run title @s actionbar ' +
             js([{'text': '🚀 Roquettes  ', 'color': 'red'}, {'score': {'name': '@s', 'objective': 'mg.grk'}, 'color': 'white', 'bold': True}, GAP] + money))
    L.append('title @s actionbar ' + js(money))
    return L


w('gta/hud', ['# Toutes les 0,5 s : munitions et dollars (sauf pendant un message)',
              'execute as @a[tag=mg.gtw,scores={mg.gal=..0}] run function mg:gta/hud_one'])
w('gta/hud_one', ['# @s : barre d\'action (police verte du pack si $rp = 1) ; mission en cours en priorité',
                  'execute if score @s mg.gmt matches 1.. run return run function mg:gta/mis_hud',
                  'execute if score $rp mg.st matches 1 run return run function mg:gta/hud_rp',
                  'function mg:gta/hud_plain'])
w('gta/hud_rp', ['# @s : munitions + dollars en chiffres GTA ; sans arme : mini-carte + dollars'] + hud_lines(MONEY_RP)[:-1] + ['function mg:gta/mini_show'])
w('gta/mini_show', ['# @s : mini-carte (case 30 × 30 de sa position) au-dessus des dollars',
                    'execute store result score $gmi mg.st run data get entity @s Pos[0]', 'execute store result score $gmj mg.st run data get entity @s Pos[2]',
                    f'scoreboard players add $gmi mg.st {HX}', f'scoreboard players remove $gmj mg.st {Z - HX}',
                    'scoreboard players set #30 mg.st 30', 'scoreboard players set #177 mg.st 177',
                    'scoreboard players operation $gmi mg.st *= #30 mg.st', 'scoreboard players operation $gmi mg.st /= #177 mg.st',
                    'scoreboard players operation $gmj mg.st *= #30 mg.st', 'scoreboard players operation $gmj mg.st /= #177 mg.st',
                    'execute if score $gmi mg.st matches ..-1 run scoreboard players set $gmi mg.st 0', 'execute if score $gmi mg.st matches 30.. run scoreboard players set $gmi mg.st 29',
                    'execute if score $gmj mg.st matches ..-1 run scoreboard players set $gmj mg.st 0', 'execute if score $gmj mg.st matches 30.. run scoreboard players set $gmj mg.st 29'] +
  [f'execute if score $gmj mg.st matches {j} run return run function mg:gta/mini/row_{j}' for j in range(30)])
for j in range(30):
    w(f'gta/mini/row_{j}', [f'# Mini-carte, ligne {j}'] +
      [f'execute if score $gmi mg.st matches {i} run return run title @s actionbar ' +
       js([{'text': '\ue600\ue601', 'font': 'mg:gta_mini', 'color': 'white', 'shadow_color': 0},
           {'text': chr(0xE700 + 30 * j + i), 'font': 'mg:gta_mini', 'color': '#FF2A2A', 'shadow_color': 0}, {'text': '   '}] + MONEY_RP)
       for i in range(30)])
w('gta/hud_plain', ['# @s : munitions + dollars (sans pack)'] + hud_lines(MONEY_PL))
