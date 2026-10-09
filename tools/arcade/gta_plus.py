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
w('gta/pcar_remove', ['# @s : policier d\'une voiture de police qui repart : la voiture aussi',
                      'execute on vehicle run function mg:gta/veh_remove', 'tp @s ~ -300 ~'])
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

# ---------------------------------------------------------------- téléphone et missions
# mg.gmt : mission en cours (0 aucune, 1 livraison, 2 contrat, 3 contre-la-montre) ; mg.gms : étape ; mg.gmtime : ticks restants.
# Les objets de mission (tag mg.gmo) portent le mg.bid du joueur.
MIS = {1: ('📦 Livraison', 300, 1800), 2: ('🎯 Contrat', 500, 2400), 3: ('🏁 Contre-la-montre', 400, 1500)}
PHONE = ('item replace entity @s hotbar.6 with minecraft:warped_fungus_on_a_stick[custom_data={gtaphone:1b},item_model="minecraft:recovery_compass",unbreakable={},'
         f'custom_name={js({"text": "📱 Téléphone", "color": "aqua", "bold": True, "italic": False})},'
         f'lore=[{js({"text": "Clic droit : missions (livraison, contrat, contre-la-montre)", "color": "gray", "italic": False})}]]')
NITRO = ('item replace entity @s hotbar.5 with minecraft:warped_fungus_on_a_stick[custom_data={gtanitro:1b},item_model="minecraft:blaze_powder",unbreakable={},'
         f'custom_name={js({"text": "🔥 Nitro / 📯 Klaxon", "color": "gold", "bold": True, "italic": False})},'
         f'lore=[{js({"text": "En voiture : nitro (recharge 15 s), sinon klaxon", "color": "gray", "italic": False})}]]')
w('gta/kit_plus', ['# @s : téléphone, nitro', PHONE, NITRO])
_TIPS = {1: "Récupère un colis puis livre-le à l'adresse indiquée", 2: 'Élimine la cible marquée (attention à ses gardes du corps)',
         3: 'Passe les 5 points de contrôle à temps (prends une voiture !)'}
DLG = {'type': 'minecraft:multi_action', 'title': {'text': '📱 Téléphone', 'color': 'aqua', 'bold': True}, 'pause': False, 'can_close_with_escape': True,
       'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Choisis un contrat. Une seule mission à la fois ; la mort ou le temps écoulé la font échouer.', 'color': 'gray'}]}],
       'columns': 1, 'exit_action': {'label': {'text': 'Raccrocher', 'color': 'gray'}},
       'actions': [{'label': [{'text': MIS[k][0], 'color': 'gold', 'bold': True}, {'text': f'  +{MIS[k][1]} $  ·  {MIS[k][2] // 20} s', 'color': 'green'}],
                    'tooltip': {'text': _TIPS[k], 'color': 'gray'}, 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.gmis set {k}'}} for k in MIS] +
                  [{'label': {'text': '❌ Abandonner la mission', 'color': 'red'}, 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.gmis set 9'}}]}
w('gta/phone', ['# @s : clic sur le téléphone', 'scoreboard players reset @s mg.gqs', 'scoreboard players enable @s mg.gmis', 'dialog show @s ' + js(DLG)])
w('gta/mis_cmd', ['# @s : choix dans le téléphone (mg.gmis)', 'scoreboard players operation $gmc mg.st = @s mg.gmis', 'scoreboard players reset @s mg.gmis',
                  'execute if score $gmc mg.st matches 9 run return run function mg:gta/mis_fail',
                  'execute if score @s mg.gmt matches 1.. run return run title @s actionbar {"text":"📱 Termine (ou abandonne) ta mission en cours d\'abord","color":"red"}'] +
  [f'execute if score $gmc mg.st matches {k} at @s run function mg:gta/mis{k}_start' for k in MIS])

OWN = ['scoreboard players operation $gb mg.st = @s mg.bid', 'tag @e remove mg.gmine', 'execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine']
ADOPT = ['tag @e[tag=mg.gmnew] add mg.gmo', 'scoreboard players operation @e[tag=mg.gmnew] mg.bid = $gb mg.st', 'tag @e[tag=mg.gmnew] remove mg.gmnew']


def mis_start(k, lines):
    nm, rw, t = MIS[k]
    return ([f'# @s démarre : {nm}', f'scoreboard players set @s mg.gmt {k}', 'scoreboard players set @s mg.gms 1', f'scoreboard players set @s mg.gmtime {t}',
             'scoreboard players operation $gb mg.st = @s mg.bid'] + lines + ADOPT +
            ['title @s times 5 40 10', 'title @s title ' + js({"text": nm.upper(), "color": "gold", "bold": True}),
             'playsound minecraft:block.note_block.chime player @s ~ ~ ~ 1 1.2', 'scoreboard players set @s mg.gtl 50'])


def MARK(item, tag):
    return (f'summon minecraft:item_display ~ ~1.2 ~ {{Tags:["mg.gta","mg.gmnew","{tag}"],item:{{id:"{item}",count:1}},billboard:"vertical",'
            f'Glowing:1b,glow_color_override:16766720,{TR % (0, 0, 0, 1.2, 1.2, 1.2)}}}')


w('gta/mis1_start', mis_start(1, ['execute as @e[type=minecraft:marker,tag=mg.gix,distance=30..90,sort=random,limit=1] at @s run ' + MARK('minecraft:chest', 'mg.gmpk'),
                                  'title @s subtitle {"text":"Va chercher le colis (faisceau doré)","color":"yellow"}']))
w('gta/mis2_start', mis_start(2, ['execute as @e[type=minecraft:marker,tag=mg.gsw,distance=50..110,sort=random,limit=1] at @s run function mg:gta/mis2_vip',
                                  'title @s subtitle {"text":"Élimine la cible marquée","color":"yellow"}']))
GUARD = ('summon minecraft:wither_skeleton ~{dx} ~ ~ {{Tags:["mg.gta","mg.gtg","mg.npc","mg.gmnew"],PersistenceRequired:1b,CustomName:{{"text":"Garde du corps","color":"dark_gray"}},'
         'equipment:{{head:{{id:"minecraft:leather_helmet",count:1,components:{{"minecraft:dyed_color":1315860}}}},mainhand:{{id:"minecraft:iron_sword",count:1}}}},drop_chances:{{head:0f,mainhand:0f}}}}')
w('gta/mis2_vip', ['# La cible et ses deux gardes du corps',
                   'summon minecraft:villager ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.npc","mg.gmnew","mg.gmvip"],PersistenceRequired:1b,Glowing:1b,'
                   'VillagerData:{profession:"minecraft:nitwit",type:"minecraft:swamp",level:1},CustomName:{"text":"🎯 La cible","color":"red","bold":true},CustomNameVisible:1b}',
                   GUARD.format(dx=1), GUARD.format(dx=-1)])
w('gta/mis3_start', mis_start(3, ['execute as @e[type=minecraft:marker,tag=mg.gix,distance=40..80,sort=random,limit=1] at @s run ' + MARK('minecraft:yellow_stained_glass', 'mg.gmcp'),
                                  'title @s subtitle {"text":"Point de contrôle 1 / 5 : fonce !","color":"yellow"}']))
w('gta/mis_tick', ['# @s (mission en cours, toutes les 5 ticks, à sa position) : temps, étapes, faisceau sur l\'objectif'] + OWN +
  ['scoreboard players remove @s mg.gmtime 5', 'scoreboard players operation @s mg.gmsec = @s mg.gmtime', 'scoreboard players set #20 mg.st 20',
   'scoreboard players operation @s mg.gmsec /= #20 mg.st',
   'execute if score @s mg.gmtime matches ..0 run return run function mg:gta/mis_fail',
   'execute at @e[tag=mg.gmine] run particle minecraft:end_rod ~ ~3 ~ 0.05 4 0.05 0 8 force @s',
   'execute if score @s mg.gmt matches 1 if score @s mg.gms matches 1 if entity @e[tag=mg.gmine,tag=mg.gmpk,distance=..2.5] run return run function mg:gta/mis1_picked',
   'execute if score @s mg.gmt matches 1 if score @s mg.gms matches 2 if entity @e[tag=mg.gmine,tag=mg.gmdl,distance=..3] run return run function mg:gta/mis_win',
   'execute if score @s mg.gmt matches 2 unless entity @e[tag=mg.gmine,tag=mg.gmvip] run return run function mg:gta/mis_win',
   'execute if score @s mg.gmt matches 3 if entity @e[tag=mg.gmine,tag=mg.gmcp,distance=..4] run return run function mg:gta/mis3_next'])
w('gta/mis1_picked', ['# Colis récupéré : livraison à 60..120 blocs', 'kill @e[tag=mg.gmine]', 'scoreboard players set @s mg.gms 2',
                      'scoreboard players operation $gb mg.st = @s mg.bid',
                      'execute as @e[type=minecraft:marker,tag=mg.gix,distance=60..120,sort=random,limit=1] at @s run ' + MARK('minecraft:barrel', 'mg.gmdl')] + ADOPT +
  ['title @s subtitle {"text":"📦 Colis récupéré : livre-le au faisceau doré !","color":"yellow"}', 'title @s title {"text":" "}',
   'playsound minecraft:item.armor.equip_leather player @s ~ ~ ~ 1 1'])
w('gta/mis3_next', ['# Point de contrôle passé', 'scoreboard players add @s mg.gms 1', 'playsound minecraft:block.note_block.pling player @s ~ ~ ~ 1 1.6',
                    'execute if score @s mg.gms matches 6.. run return run function mg:gta/mis_win',
                    'scoreboard players operation $gb mg.st = @s mg.bid',
                    'execute at @e[tag=mg.gmine,limit=1] as @e[type=minecraft:marker,tag=mg.gix,distance=40..80,sort=random,limit=1] at @s run ' + MARK('minecraft:yellow_stained_glass', 'mg.gmcp'),
                    'kill @e[tag=mg.gmine]'] + ADOPT +
  ['title @s actionbar [{"text":"🏁 Point de contrôle ","color":"gold"},{"score":{"name":"@s","objective":"mg.gms"},"color":"yellow","bold":true},{"text":" / 5","color":"gold"}]',
   'scoreboard players set @s mg.gal 30'])
WIN = ['# @s réussit sa mission : récompense', 'scoreboard players set $gcv mg.st 0']
WIN += [f'execute if score @s mg.gmt matches {k} run scoreboard players set $gcv mg.st {v[1]}' for k, v in MIS.items()]
WIN += ['scoreboard players operation @s mg.gta += $gcv mg.st', 'function mg:gta/mis_clean',
        'title @s times 5 50 15', 'title @s title {"text":"MISSION RÉUSSIE","color":"gold","bold":true}',
        'title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]',
        'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1', 'scoreboard players set @s mg.gtl 60']
w('gta/mis_win', WIN)
w('gta/mis_fail', ['# @s : mission échouée ou abandonnée', 'execute unless score @s mg.gmt matches 1.. run return 0', 'function mg:gta/mis_clean',
                   'title @s times 5 40 15', 'title @s title {"text":"MISSION ÉCHOUÉE","color":"red","bold":true}',
                   'execute at @s run playsound minecraft:entity.villager.no player @s ~ ~ ~ 1 0.8', 'scoreboard players set @s mg.gtl 60'])
w('gta/mis_clean', ['# @s : objets de sa mission retirés'] + OWN + ['kill @e[tag=mg.gmine]', 'scoreboard players set @s mg.gmt 0', 'scoreboard players set @s mg.gms 0'])
MH = ['# @s : barre d\'action pendant une mission']
_STEP = {1: ' : colis puis livraison', 2: ' : élimine la cible', 3: ' : points de contrôle'}
for k, (nm, rw, t) in MIS.items():
    MH.append(f'execute if score @s mg.gmt matches {k} run return run title @s actionbar ' +
              js([{'text': nm + _STEP[k] + '  ', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.gmsec'}, 'color': 'white', 'bold': True},
                  {'text': ' s', 'color': 'gray'}, {'text': '      💵 ', 'color': 'green'}, {'score': {'name': '@s', 'objective': 'mg.gta'}, 'color': 'green', 'bold': True}]))
w('gta/mis_hud', MH)

# ---------------------------------------------------------------- nitro, klaxon, peinture
w('gta/nitro', ['# @s : clic sur nitro / klaxon', 'scoreboard players reset @s mg.gqs',
                'execute unless predicate mg:in_vehicle run return run function mg:gta/horn',
                'execute if score @s mg.gnit matches 1.. run return run function mg:gta/horn',
                'scoreboard players set @s mg.gnit 300',
                'execute on vehicle run effect give @s minecraft:speed 3 4 true',
                'execute on vehicle at @s run particle minecraft:flame ^ ^0.4 ^-2 0.2 0.1 0.2 0.05 30 force',
                'execute at @s run playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.7',
                'title @s actionbar {"text":"🔥 NITRO !","color":"gold","bold":true}', 'scoreboard players set @s mg.gal 30'])
w('gta/horn', ['# @s : klaxon', 'execute at @s run playsound minecraft:item.goat_horn.sound.2 player @a ~ ~ ~ 2 1.6'])
with open(os.path.join(C.D, 'predicate', 'in_vehicle.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'vehicle': {}}}, f, indent=2)
    f.write('\n')
COLORS = ['red', 'orange', 'yellow', 'lime', 'cyan', 'blue', 'purple', 'magenta', 'black', 'white', 'pink', 'gray']
PT = ['# @s : peinture aléatoire de la carrosserie de son véhicule (mg.gveh)', 'scoreboard players operation $gv mg.st = @s mg.gveh',
      'execute unless score @s mg.gveh matches 1.. run return run title @s actionbar {"text":"🎨 Achète d\'abord un véhicule (concession) ou sors-en un du garage","color":"red"}',
      f'execute store result score $gr mg.st run random value 0..{len(COLORS) - 1}']
PT += [f'execute if score $gr mg.st matches {k} as @e[type=minecraft:block_display,tag=mg.gvb] if score @s mg.gvid = $gv mg.st run data merge entity @s {{block_state:{{Name:"minecraft:{c}_concrete"}}}}'
       for k, c in enumerate(COLORS)]
PT += ['playsound minecraft:item.dye.use player @s ~ ~ ~ 1 1', 'title @s actionbar {"text":"🎨 Nouvelle peinture !","color":"light_purple","bold":true}', 'scoreboard players set @s mg.gal 30']
w('gta/paint', PT)
C.objectives([('mg.gmis', 'trigger'), ('mg.gmt', 'dummy'), ('mg.gms', 'dummy'), ('mg.gmtime', 'dummy'), ('mg.gmsec', 'dummy'), ('mg.gnit', 'dummy')])

# ---------------------------------------------------------------- lieux : hôpital, commissariat, casino, boîte de nuit
PL = CITY['places']
HOSP, POLI, CAS, CLUB = PL['hospital'], PL['police'], PL['casino'], PL['club']
w('gta/respawn_at', ['# @s vient de mourir : réapparition à l\'hôpital (WASTED) ou au commissariat (BUSTED, tag mg.gbust)',
                     f'execute if entity @s[tag=mg.gbust] in {DIM} run tp @s {POLI[0] + 0.5} 66 {Z + POLI[1] + 0.5} 0 0',
                     f'execute unless entity @s[tag=mg.gbust] in {DIM} run tp @s {HOSP[0] + 0.5} 66 {Z + HOSP[1] + 0.5} 0 0',
                     'tag @s remove mg.gbust'])
SIGNS = [(HOSP[0], HOSP[1] - 2, '🏥 HÔPITAL', 'red'), (POLI[0], POLI[1] - 2, '🚓 COMMISSARIAT', 'blue'),
         (CAS['door'][0], CAS['door'][1], '🎰 NEO CASINO', 'gold'), ((CLUB['box'][0] + CLUB['box'][2]) // 2, CLUB['box'][1], '🪩 NEO CLUB', 'light_purple')]
SIGN_CMDS = [f'summon minecraft:text_display {x + 0.5} 70.6 {Z + z - 0.1} {{Tags:["mg.gta"],Rotation:[180f,0f],text:{js({"text": t, "color": c, "bold": True})},'
             f'background:-1442840576,{TR % (0, 0, 0, 1.6, 1.6, 1.6)}}}' for (x, z, t, c) in SIGNS]
w('gta/places_setup', ['# Enseignes des lieux (contexte : dimension mg:gta)'] + SIGN_CMDS)
# casino
w('gta/casino_slot', ['# @s joue à la machine à sous (déjà payée 50 $) : 55 % rien, 30 % 100 $, 12 % 250 $, 3 % jackpot 1 000 $',
                      'execute store result score $gr mg.st run random value 0..99', 'scoreboard players set $gcv mg.st 0',
                      'execute if score $gr mg.st matches 55..84 run scoreboard players set $gcv mg.st 100',
                      'execute if score $gr mg.st matches 85..96 run scoreboard players set $gcv mg.st 250',
                      'execute if score $gr mg.st matches 97.. run scoreboard players set $gcv mg.st 1000',
                      'scoreboard players operation @s mg.gta += $gcv mg.st', 'scoreboard players set @s mg.gal 40',
                      'execute if score $gcv mg.st matches 0 run title @s actionbar {"text":"🎰 🍋 🍒 🔔 … perdu !","color":"gray"}',
                      'execute if score $gcv mg.st matches 100 run title @s actionbar {"text":"🎰 🍒 🍒 🍋 … +100 $","color":"green","bold":true}',
                      'execute if score $gcv mg.st matches 250 run title @s actionbar {"text":"🎰 🔔 🔔 🔔 … +250 $ !","color":"gold","bold":true}',
                      'execute if score $gcv mg.st matches 1000 run title @s title {"text":"💰 JACKPOT 💰","color":"gold","bold":true}',
                      'execute if score $gcv mg.st matches 1000 run tellraw @a[tag=mg.gtw] [{"selector":"@s","color":"yellow"},{"text":" a touché le JACKPOT du casino : 1 000 $ !","color":"gold"}]',
                      'execute if score $gcv mg.st matches 1.. at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.4',
                      'execute if score $gcv mg.st matches 0 at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6'])
w('gta/casino_roulette', ['# @s mise 100 $ à la roulette : 47 % de chances de doubler',
                          'execute store result score $gr mg.st run random value 0..99', 'scoreboard players set @s mg.gal 40',
                          'execute if score $gr mg.st matches ..46 run scoreboard players add @s mg.gta 200',
                          'execute if score $gr mg.st matches ..46 run title @s actionbar {"text":"🎡 Rouge ! +200 $","color":"red","bold":true}',
                          'execute if score $gr mg.st matches 47.. run title @s actionbar {"text":"🎡 Noir… la banque gagne","color":"gray"}',
                          'execute if score $gr mg.st matches ..46 at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.2',
                          'execute if score $gr mg.st matches 47.. at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6'])
# boîte de nuit : piste qui change de couleur, lasers, musique pour ceux qui sont dedans
FX1, FZ1, FX2, FZ2 = CLUB['floor']
BX1, BZ1, BX2, BZ2 = CLUB['box']
CL = ['magenta', 'cyan', 'yellow', 'lime', 'purple', 'orange', 'pink', 'light_blue']
for k in range(4):
    w(f'gta/club_floor_{k}', [f'# Piste de danse, motif {k}'] + [f'setblock {x} 65 {Z + z} minecraft:{CL[(x + z * (k + 1) + 3 * k) % len(CL)]}_concrete'
                                                              for x in range(FX1, FX2 + 1) for z in range(FZ1, FZ2 + 1)])
w('gta/club_fx', ['# Boîte de nuit (toutes les 0,5 s si quelqu\'un y est) : piste, lasers', 'execute store result score $gr mg.st run random value 0..3'] +
  [f'execute if score $gr mg.st matches {k} in {DIM} run function mg:gta/club_floor_{k}' for k in range(4)] +
  [f'execute in {DIM} run particle minecraft:dust{{color:[1.0,0.1,0.9],scale:1.6}} {CLUB["dj"][0] + 0.5} 70 {Z + CLUB["dj"][1]} 3 0.5 4 0 25 force',
   f'execute in {DIM} run particle minecraft:dust{{color:[0.1,0.9,1.0],scale:1.6}} {CLUB["dj"][0] + 0.5} 70 {Z + CLUB["dj"][1]} 3 0.5 4 0 25 force',
   f'execute in {DIM} run particle minecraft:end_rod {CLUB["dj"][0] + 0.5} 68 {Z + CLUB["dj"][1]} 2 0.2 3 0.02 6 force'])
CLUBSEL = f'x={BX1},y=64,z={Z + BZ1},dx={BX2 - BX1},dy=8,dz={BZ2 - BZ1}'
w('gta/club_tick', ['# Toutes les 0,5 s : musique pour ceux qui entrent, coupée pour ceux qui sortent, animation',
                    f'execute in {DIM} as @a[tag=mg.gtw,tag=!mg.gclub,{CLUBSEL}] at @s run function mg:gta/club_in',
                    f'execute as @a[tag=mg.gclub] at @s unless entity @s[{CLUBSEL}] run function mg:gta/club_out',
                    'execute if entity @a[tag=mg.gclub] run function mg:gta/club_fx'])
w('gta/club_in', ['tag @s add mg.gclub', 'stopsound @s record', 'tag @s remove mg.gdrv', 'playsound minecraft:music_disc.pigstep record @s ~ ~ ~ 1 1 0.8',
                  'title @s actionbar {"text":"🪩 NEO CLUB","color":"light_purple","bold":true}', 'scoreboard players set @s mg.gal 40'])
w('gta/club_out', ['tag @s remove mg.gclub', 'stopsound @s record'])

# ---------------------------------------------------------------- casino : fenêtres de jeu (mise au choix)
# Trigger mg.gcas : 1m machine à sous, 2pm roulette (p : 1 rouge, 2 noir, 3 vert), 3m dés ; m : 1..5 = 10 / 50 / 100 / 500 / 1000 $.
BETS = [10, 50, 100, 500, 1000]
MISE = {'type': 'minecraft:single_option', 'key': 'mise', 'label': {'text': 'Mise', 'color': 'gold'}, 'label_visible': True,
        'options': [{'id': str(k + 1), 'display': {'text': f'{b} $', 'color': 'green'}, **({'initial': True} if k == 1 else {})} for k, b in enumerate(BETS)]}
EXIT = {'label': {'text': 'Quitter la table', 'color': 'gray'}}
D_SLOT = {'type': 'minecraft:multi_action', 'title': {'text': '🎰 Machine à sous', 'color': 'gold', 'bold': True}, 'pause': False, 'can_close_with_escape': True,
          'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': '🍒🍒 ×2   🔔🔔🔔 ×5   ', 'color': 'yellow'}, {'text': '777', 'color': 'red', 'bold': True}, {'text': ' JACKPOT ×20', 'color': 'yellow'}]}],
          'inputs': [MISE], 'columns': 1, 'exit_action': EXIT,
          'actions': [{'label': {'text': '🎰 Tirer le levier', 'color': 'gold', 'bold': True}, 'action': {'type': 'minecraft:dynamic/run_command', 'template': 'trigger mg.gcas set 1$(mise)'}}]}
D_ROUL = {'type': 'minecraft:multi_action', 'title': {'text': '🎡 Roulette', 'color': 'red', 'bold': True}, 'pause': False, 'can_close_with_escape': True,
          'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Rouge ou noir : ×2 (18 cases sur 37)   ·   Vert, le zéro : ×36', 'color': 'gray'}]}],
          'inputs': [{'type': 'minecraft:single_option', 'key': 'pari', 'label': {'text': 'Pari', 'color': 'gold'}, 'label_visible': True,
                      'options': [{'id': '1', 'display': {'text': '🔴 Rouge', 'color': 'red'}, 'initial': True}, {'id': '2', 'display': {'text': '⚫ Noir', 'color': 'dark_gray'}},
                                  {'id': '3', 'display': {'text': '🟢 Zéro (vert)', 'color': 'green'}}]}, MISE],
          'columns': 1, 'exit_action': EXIT,
          'actions': [{'label': {'text': '🎡 Lancer la bille', 'color': 'red', 'bold': True}, 'action': {'type': 'minecraft:dynamic/run_command', 'template': 'trigger mg.gcas set 2$(pari)$(mise)'}}]}
D_DICE = {'type': 'minecraft:multi_action', 'title': {'text': '🎲 Dés', 'color': 'aqua', 'bold': True}, 'pause': False, 'can_close_with_escape': True,
          'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Deux dés contre deux dés du croupier : plus haut = ×2, égalité = mise rendue', 'color': 'gray'}]}],
          'inputs': [MISE], 'columns': 1, 'exit_action': EXIT,
          'actions': [{'label': {'text': '🎲 Lancer les dés', 'color': 'aqua', 'bold': True}, 'action': {'type': 'minecraft:dynamic/run_command', 'template': 'trigger mg.gcas set 3$(mise)'}}]}
for nm, d in (('slot', D_SLOT), ('roulette', D_ROUL), ('dice', D_DICE)):
    w(f'gta/cas_ui_{nm}', [f'# @s : fenêtre du casino ({nm})', 'scoreboard players enable @s mg.gcas', 'dialog show @s ' + js(d)])
CM = ['# @s a validé une fenêtre du casino (mg.gcas)', 'scoreboard players operation $gcc mg.st = @s mg.gcas', 'scoreboard players reset @s mg.gcas',
      'scoreboard players operation $gcm mg.st = $gcc mg.st', 'scoreboard players set #10 mg.st 10', 'scoreboard players operation $gcm mg.st %= #10 mg.st',
      'scoreboard players set $gbet mg.st 0']
CM += [f'execute if score $gcm mg.st matches {k + 1} run scoreboard players set $gbet mg.st {b}' for k, b in enumerate(BETS)]
CM += ['execute if score $gbet mg.st matches 0 run return 0', 'execute if entity @s[tag=mg.gslot] run return 0',
       'execute if score @s mg.gta < $gbet mg.st run scoreboard players set @s mg.gal 40',
       'execute if score @s mg.gta < $gbet mg.st run return run title @s actionbar [{"text":"💸 Pas assez d\'argent pour miser ","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"gold"},{"text":" $","color":"red"}]',
       'scoreboard players operation @s mg.gta -= $gbet mg.st', 'scoreboard players set @s mg.gal 60', 'title @s times 2 40 10',
       'execute if score $gcc mg.st matches 11..15 run return run function mg:gta/cas_slot',
       'execute if score $gcc mg.st matches 211..215 run return run function mg:gta/cas_roul {p:1}',
       'execute if score $gcc mg.st matches 221..225 run return run function mg:gta/cas_roul {p:2}',
       'execute if score $gcc mg.st matches 231..235 run return run function mg:gta/cas_roul {p:3}',
       'execute if score $gcc mg.st matches 31..35 run return run function mg:gta/cas_dice']
w('gta/cas_cmd', CM)


def pay(mult_score):
    return ['scoreboard players operation $gwin mg.st = $gbet mg.st', f'scoreboard players operation $gwin mg.st *= {mult_score} mg.st',
            'scoreboard players operation @s mg.gta += $gwin mg.st']


WIN_MSG = ('title @s subtitle [{"text":"+","color":"green"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $","color":"green"}]')
LOSE_MSG = 'title @s subtitle [{"text":"-","color":"red"},{"score":{"name":"$gbet","objective":"mg.st"},"color":"red"},{"text":" $","color":"red"}]'
SYM = [{'text': '🍒', 'color': 'red'}, {'text': '🍋', 'color': 'yellow'}, {'text': '🔔', 'color': 'gold'},
       {'text': '💎', 'color': 'aqua'}, {'text': '⭐', 'color': 'yellow'}, {'text': '7', 'color': 'red', 'bold': True}]
STOP = (20, 30, 42)                                                          # tick d'arrêt de chaque rouleau
w('gta/cas_slot', ['# Machine à sous : 73 % perdu, 20 % 🍒🍒 ×2, 6 % 🔔🔔🔔 ×5, 1 % 777 ×20 (la maison garde ~10 %). Tirage maintenant, rouleaux animés, paiement à la fin.',
                   'data modify storage mg:gta sym set value ' + js(SYM),
                   'execute store result score @s mg.gsr run random value 0..99',
                   'execute store result score @s mg.gs1 run random value 0..5', 'execute store result score @s mg.gs2 run random value 0..5',
                   'execute store result score @s mg.gs3 run random value 0..5',
                   '# perdu : jamais 🍒🍒 en tête ni trois pareils',
                   'execute if score @s mg.gsr matches ..72 if score @s mg.gs1 matches 0 if score @s mg.gs2 matches 0 run scoreboard players set @s mg.gs2 1',
                   'execute if score @s mg.gsr matches ..72 if score @s mg.gs1 = @s mg.gs2 if score @s mg.gs2 = @s mg.gs3 run function mg:gta/cas_slot_bump',
                   'execute if score @s mg.gsr matches 73..92 run scoreboard players set @s mg.gs1 0', 'execute if score @s mg.gsr matches 73..92 run scoreboard players set @s mg.gs2 0',
                   'execute if score @s mg.gsr matches 73..92 run scoreboard players remove @s mg.gs3 1',
                   'execute if score @s mg.gsr matches 73..92 if score @s mg.gs3 matches ..0 run scoreboard players set @s mg.gs3 1',
                   'execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs1 2', 'execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs2 2',
                   'execute if score @s mg.gsr matches 93..98 run scoreboard players set @s mg.gs3 2',
                   'execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs1 5', 'execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs2 5',
                   'execute if score @s mg.gsr matches 99 run scoreboard players set @s mg.gs3 5',
                   'scoreboard players operation @s mg.gsb = $gbet mg.st', 'scoreboard players set @s mg.gsa 0', 'tag @s add mg.gslot',
                   'title @s clear', 'title @s times 0 12 4', 'title @s subtitle {"text":"🎰 les rouleaux tournent…","color":"gray"}',
                   'playsound minecraft:block.piston.extend player @a ~ ~ ~ 0.8 1.6',
                   'particle minecraft:wax_on ~ ~1.5 ~ 0.4 0.4 0.4 0 12'])
w('gta/cas_slot_bump', ['# @s : trois symboles pareils sur un tirage perdant → le troisième change', 'scoreboard players add @s mg.gs3 1',
                        'execute if score @s mg.gs3 matches 6.. run scoreboard players set @s mg.gs3 0',
                        'execute if score @s mg.gs1 matches 0 if score @s mg.gs3 matches 0 run scoreboard players set @s mg.gs3 1'])
SA = ['# @s (tag mg.gslot) : une image de l\'animation de la machine à sous', 'scoreboard players add @s mg.gsa 1',
      'scoreboard players set #6 mg.st 6', 'scoreboard players set #2 mg.st 2',
      'scoreboard players operation $ga mg.st = @s mg.gsa', 'scoreboard players operation $ga mg.st /= #2 mg.st']
for k, off in enumerate((0, 2, 4)):
    n = k + 1
    SA += [f'scoreboard players operation $gi{n} mg.st = $ga mg.st', f'scoreboard players add $gi{n} mg.st {off}', f'scoreboard players operation $gi{n} mg.st %= #6 mg.st',
           f'execute if score @s mg.gsa matches {STOP[k]}.. run scoreboard players operation $gi{n} mg.st = @s mg.gs{n}',
           f'execute store result storage mg:gta sl.i{n} int 1 run scoreboard players get $gi{n} mg.st']
SA += ['function mg:gta/cas_slot_pick with storage mg:gta sl',
       f'execute if score @s mg.gsa matches ..{STOP[2] - 1} run function mg:gta/cas_slot_show with storage mg:gta sl',
       'scoreboard players operation $gp mg.st = @s mg.gsa', 'scoreboard players operation $gp mg.st %= #2 mg.st',
       f'execute if score @s mg.gsa matches ..{STOP[2] - 1} if score $gp mg.st matches 0 run playsound minecraft:block.note_block.hat player @a ~ ~ ~ 0.35 1.8']
SA += [f'execute if score @s mg.gsa matches {t} run playsound minecraft:block.note_block.basedrum player @a ~ ~ ~ 0.9 {0.8 + 0.2 * k:.1f}' for k, t in enumerate(STOP)]
SA += [f'execute if score @s mg.gsa matches {STOP[2]}.. run function mg:gta/cas_slot_final with storage mg:gta sl',
       f'execute if score @s mg.gsa matches {STOP[2]}.. run function mg:gta/cas_slot_end',
       f'execute if score @s mg.gsa matches {STOP[2]}.. run function mg:gta/cas_reopen {{d:"slot"}}',
       f'execute if score @s mg.gsa matches {STOP[2]}.. run tag @s remove mg.gslot']
w('gta/cas_slot_anim', SA)
w('gta/cas_slot_pick', ['$data modify storage mg:gta sl.a set from storage mg:gta sym[$(i1)]', '$data modify storage mg:gta sl.b set from storage mg:gta sym[$(i2)]',
                        '$data modify storage mg:gta sl.c set from storage mg:gta sym[$(i3)]'])
FR = '{"text":"▌ ","color":"dark_gray"},$(a),{"text":"  │  ","color":"dark_gray"},$(b),{"text":"  │  ","color":"dark_gray"},$(c),{"text":" ▐","color":"dark_gray"}'
w('gta/cas_slot_show', ['$title @s title [' + FR + ']'])
w('gta/cas_slot_final', ['title @s times 0 30 10', '$title @s title [' + FR + ']'])
w('gta/cas_slot_end', ['# @s : les rouleaux sont arrêtés, paiement', 'scoreboard players operation $gbet mg.st = @s mg.gsb',
                       'scoreboard players operation $gr mg.st = @s mg.gsr',
                       'scoreboard players set #2 mg.st 2', 'scoreboard players set #5 mg.st 5', 'scoreboard players set #20 mg.st 20',
                       'execute if score $gr mg.st matches ..72 run ' + LOSE_MSG,
                       'execute if score $gr mg.st matches ..72 run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6'] +
  ['execute if score $gr mg.st matches 73..92 run ' + l for l in pay('#2')] +
  ['execute if score $gr mg.st matches 93..98 run ' + l for l in pay('#5')] +
  ['execute if score $gr mg.st matches 99 run ' + l for l in pay('#20')] +
  ['execute if score $gr mg.st matches 73.. run ' + WIN_MSG,
   'execute if score $gr mg.st matches 73.. run playsound minecraft:entity.player.levelup player @a ~ ~ ~ 1 1.3',
   'execute if score $gr mg.st matches 73.. run particle minecraft:happy_villager ~ ~1.5 ~ 0.6 0.6 0.6 0 25',
   'execute if score $gr mg.st matches 93.. run particle minecraft:wax_off ~ ~2 ~ 0.8 0.8 0.8 0.5 40',
   'execute if score $gr mg.st matches 99 run particle minecraft:totem_of_undying ~ ~1.5 ~ 0.5 1 0.5 0.6 120',
   'execute if score $gr mg.st matches 99 run playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 1',
   'execute if score $gr mg.st matches 99 run tellraw @a[tag=mg.gtw] [{"selector":"@s","color":"yellow"},{"text":" touche le JACKPOT au casino : ","color":"gold"},{"score":{"name":"$gwin","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]'])
w('gta/cas_roul', ['# Roulette (macro $(p) : 1 rouge, 2 noir, 3 vert) : 37 cases, 0 vert, 1..18 rouge, 19..36 noir',
                   'execute store result score $gr mg.st run random value 0..36',
                   'scoreboard players set $gok mg.st 0',
                   'scoreboard players set #p1 mg.st 0', 'scoreboard players set #p2 mg.st 0', 'scoreboard players set #p3 mg.st 0',
                   '$scoreboard players set #p$(p) mg.st 1',
                   'execute if score $gr mg.st matches 1..18 if score #p1 mg.st matches 1 run scoreboard players set $gok mg.st 2',
                   'execute if score $gr mg.st matches 19..36 if score #p2 mg.st matches 1 run scoreboard players set $gok mg.st 2',
                   'execute if score $gr mg.st matches 0 if score #p3 mg.st matches 1 run scoreboard players set $gok mg.st 36',
                   'execute if score $gr mg.st matches 0 run title @s title [{"text":"🟢 ","color":"green"},{"score":{"name":"$gr","objective":"mg.st"},"color":"green","bold":true}]',
                   'execute if score $gr mg.st matches 1..18 run title @s title [{"text":"🔴 ","color":"red"},{"score":{"name":"$gr","objective":"mg.st"},"color":"red","bold":true}]',
                   'execute if score $gr mg.st matches 19..36 run title @s title [{"text":"⚫ ","color":"dark_gray"},{"score":{"name":"$gr","objective":"mg.st"},"color":"white","bold":true}]',
                   'execute if score $gok mg.st matches 0 run ' + LOSE_MSG,
                   'execute if score $gok mg.st matches 0 at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6',
                   'execute if score $gok mg.st matches 1.. run scoreboard players operation $gwin mg.st = $gbet mg.st',
                   'execute if score $gok mg.st matches 1.. run scoreboard players operation $gwin mg.st *= $gok mg.st',
                   'execute if score $gok mg.st matches 1.. run scoreboard players operation @s mg.gta += $gwin mg.st',
                   'execute if score $gok mg.st matches 1.. run ' + WIN_MSG,
                   'execute if score $gok mg.st matches 1.. at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 1.3',
                   'execute at @s run playsound minecraft:block.wooden_button.click_on player @s ~ ~ ~ 1 1.8',
                   'function mg:gta/cas_reopen {d:"roulette"}'])
w('gta/cas_dice', ['# Dés : 2d6 du joueur contre 2d6 du croupier',
                   'execute store result score $gd1 mg.st run random value 2..12', 'execute store result score $gd2 mg.st run random value 2..12',
                   'title @s title [{"text":"🎲 ","color":"white"},{"score":{"name":"$gd1","objective":"mg.st"},"color":"aqua","bold":true},{"text":"  contre  ","color":"gray"},{"score":{"name":"$gd2","objective":"mg.st"},"color":"red","bold":true}]',
                   'scoreboard players set #2 mg.st 2',
                   'execute if score $gd1 mg.st > $gd2 mg.st run ' + pay('#2')[0], 'execute if score $gd1 mg.st > $gd2 mg.st run ' + pay('#2')[1],
                   'execute if score $gd1 mg.st > $gd2 mg.st run ' + pay('#2')[2], 'execute if score $gd1 mg.st > $gd2 mg.st run ' + WIN_MSG,
                   'execute if score $gd1 mg.st = $gd2 mg.st run scoreboard players operation @s mg.gta += $gbet mg.st',
                   'execute if score $gd1 mg.st = $gd2 mg.st run title @s subtitle {"text":"Égalité : mise rendue","color":"yellow"}',
                   'execute if score $gd1 mg.st < $gd2 mg.st run ' + LOSE_MSG,
                   'execute at @s run playsound minecraft:block.note_block.hat player @s ~ ~ ~ 1 1.4',
                   'function mg:gta/cas_reopen {d:"dice"}'])
w('gta/cas_reopen', ['# Rouvre la fenêtre du jeu après 2 s (le joueur rejoue ou ferme)', '$tag @s add mg.gcas_$(d)', 'scoreboard players set @s mg.gcre 40'])
w('gta/cas_reopen_tick', ['# @s : réouverture de la fenêtre du casino', 'execute if entity @s[tag=mg.gcas_slot] run function mg:gta/cas_ui_slot',
                          'execute if entity @s[tag=mg.gcas_roulette] run function mg:gta/cas_ui_roulette', 'execute if entity @s[tag=mg.gcas_dice] run function mg:gta/cas_ui_dice',
                          'tag @s remove mg.gcas_slot', 'tag @s remove mg.gcas_roulette', 'tag @s remove mg.gcas_dice'])
C.objectives([('mg.gcas', 'trigger'), ('mg.gcre', 'dummy'), ('mg.gsa', 'dummy'), ('mg.gsr', 'dummy'), ('mg.gsb', 'dummy'),
              ('mg.gs1', 'dummy'), ('mg.gs2', 'dummy'), ('mg.gs3', 'dummy')])
