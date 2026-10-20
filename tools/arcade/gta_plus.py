# Neo GTA, systèmes de ville vivante : exécuté par gen_gta.py (exec) après les véhicules, avant le câblage.
# Utilise w, js, C, G, Z, DIM, INTER, AV, ST, PARK, in_park, CARS, SH, DSP, H, TR, HX, LIMIT? (non), etc.
#
# Circulation : voitures PNJ (marqueur mg.gtraf + carrosserie mg.gtrd) qui roulent à droite sur le graphe des rues,
#   choisissent une direction au hasard à chaque carrefour, s'arrêtent devant un obstacle (klaxon), se volent accroupi.
# Passants qui fuient les coups de feu (husk invisible et immobile une seconde : les villageois paniquent).
# Police : voitures de police pilotées par un policier (2 ★), barrages (4 ★), hélico de police (5 ★) ; on ne sème la
#   une étoile de moins toutes les 15 s sans nouveau délit.

# ---------------------------------------------------------------- graphe des rues
NODES = INTER
IDX = {p: i for i, p in enumerate(NODES)}
DIRS = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}           # 0 sud (+z), 1 ouest, 2 nord, 3 est (lacet 0 / 90 / 180 / 270)
RIGHT = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}          # main droite selon le cap
YAW = {0: 0, 1: 90, 2: 180, 3: 270}


def neighbour(i, h):
    cx, cz = NODES[i]
    if h in (0, 2):                                              # le long d'une avenue
        zs = sorted(s for s in ST if (cx, s) in IDX)
        k = zs.index(cz) + (1 if h == 0 else -1)
        if 0 <= k < len(zs):
            nz = zs[k]
            if not in_park(cx, (cz + nz) // 2):
                return IDX[(cx, nz)]
    else:                                                        # le long d'une rue
        xs = sorted(c for c in AV if (c, cz) in IDX)
        k = xs.index(cx) + (1 if h == 3 else -1)
        if 0 <= k < len(xs):
            nx = xs[k]
            if not in_park((cx + nx) // 2, cz):
                return IDX[(nx, cz)]
    return None


NB = {(i, h): neighbour(i, h) for i in range(len(NODES)) for h in range(4)}


def lane(i, h):
    cx, cz = NODES[i]
    rx, rz = RIGHT[h]
    off = 2 if h in (0, 2) else 1.5
    return cx + 0.5 + rx * off, cz + 0.5 + rz * off


def go_lines(i, h2):
    """Lignes qui lancent la voiture (@s, marqueur) depuis le carrefour i vers le cap h2."""
    j = NB[(i, h2)]
    px, pz = lane(i, h2)
    tx, tz = lane(j, h2)
    return [f'tp @s {px} 65 {Z + pz} {YAW[h2]} 0', f'scoreboard players set @s mg.gth {h2}', f'scoreboard players set @s mg.gtn {j}',
            f'scoreboard players set @s mg.gttx {int(round(tx * 10))}', f'scoreboard players set @s mg.gttz {int(round((Z + tz) * 10))}']


for i in range(len(NODES)):
    D = [f'# Voiture PNJ arrivée au carrefour {i} {NODES[i]} : nouvelle direction au hasard (tout droit, gauche, droite ; demi-tour en cul-de-sac)']
    for h in range(4):
        opts = [h2 for h2 in (h, (h + 1) % 4, (h + 3) % 4) if NB[(i, h2)] is not None]
        if not opts:
            opts = [(h + 2) % 4] if NB[(i, (h + 2) % 4)] is not None else []
        if not opts:
            continue
        fn = f'gta/traffic/n{i}_{h}'
        L = [f'# Carrefour {i}, arrivée au cap {h}', f'execute store result score $gr mg.st run random value 0..{len(opts) - 1}']
        for k, h2 in enumerate(opts):
            w(f'{fn}_{k}', [f'# Carrefour {i} : départ au cap {h2}'] + go_lines(i, h2))
            L.append(f'execute if score $gr mg.st matches {k} run return run function mg:{fn}_{k}')
        w(fn, L)
        D.append(f'execute if score @s mg.gth matches {h} run return run function mg:{fn}')
    w(f'gta/traffic/n{i}', D)
w('gta/traffic/arrive', ['# @s (voiture PNJ) atteint son carrefour cible (mg.gtn)'] +
  [f'execute if score @s mg.gtn matches {i} run return run function mg:gta/traffic/n{i}' for i in range(len(NODES))])

# carrosseries : celles des voitures (fichiers déjà générés), étiquettes de circulation
import re as _re
for (n, *_rest) in CARS:
    src = open(os.path.join(C.F, 'gta', 'car', f'spawn_{n}.mcfunction'), encoding='utf-8').read().split('\n')
    body = [l.replace('"mg.gta","mg.gvd","mg.gvn","mg.gcard","mg.gvb"', '"mg.gta","mg.gtrd","mg.gvn"').replace('"mg.gta","mg.gvd","mg.gvn","mg.gcard"', '"mg.gta","mg.gtrd","mg.gvn"')
            for l in src if l.startswith('summon minecraft:block_display')]
    w(f'gta/traffic/body_{n}', [f'# Carrosserie de voiture PNJ (modèle {n})'] + body)
SP = ['# Une voiture PNJ à ce carrefour (contexte : marqueur mg.gix) : modèle au hasard, direction au hasard',
      'scoreboard players add $gvid mg.st 1',
      'summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.gtraf","mg.gvn","mg.gtnew"]}',
      f'execute store result score $gr mg.st run random value 1..{len(CARS)}',
      'scoreboard players operation @e[type=minecraft:marker,tag=mg.gtnew] mg.gtmod = $gr mg.st']
SP += [f'execute if score $gr mg.st matches {n} run function mg:gta/traffic/body_{n}' for (n, *_r) in CARS]
SP += ['summon minecraft:interaction ~ ~ ~ {Tags:["mg.gta","mg.gtint","mg.gvn"],width:2.4f,height:1.7f,response:1b}',
       'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn',
       'scoreboard players set @e[type=minecraft:marker,tag=mg.gtnew] mg.gtw8 0',
       'execute as @e[type=minecraft:marker,tag=mg.gtnew] run function mg:gta/traffic/start', 'tag @e[tag=mg.gtnew] remove mg.gtnew']
w('gta/traffic/spawn', SP)
ST_ = ['# @s (nouvelle voiture PNJ) : carrefour le plus proche, cap au hasard']
for i, (x, z) in enumerate(NODES):
    ST_.append(f'execute if entity @s[x={x},y=65,z={Z + z},distance=..1.5] run scoreboard players set @s mg.gtn {i}')
ST_ += ['execute store result score @s mg.gth run random value 0..3', 'function mg:gta/traffic/arrive']
w('gta/traffic/start', ST_)
w('gta/traffic/tick', ['# @s : voiture PNJ (chaque tick) : avance de 0,3 bloc sauf obstacle, carrefour atteint, carrosserie',
                       'scoreboard players add @s mg.gtw8 1',
                       'execute positioned ^ ^ ^2.6 if entity @e[type=!minecraft:marker,type=!minecraft:block_display,type=!minecraft:item_display,type=!minecraft:text_display,type=!minecraft:item,type=!minecraft:arrow,distance=..1.9] run return run function mg:gta/traffic/blocked',
                       'execute positioned ^ ^ ^2.6 if entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..1.9] run return run function mg:gta/traffic/blocked',
                       'scoreboard players set @s mg.gtw8 0',
                       'tp @s ^ ^ ^0.3',
                       'execute store result score $gpx mg.st run data get entity @s Pos[0] 10', 'execute store result score $gpz mg.st run data get entity @s Pos[2] 10',
                       'execute if score @s mg.gth matches 3 if score $gpx mg.st >= @s mg.gttx run function mg:gta/traffic/arrive',
                       'execute if score @s mg.gth matches 1 if score $gpx mg.st <= @s mg.gttx run function mg:gta/traffic/arrive',
                       'execute if score @s mg.gth matches 0 if score $gpz mg.st >= @s mg.gttz run function mg:gta/traffic/arrive',
                       'execute if score @s mg.gth matches 2 if score $gpz mg.st <= @s mg.gttz run function mg:gta/traffic/arrive',
                       'execute at @s run function mg:gta/traffic/sync'])
w('gta/traffic/blocked', ['# @s : obstacle devant (joueur, passant, voiture) : arrêt, klaxon au bout de 3 s',
                          'execute if score @s mg.gtw8 matches 60 run playsound minecraft:block.note_block.didgeridoo neutral @a ~ ~ ~ 1.5 1.6',
                          'execute if score @s mg.gtw8 matches 63 run playsound minecraft:block.note_block.didgeridoo neutral @a ~ ~ ~ 1.5 1.6',
                          'execute if score @s mg.gtw8 matches 300.. run return run function mg:gta/traffic/despawn',
                          'execute at @s run function mg:gta/traffic/sync'])
w('gta/traffic/despawn', ['# @s : voiture PNJ bloquée depuis 15 s : elle disparaît (une autre apparaîtra ailleurs)',
                          'scoreboard players operation $gv mg.st = @s mg.gvid',
                          'execute as @e[tag=mg.gta,type=!minecraft:marker] if score @s mg.gvid = $gv mg.st run kill @s', 'kill @s'])
w('gta/traffic/sync', ['# @s (voiture PNJ, à sa position) : la carrosserie suit', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                       'execute as @e[type=minecraft:block_display,tag=mg.gtrd] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~ ~ 0',
                       'execute as @e[type=minecraft:interaction,tag=mg.gtint] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~'])
STEAL = ['# @s (voiture PNJ) volée par le joueur tagué mg.gthief : devient une vraie voiture pilotable, il monte au volant (une chance sur deux d\'être vu : ★)',
         'scoreboard players operation $gv mg.st = @s mg.gvid', 'execute as @e[tag=mg.gta,type=!minecraft:marker] if score @s mg.gvid = $gv mg.st run kill @s']
STEAL += [f'execute if score @s mg.gtmod matches {n} run function mg:gta/car/spawn_{n}' for (n, *_r) in CARS]
STEAL += ['scoreboard players operation $gv mg.st = $gvid mg.st', 'execute as @a[tag=mg.gthief,limit=1] run function mg:gta/car_mount',
          'execute as @a[tag=mg.gthief] run title @s actionbar {"text":"🔑 Voiture volée !","color":"gold","bold":true}',
          'execute as @a[tag=mg.gthief] run scoreboard players set @s mg.gal 40',
          'execute store result score $gr mg.st run random value 0..1', 'execute if score $gr mg.st matches 0 as @a[tag=mg.gthief] run function mg:gta/wanted_up',
          'playsound minecraft:block.iron_door.open neutral @a ~ ~ ~ 1 1.2', 'kill @s']
w('gta/traffic/steal', STEAL)
w('gta/traffic/int', ['# @s (zone cliquable d\'une voiture PNJ) : le joueur qui a cliqué la vole', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                      'execute on target run tag @s add mg.gthief',
                      'execute as @e[type=minecraft:marker,tag=mg.gtraf] if score @s mg.gvid = $gv mg.st at @s run function mg:gta/traffic/steal',
                      'tag @a remove mg.gthief'])
w('gta/traffic/steal_near', ['# @s (joueur accroupi) : vole la voiture PNJ la plus proche', 'tag @s add mg.gthief',
                             'execute as @e[type=minecraft:marker,tag=mg.gtraf,distance=..2.6,limit=1,sort=nearest] at @s run function mg:gta/traffic/steal',
                             'tag @a remove mg.gthief'])
w('gta/traffic/second', ['# Chaque seconde : 14 voitures PNJ en ville',
                         'execute store result score $gtc mg.st if entity @e[type=minecraft:marker,tag=mg.gtraf]',
                         'execute if score $gtc mg.st matches ..13 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..18] unless entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..6] run function mg:gta/traffic/spawn'])

# ---------------------------------------------------------------- passants qui fuient les coups de feu
w('gta/panic', ['# @s vient de tirer : les passants proches paniquent (husk invisible et immobile une seconde, ils le fuient)',
                'execute if entity @e[type=minecraft:husk,tag=mg.gpanic,distance=..10] run return 0',
                'summon minecraft:husk ~ ~ ~ {Tags:["mg.gta","mg.npc","mg.gpanic"],NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,'
                'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:scale",base:0.2}]}',
                'scoreboard players set @e[type=minecraft:husk,tag=mg.gpanic,distance=..1] mg.gtw8 30'])
w('gta/panic_tick', ['scoreboard players remove @e[type=minecraft:husk,tag=mg.gpanic] mg.gtw8 1',
                     'execute as @e[type=minecraft:husk,tag=mg.gpanic,scores={mg.gtw8=..0}] run tp @s ~ -300 ~'])

# ---------------------------------------------------------------- police : voitures de police, barrages, hélico
w('gta/pcar_spawn', ['# Voiture de police pilotée par un policier (contexte : carrefour) : elle poursuit le joueur recherché',
                     'function mg:gta/car/spawn_5',
                     'scoreboard players operation $gpv mg.st = $gvid mg.st',
                     'execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gpv mg.st run tag @s add mg.gpcar',
                     'execute if score $rp mg.st matches 1 run ' + cop('mg:gun_pistol'),
                     'execute unless score $rp mg.st matches 1 run ' + cop('minecraft:crossbow'),
                     'team join mg_gciv @e[tag=mg.gcopn]',
                     'execute as @e[tag=mg.gcopn] run ride @s mount @e[type=minecraft:horse,tag=mg.gpcar,tag=!mg.gpcarr,limit=1,sort=nearest]',
                     'tag @e[tag=mg.gpcar] add mg.gpcarr', 'tag @e[tag=mg.gcopn] remove mg.gcopn',
                     'playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 2 1.4'])
w('gta/roadblock', ['# Barrage de police (4 ★) à ce carrefour : deux voitures en travers, quatre policiers',
                    'execute positioned ~-2 ~ ~ run function mg:gta/car/spawn_5', 'execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gvid mg.st run function mg:gta/roadblock_car',
                    'execute positioned ~2 ~ ~ run function mg:gta/car/spawn_5', 'execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gvid mg.st run function mg:gta/roadblock_car',
                    'function mg:gta/cop_spawn', 'execute positioned ~ ~ ~2 run function mg:gta/cop_spawn',
                    'summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.grblk"]}',
                    'tellraw @a[tag=mg.gtw,scores={mg.gwl=4..},distance=..80] {"text":"🚧 Barrage de police à proximité !","color":"red","bold":true}'])
w('gta/roadblock_car', ['# @s : voiture de barrage (immobile, en travers)', 'data merge entity @s {NoAI:1b}', 'tag @s add mg.grbc',
                        'execute at @s run tp @s ~ ~ ~ 90 0'])
PH = ['# Hélico de police (5 ★) : point d\'ancrage + carrosserie, survole le joueur recherché le plus proche, projecteur et tireur',
      'scoreboard players add $gvid mg.st 1',
      'summon minecraft:marker ~ ~20 ~ {Tags:["mg.gta","mg.gphel","mg.gcop","mg.gswat","mg.gvn"]}',
      H('white_concrete', -0.9, -0.6, -1.4, 1.8, 1.5, 2.8), H('blue_concrete', -0.91, -0.1, -1.41, 1.82, 0.3, 2.82),
      H('light_blue_stained_glass', -0.8, -0.5, 1.4, 1.6, 1.25, 0.9), H('white_concrete', -0.2, 0.1, -5.2, 0.4, 0.4, 3.8),
      H('blue_concrete', -0.06, 0.3, -5.3, 0.12, 1.1, 0.6), H('gray_concrete', -1.0, -1.25, -1.3, 0.12, 0.12, 3.0), H('gray_concrete', 0.88, -1.25, -1.3, 0.12, 0.12, 3.0),
      H('red_stained_glass', -0.5, 0.95, -0.2, 0.4, 0.15, 0.4), H('blue_stained_glass', 0.1, 0.95, -0.2, 0.4, 0.15, 0.4),
      DSP('mg.ghrot', 'black_concrete', -4.5, SH + 1.3, -0.15, 9, 0.08, 0.3), DSP('mg.ghrot', 'black_concrete', -0.15, SH + 1.3, -4.5, 0.3, 0.08, 9),
      'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st',
      'tag @e[tag=mg.gvn,type=minecraft:block_display] add mg.gphb', 'tag @e[tag=mg.gvn] remove mg.gvn',
      'tellraw @a[tag=mg.gtw,scores={mg.gwl=5..}] {"text":"🚁 L\'hélicoptère de police est sur toi !","color":"red","bold":true}']
w('gta/pheli_spawn', [l.replace('"mg.gvd",', '').replace('"mg.ghbody"', '"mg.gphb"').replace('"mg.ghrot"', '"mg.gphr"') for l in PH])
w('gta/pheli_tick', ['# @s : hélico de police (chaque tick) : vole vers 14 blocs au-dessus du joueur recherché le plus proche',
                     'execute unless entity @a[tag=mg.gtw,scores={mg.gwl=5..},distance=..120] run return run function mg:gta/pheli_remove',
                     'execute at @p[tag=mg.gtw,scores={mg.gwl=5..}] positioned ~ ~14 ~ run summon minecraft:marker ~ ~ ~ {Tags:["mg.gta","mg.gphto"]}',
                     'execute at @s facing entity @e[type=minecraft:marker,tag=mg.gphto,limit=1,sort=nearest] feet unless entity @e[type=minecraft:marker,tag=mg.gphto,distance=..1.5] run tp @s ^ ^ ^0.45 ~ 0',
                     'kill @e[type=minecraft:marker,tag=mg.gphto]',
                     'scoreboard players operation $gv mg.st = @s mg.gvid',
                     'execute at @s as @e[type=minecraft:block_display,tag=mg.gphb] if score @s mg.gvid = $gv mg.st run tp @s ~ ~ ~ ~ 0',
                     'execute at @s as @e[type=minecraft:block_display,tag=mg.gphr] if score @s mg.gvid = $gv mg.st rotated as @s run tp @s ~ ~ ~ ~40 0',
                     'execute if score $gq mg.st matches 0 at @s run playsound minecraft:entity.bee.loop hostile @a ~ ~ ~ 3 0.5',
                     'execute if score $gq mg.st matches 10 at @s run playsound minecraft:entity.bee.loop hostile @a ~ ~ ~ 3 0.5',
                     'execute if score $gq2 mg.st matches 0 at @p[tag=mg.gtw,scores={mg.gwl=5..}] run particle minecraft:dust{color:[1.0,1.0,0.85],scale:2.5} ~ ~0.2 ~ 1.4 0.05 1.4 0 14 force'])
w('gta/pheli_remove', ['# @s : l\'hélico de police repart', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                       'execute as @e[type=minecraft:block_display] if score @s mg.gvid = $gv mg.st run kill @s', 'kill @s'])
w('gta/veh_remove', ['# @s : véhicule (cheval ou ghast) retiré sans explosion : sa carrosserie et sa zone cliquable aussi', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                     'execute as @e[type=minecraft:block_display] if score @s mg.gvid = $gv mg.st run kill @s',
                     'execute as @e[type=minecraft:interaction] if score @s mg.gvid = $gv mg.st run kill @s', 'tp @s ~ -300 ~'])
w('gta/police_plus', ['# Chaque seconde (@s = joueur recherché, à sa position) : voitures de police, barrage, hélico',
                      'execute store result score $gpc mg.st if entity @e[type=minecraft:horse,tag=mg.gpcar,distance=..60]',
                      'scoreboard players operation $gpw mg.st = @s mg.gwl', 'scoreboard players remove $gpw mg.st 1',
                      'execute if score @s mg.gwl matches 2.. if score $gpc mg.st < $gpw mg.st as @e[type=minecraft:marker,tag=mg.gix,distance=25..55,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..15] run function mg:gta/pcar_spawn',
                      'execute if score @s mg.gwl matches 4.. unless entity @e[type=minecraft:marker,tag=mg.grblk,distance=..60] as @e[type=minecraft:marker,tag=mg.gix,distance=20..45,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/roadblock',
                      'execute if score @s mg.gwl matches 5.. unless entity @e[type=minecraft:marker,tag=mg.gphel] run function mg:gta/pheli_spawn'])
w('gta/police_clean', ['# Chaque seconde : voitures de police sans policier, barrages loin de tout joueur recherché',
                       'execute as @e[type=minecraft:horse,tag=mg.gpcar] unless predicate mg:has_passenger run function mg:gta/veh_remove',
                       'execute as @e[type=minecraft:marker,tag=mg.grblk] at @s unless entity @a[tag=mg.gtw,scores={mg.gwl=1..},distance=..80] run function mg:gta/roadblock_remove'])
w('gta/roadblock_remove', ['# @s (marqueur de barrage) : le barrage est levé',
                           'execute as @e[type=minecraft:horse,tag=mg.grbc,distance=..6] run function mg:gta/veh_remove', 'kill @s'])
os.makedirs(os.path.join(C.D, 'predicate'), exist_ok=True)
with open(os.path.join(C.D, 'predicate', 'has_passenger.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'passenger': {}}}, f, indent=2)
    f.write('\n')
C.objectives([('mg.gth', 'dummy'), ('mg.gtn', 'dummy'), ('mg.gttx', 'dummy'), ('mg.gttz', 'dummy'), ('mg.gtmod', 'dummy'), ('mg.gtw8', 'dummy')])
