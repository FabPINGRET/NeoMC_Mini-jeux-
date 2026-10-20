"""🦖 Terra Nova : colonie préhistorique, monde libre (dimension mg:terranova) relié au lobby par un portail (en face de Neo GTA).

    python tools/arcade/gen_terranova.py .      (avant tools/duel/gen_duel.py : il ajoute une garde à terra/menu_go, réécrit ici)

Monde
- Dimension mg:terranova (data/mg/dimension/terranova.json) : vide, biome the_void (aucune apparition naturelle). Carte bornée
  192 × 192 construite une fois par mg:terra/world_build (~2 min) : jungle (relief, rivière, falaises au bord, arbres et
  bambous posés par « place feature »), colonie fortifiée au centre, 3 outposts. Ajouter la dimension demande un
  redémarrage du serveur (pas un simple /reload).
- Session : démarre au premier joueur (chargement forcé + entités), s'arrête au dernier (entités retirées, outposts réparés).
- Joueurs : tags mg.tvw + mg.surv (comme Neo GTA : exclus des mini-jeux, menu « retour au lobby »). Crédits (mg.tvc) gardés
  d'une visite à l'autre, équipement de base à chaque arrivée.

Jeu
- Colonie (sûre, défenses du périmètre) : dépôt d'équipement (7 présentoirs), infirmerie (soins), tableau des missions,
  portes nord et sud, portail du temps (retour au spawn).
- Armes : bâton électrique (étourdit), fusil à impulsions (surchauffe), canon sonique (onde en cône qui repousse),
  lance-filets et pièges au sol (immobilisent).
- Dinosaures (mobs vanilla invisibles + modèle en block_display) : slashers (vindicateurs, en meute, traquent),
  carnotaure (hoglin, mini-boss, casse les structures légères des outposts), brachiosaures (dromadaires) et
  pachycéphalosaures (chèvres) neutres.
- Missions : récupération de matériel (caisse à ramener), défense d'outpost (90 s), chasse aux slashers, chasse au carnotaure.
"""
import json
import math
import os
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import shutil
for _d in ('b', 'r', 'bio', 'an', 'dino', 'rpg'):                  # dossiers entièrement générés : repartis de zéro
    shutil.rmtree(os.path.join(C.F, 'terra', _d), ignore_errors=True)
w, js = C.w, C.js
DIM = 'mg:terranova'
HX = 96                                  # carte : x, z de -96 à 95
FL = '-112 -112 111 111'                 # chargement forcé (marge d'un chunk pour les arbres)
WALL = 28                                # enceinte de la colonie
G = 64                                   # sol de la colonie (on marche à y 65)
PX, PZ = -9, -19                         # portail du lobby (en face de celui de Neo GTA, x 9 z -19)
SPAWN = (0.5, 65, 4.5)                   # arrivée : place centrale, regard vers le nord
MED = (16.5, 65, 17.5)                   # réapparition : infirmerie
EXITA = (-12, 16)                        # portail du temps (sortie), ouverture z 15..17
COLONY_BOX = f'x={-WALL},y=58,z={-WALL},dx={2 * WALL},dy=30,dz={2 * WALL}'
TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
rnd = random.Random(2042)

# Les blocs de génération ci-dessous vivent dans les tv_*.py voisins : mêmes globals, ordre inchangé.
# relief : bruit, hauteurs H, surface, points d'apparition, TERRAIN et VEG (tv_relief.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_relief.py'), encoding='utf-8').read())

# colonie (fill / setb / building) et avant-postes (tv_colony.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_colony.py'), encoding='utf-8').read())

# ---------------------------------------------------------------- régions du RPG (tv_world.py)
TVW = dict(globals())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_world.py'), encoding='utf-8').read(), TVW)
R_TERRAIN, RS_CMD, R_VEG, R_BIOME, V_PATCH, V_BIOME, VSTRUCT, FL_REGIONS = (TVW[k] for k in (
    'R_TERRAIN', 'RS_CMD', 'R_VEG', 'R_BIOME', 'V_PATCH', 'V_BIOME', 'VSTRUCT', 'FL_REGIONS'))
VCARVE = []                                         # mondes construits avant les cols : falaises creusées
for (x, z), h0 in sorted(H_OLD.items()):
    h = H[(x, z)]
    if h != h0:
        VCARVE += [f'fill {x} 56 {z} {x} {h - 1} {z} minecraft:{under(x, z)}', f'setblock {x} {h} {z} minecraft:{surface(x, z)}',
                   f'fill {x} {h + 1} {z} {x} {max(h, h0) + 12} {z} minecraft:air']

# ---------------------------------------------------------------- étapes de construction
STEPS = []
for i in range(0, len(TERRAIN), 450):
    STEPS.append(TERRAIN[i:i + 450])
for i in range(0, len(S), 300):
    STEPS.append(S[i:i + 300])
for i in range(0, len(VEG), 40):
    STEPS.append(VEG[i:i + 40])
for i, L in enumerate(STEPS, 1):
    w(f'terra/b/s{i}', [f'# Construction de Terra Nova, étape {i}/{len(STEPS)} (dimension {DIM}, générée)'] + L)
NS = len(STEPS)
w('terra/wb_step', ['# Une étape de construction de Terra Nova par tick ($tvb), dans la dimension. Planifiée.',
                    'scoreboard players add $tvb mg.st 1'] +
  [f'execute if score $tvb mg.st matches {i} in {DIM} run function mg:terra/b/s{i}' for i in range(1, NS + 1)] +
  [f'execute if score $tvb mg.st matches {NS + 1} run function mg:terra/wb_done',
   f'execute if score $tvb mg.st matches ..{NS} run schedule function mg:terra/wb_step 1t'])
w('terra/wb_done', ['# Vallée de Terra Nova prête : drapeau, puis construction des régions du RPG',
                    f'execute in {DIM} run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                    f'execute in {DIM} if block 0 {G} 0 minecraft:chiseled_stone_bricks run data modify storage mg:terra built set value 1b',
                    'function mg:terra/world_build2'])
# régions : chargement forcé de toute la carte, une étape par tick
RSTEPS = []
for k in ('n', 'e', 'w', 's'):
    for L, n in ((R_TERRAIN[k], 450), (RS_CMD[k], 200), (R_VEG[k], 40)):
        for i in range(0, len(L), n):
            RSTEPS.append(L[i:i + n])
for L in (VCARVE + V_PATCH + VSTRUCT,):
    for i in range(0, len(L), 300):
        RSTEPS.append(L[i:i + 300])
for i, L in enumerate(RSTEPS, 1):
    w(f'terra/r/s{i}', [f'# Construction des régions de Terra Nova, étape {i}/{len(RSTEPS)} (dimension {DIM}, générée)'] + L)
NR = len(RSTEPS)
FL_ALL = [FL] + list(FL_REGIONS.values())
w('terra/rb_step', ['# Une étape de construction des régions par tick ($tvrb), dans la dimension. Planifiée.',
                    'scoreboard players add $tvrb mg.st 1'] +
  [f'execute if score $tvrb mg.st matches {i} in {DIM} run function mg:terra/r/s{i}' for i in range(1, NR + 1)] +
  [f'execute if score $tvrb mg.st matches {NR + 1} run function mg:terra/rb_done',
   f'execute if score $tvrb mg.st matches ..{NR} run schedule function mg:terra/rb_step 1t'])
w('terra/world_build2', ['# Construction des régions du RPG (marais, plaines, canyon, volcan) + cols de la vallée (~3 min)',
                         'scoreboard players set $tvrb mg.st 0'] + [f'execute in {DIM} run forceload add {f}' for f in FL_ALL] +
  ['schedule function mg:terra/rb_step 100t'])
# biomes du datapack : connus seulement après un redémarrage du serveur. Les fonctions bio/* ne se chargent pas avant :
# mg:terra/bio_try (session, fin de construction) teste mg:terra/bio/ok et lance le remplissage une fois.
BIO = [l for k in ('n', 'e', 'w', 's') for l in R_BIOME[k]] + V_BIOME
for i in range(0, len(BIO), 150):
    w(f'terra/bio/s{i // 150 + 1}', [f'# Biomes de Terra Nova, étape {i // 150 + 1} (dimension {DIM})'] + BIO[i:i + 150])
NB = (len(BIO) + 149) // 150
w('terra/bio/ok', ['# Se charge seulement si les biomes du datapack existent (sinon l’appel échoue)', 'execute if biome 0 0 0 mg:tv_jungle run return 1', 'return 1'])
w('terra/bio_try', ['# Biomes des régions posés une seule fois, dès que le serveur les connaît (après un redémarrage)',
                    'execute if data storage mg:terra bio run return 0', 'execute unless data storage mg:terra v2 run return 0',
                    'scoreboard players set $tvbo mg.st 0', 'execute store result score $tvbo mg.st run function mg:terra/bio/ok',
                    'execute unless score $tvbo mg.st matches 1 run return 0',
                    'data modify storage mg:terra bio set value 1b', 'scoreboard players set $tvbs mg.st 0'] +
  [f'execute in {DIM} run forceload add {f}' for f in FL_ALL] + ['schedule function mg:terra/bio_step 60t'])
w('terra/bio_step', ['# Une étape de biomes par tick (zone chargée : session ou fin de construction)', 'scoreboard players add $tvbs mg.st 1'] +
  [f'execute if score $tvbs mg.st matches {i} in {DIM} run function mg:terra/bio/s{i}' for i in range(1, NB + 1)] +
  [f'execute if score $tvbs mg.st matches ..{NB - 1} run return run schedule function mg:terra/bio_step 1t'] +
  [f'execute unless score $tvw mg.st matches 1 in {DIM} run forceload remove {f}' for f in FL_ALL])
w('terra/rb_done', ['# Régions prêtes : bords de la carte, drapeau, plus de chargement forcé si personne ne joue',
                    f'execute in {DIM} run kill @e[type=minecraft:item,x=-260,y=40,z=-260,dx=520,dy=140,dz=520]',
                    f'execute in {DIM} run function mg:terra/walls_old', f'execute in {DIM} run function mg:terra/walls',
                    'data modify storage mg:terra v2 set value 1b'] +
  [f'execute unless score $tvw mg.st matches 1 in {DIM} run forceload remove {f}' for f in FL_ALL] +
  ['function mg:terra/bio_try', 'tellraw @a[tag=mg.admin] {"text":"🦖 Terra Nova est construite (vallée et régions du RPG).","color":"green"}'])
w('terra/world_build', ['# Première construction de Terra Nova (ou reconstruction complète, ~2 min)',
                        f'execute in {DIM} run forceload add {FL}', 'scoreboard players set $tvb mg.st 0',
                        'schedule function mg:terra/wb_step 40t'])
os.makedirs(os.path.join(C.D, 'dimension'), exist_ok=True)
with open(os.path.join(C.D, 'dimension', 'terranova.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'type': 'minecraft:overworld', 'generator': {'type': 'minecraft:flat', 'settings': {
        'biome': 'minecraft:the_void', 'layers': [], 'lakes': False, 'features': False, 'structure_overrides': []}}}, f, indent=2)
    f.write('\n')
os.makedirs(os.path.join(C.D, 'tags', 'block'), exist_ok=True)
with open(os.path.join(C.D, 'tags', 'block', 'tv_light.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': [f'minecraft:{b}' for b in LIGHT]}, f, indent=2)
    f.write('\n')
with open(os.path.join(C.D, 'tags', 'block', 'tv_pass.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': ['#mg:ray_pass', '#minecraft:leaves', 'minecraft:bamboo', 'minecraft:firefly_bush',
                          {'id': 'minecraft:bush', 'required': False}, 'minecraft:cocoa', 'minecraft:melon_stem']}, f, indent=2)
    f.write('\n')

# objets, portail du lobby, entrée / sortie / session (tv_gear.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_gear.py'), encoding='utf-8').read())

# dinosaures (dont l'exec de tv_dino_fn.py) et armes (tv_combat.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_combat.py'), encoding='utf-8').read())

# boutique, tableau des missions, missions 1 à 4 (tv_missions.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_missions.py'), encoding='utf-8').read())

# mort, interface, tick de la session, SEC (tv_loop.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_loop.py'), encoding='utf-8').read())

# ================================================================ câblage
C.patch('core/tick', 'function mg:gta/lobby_tick', ['function mg:terra/lobby_tick'])
C.patch('core/tick', 'function mg:gta/pre_tick', ['function mg:terra/pre_tick'])
C.patch('survie/leave', 'execute if entity @s[tag=mg.gtw] run return run function mg:gta/leave',
        ['execute if entity @s[tag=mg.tvw] run return run function mg:terra/leave'])
C.patch('survie/cmd', 'execute if score @s mg.sv matches 4 run function mg:gta/menu_go', ['execute if score @s mg.sv matches 7 run function mg:terra/menu_go'])
_cmd = C.lines_of('survie/cmd')
if _cmd and '4 = Neo GTA,' in _cmd[0] and 'Terra Nova' not in _cmd[0]:
    _cmd[0] = _cmd[0].replace('4 = Neo GTA,', '4 = Neo GTA, 7 = Terra Nova,')
    C.w('survie/cmd', _cmd[:-1] if _cmd[-1] == '' else _cmd)
_pa = C.lines_of('core/pull_all')
_pa = [l.replace('tag @a[tag=mg.surv,tag=!mg.gtw] add mg.pulls', 'tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw] add mg.pulls') for l in _pa]
if 'tag @a[tag=mg.tvw] add mg.pullt' not in _pa:
    i = _pa.index('tag @a[tag=mg.gtw] add mg.pullg')
    _pa[i + 1:i + 1] = ['tag @a[tag=mg.tvw] add mg.pullt']
    j = _pa.index('execute as @a[tag=mg.pullg] in minecraft:overworld run function mg:gta/leave')
    _pa[j + 1:j + 1] = ['execute as @a[tag=mg.pullt] in minecraft:overworld run function mg:terra/leave']
C.w('core/pull_all', _pa[:-1] if _pa[-1] == '' else _pa)
C.patch('core/optout', 'execute if entity @s[tag=mg.pullg] in minecraft:overworld run function mg:gta/enter',
        ['execute if entity @s[tag=mg.pullt] in minecraft:overworld run function mg:terra/enter'])
C.patch('core/optout', 'tag @s remove mg.pullg', ['tag @s remove mg.pullt'])
C.patch('core/request', 'tag @a remove mg.pullg', ['tag @a remove mg.pullt'])
_st = C.lines_of('survie/tick')
_st = [l.replace('execute as @a[tag=mg.surv,tag=!mg.svg2,scores={mg.svid=1..}] run function mg:survie/regen_now',
                 'execute as @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.svg2,scores={mg.svid=1..}] run function mg:survie/regen_now') for l in _st]
C.w('survie/tick', _st[:-1] if _st[-1] == '' else _st)
C.patch('desinstaller', 'execute if score $tmap mg.st matches 1 run function mg:lobby/theme/map/end',
        ['execute as @a[tag=mg.tvw] in minecraft:overworld run function mg:terra/leave'], where='before')
C.patch('core/load', 'execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1',
        ['# Terra Nova : construite une fois (dimension mg:terranova, ~2 min, après Neo City), règles du monde',
         'execute if score $setup mg.st matches 1 unless data storage mg:terra built run schedule function mg:terra/world_build 200s',
         'execute if score $setup mg.st matches 1 unless data storage mg:lobby tvclean run schedule function mg:terra/spawn_clean 9s',
         'scoreboard players set $tvw mg.st 0', 'function mg:terra/rules'])
C.objectives([('mg.tvq', 'minecraft.used:minecraft.warped_fungus_on_a_stick'), ('mg.tvdd', 'minecraft.custom:minecraft.damage_dealt'),
              ('mg.tvdt', 'minecraft.custom:minecraft.damage_taken'), ('mg.tvkr', 'minecraft.killed:minecraft.vindicator'),
              ('mg.tvkc', 'minecraft.killed:minecraft.hoglin'), ('mg.tvkb', 'minecraft.killed:minecraft.camel'), ('mg.tvkg', 'minecraft.killed:minecraft.goat'),
              ('mg.tvms', 'trigger'), ('mg.tvpid', 'dummy'), ('mg.tvid', 'dummy'), ('mg.tvo', 'dummy'), ('mg.tvk', 'dummy'), ('mg.tvh', 'dummy'),
              ('mg.tvcd', 'dummy'), ('mg.tvsc', 'dummy'), ('mg.tvnet', 'dummy'), ('mg.tvtr', 'dummy'), ('mg.tvst', 'dummy'), ('mg.tvm', 'dummy'),
              ('mg.tvmo', 'dummy'), ('mg.tvmp', 'dummy'), ('mg.tvhm', 'dummy'), ('mg.tval', 'dummy'), ('mg.tvx', 'dummy'), ('mg.tvy', 'dummy'),
              ('mg.tvz', 'dummy')])
C.objectives([('mg.tvat', 'dummy'), ('mg.tvaf', 'dummy'), ('mg.tvas', 'dummy'), ('mg.tvses', 'dummy'), ('mg.tvak', 'dummy'), ('mg.tvab', 'dummy'), ('mg.tvph', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['scoreboard objectives add mg.tvc dummy {"text":"₵ Terra Nova","color":"green"}'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        ['scoreboard objectives remove mg.tvc', 'schedule clear mg:terra/wb_step', 'schedule clear mg:terra/world_build', 'schedule clear mg:terra/session_setup',
         'schedule clear mg:terra/spawn_clean', f'execute in {DIM} run forceload remove all', 'kill @e[tag=mg.tvport]', 'kill @e[tag=mg.tv]',
         'team remove mg_tv', 'bossbar remove mg:tvcarno', 'bossbar remove mg:tvo1', 'bossbar remove mg:tvo2', 'bossbar remove mg:tvo3',
         'data remove storage mg:terra built', 'data remove storage mg:terra d', 'data remove storage mg:terra h', 'data remove storage mg:lobby tvclean'])
# menu Échap : bouton « Aller à Terra Nova » (après Neo GTA)
_mp = os.path.join(C.D, 'dialog', 'main_menu.json')
_m = json.load(open(_mp, encoding='utf-8'))
if not any(a['action'].get('command') == 'trigger mg.sv set 7' for a in _m['actions']):
    i = next(i for i, a in enumerate(_m['actions']) if a['action'].get('command') == 'trigger mg.sv set 4')
    _m['actions'].insert(i + 1, {'label': [{'text': '🦖 Aller à Terra Nova', 'color': 'green', 'bold': True}],
                                 'tooltip': [{'text': 'Colonie préhistorique : missions, jungle, dinosaures (tes crédits y sont gardés)', 'color': 'gray'}],
                                 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.sv set 7'}})
    with open(_mp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(_m, f, ensure_ascii=False, indent=2)
        f.write('\n')
print(f'Terra Nova OK : {len(TERRAIN)} cmd de relief, {len(S)} de colonie, {len(VEG)} de végétation, {NS} étapes, '
      f'{len(CRATES)} caisses, {len(SPAWNS)} points d\'apparition ({len(FAR)} lointains), {len(HERBS)} herbivores')
# ================================================================ RPG (tv_rpg.py) : niveaux, campagne, PNJ, boss, forge, voyages
TVR = dict(globals())
TVR.update({k: TVW[k] for k in ('POIS', 'CAMPS', 'MARKERS', 'DATA_PTS', 'CELL', 'RIFT', 'VOLC', 'LAG', 'FORT', 'DELTA', 'CALD_Y', 'REGIONS',
                                'PASS_GATE', 'ECHO', 'LOOKOUT', 'REFUGE', 'BRIDGE', 'BR_Y', 'STATION', 'ground', 'EGGS', 'LAB_NPC', 'FORGE_NPC',
                                'COLONY_BEACON', 'DUNGEONS', 'CACHES')})
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_rpg.py'), encoding='utf-8').read(), TVR)
if os.environ.get('TV_DUMP'):                       # aperçu de la carte (outil de mise au point)
    import pickle
    pickle.dump({'H': H, 'surface': {c: surface(*c) for c in H}, 'COL': TVW['COL'], 'POIS': TVW['POIS'], 'MARKERS': TVW['MARKERS']},
                open(os.environ['TV_DUMP'], 'wb'))
