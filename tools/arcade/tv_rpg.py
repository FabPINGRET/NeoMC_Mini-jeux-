"""⚔ Terra Nova RPG : niveaux, campagne (chapitres, PNJ), bestiaire, trophées et forge, boss, voyages, monture.
Exécuté à la fin de gen_terranova.py (exec dans une copie de ses globales + les données de tv_world.py).

Scores des joueurs (gardés d'une visite à l'autre) :
  mg.trlv niveau (1..20), mg.trxp XP du niveau, mg.trch étape de la campagne (0..100), mg.trqp progression de l'étape,
  mg.trbs bestiaire (bits), mg.trpo lieux découverts (bits), mg.trtv balises de voyage (bits), mg.treg œufs d'ambre (bits),
  mg.trwp fusil (1..4), mg.trml mêlée (1..3), mg.trar armure (0..4), mg.trmt monture (0/1),
  trophées : mg.trgr griffes, mg.trdn dents, mg.trvn glandes à venin, mg.trec écailles de spinosaure, mg.trai ailes, mg.trrx crocs du Roi.
"""
import math as _m

P = 'terra/rpg'
SPECIES_ORDER = ['raptor', 'compy', 'dilo', 'galli', 'pachy', 'trike', 'stego', 'ankylo', 'brachio', 'ptera', 'carno', 'spino', 'rex']
BEST = {
    'raptor': ('Slasher', 'Chasseur en meute, rapide et rusé. Il bondit sur sa proie.', 'griffe'),
    'compy': ('Compsognathus', 'Minuscule mais jamais seul : les nuées submergent les imprudents.', None),
    'dilo': ('Dilophosaure', 'Déploie sa collerette et crache un venin aveuglant à distance.', 'glande à venin'),
    'galli': ('Gallimimus', 'Herbivore véloce qui file au moindre bruit. Protégé.', None),
    'pachy': ('Pachycéphalosaure', 'Crâne en dôme : il charge tête baissée. Protégé.', None),
    'trike': ('Tricératops', 'Paisible tant qu\'on le laisse tranquille. Ses cornes ne pardonnent pas.', None),
    'stego': ('Stégosaure', 'Les pointes de sa queue fauchent quiconque s\'approche de trop près.', None),
    'ankylo': ('Ankylosaure', 'Un char d\'assaut vivant, armé d\'une massue au bout de la queue.', None),
    'brachio': ('Brachiosaure', 'Le géant de la vallée. On peut le monter avec une selle.', None),
    'ptera': ('Ptéranodon', 'Plonge du ciel sur les voyageurs isolés.', 'aile'),
    'carno': ('Carnotaure', 'Prédateur cornu qui charge et brise les palissades.', 'dent'),
    'spino': ('Spinosaure', 'La reine du marais. Plonge, ressurgit et appelle ses petits.', 'écaille'),
    'rex': ('Roi Tyran', 'Le plus grand prédateur de Terra Nova. Son rugissement glace le sang.', 'croc du Roi'),
}
TAGS = {'raptor': 'mg.tvraptor', 'compy': 'mg.tvcompy', 'dilo': 'mg.tvdilo', 'galli': 'mg.tvgalli', 'pachy': 'mg.tvpachy',
        'trike': 'mg.tvtrike', 'stego': 'mg.tvstego', 'ankylo': 'mg.tvankylo', 'brachio': 'mg.tvbrach', 'ptera': 'mg.tvptera',
        'carno': 'mg.tvcarno', 'spino': 'mg.tvspino', 'rex': 'mg.tvrex'}
NPCS = {1: ('varga', '⚔ Commandante Varga', 'gold', (14.5, 65, -14.5), 90, 'minecraft:cartographer'),
        2: ('ossei', '🔬 Dr Ossei', 'aqua', LAB_NPC, 0, 'minecraft:librarian'),
        3: ('jo', '⚒ Jo, forgeronne', 'red', FORGE_NPC, 180, 'minecraft:armorer'),
        4: ('nyla', '🏹 Nyla, éclaireuse', 'green', (DELTA[0] + 3.5, ground(*DELTA), DELTA[1] - 2.5), 90, 'minecraft:leatherworker')}
VARGA_POS = (14, 65, -15)
OSSEI_POS = (int(LAB_NPC[0]), 65, int(LAB_NPC[2]))
REG_IDX = {'v': 0, 'n': 1, 'e': 2, 'w': 3, 's': 4}
REG_BOX = {1: 'x=-96,y=-64,z=-256,dx=191,dy=400,dz=159', 2: 'x=96,y=-64,z=-96,dx=159,dy=400,dz=191',
           3: 'x=-256,y=-64,z=-96,dx=159,dy=400,dz=191', 4: 'x=-96,y=-64,z=96,dx=191,dy=400,dz=159'}
GATE_CH = {1: 30, 2: 50, 3: 60, 4: 70}
GATE_BACK = {}
for k, (gx, gz) in PASS_GATE.items():
    dx, dz = {'n': (0, 6), 's': (0, -6), 'e': (-6, 0), 'w': (6, 0)}[k]
    GATE_BACK[REG_IDX[k]] = (gx + dx + 0.5, H[(gx + dx, gz + dz)] + 1, gz + dz + 0.5)
TEXT = lambda t, c='gray', **k: {'text': t, 'color': c, **k}
STATION_C = (STATION[0], 64, STATION[1])
LAG_C = (LAG[0], 65, LAG[1])
CALD = (VOLC[0], CALD_Y + 1, VOLC[1])
BRIDGE_C = (BRIDGE[0], BR_Y + 1, BRIDGE[1])
DELTA_C = (DELTA[0], ground(*DELTA), DELTA[1])
FORT_C = (FORT[0], 65, FORT[1])

# ---------------------------------------------------------------- étapes de la campagne : n° -> (titre du chapitre, objectif, cible du 📡)
CH = {
    0: ('Prologue', 'Parle à la Commandante Varga (QG de la colonie)', VARGA_POS),
    10: ('I · Premiers pas', 'Abats 3 slashers dans la jungle', None),
    15: ('I · Premiers pas', 'Retourne voir la Commandante Varga', VARGA_POS),
    20: ('II · Le scanner', 'Va voir le Dr Ossei au labo (est de la place)', OSSEI_POS),
    25: ('II · Le scanner', 'Scanne 2 espèces de dinosaures (clic droit avec le scanner)', None),
    28: ('II · Le scanner', 'Retourne voir le Dr Ossei', OSSEI_POS),
    30: ('III · Le signal du marais', 'Passe le col nord et rejoins la Station engloutie', STATION_C),
    32: ('III · Le signal du marais', 'Récupère les 3 modules de données (accroupi près d\'un module)', STATION_C),
    35: ('III · Le signal du marais', 'Rapporte les modules au Dr Ossei', OSSEI_POS),
    40: ('IV · La reine du marais', 'Abats le Spinosaure dans la Lagune de l\'Antre', LAG_C),
    45: ('IV · La reine du marais', 'Rends compte à la Commandante Varga', VARGA_POS),
    50: ('V · Les grandes plaines', 'Passe le col est et rejoins Camp Delta', DELTA_C),
    52: ('V · Les grandes plaines', 'Parle à Nyla, l\'éclaireuse de Camp Delta', DELTA_C),
    55: ('V · Les grandes plaines', 'Scanne un tricératops, un stégosaure et un ankylosaure', (190, 70, 0)),
    58: ('V · Les grandes plaines', 'Retourne voir Nyla à Camp Delta', DELTA_C),
    60: ('VI · Le vol de la cellule', 'Passe le col ouest et approche du Fort des Renégats', FORT_C),
    62: ('VI · Le vol de la cellule', 'Abats le lieutenant Varek, chef du fort', FORT_C),
    64: ('VI · Le vol de la cellule', 'Récupère la cellule d\'énergie dans l\'entrepôt (accroupi)', CELL),
    66: ('VI · Le vol de la cellule', 'Rapporte la cellule à la Commandante Varga', VARGA_POS),
    70: ('VII · La faille', 'Le Dr Ossei a analysé la cellule : va le voir', OSSEI_POS),
    72: ('VII · La faille', 'Passe le col sud et gravis le Mont Cendre jusqu\'au Pont d\'obsidienne', BRIDGE_C),
    75: ('VII · La faille', 'Atteins la Caldeira du Roi, au sommet du volcan', CALD),
    80: ('VIII · Le Roi Tyran', 'Abats le Roi Tyran', CALD),
    85: ('VIII · Le Roi Tyran', 'Approche-toi de la faille temporelle', RIFT),
    90: ('Épilogue', 'Retourne à la colonie : la Commandante Varga t\'attend', VARGA_POS),
    100: ('Héros de Terra Nova', 'Contrats au tableau du QG, boss à revaincre, bestiaire et œufs d\'ambre', None),
}


def chfn(n):
    return f'function mg:{P}/ch {{n:{n}}}'


# ================================================================ constantes, XP, niveaux
w(f'{P}/consts', ['# Constantes (puissances de 2 pour les bits, diviseurs)'] +
  [f'scoreboard players set #p{i} mg.st {2 ** i}' for i in range(20)] +
  ['scoreboard players set #2 mg.st 2', 'scoreboard players set #40 mg.st 40', 'scoreboard players set #100 mg.st 100',
   'scoreboard players set #5 mg.st 5', 'scoreboard players set #m1 mg.st -1'])


def bit_test(score, i):
    """Lignes : $b = bit i du score de @s (0/1)."""
    return [f'scoreboard players operation $b mg.st = @s {score}', f'scoreboard players operation $b mg.st /= #p{i} mg.st',
            'scoreboard players operation $b mg.st %= #2 mg.st']


w(f'{P}/xp', ['# @s gagne $(n) XP (macro)', '$scoreboard players add @s mg.trxp $(n)',
              '$tellraw @s [{"text":"  +$(n) XP","color":"aqua"}]', f'function mg:{P}/lvchk'])
w(f'{P}/lvchk', ['# @s : passage(s) de niveau (besoin = 80 + 40 × niveau)',
                 'execute if score @s mg.trlv matches 20.. run return run scoreboard players set @s mg.trxp 0',
                 'scoreboard players operation $need mg.st = @s mg.trlv', 'scoreboard players operation $need mg.st *= #40 mg.st',
                 'scoreboard players add $need mg.st 80', 'execute if score @s mg.trxp < $need mg.st run return 0',
                 'scoreboard players operation @s mg.trxp -= $need mg.st', 'scoreboard players add @s mg.trlv 1',
                 f'function mg:{P}/lvup', f'function mg:{P}/lvchk'])
w(f'{P}/lvup', ['# @s monte de niveau : annonce, effets, statistiques, soin',
                'title @s times 5 50 15', 'title @s title [{"text":"⭐ NIVEAU ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.trlv"},"color":"yellow","bold":true}]',
                'title @s subtitle {"text":"Plus robuste : +1 cœur tous les 2 niveaux","color":"gray"}',
                'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2',
                'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.4 0.8 0.4 0.4 40',
                'tellraw @a[tag=mg.tvw] [{"text":"⭐ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" atteint le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.trlv"},"color":"gold","bold":true}]',
                f'function mg:{P}/stats', 'function mg:core/heal', 'scoreboard players add @s mg.trsp 1'])
w(f'{P}/stats', ['# @s : bonus de vie du niveau (2 PV tous les 2 niveaux)', 'attribute @s minecraft:max_health modifier remove mg:trlv',
                 'scoreboard players operation $hp mg.st = @s mg.trlv', 'scoreboard players remove $hp mg.st 1',
                 'scoreboard players operation $hp mg.st /= #2 mg.st', 'scoreboard players operation $hp mg.st *= #2 mg.st',
                 'execute store result storage mg:terra s.hp int 1 run scoreboard players get $hp mg.st',
                 f'function mg:{P}/stats_m with storage mg:terra s', f'function mg:{P}/cl/passive', f'function mg:{P}/st/apply'])
w(f'{P}/stats_m', ['$attribute @s minecraft:max_health modifier add mg:trlv $(hp) add_value'])

# ================================================================ campagne : changement d'étape, objectif, localisateur
w(f'{P}/ch', ['# @s passe à l\'étape $(n) de la campagne', '$scoreboard players set @s mg.trch $(n)', 'scoreboard players set @s mg.trqp 0',
              'execute if score @s mg.trch matches 30 run function mg:terra/rpg/cs/pass_n', 'execute if score @s mg.trch matches 50 run function mg:terra/rpg/cs/pass_e',
              'execute if score @s mg.trch matches 60 run function mg:terra/rpg/cs/pass_w', 'execute if score @s mg.trch matches 72 run function mg:terra/rpg/cs/pass_s',
              f'function mg:{P}/obj_say', f'function mg:{P}/qloc',
              'execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 0.9'])
OS = ['# @s : annonce de l\'objectif de l\'étape en cours']
QL = ['# @s : 📡 localisateur vers l\'objectif de la campagne (sauf mission en cours)', 'execute if score @s mg.tvm matches 1.. run return 0']
HUDQ = []
for n, (title, obj, tgt) in CH.items():
    OS.append(f'execute if score @s mg.trch matches {n} run return run tellraw @s ' +
              js([TEXT('📜 ', 'gold'), TEXT(title, 'gold', bold=True), TEXT(' — ', 'dark_gray'), TEXT(obj, 'yellow')]))
    if tgt:
        QL.append(f'execute if score @s mg.trch matches {n} run return run function mg:terra/loc {{x:{int(tgt[0])},y:{int(tgt[1])},z:{int(tgt[2])}}}')
    HUDQ.append((n, obj))
QL += [LOC_HOME, 'scoreboard players set @s mg.tron 0']
w(f'{P}/obj_say', OS)
w(f'{P}/qloc', QL)
w(f'{P}/quest', ['# @s : rappel de la campagne (trigger mg.trtk 9 ou commande)', f'function mg:{P}/obj_say', f'function mg:{P}/qloc'])

# ================================================================ entrée / sortie du monde, équipement par paliers
BLADE = (f'minecraft:golden_sword[custom_data={{tv:12}},unbreakable={{}},custom_name={nm("🗡 Lame d\'ambre", "gold")},'
         f'lore={lo("Mêlée : étourdit le dinosaure touché", "Forgée avec des griffes de slasher")},'
         'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:tvbl",amount:8.0,operation:"add_value",slot:"mainhand"},'
         '{type:"minecraft:attack_speed",id:"mg:tvbs",amount:-2.2,operation:"add_value",slot:"mainhand"}]]')
CROC = (f'minecraft:netherite_sword[custom_data={{tv:13}},unbreakable={{}},enchantment_glint_override=true,custom_name={nm("🦷 Croc du Tyran", "dark_red")},'
        f'lore={lo("Mêlée : étourdit, dégâts énormes", "Taillé dans un croc du Roi Tyran")},'
        'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:tvcr",amount:13.0,operation:"add_value",slot:"mainhand"},'
        '{type:"minecraft:attack_speed",id:"mg:tvcs",amount:-2.4,operation:"add_value",slot:"mainhand"}]]')
RIFLE3 = (f'{WF}[custom_data={{tv:7}},item_model="minecraft:crossbow",unbreakable={{}},enchantment_glint_override=true,'
          f'custom_name={nm("🔫 Fusil à plasma Mk3", "light_purple")},lore={lo("Tir violet perforant, chauffe peu", "Clic droit : tir")}]')
RIFLE4 = (f'{WF}[custom_data={{tv:8}},item_model="minecraft:trident",unbreakable={{}},enchantment_glint_override=true,'
          f'custom_name={nm("⚡ Lance-foudre", "yellow")},lore={lo("La foudre du Roi Tyran", "Clic droit : éclair dévastateur")}]')
SCANNER = (f'{WF}[custom_data={{tv:10}},item_model="minecraft:spyglass",unbreakable={{}},custom_name={nm("🔬 Scanner du Dr Ossei", "aqua")},'
           f'lore={lo("Clic droit en visant un dinosaure (16 blocs)", "Ajoute l\'espèce au bestiaire : +XP")}]')
WHISTLE = (f'{WF}[custom_data={{tv:11}},item_model="minecraft:goat_horn",unbreakable={{}},custom_name={nm("🦖 Sifflet de raptor", "green")},'
           f'lore={lo("Clic droit : ton raptor apprivoisé accourt", "Monte dessus et galope (Z, espace = saut)")}]')


def armor(tier):
    if tier == 0:
        return [('chest', UNIF_C), ('feet', UNIF_B)]
    if tier == 1:
        return [(s, ARM[s]) for s in ('head', 'chest', 'legs')] + [('feet', UNIF_B)]
    mat, name, col, extra = {2: ('iron', '🛡 Armure renforcée', 'white', ''),
                             3: ('diamond', '🛡 Armure d\'écailles', 'dark_aqua', ',trim={material:"minecraft:emerald",pattern:"minecraft:wild"}'),
                             4: ('netherite', '🛡 Armure du Tyran', 'dark_red', ',trim={material:"minecraft:gold",pattern:"minecraft:rib"}')}[tier]
    out = []
    for s, p in [('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings'), ('feet', 'boots')]:
        out.append((s, f'minecraft:{mat}_{p}[unbreakable={{}},custom_data={{tvarm:{tier}b}},custom_name={nm(name, col)}{extra}]'))
    return out


KIT = ['# @s : équipement selon ses paliers (mêlée, fusil, armure, scanner, sifflet)',
       f'execute if score @s mg.trml matches ..1 run item replace entity @s hotbar.0 with {PROD}',
       f'execute if score @s mg.trml matches 2 run item replace entity @s hotbar.0 with {BLADE}',
       f'execute if score @s mg.trml matches 3.. run item replace entity @s hotbar.0 with {CROC}',
       f'execute if score @s mg.trwp matches ..1 run item replace entity @s hotbar.1 with {RIFLE1}',
       f'execute if score @s mg.trwp matches 2 run item replace entity @s hotbar.1 with {RIFLE2}',
       f'execute if score @s mg.trwp matches 3 run item replace entity @s hotbar.1 with {RIFLE3}',
       f'execute if score @s mg.trwp matches 4.. run item replace entity @s hotbar.1 with {RIFLE4}',
       f'execute if score @s mg.trch matches 25.. run item replace entity @s hotbar.2 with {SCANNER}',
       f'execute if score @s mg.trmt matches 1.. run item replace entity @s hotbar.3 with {WHISTLE}', f'function mg:{P}/cl/kit', f'function mg:{P}/carnet_kit']
for t in range(5):
    KIT += [f'execute if score @s mg.trar matches {t}{".." if t == 4 else ""} run item replace entity @s armor.{s} with {it}' for s, it in armor(t)]
w(f'{P}/kit', KIT)
w(f'{P}/join', ['# @s : scores du RPG à la première visite',
                'execute unless score @s mg.trlv matches 1.. run scoreboard players set @s mg.trlv 1'] +
  [f'execute unless score @s {o} matches -2147483648.. run scoreboard players set @s {o} {v}' for o, v in [
      ('mg.trxp', 0), ('mg.trch', 0), ('mg.trqp', 0), ('mg.trbs', 0), ('mg.trpo', 0), ('mg.trtv', 1), ('mg.treg', 0), ('mg.trwp', 1),
      ('mg.trml', 1), ('mg.trar', 0), ('mg.trmt', 0), ('mg.trgr', 0), ('mg.trdn', 0), ('mg.trvn', 0), ('mg.trec', 0), ('mg.trai', 0),
      ('mg.trrx', 0), ('mg.trcl', 0), ('mg.trcd', 0), ('mg.trdg', 0), ('mg.trs1', 0), ('mg.trs2', 0), ('mg.trs3', 0), ('mg.trs4', 0),
      ('mg.trkt', 0), ('mg.trel', 0), ('mg.trac', 0), ('mg.trtc', 0), ('mg.trsq', 0), ('mg.trsa', 0), ('mg.trq4', 0)]] +
  ['# points de caractéristique : 1 par niveau gagné (rattrapage pour les colons déjà avancés)',
   'execute unless score @s mg.trsp matches -2147483648.. run function mg:terra/rpg/st/backfill'] +
  ['scoreboard players set @s mg.trrg 0', 'scoreboard players set @s mg.trpk 0', 'scoreboard players set @s mg.trsc 0',
   'scoreboard players set @s mg.trdt 0', 'scoreboard players enable @s mg.trtk', f'function mg:{P}/stats'])
w(f'{P}/enter', ['# @s arrive à Terra Nova (après le kit) : rappel de la campagne',
                 'tellraw @s ' + js([TEXT('⭐ Niveau ', 'gold'), {'score': {'name': '@s', 'objective': 'mg.trlv'}, 'color': 'yellow', 'bold': True},
                                     TEXT('   📜 Campagne : ', 'gold'), TEXT('[voir l\'objectif]', 'aqua', click_event={'action': 'run_command', 'command': '/trigger mg.trtk set 9'})]),
                 f'function mg:{P}/obj_say', f'function mg:{P}/qloc',
                 'execute if score @s mg.trcl matches 0 run tellraw @s ' + js([TEXT('🎖 Choisis ta classe auprès de la Commandante Varga (QG) : ', 'gold'), TEXT('[choisir]', 'yellow', click_event={'action': 'run_command', 'command': '/trigger mg.trtk set 600'})])])
w(f'{P}/leave', ['# @s quitte Terra Nova : bonus de vie retiré, monture renvoyée', 'attribute @s minecraft:max_health modifier remove mg:trlv',
                 f'function mg:{P}/mount_gone', 'scoreboard players set @s mg.trrg 0', f'function mg:{P}/cl/remove', f'function mg:{P}/cs/stop', f'function mg:{P}/st/remove'])

# ================================================================ régions : titres, accès par la campagne
RC = ['# Chaque seconde, @s (joueur) : région où il se trouve (0 vallée, 1 nord, 2 est, 3 ouest, 4 sud)', 'scoreboard players set $r mg.st 0']
RC += [f'execute if entity @s[{box}] run scoreboard players set $r mg.st {i}' for i, box in REG_BOX.items()]
RC += [f'execute unless score @s mg.trrg = $r mg.st run function mg:{P}/region_chg']
w(f'{P}/region', RC)
RG = ['# @s change de région ($r) : accès selon la campagne, titre de la région']
for i, ch in GATE_CH.items():
    RG.append(f'execute if score $r mg.st matches {i} unless score @s mg.trch matches {ch}.. unless entity @s[tag=mg.trfree] run return run function mg:{P}/deny_{i}')
RG.append('scoreboard players operation @s mg.trrg = $r mg.st')
RG.append('title @s times 10 50 15')
RG.append(f'execute if score $r mg.st matches 0 run title @s title {js(TEXT("VALLÉE DE LA COLONIE", "green", bold=True))}')
RG.append(f'execute if score $r mg.st matches 0 run title @s subtitle {js(TEXT("Terres des colons · niveau 1 et plus", "gray"))}')
for k, i in REG_IDX.items():
    if k == 'v':
        continue
    R = REGIONS[k]
    RG.append(f'execute if score $r mg.st matches {i} run title @s title {js(TEXT(R["name"].upper(), R["col"], bold=True))}')
    RG.append(f'execute if score $r mg.st matches {i} run title @s subtitle {js(TEXT("Niveau conseillé " + str(R["lv"]), "gray"))}')
    RG.append(f'execute if score $r mg.st matches {i} at @s run playsound minecraft:event.mob_effect.raid_omen ambient @s ~ ~ ~ 0.5 1.4')
w(f'{P}/region_chg', RG)
for i, ch in GATE_CH.items():
    gx, gy, gz = GATE_BACK[i]
    title = [t for n, (t, _, _) in CH.items() if n == ch][0]
    w(f'{P}/deny_{i}', ['# @s n\'a pas encore accès à cette région : retour au col', f'tp @s {gx} {gy} {gz}',
                        'tellraw @s ' + js([TEXT('⛔ ', 'red'), TEXT('Expédition non autorisée. ', 'red', bold=True),
                                            TEXT(f'La Commandante Varga ouvrira ce col au chapitre « {title} ».', 'gray')]),
                        'execute at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 0.8 0.6'])

# ================================================================ lieux à découvrir, balises de voyage
PO = ['# Chaque seconde : découverte des lieux (joueurs proches)']
for i, (key, name, reg, x, y, z, r, xp) in enumerate(POIS):
    PO.append(f'execute positioned {x} {y} {z} as @a[tag=mg.tvw,distance=..{r}] run function mg:{P}/poi/{key}')
    camp = [c for c in CAMPS if c[1] == key]
    L = [f'# @s découvre « {name} »'] + bit_test('mg.trpo', i) + ['execute if score $b mg.st matches 1 run return 0',
                                                                    f'scoreboard players operation @s mg.trpo += #p{i} mg.st']
    if xp:
        L += ['title @s times 10 50 15', f'title @s title {js(TEXT(name, "yellow", bold=True))}',
              f'title @s subtitle {js(TEXT("✦ Lieu découvert", "gold"))}',
              'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6', f'function mg:{P}/xp {{n:{xp}}}']
    if camp:
        n, ck, cname, cx, cy, cz = camp[0]
        L += bit_test('mg.trtv', n - 1) + [f'execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trtv += #p{n - 1} mg.st',
                                           f'execute in {DIM} run spawnpoint @s {int(cx)} {int(cy)} {int(cz)}',
                                           'tellraw @s ' + js([TEXT('🌀 Balise de voyage activée : ', 'light_purple'), TEXT(cname, 'yellow'),
                                                               TEXT(' (réapparition ici, voyage depuis n\'importe quelle balise)', 'gray')])]
    w(f'{P}/poi/{key}', L)
w(f'{P}/pois', PO)
TRAVEL = {'type': 'minecraft:multi_action', 'title': TEXT('🌀 Balises de voyage', 'light_purple', bold=True),
          'external_title': TEXT('🌀 Voyage', 'light_purple'), 'pause': False, 'can_close_with_escape': True, 'columns': 1,
          'body': [{'type': 'minecraft:plain_message', 'contents': [TEXT('Les balises activées (en t\'y rendant) te permettent d\'y voyager instantanément.\n'
                                                                         'Tu y réapparais si tu tombes au combat.', 'gray')]}],
          'actions': [{'label': [TEXT(f'🌀 {cname}', 'light_purple', bold=True)], 'tooltip': [TEXT('Voyager ici', 'gray')],
                       'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.trtk set {500 + n}'}} for n, ck, cname, *_ in CAMPS]}
w(f'{P}/travel', ['# @s : fenêtre de voyage', 'scoreboard players enable @s mg.trtk', f'dialog show @s {js(TRAVEL)}',
                  'execute at @s run playsound minecraft:block.beacon.ambient player @s ~ ~ ~ 0.6 1.5'])
for n, ck, cname, cx, cy, cz in CAMPS:
    w(f'{P}/go/{n}', [f'# @s voyage vers {cname}'] + bit_test('mg.trtv', n - 1) +
      ['execute if score $b mg.st matches 0 run return run tellraw @s ' + js(TEXT(f'🌀 Balise « {cname} » pas encore activée : va la découvrir à pied.', 'red')),
       'execute if entity @s[tag=mg.tvcar] run return run tellraw @s {"text":"📦 Impossible avec la caisse !","color":"red"}',
       f'execute in {DIM} run tp @s {cx} {cy} {cz}', f'execute in {DIM} run spawnpoint @s {int(cx)} {int(cy)} {int(cz)}',
       'execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.7 1.2',
       'execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.9 0.4 0.05 60'])

# ================================================================ dialogues des PNJ
def dlg(title, col, text, buttons, close=True):
    acts = [{'label': [TEXT(l, c, bold=True)], 'tooltip': [TEXT(t, 'gray')], 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.trtk set {v}'}}
            for (l, c, t, v) in buttons]
    if close:
        acts.append({'label': [TEXT('Au revoir', 'gray')], 'tooltip': [TEXT('Fermer', 'gray')], 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.trtk set 8'}})
    return {'type': 'minecraft:multi_action', 'title': TEXT(title, col, bold=True), 'external_title': TEXT(title, col), 'pause': False,
            'can_close_with_escape': True, 'columns': 1, 'body': [{'type': 'minecraft:plain_message', 'contents': [TEXT(text, 'white')], 'width': 300}],
            'actions': acts}


def show(d):
    """Fenêtre de dialogue, sinon texte + liens dans le chat."""
    links = [TEXT(d['title']['text'] + ' : ', d['title']['color'], bold=True), TEXT(d['body'][0]['contents'][0]['text'] + ' ', 'gray')]
    for a in d['actions']:
        links.append({'text': f'[{a["label"][0]["text"]}] ', 'color': a['label'][0]['color'], 'bold': False,
                      'click_event': {'action': 'run_command', 'command': '/' + a['action']['command']}})
    return ['scoreboard players enable @s mg.trtk', 'scoreboard players set $dlg mg.st 0',
            f'execute store success score $dlg mg.st run dialog show @s {js(d)}', 'execute unless score $dlg mg.st matches 1 run tellraw @s ' + js(links)]


def remind():
    return f'function mg:{P}/obj_say'


VT = '⚔ Commandante Varga'
NPC_FN = {}
NPC_FN['varga'] = [
    (0, dlg(VT, 'gold', 'Bienvenue à Terra Nova, colon. Nous sommes une poignée d\'humains, 85 millions d\'années dans le passé, '
                        'et la jungle ne pardonne pas. Avant de t\'envoyer plus loin, prouve ta valeur : abats 3 slashers dans la vallée.',
            [('Je m\'en charge', 'green', 'Chapitre I : Premiers pas', 101)])),
    (15, dlg(VT, 'gold', 'Trois slashers en moins : beau travail. Le Dr Ossei a besoin de quelqu\'un de solide pour ses recherches. Va le voir au labo.',
             [('Récompense : 150 XP, 100 ₵', 'green', 'Fin du chapitre I', 102)])),
    (45, dlg(VT, 'gold', 'La reine du marais est tombée ? Incroyable. La route de l\'est est sûre maintenant : Camp Delta ne répond plus '
                         'depuis des jours. Rejoins-les par le col est.', [('Récompense : 500 XP, 300 ₵', 'green', 'Fin du chapitre IV', 103)])),
    (66, dlg(VT, 'gold', 'La cellule ! Les Renégats ne nous priveront plus d\'énergie. Le Dr Ossei veut l\'analyser : '
                         'elle a réagi à quelque chose au sud, du côté du volcan.', [('Récompense : 700 XP, 500 ₵', 'green', 'Fin du chapitre VI', 104)])),
    (90, dlg(VT, 'gold', 'Le Roi Tyran est mort et la faille s\'est refermée. Le portail du temps est stable : Terra Nova survivra. '
                         'Au nom de toute la colonie, merci, héros.', [('Recevoir les honneurs : 1500 XP, 1000 ₵', 'gold', 'Fin de la campagne', 105)])),
    (100, dlg(VT, 'gold', 'Héros de Terra Nova. Le tableau des contrats t\'attend, et on raconte que le Roi Tyran et la reine du marais '
                          'ont des héritiers…', [('📋 Contrats de la colonie', 'yellow', 'Missions répétables', 110)])),
]
OT = '🔬 Dr Ossei'
NPC_FN['ossei'] = [
    (20, dlg(OT, 'aqua', 'Ah, la Commandante t\'envoie ! Prends ce scanner : vise un dinosaure et clic droit. Chaque nouvelle espèce '
                         'enrichit notre bestiaire. Scanne-m\'en deux, pour commencer.', [('Prendre le scanner', 'green', 'Chapitre II : Le scanner', 201)])),
    (28, dlg(OT, 'aqua', 'Superbe ! Mais j\'ai un problème : notre drone de recherche s\'est écrasé dans le marais, au nord. '
                         'Ses modules de données sont précieux. La Commandante ouvre le col nord pour toi.',
             [('Récompense : 150 XP — en route !', 'green', 'Chapitre III : Le signal du marais', 202)])),
    (35, dlg(OT, 'aqua', 'Les modules… regarde ces relevés : une énorme créature vit dans la lagune. Un spinosaure ! '
                         'Elle attaque tout ce qui approche de l\'Antre. Il faut l\'arrêter.', [('Récompense : 300 XP, 200 ₵', 'green', 'Chapitre IV : La reine du marais', 203)])),
    (70, dlg(OT, 'aqua', 'Cette cellule a capté une signature temporelle… au cœur du Mont Cendre. Une faille ! Si elle s\'élargit, '
                         'le portail de la colonie s\'effondre. Et quelque chose de gigantesque garde le cratère.',
             [('J\'y vais', 'red', 'Chapitre VII : La faille', 204)])),
]
NPC_FN['nyla'] = [
    (52, dlg('🏹 Nyla, éclaireuse', 'green', 'Un colon ! Enfin. Avant tout : j\'étudie les grands herbivores des plaines. Scanne pour moi un tricératops, '
                                            'un stégosaure et un ankylosaure. Approche doucement : ils chargent si on les provoque.',
             [('Accepter', 'green', 'Scanner trois herbivores', 401)])),
    (58, dlg('🏹 Nyla, éclaireuse', 'green', 'Merci. Mais il y a pire : cette nuit, des Renégats ont volé la cellule d\'énergie du camp. '
                                            'Leur fort est au fond du canyon, à l\'ouest. Je préviens la Commandante : le col ouest est ouvert.',
             [('Récompense : 400 XP', 'green', 'Chapitre VI : Le vol de la cellule', 402)])),
]
for npc, lst in NPC_FN.items():
    L = [f'# @s parle à {npc} : dialogue selon l\'étape de la campagne']
    for n, d in lst:
        w(f'{P}/d/{npc}_{n}', [f'# {npc}, étape {n}'] + show(d))
        L.append(f'execute if score @s mg.trch matches {n} run return run function mg:{P}/d/{npc}_{n}')
    if npc == 'ossei':
        L.append(f'return run function mg:{P}/d/ossei_gen')
    elif npc == 'nyla':
        L.append(f'return run function mg:{P}/d/nyla_gen')
    else:
        L.append(f'return run function mg:{P}/d/{npc}_gen')
    w(f'{P}/npc_{npc}', L)
w(f'{P}/d/varga_gen', show(dlg(VT, 'gold', 'Tu as tes ordres, colon. Le 📡 localisateur t\'indique où aller.',
                               [('🎖 Ma classe', 'gold', 'Soldat, Éclaireur, Scientifique, Ingénieur', 600),
                                ('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9), ('📋 Contrats de la colonie', 'yellow', 'Missions répétables', 110)])))
w(f'{P}/d/ossei_gen', show(dlg(OT, 'aqua', 'La science n\'attend pas ! Rapporte-moi des espèces inconnues… et si tu croises des œufs d\'ambre, '
                                          'ils m\'intéressent beaucoup : six ont été perdus dans la vallée et les régions.',
                               [('📖 Bestiaire', 'aqua', 'Espèces scannées', 210), ('🥚 Les œufs d\'ambre', 'gold', 'Quête : 6 œufs à retrouver', 211),
                                ('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)])))
w(f'{P}/d/nyla_gen', show(dlg('🏹 Nyla, éclaireuse', 'green', 'Les plaines sont belles mais dangereuses : méfie-toi des ptéranodons près des Aiguilles.',
                              [('📜 Rappel de l\'objectif', 'yellow', 'Objectif en cours', 9)])))

# ---------------------------------------------------------------- forge de Jo
RECIPES = [  # (n°, nom, coût, condition, effet, description)
    (301, '🗡 Lame d\'ambre', [('mg.trgr', 8, 'griffes')], 150, 'mg.trml', 2, 'Mêlée 8 + étourdissement (remplace le bâton électrique)'),
    (302, '🔫 Fusil à plasma Mk3', [('mg.trvn', 6, 'glandes à venin'), ('mg.trec', 2, 'écailles de spinosaure')], 350, 'mg.trwp', 3,
     'Tir perforant, peu de surchauffe (il faut le Mk2 du dépôt)'),
    (303, '🛡 Armure renforcée', [('mg.trgr', 10, 'griffes'), ('mg.trdn', 2, 'dents de carnotaure')], 250, 'mg.trar', 2, 'Armure en fer complète'),
    (304, '🛡 Armure d\'écailles', [('mg.trec', 3, 'écailles de spinosaure'), ('mg.trai', 4, 'ailes de ptéranodon')], 400, 'mg.trar', 3, 'Armure en diamant'),
    (305, '⚡ Lance-foudre', [('mg.trrx', 1, 'croc du Roi')], 600, 'mg.trwp', 4, 'L\'arme ultime (il faut le Mk3)'),
    (306, '🛡 Armure du Tyran', [('mg.trrx', 1, 'croc du Roi'), ('mg.trdn', 4, 'dents de carnotaure')], 800, 'mg.trar', 4, 'Armure en netherite'),
    (307, '🦷 Croc du Tyran', [('mg.trrx', 1, 'croc du Roi')], 300, 'mg.trml', 3, 'Mêlée 13 + étourdissement'),
]
FORGE_D = dlg('⚒ Jo, forgeronne', 'red', 'Apporte-moi des trophées de chasse et des crédits, je te forge du solide. Tes trophées sont listés dans le chat.',
              [(r[1], 'gold', f'{" + ".join(f"{q} {lab}" for _, q, lab in r[2])} + {r[3]} ₵ : {r[6]}', r[0]) for r in RECIPES])
TROPHY_LINE = [TEXT('⚒ Tes trophées : ', 'red', bold=True)]
for o, lab in [('mg.trgr', 'griffes'), ('mg.trdn', 'dents'), ('mg.trvn', 'glandes'), ('mg.trec', 'écailles'), ('mg.trai', 'ailes'), ('mg.trrx', 'crocs du Roi')]:
    TROPHY_LINE += [{'score': {'name': '@s', 'objective': o}, 'color': 'yellow'}, TEXT(f' {lab}  ', 'gray')]
TROPHY_LINE += [{'score': {'name': '@s', 'objective': 'mg.tvc'}, 'color': 'green'}, TEXT(' ₵', 'green')]
w(f'{P}/npc_jo', ['# @s parle à Jo (forge)', 'tellraw @s ' + js(TROPHY_LINE)] + show(FORGE_D))
for (n, name, cost, cred, sc, tier, desc) in RECIPES:
    L = [f'# @s demande « {name} » à la forge',
         f'execute if score @s {sc} matches {tier}.. run return run tellraw @s ' + js(TEXT('⚒ « Tu as déjà ça, ou mieux ! »', 'yellow'))]
    if n == 302:
        L.append('execute unless score @s mg.trwp matches 2.. run return run tellraw @s ' + js(TEXT('⚒ « Il me faut ton fusil Mk2 comme base : achète-le au dépôt. »', 'red')))
    if n == 305:
        L.append('execute unless score @s mg.trwp matches 3.. run return run tellraw @s ' + js(TEXT('⚒ « Il me faut ton fusil à plasma Mk3 comme base. »', 'red')))
    for o, q, lab in cost:
        L.append(f'execute unless score @s {o} matches {q}.. run return run tellraw @s ' + js(TEXT(f'⚒ « Il me manque des {lab} : il en faut {q}. »', 'red')))
    L.append(f'execute unless score @s mg.tvc matches {cred}.. run return run tellraw @s ' + js(TEXT(f'⚒ « Ça coûte {cred} ₵ : reviens avec les crédits. »', 'red')))
    L += [f'scoreboard players remove @s {o} {q}' for o, q, _ in cost] + [f'scoreboard players remove @s mg.tvc {cred}', f'scoreboard players set @s {sc} {tier}',
                                                                         f'function mg:{P}/kit', 'title @s times 5 50 15',
                                                                         f'title @s title {js(TEXT(name, "gold", bold=True))}',
                                                                         f'title @s subtitle {js(TEXT("forgé par Jo", "gray"))}',
                                                                         'execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1',
                                                                         'execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12']
    w(f'{P}/craft_{n}', L)

# ---------------------------------------------------------------- choix (trigger mg.trtk) : chaque action revérifie l'étape
TK = ['# @s : choix dans un dialogue (trigger mg.trtk)', 'scoreboard players operation $tk mg.st = @s mg.trtk',
      'scoreboard players reset @s mg.trtk', 'scoreboard players enable @s mg.trtk',
      f'execute if score $tk mg.st matches 9 run function mg:{P}/quest',
      'execute if score $tk mg.st matches 110 run function mg:terra/board',
      f'execute if score $tk mg.st matches 101 if score @s mg.trch matches 0 run {chfn(10)}',
      f'execute if score $tk mg.st matches 102 if score @s mg.trch matches 15 run function mg:{P}/rw {{xp:150,c:100,n:20}}',
      f'execute if score $tk mg.st matches 103 if score @s mg.trch matches 45 run function mg:{P}/rw {{xp:500,c:300,n:50}}',
      f'execute if score $tk mg.st matches 104 if score @s mg.trch matches 66 run function mg:{P}/rw {{xp:700,c:500,n:70}}',
      f'execute if score $tk mg.st matches 105 if score @s mg.trch matches 90 run function mg:{P}/finale',
      f'execute if score $tk mg.st matches 201 if score @s mg.trch matches 20 run function mg:{P}/give_scanner',
      f'execute if score $tk mg.st matches 202 if score @s mg.trch matches 28 run function mg:{P}/rw {{xp:150,c:0,n:30}}',
      f'execute if score $tk mg.st matches 203 if score @s mg.trch matches 35 run function mg:{P}/rw {{xp:300,c:200,n:40}}',
      f'execute if score $tk mg.st matches 204 if score @s mg.trch matches 70 run {chfn(72)}',
      f'execute if score $tk mg.st matches 210 run function mg:{P}/bestiary', f'execute if score $tk mg.st matches 600 run function mg:{P}/cl/menu',
      f'execute if score $tk mg.st matches 601..604 run function mg:{P}/cl/pick_tk',
      f'execute if score $tk mg.st matches 211 run function mg:{P}/eggs',
      f'execute if score $tk mg.st matches 401 if score @s mg.trch matches 52 run {chfn(55)}',
      f'execute if score $tk mg.st matches 402 if score @s mg.trch matches 58 run function mg:{P}/rw {{xp:400,c:0,n:60}}']
TK += [f'execute if score $tk mg.st matches {r[0]} run function mg:{P}/craft_{r[0]}' for r in RECIPES]
TK += [f'execute if score $tk mg.st matches {500 + n} run function mg:{P}/go/{n}' for n, *_ in CAMPS]
TK += [f'function mg:{P}/tk2']
w(f'{P}/tk', TK)
w(f'{P}/rw', ['# @s : récompense d\'étape (macro xp, c crédits, n étape suivante)', '$scoreboard players add @s mg.tvc $(c)',
              '$tellraw @s [{"text":"  +$(c) ₵","color":"green"}]', '$function mg:terra/rpg/xp {n:$(xp)}', '$function mg:terra/rpg/ch {n:$(n)}',
              'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1'])
w(f'{P}/give_scanner', ['# Le Dr Ossei donne le scanner', f'item replace entity @s hotbar.2 with {SCANNER}', chfn(25),
                        'tellraw @s ' + js(TEXT('🔬 Scanner reçu (case 3) : vise un dinosaure à moins de 16 blocs et fais clic droit.', 'aqua'))])
w(f'{P}/finale', ['# Fin de la campagne : honneurs, titre de héros, générique', 'scoreboard players add @s mg.tvc 1000', f'function mg:{P}/xp {{n:1500}}',
                  chfn(100), f'function mg:{P}/cs/finale', 'title @s times 20 100 30', 'title @s title {"text":"HÉROS DE TERRA NOVA","color":"gold","bold":true}',
                  'title @s subtitle {"text":"La colonie te doit sa survie","color":"yellow"}',
                  'tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a terminé la campagne de Terra Nova !","color":"gold"}]',
                  'execute at @s run playsound minecraft:ui.toast.challenge_complete player @a ~ ~ ~ 1 0.8',
                  'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_trail:true}]}}}}',
                  'tellraw @s ' + js([TEXT('\n— Terra Nova —\n', 'green', bold=True), TEXT('Une campagne NeoMC. Merci d\'avoir joué !\n', 'gray'),
                                      TEXT('Le bestiaire, les œufs d\'ambre et les boss t\'attendent toujours.', 'aqua')])])

# ---------------------------------------------------------------- bestiaire, scanner
BL = ['# @s : liste du bestiaire dans le chat', 'tellraw @s ' + js(TEXT('\n📖 Bestiaire du Dr Ossei', 'aqua', bold=True))]
for i, k in enumerate(SPECIES_ORDER):
    name, desc, troph = BEST[k]
    BL += bit_test('mg.trbs', i)
    BL.append('execute if score $b mg.st matches 1 run tellraw @s ' + js([TEXT(' ✔ ', 'green'), TEXT(name, 'yellow', bold=True), TEXT(' — ' + desc, 'gray')]))
    BL.append('execute if score $b mg.st matches 0 run tellraw @s ' + js([TEXT(' ✖ ', 'dark_gray'), TEXT('??? (espèce inconnue)', 'dark_gray')]))
w(f'{P}/bestiary', BL)
SC = ['# @s : scanner (clic droit) : rayon de 16 blocs vers un dinosaure',
      'execute if score @s mg.trsc matches 1.. run return 0', 'scoreboard players set @s mg.trsc 10', 'scoreboard players set $tvr mg.st 0',
      'tag @s add mg.trsh', 'scoreboard players set $tvsp mg.st -1',
      'execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/rpg/scan_ray', 'tag @s remove mg.trsh',
      'execute if score $tvsp mg.st matches -1 run return run title @s actionbar {"text":"🔬 Aucun dinosaure visé","color":"gray"}',
      'execute at @s run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.5 2']
for i, k in enumerate(SPECIES_ORDER):
    SC.append(f'execute if score $tvsp mg.st matches {i} run function mg:{P}/scan/{k}')
w(f'{P}/scan', SC)
w(f'{P}/scan_ray', ['# Un pas (0,5 bloc) du scanner', 'particle minecraft:dust{color:[0.3,0.9,1.0],scale:0.5} ~ ~ ~ 0 0 0 0 1', 'scoreboard players add $tvr mg.st 1',
                    'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvd,tag=!mg.trmount,dx=0,dy=0,dz=0,limit=1] run return run function mg:terra/rpg/scan_id',
                    'execute unless block ~ ~ ~ #mg:tv_pass run return 0', 'execute if score $tvr mg.st matches ..32 positioned ^ ^ ^0.5 run function mg:terra/rpg/scan_ray'])
w(f'{P}/scan_id', ['# @s (dinosaure visé) : espèce -> $tvsp'] + [f'execute if entity @s[tag={TAGS[k]}] run scoreboard players set $tvsp mg.st {i}'
                                                                  for i, k in enumerate(SPECIES_ORDER)] +
  ['execute at @s run particle minecraft:glow ~ ~1 ~ 0.4 0.6 0.4 0 12'])
for i, k in enumerate(SPECIES_ORDER):
    name, desc, troph = BEST[k]
    L = [f'# @s scanne : {name}'] + bit_test('mg.trbs', i) + [
        'execute if score $b mg.st matches 1 run return run title @s actionbar ' + js([TEXT('🔬 ' + name, 'aqua'), TEXT(' : déjà au bestiaire', 'gray')]),
        'scoreboard players set @s mg.tval 60', f'scoreboard players operation @s mg.trbs += #p{i} mg.st',
        'title @s actionbar ' + js([TEXT('🔬 Nouvelle espèce : ', 'aqua', bold=True), TEXT(name, 'yellow', bold=True)]),
        'tellraw @s ' + js([TEXT('📖 ', 'aqua'), TEXT(name, 'yellow', bold=True), TEXT(' — ' + desc, 'gray')]),
        'execute at @s run playsound minecraft:entity.villager.work_cartographer player @s ~ ~ ~ 0.8 1.4',
        f'function mg:{P}/xp {{n:40}}', f'execute if score @s mg.trcl matches 3 run function mg:{P}/xp {{n:20}}',
        'execute if score @s mg.trch matches 25 run scoreboard players add @s mg.trqp 1',
        f'execute if score @s mg.trch matches 25 if score @s mg.trqp matches 2.. run {chfn(28)}']
    if k in ('trike', 'stego', 'ankylo'):
        idx = [SPECIES_ORDER.index(x) for x in ('trike', 'stego', 'ankylo')]
        L += [f'execute if score @s mg.trch matches 55 run function mg:{P}/herd_chk']
    if i == 0:
        pass
    L.append(f'execute if score @s mg.trbs matches {2 ** len(SPECIES_ORDER) - 1} run function mg:{P}/best_done')
    w(f'{P}/scan/{k}', L)
HC = ['# @s (étape 55) : a-t-il scanné tricératops, stégosaure et ankylosaure ?', 'scoreboard players set $hc mg.st 0']
for k in ('trike', 'stego', 'ankylo'):
    HC += bit_test('mg.trbs', SPECIES_ORDER.index(k)) + ['scoreboard players operation $hc mg.st += $b mg.st']
HC.append(f'execute if score $hc mg.st matches 3 run {chfn(58)}')
w(f'{P}/herd_chk', HC)
w(f'{P}/best_done', ['# @s a complété le bestiaire', 'title @s title {"text":"📖 BESTIAIRE COMPLET","color":"aqua","bold":true}',
                     'scoreboard players add @s mg.tvc 500', f'function mg:{P}/xp {{n:600}}',
                     'tellraw @a[tag=mg.tvw] [{"text":"📖 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" a complété le bestiaire de Terra Nova ! (+500 ₵)","color":"aqua"}]'])

# ---------------------------------------------------------------- œufs d'ambre et monture
w(f'{P}/eggs', ['# @s : quête des œufs d\'ambre (Dr Ossei)'] + [
    'scoreboard players set $n mg.st 0'] + sum([bit_test('mg.treg', i) + ['scoreboard players operation $n mg.st += $b mg.st'] for i in range(len(EGGS))], []) + [
    'tag @s add mg.tregq',
    'execute if score @s mg.trmt matches 1.. run return run tellraw @s ' + js(TEXT('🔬 « Ton raptor grandit bien, à ce que je vois ! »', 'aqua')),
    f'execute if score $n mg.st matches {len(EGGS)}.. run return run function mg:{P}/egg_reward',
    'tellraw @s [{"text":"🥚 Œufs d\'ambre : ","color":"gold"},{"score":{"name":"$n","objective":"mg.st"},"color":"yellow","bold":true},'
    f'{{"text":" / {len(EGGS)}. Ils brillent (accroupi à côté pour le ramasser) : deux dans la vallée, un par région.","color":"gray"}}]'])
w(f'{P}/egg_reward', ['# @s a rapporté les 6 œufs : un raptor apprivoisé', 'scoreboard players set @s mg.trmt 1', f'function mg:{P}/xp {{n:500}}',
                      f'item replace entity @s hotbar.3 with {WHISTLE}', 'title @s title {"text":"🦖 RAPTOR APPRIVOISÉ","color":"green","bold":true}',
                      'title @s subtitle {"text":"Sifflet en case 4 : clic droit pour l\'appeler","color":"gray"}',
                      'execute at @s run playsound minecraft:entity.fox.screech player @s ~ ~ ~ 1 1.4'])
EG = ['# Tous les 5 ticks : ramassage des œufs d\'ambre (quête acceptée, accroupi à 2 blocs)']
for i, (x, y, z) in enumerate(EGGS):
    EG.append(f'execute positioned {x + 0.5} {y} {z + 0.5} as @a[tag=mg.tregq,distance=..2.2] if predicate mg:sneak run function mg:{P}/egg/{i}')
    w(f'{P}/egg/{i}', [f'# @s ramasse l\'œuf d\'ambre {i + 1}'] + bit_test('mg.treg', i) + ['execute if score $b mg.st matches 1 run return 0',
                                                                                   f'scoreboard players operation @s mg.treg += #p{i} mg.st',
                                                                                   f'function mg:{P}/xp {{n:60}}',
                                                                                   'title @s actionbar {"text":"🥚 Œuf d\'ambre ramassé ! Rapporte-les au Dr Ossei","color":"gold","bold":true}',
                                                                                   'scoreboard players set @s mg.tval 60',
                                                                                   'execute at @s run playsound minecraft:entity.chicken.egg player @s ~ ~ ~ 1 0.6'])
w(f'{P}/eggs_tick', EG)
w(f'{P}/whistle', ['# @s : sifflet : son raptor apparaît à côté de lui (l\'ancien est renvoyé) et il monte dessus',
                   'execute if score @s mg.trmt matches ..0 run return 0', 'execute if score @s mg.trsc matches 1.. run return 0', 'scoreboard players set @s mg.trsc 40',
                   f'function mg:{P}/mount_gone', 'tag @e[tag=mg.tvlast] remove mg.tvlast', 'scoreboard players add $tvid mg.st 1',
                   'summon minecraft:horse ~ ~ ~ {Tags:["mg.tv","mg.tvd","mg.tvn","mg.tvlast","mg.trmount","mg.tvs_raptor"],Tame:1b,PersistenceRequired:1b,Silent:1b,'
                   'SaddleItem:{id:"minecraft:saddle",count:1},equipment:{saddle:{id:"minecraft:saddle",count:1}},'
                   + INVIS + ',attributes:[{id:"minecraft:movement_speed",base:0.34},{id:"minecraft:jump_strength",base:0.95},{id:"minecraft:max_health",base:40},'
                   '{id:"minecraft:step_height",base:1.6},{id:"minecraft:safe_fall_distance",base:12}]}',
                   'data modify entity @e[tag=mg.tvlast,limit=1] Owner set from entity @s UUID',
                   'execute if score $rp mg.st matches 1 run function mg:terra/dino/raptor_rp',
                   'execute unless score $rp mg.st matches 1 run function mg:terra/dino/raptor_bd',
                   'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st', 'scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st',
                   'scoreboard players operation @e[tag=mg.tvlast] mg.tvo = @s mg.tvpid', 'scoreboard players set @e[tag=mg.tvlast] mg.tvph 0', 'tag @e[tag=mg.tvn] remove mg.tvn',
                   'ride @s mount @e[tag=mg.tvlast,limit=1]', 'execute at @s run playsound minecraft:entity.fox.screech player @a ~ ~ ~ 1 1.3'])
w(f'{P}/mount_gone', ['# @s : sa monture disparaît', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                      'execute as @e[tag=mg.trmount] if score @s mg.tvo = $own mg.st at @s run tp @s ~ -400 ~'])

# ================================================================ modules de données (étape 32) et cellule (étape 64)
MT = ['# Tous les 5 ticks, @s (accroupi, étape 32 ou 64) : ramassage d\'un module / de la cellule (2 s)', 'scoreboard players set $k mg.st 0',
      'execute if score @s mg.trch matches 32 as @e[type=minecraft:marker,tag=mg.trmod,distance=..2.2] run scoreboard players operation $k mg.st = @s mg.trnid',
      'execute if score @s mg.trch matches 64 if entity @e[type=minecraft:marker,tag=mg.trcell,distance=..2.5] run scoreboard players set $k mg.st 9',
      'execute if score $k mg.st matches 0 run return run scoreboard players set @s mg.trpk 0']
for k in range(1, 4):
    MT += [f'execute if score $k mg.st matches {k} run scoreboard players set $kb mg.st {2 ** (k - 1)}']
MT += ['scoreboard players operation $b mg.st = @s mg.trqp', 'execute if score $k mg.st matches 1..3 run scoreboard players operation $b mg.st /= $kb mg.st',
       'execute if score $k mg.st matches 1..3 run scoreboard players operation $b mg.st %= #2 mg.st',
       'execute if score $k mg.st matches 1..3 if score $b mg.st matches 1 run return run title @s actionbar {"text":"💾 Module déjà récupéré","color":"gray"}',
       'scoreboard players add @s mg.trpk 1', 'scoreboard players set @s mg.tval 10']
for i in range(1, 9):
    MT.append(f'execute if score @s mg.trpk matches {i} run title @s actionbar [{{"text":"💾 Récupération ","color":"aqua"}},{{"text":"{"▮" * i}","color":"green"}},{{"text":"{"▮" * (8 - i)}","color":"dark_gray"}}]')
MT += [f'execute if score @s mg.trpk matches 8.. if score $k mg.st matches 1..3 run function mg:{P}/mod_got',
       f'execute if score @s mg.trpk matches 8.. if score $k mg.st matches 9 run function mg:{P}/cell_got']
w(f'{P}/mod_try', MT)
w(f'{P}/mod_got', ['# @s récupère le module $k : embuscade dans le marais', 'scoreboard players set @s mg.trpk 0',
                   'scoreboard players operation @s mg.trqp += $kb mg.st', f'function mg:{P}/xp {{n:50}}',
                   'title @s actionbar {"text":"💾 Module récupéré !","color":"aqua","bold":true}',
                   'execute at @s run playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.7 1.6',
                   'tellraw @s {"text":"⚠ Le signal du module attire des dilophosaures !","color":"red"}',
                   'execute at @s positioned ~6 ~ ~6 run function mg:terra/dino/dilo', 'tag @e[tag=mg.tvlast] add mg.trr',
                   'execute at @s positioned ~-6 ~ ~-4 run function mg:terra/dino/compy', 'tag @e[tag=mg.tvlast] add mg.trr',
                   'execute at @s positioned ~-6 ~ ~-5 run function mg:terra/dino/compy', 'tag @e[tag=mg.tvlast] add mg.trr',
                   f'execute if score @s mg.trqp matches 7.. run {chfn(35)}'])
w(f'{P}/cell_got', ['# @s récupère la cellule d\'énergie', 'scoreboard players set @s mg.trpk 0', f'function mg:{P}/xp {{n:150}}', chfn(66),
                    'title @s title {"text":"🔋 Cellule récupérée","color":"aqua","bold":true}',
                    'execute at @s run playsound minecraft:block.respawn_anchor.charge player @a ~ ~ ~ 1 1'])

# ================================================================ apparitions par région (population), capacités
CAPS = {'n': {'dilo': (6, 1), 'compy': (12, 4), 'raptor': (3, 2)},
        'e': {'trike': (5, 2), 'stego': (4, 1), 'ankylo': (3, 1), 'galli': (9, 3), 'brachio': (2, 1), 'ptera': (3, 1), 'raptor': (3, 2)},
        'w': {'raptor': (6, 2), 'ptera': (4, 1), 'dilo': (2, 1), 'sixer': (8, 2)},
        's': {'carno': (2, 1), 'ankylo': (3, 1), 'raptor': (6, 3), 'compy': (8, 4)}}
for k, caps in CAPS.items():
    L = [f'# Région {REGIONS[k]["name"]} (un joueur y est) : complète la population près des joueurs']
    for sp, (cap, grp) in caps.items():
        tag = 'mg.trsix' if sp == 'sixer' else f'mg.tvs_{sp}'
        L += [f'execute store result score $n mg.st if entity @e[tag={tag},tag=mg.trr_{k}]',
              f'execute if score $n mg.st matches ..{cap - 1} run function mg:{P}/sp/{k}_{sp}']
        w(f'{P}/sp/{k}_{sp}', [f'# Un groupe de {sp} sur un point de la région {k} (joueur entre 24 et 72 blocs, aucun à moins de 20)',
                               'tag @e[tag=mg.trok] remove mg.trok',
                               f'execute as @e[type=minecraft:marker,tag=mg.trsp_{k},tag=mg.trsp_{sp}] at @s '
                               f'if entity @a[tag=mg.tvw,distance=24..72] unless entity @a[tag=mg.tvw,distance=..20] run tag @s add mg.trok',
                               f'execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:{P}/sp/{k}_{sp}_at', 'tag @e[tag=mg.trok] remove mg.trok'])
        fn = 'function mg:terra/rpg/sixer' if sp == 'sixer' else f'function mg:terra/dino/{sp}'
        AT = []
        for g in range(grp):
            AT += [f'execute positioned ~{g % 2 * 2} ~ ~{g // 2 * 2} run {fn}', 'tag @e[tag=mg.tvlast] add mg.trnew']
        AT += [f'tag @e[tag=mg.trnew] add mg.trr_{k}', 'tag @e[tag=mg.trnew] add mg.trr']
        if sp in ('raptor', 'compy', 'carno'):
            AT.append('execute as @e[tag=mg.trnew] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..50]')
        AT.append(f'function mg:{P}/zone/{k}')
        AT.append('tag @e[tag=mg.trnew] remove mg.trnew')
        w(f'{P}/sp/{k}_{sp}_at', AT)
    w(f'{P}/pop_{k}', L)
w(f'{P}/sixer', ['# Renégat (humain hostile, arbalète)', 'tag @e[tag=mg.tvlast] remove mg.tvlast',
                 'summon minecraft:pillager ~ ~ ~ {Tags:["mg.tv","mg.tvhos","mg.tvtg","mg.trsix","mg.tvlast"],PersistenceRequired:1b,CanJoinRaid:0b,PatrolLeader:0b,'
                 'DeathLootTable:"minecraft:empty",CustomName:{"text":"Renégat","color":"red"},'
                 'equipment:{mainhand:{id:"minecraft:crossbow",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":10040115}},'
                 'head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":3355443}}},drop_chances:{mainhand:0f,chest:0f,head:0f},'
                 'attributes:[{id:"minecraft:max_health",base:24},{id:"minecraft:follow_range",base:32}],Health:24f}'])
AB = ['# Chaque seconde : capacités des dinosaures (bond, crachat, charge, coup de queue, fuite)',
      'execute as @e[tag=mg.tvraptor,tag=!mg.tvnetted,tag=!mg.trmount] at @s if entity @a[tag=mg.tvw,tag=mg.tvout,gamemode=adventure,distance=3..7] if predicate mg:tv_c33 run function mg:terra/rpg/ab/pounce',
      'execute as @e[tag=mg.tvdilo,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=4..14] if predicate mg:tv_c50 run function mg:terra/rpg/ab/spit',
      'execute as @e[tag=mg.tvcarno,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=6..18] if predicate mg:tv_c20 run function mg:terra/rpg/ab/charge',
      'execute as @e[tag=mg.tvdef,tag=!mg.tvnetted] at @s if entity @a[tag=mg.tvw,gamemode=adventure,distance=..4.5] if predicate mg:tv_c50 run function mg:terra/rpg/ab/swipe',
      'execute as @e[tag=mg.tvgalli] at @s if entity @a[tag=mg.tvw,distance=..7] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw]']
w(f'{P}/abilities', AB)
w(f'{P}/ab/pounce', ['# @s (slasher) bondit sur le colon le plus proche', 'scoreboard players set @s mg.tvat 8',
                     'execute facing entity @p[tag=mg.tvw,gamemode=adventure] feet rotated ~ -16 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.0}',
                     'function mg:terra/push', 'playsound minecraft:entity.fox.screech hostile @a ~ ~ ~ 1 1.3'])
w(f'{P}/ab/spit', ['# @s (dilophosaure) : collerette déployée, crachat de venin', 'scoreboard players set @s mg.tvat 12', 'tag @s add mg.trsrc',
                   'scoreboard players set $tvr mg.st 0', 'playsound minecraft:entity.llama.spit hostile @a ~ ~ ~ 1.5 0.6',
                   'execute anchored eyes facing entity @p[tag=mg.tvw,gamemode=adventure,distance=..14] eyes positioned ^ ^ ^1 run function mg:terra/rpg/ab/spit_ray',
                   'tag @s remove mg.trsrc'])
w(f'{P}/ab/spit_ray', ['particle minecraft:dust{color:[0.55,0.95,0.2],scale:1.1} ~ ~ ~ 0.05 0.05 0.05 0 2', 'scoreboard players add $tvr mg.st 1',
                       'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..1.0] run return run function mg:terra/rpg/ab/spit_hit',
                       'execute unless block ~ ~ ~ #mg:tv_pass run return 0', 'execute if score $tvr mg.st matches ..22 positioned ^ ^ ^0.7 run function mg:terra/rpg/ab/spit_ray'])
w(f'{P}/ab/spit_hit', ['# @s (joueur) touché par le venin', 'effect give @s minecraft:poison 4 0', 'effect give @s minecraft:blindness 3 0 true',
                       'damage @s 2 minecraft:mob_attack by @e[tag=mg.trsrc,limit=1]', 'particle minecraft:item_slime ~ ~1.5 ~ 0.3 0.3 0.3 0 12',
                       'title @s actionbar {"text":"🟢 Venin de dilophosaure !","color":"green","bold":true}', 'scoreboard players set @s mg.tval 30'])
w(f'{P}/ab/charge', ['# @s (carnotaure) : rugit et charge', 'scoreboard players set @s mg.tvat 12', 'tag @s add mg.tvroar',
                     'effect give @s minecraft:speed 3 2 true', 'playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.7',
                     'damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..20]'])
w(f'{P}/ab/swipe', ['# @s (herbivore défensif) : coup de queue / de cornes sur la cible qui le provoque', 'tag @a remove mg.trtg',
                    'execute on target if entity @s[tag=mg.tvw] run tag @s add mg.trtg',
                    'execute unless entity @a[tag=mg.trtg,distance=..4.5] run return 0', 'scoreboard players set @s mg.tvat 10',
                    'damage @p[tag=mg.trtg] 6 minecraft:mob_attack by @s', 'playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 1 0.6',
                    'particle minecraft:sweep_attack ~ ~1 ~ 1 0.4 1 0 4', 'tag @a remove mg.trtg'])

# ================================================================ boss : Spinosaure (lagune), lieutenant Varek (fort), Roi Tyran (caldeira)
lx, ly, lz = LAG_C
LAG_PTS = [(round(lx + 14 * _m.cos(_m.radians(a))), round(lz + 14 * _m.sin(_m.radians(a)))) for a in range(0, 360, 45)]
w(f'{P}/boss/spino_start', ['# La reine du marais surgit de la lagune', f'execute positioned {lx + 0.5} {ly} {lz + 0.5} run function mg:terra/dino/spino',
                            'tag @e[tag=mg.tvlast] add mg.trboss', 'scoreboard players set $trspa mg.st 1', 'scoreboard players set $trs1 mg.st 6',
                            'scoreboard players set $trs2 mg.st 14', 'scoreboard players set $trs3 mg.st 18', 'scoreboard players set $trsr mg.st 0',
                            'bossbar set mg:trspino max 650', 'bossbar set mg:trspino value 650',
                            f'execute positioned {lx} {ly} {lz} as @a[tag=mg.tvw,gamemode=adventure,distance=..60] run function mg:{P}/cs/boss_spino',
                            'execute as @e[tag=mg.tvspino] run data merge entity @s {NoAI:1b}', 'scoreboard players set @e[tag=mg.tvspino] mg.tvat 120',
                            'tag @e[tag=mg.tvspino] add mg.tvroar', f'schedule function mg:{P}/boss/wake 120t',
                            f'particle minecraft:splash {lx} {ly + 1} {lz} 3 1 3 0 200 force'])
w(f'{P}/boss/spino', ['# Chaque seconde (Spinosaure en vie) : barre, laisse, phases, attaques',
                      f'execute positioned {lx} {ly} {lz} run bossbar set mg:trspino players @a[tag=mg.tvw,distance=..56]',
                      'execute store result bossbar mg:trspino value run data get entity @e[tag=mg.tvspino,limit=1] Health',
                      f'execute positioned {lx} {ly} {lz} unless entity @e[tag=mg.tvspino,distance=..30] run tp @e[tag=mg.tvspino] {lx + 0.5} {ly} {lz + 0.5}',
                      f'execute positioned {lx} {ly} {lz} unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players add $trsr mg.st 1',
                      f'execute positioned {lx} {ly} {lz} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..44] run scoreboard players set $trsr mg.st 0',
                      f'execute if score $trsr mg.st matches 15.. run return run function mg:{P}/boss/spino_reset',
                      'execute as @e[tag=mg.tvspino] store result score $hp mg.st run data get entity @s Health',
                      'execute if score $hp mg.st matches ..160 as @e[tag=mg.tvspino,tag=!mg.trp3] at @s run function mg:terra/rpg/boss/spino_p3',
                      'scoreboard players remove $trs1 mg.st 1', 'scoreboard players remove $trs2 mg.st 1', 'scoreboard players remove $trs3 mg.st 1',
                      f'execute if score $trs1 mg.st matches ..0 as @e[tag=mg.tvspino] at @s run function mg:{P}/boss/spino_sweep',
                      f'execute if score $hp mg.st matches ..390 if score $trs2 mg.st matches ..0 as @e[tag=mg.tvspino] run function mg:{P}/boss/spino_dive',
                      f'execute if score $hp mg.st matches ..390 if score $trs3 mg.st matches ..0 run function mg:{P}/boss/spino_call'])
w(f'{P}/boss/spino_sweep', ['# Coup de queue circulaire', 'scoreboard players set $trs1 mg.st 7', 'scoreboard players set @s mg.tvat 12',
                            'particle minecraft:sweep_attack ~ ~1 ~ 3 0.3 3 0 16', 'playsound minecraft:entity.player.attack.sweep hostile @a ~ ~ ~ 2 0.5',
                            'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..6] run damage @s 8 minecraft:mob_attack by @e[tag=mg.tvspino,limit=1]'])
DV = ['# Plongeon : la reine disparaît sous l\'eau et ressurgit près d\'un colon', 'scoreboard players set $trs2 mg.st 13',
      'execute at @s run particle minecraft:splash ~ ~1 ~ 2 1 2 0 120 force', 'execute at @s run playsound minecraft:entity.generic.splash hostile @a ~ ~ ~ 2 0.5',
      'execute store result score $r mg.st run random value 0..7']
DV += [f'execute if score $r mg.st matches {i} run tp @s {x + 0.5} 62 {z + 0.5}' for i, (x, z) in enumerate(LAG_PTS)]
DV += ['execute at @s run particle minecraft:bubble_column_up ~ ~ ~ 1.5 1 1.5 0.2 160 force',
       'execute at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.6', 'scoreboard players set @s mg.tvat 12', 'tag @s add mg.tvroar',
       'execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..4] run damage @s 10 minecraft:mob_attack by @e[tag=mg.tvspino,limit=1]']
w(f'{P}/boss/spino_dive', DV)
w(f'{P}/boss/spino_call', ['# La reine appelle ses petits (compys) et un dilophosaure', 'scoreboard players set $trs3 mg.st 22',
                           f'execute positioned {lx + 6} {ly} {lz} run function mg:terra/dino/compy', 'tag @e[tag=mg.tvlast] add mg.trr',
                           f'execute positioned {lx - 6} {ly} {lz} run function mg:terra/dino/compy', 'tag @e[tag=mg.tvlast] add mg.trr',
                           f'execute positioned {lx} {ly} {lz + 6} run function mg:terra/dino/compy', 'tag @e[tag=mg.tvlast] add mg.trr',
                           f'execute positioned {lx} {ly} {lz - 6} run function mg:terra/dino/dilo', 'tag @e[tag=mg.tvlast] add mg.trr',
                           f'execute positioned {lx} {ly} {lz} run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 1.2'])
w(f'{P}/boss/spino_p3', ['# Reine enragée (25 %)', 'tag @s add mg.trp3', 'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 0 true',
                         'scoreboard players set @s mg.tvat 16', 'tag @s add mg.tvroar', 'playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 2 0.8',
                         'tellraw @a[tag=mg.tvw,distance=..60] {"text":"🦖 La reine du marais est enragée !","color":"red","bold":true}'])
w(f'{P}/boss/spino_reset', ['# Plus personne près de la lagune : la reine replonge (combat remis à zéro)', 'scoreboard players set $trspa mg.st 0',
                            'execute as @e[tag=mg.tvspino] at @s run tp @s ~ -400 ~', 'bossbar set mg:trspino players'])
w(f'{P}/boss/spino_win', ['# La reine du marais est vaincue', 'scoreboard players set $trspa mg.st 0', 'scoreboard players set $trspc mg.st 120',
                          'bossbar set mg:trspino players',
                          f'execute positioned {lx} {ly} {lz} as @a[tag=mg.tvw,distance=..64] run function mg:{P}/boss/spino_reward',
                          f'execute positioned {lx} {ly} {lz} run title @a[tag=mg.tvw,distance=..64] title {{"text":"VICTOIRE","color":"gold","bold":true}}',
                          f'execute positioned {lx} {ly} {lz} run title @a[tag=mg.tvw,distance=..64] subtitle {{"text":"La reine du marais est tombée","color":"gray"}}'])
w(f'{P}/boss/spino_reward', ['# @s a participé à la victoire sur le Spinosaure', 'scoreboard players add @s mg.trec 3', f'function mg:{P}/xp {{n:400}}',
                             'tellraw @s {"text":"  +3 écailles de spinosaure (forge de Jo)","color":"dark_aqua"}',
                             f'execute if score @s mg.trch matches 40 run {chfn(45)}',
                             'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 0.9'])
# ---- lieutenant Varek (évocateur) et sa garde
fx_, fy_, fz_ = FORT_C
VAREK = (fx_ - 9 + 0.5, 65, fz_ + 9 + 0.5)
w(f'{P}/boss/varek_start', ['# Le lieutenant Varek sort de son QG avec sa garde',
                            f'summon minecraft:evoker {VAREK[0]} {VAREK[1]} {VAREK[2]} {{Tags:["mg.tv","mg.tvhos","mg.tvtg","mg.trvarek","mg.trboss"],PersistenceRequired:1b,'
                            'CanJoinRaid:0b,DeathLootTable:"minecraft:empty",CustomName:{"text":"Lieutenant Varek","color":"dark_red","bold":true},CustomNameVisible:1b,'
                            'attributes:[{id:"minecraft:max_health",base:140},{id:"minecraft:follow_range",base:40}],Health:140f}',
                            'scoreboard players set $trva mg.st 1', 'scoreboard players set $trvr mg.st 0'] +
  [f'execute positioned {fx_ + dx} 65 {fz_ + dz} run function mg:{P}/sixer' for dx, dz in [(-6, 4), (-6, 14), (2, 9), (-2, 12)]] +
  ['tellraw @a[tag=mg.tvw,x=-230,y=0,z=-30,dx=60,dy=200,dz=70] {"text":"⚔ Lieutenant Varek : « Encore un colon ? Personne ne repart du fort ! »","color":"dark_red"}',
   f'execute positioned {fx_} {fy_} {fz_} as @a[tag=mg.tvw,gamemode=adventure,distance=..40] run function mg:{P}/cs/boss_varek',
   'execute as @e[tag=mg.trvarek] run data merge entity @s {NoAI:1b}', f'schedule function mg:{P}/boss/wake 90t'])
w(f'{P}/boss/varek', ['# Chaque seconde (Varek en vie)', f'execute positioned {fx_} {fy_} {fz_} run bossbar set mg:trvarek players @a[tag=mg.tvw,distance=..48]',
                      'execute store result bossbar mg:trvarek value run data get entity @e[tag=mg.trvarek,limit=1] Health',
                      f'execute positioned {fx_} {fy_} {fz_} unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..56] run scoreboard players add $trvr mg.st 1',
                      f'execute positioned {fx_} {fy_} {fz_} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..56] run scoreboard players set $trvr mg.st 0',
                      f'execute if score $trvr mg.st matches 20.. run function mg:{P}/boss/varek_reset'])
w(f'{P}/boss/varek_reset', ['scoreboard players set $trva mg.st 0', 'execute as @e[tag=mg.trvarek] at @s run tp @s ~ -400 ~', 'bossbar set mg:trvarek players'])
w(f'{P}/boss/varek_win', ['# Varek est vaincu', 'scoreboard players set $trva mg.st 0', 'scoreboard players set $trvc mg.st 120', 'bossbar set mg:trvarek players',
                          f'execute positioned {fx_} {fy_} {fz_} as @a[tag=mg.tvw,distance=..64] run function mg:{P}/boss/varek_reward'])
w(f'{P}/boss/varek_reward', ['scoreboard players add @s mg.tvc 120', f'function mg:{P}/xp {{n:300}}', 'tellraw @s {"text":"  +120 ₵ (prime sur Varek)","color":"green"}',
                             f'execute if score @s mg.trch matches 62 run {chfn(64)}', 'title @s title {"text":"VAREK EST TOMBÉ","color":"gold","bold":true}'])
# ---- Roi Tyran
cx_, cy_, cz_ = CALD
GEY = [(round(cx_ + r * _m.cos(_m.radians(a))), round(cz_ + r * _m.sin(_m.radians(a)))) for r, a0 in ((5, 0), (10, 22)) for a in range(a0, 360 + a0, 45)]
w(f'{P}/boss/rex_start', ['# Le Roi Tyran se dresse dans la caldeira', f'execute positioned {cx_ + 0.5} {cy_} {cz_ - 4.5} run function mg:terra/dino/rex',
                          'tag @e[tag=mg.tvlast] add mg.trboss', 'scoreboard players set $trra mg.st 1', 'scoreboard players set $trr1 mg.st 6',
                          'scoreboard players set $trr2 mg.st 9', 'scoreboard players set $trr3 mg.st 12', 'scoreboard players set $trr4 mg.st 20', 'scoreboard players set $trrr mg.st 0',
                          'bossbar set mg:trrex max 900', 'bossbar set mg:trrex value 900',
                          f'execute positioned {cx_} {cy_} {cz_} as @a[tag=mg.tvw,gamemode=adventure,distance=..60] run function mg:{P}/cs/boss_rex',
                          'execute as @e[tag=mg.tvrex] run data merge entity @s {NoAI:1b}', 'scoreboard players set @e[tag=mg.tvrex] mg.tvat 140',
                          'tag @e[tag=mg.tvrex] add mg.tvroar', f'schedule function mg:{P}/boss/wake 140t',
                          'execute as @e[tag=mg.tvrex] run function mg:terra/rpg/boss/rex_roar'])
w(f'{P}/boss/rex', ['# Chaque seconde (Roi Tyran en vie) : barre, laisse, phases, attaques',
                    f'execute positioned {cx_} {cy_} {cz_} run bossbar set mg:trrex players @a[tag=mg.tvw,distance..60]'.replace('distance..', 'distance=..'),
                    'execute store result bossbar mg:trrex value run data get entity @e[tag=mg.tvrex,limit=1] Health',
                    f'execute positioned {cx_} {cy_} {cz_} unless entity @e[tag=mg.tvrex,distance=..16] run tp @e[tag=mg.tvrex] {cx_ + 0.5} {cy_} {cz_ + 0.5}',
                    f'execute positioned {cx_} {cy_} {cz_} unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..40] run scoreboard players add $trrr mg.st 1',
                    f'execute positioned {cx_} {cy_} {cz_} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..40] run scoreboard players set $trrr mg.st 0',
                    f'execute if score $trrr mg.st matches 15.. run return run function mg:{P}/boss/rex_reset',
                    'execute as @e[tag=mg.tvrex] store result score $hp mg.st run data get entity @s Health',
                    'execute if score $hp mg.st matches ..180 as @e[tag=mg.tvrex,tag=!mg.trp3] at @s run function mg:terra/rpg/boss/rex_p3',
                    'scoreboard players remove $trr1 mg.st 1', 'scoreboard players remove $trr2 mg.st 1', 'scoreboard players remove $trr3 mg.st 1', 'scoreboard players remove $trr4 mg.st 1',
                    'execute if score $trr1 mg.st matches ..0 as @e[tag=mg.tvrex] at @s run function mg:terra/rpg/boss/rex_stomp',
                    'execute if score $trr2 mg.st matches ..0 as @e[tag=mg.tvrex] at @s run function mg:terra/rpg/boss/rex_roar',
                    f'execute if score $hp mg.st matches ..450 if score $trr3 mg.st matches ..0 run function mg:{P}/boss/rex_geysers',
                    f'execute if score $hp mg.st matches ..450 if score $trr4 mg.st matches ..0 run function mg:{P}/boss/rex_call',
                    f'execute as @e[type=minecraft:marker,tag=mg.trgey] at @s run function mg:{P}/boss/gey_tick'])
w(f'{P}/boss/rex_stomp', ['# Piétinement : onde de choc autour du Roi', 'scoreboard players set $trr1 mg.st 8', 'scoreboard players set @s mg.tvat 10',
                          'execute unless entity @a[tag=mg.tvw,gamemode=adventure,distance=..8] run return 0',
                          'particle minecraft:explosion ~ ~0.5 ~ 3 0.2 3 0 12', 'particle minecraft:block{block_state:"minecraft:blackstone"} ~ ~0.3 ~ 4 0.2 4 0 120',
                          'playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5',
                          'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..8] run damage @s 9 minecraft:mob_attack by @e[tag=mg.tvrex,limit=1]'])
w(f'{P}/boss/rex_roar', ['# Rugissement : les colons proches sont ralentis et aveuglés un instant', 'scoreboard players set $trr2 mg.st 14',
                         'scoreboard players set @s mg.tvat 20', 'tag @s add mg.tvroar',
                         'execute at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 3 0.45',
                         'execute at @s run playsound minecraft:entity.ender_dragon.growl hostile @a ~ ~ ~ 2 0.6',
                         'execute at @s run particle minecraft:sonic_boom ^ ^3 ^3 0 0 0 0 1 force',
                         'execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..24] run effect give @s minecraft:slowness 3 1',
                         'execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..24] run effect give @s minecraft:darkness 3 0 true'])
GY = ['# Geysers de lave : trois points autour des colons s\'embrasent dans 2 s', 'scoreboard players set $trr3 mg.st 7']
for i, (x, z) in enumerate(GEY):
    GY.append(f'execute store result score $r mg.st run random value 0..{len(GEY) - 1}')
    break
GY += [f'execute if score $r mg.st matches {i} run summon minecraft:marker {x + 0.5} {cy_} {z + 0.5} {{Tags:["mg.tv","mg.trgey","mg.trgn"]}}' for i, (x, z) in enumerate(GEY)]
GY += ['execute store result score $r mg.st run random value 0..15'] + \
      [f'execute if score $r mg.st matches {i} run summon minecraft:marker {x + 0.5} {cy_} {z + 0.5} {{Tags:["mg.tv","mg.trgey","mg.trgn"]}}' for i, (x, z) in enumerate(GEY)]
GY += [f'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..30,sort=random,limit=1] at @s run summon minecraft:marker ~ {cy_} ~ {{Tags:["mg.tv","mg.trgey","mg.trgn"]}}'
       .replace('distance=..30', f'x={cx_ - 16},y={cy_ - 4},z={cz_ - 16},dx=32,dy=12,dz=32')]
GY += ['scoreboard players set @e[tag=mg.trgn] mg.tvst 2', 'tag @e[tag=mg.trgn] remove mg.trgn']
w(f'{P}/boss/rex_geysers', GY)
w(f'{P}/boss/gey_tick', ['# @s (geyser) : 2 s d\'avertissement puis jaillissement', 'scoreboard players remove @s mg.tvst 1',
                         'execute if score @s mg.tvst matches 1.. run particle minecraft:lava ~ ~0.2 ~ 0.6 0.1 0.6 0 8',
                         'execute if score @s mg.tvst matches 1.. run particle minecraft:large_smoke ~ ~0.2 ~ 0.6 0.1 0.6 0.02 10',
                         'execute if score @s mg.tvst matches 1.. run return 0',
                         'particle minecraft:flame ~ ~1 ~ 0.6 2 0.6 0.1 120 force', 'particle minecraft:lava ~ ~1 ~ 0.6 1.5 0.6 0 30 force',
                         'playsound minecraft:block.lava.extinguish hostile @a ~ ~ ~ 1.5 0.6',
                         'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..2] run damage @s 8 minecraft:in_fire',
                         'execute as @a[tag=mg.tvw,gamemode=adventure,distance=..2] run effect give @s minecraft:levitation 1 4 true', 'kill @s'])
w(f'{P}/boss/rex_call', ['# Le Roi appelle deux slashers', 'scoreboard players set $trr4 mg.st 25',
                         f'execute positioned {cx_ + 8} {cy_} {cz_} run function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.trr',
                         f'execute positioned {cx_ - 8} {cy_} {cz_} run function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.trr',
                         f'execute positioned {cx_} {cy_} {cz_} as @e[tag=mg.tvraptor,distance=..12] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure]'])
w(f'{P}/boss/rex_p3', ['# Roi enragé (20 %)', 'tag @s add mg.trp3', 'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 0 true',
                       'function mg:terra/rpg/boss/rex_roar', 'tellraw @a[tag=mg.tvw,distance=..60] {"text":"🦖 Le Roi Tyran est fou de rage !","color":"red","bold":true}'])
w(f'{P}/boss/rex_reset', ['scoreboard players set $trra mg.st 0', 'execute as @e[tag=mg.tvrex] at @s run tp @s ~ -400 ~', 'kill @e[tag=mg.trgey]', 'bossbar set mg:trrex players'])
w(f'{P}/boss/rex_win', ['# Le Roi Tyran est vaincu : la faille se révèle', 'scoreboard players set $trra mg.st 0', 'scoreboard players set $trrc mg.st 180',
                        'kill @e[tag=mg.trgey]', 'bossbar set mg:trrex players',
                        f'execute positioned {cx_} {cy_} {cz_} as @a[tag=mg.tvw,distance=..64] run function mg:{P}/boss/rex_reward',
                        f'particle minecraft:reverse_portal {RIFT[0] + 0.5} {RIFT[1] + 2} {RIFT[2]} 1 2 0.3 0.1 300 force'])
w(f'{P}/boss/rex_reward', ['scoreboard players add @s mg.trrx 1', 'scoreboard players add @s mg.tvc 400', f'function mg:{P}/xp {{n:1000}}',
                           'tellraw @s {"text":"  +1 croc du Roi, +400 ₵","color":"dark_red"}', 'title @s title {"text":"LE ROI EST MORT","color":"gold","bold":true}',
                           f'execute if score @s mg.trch matches 80 run {chfn(85)}'])
w(f'{P}/rift', ['# @s touche la faille temporelle (étape 85) : elle se referme (cinématique, retour à la colonie)', chfn(90),
                f'function mg:{P}/cs/rift',
                'execute at @s run playsound minecraft:block.end_portal.spawn player @a ~ ~ ~ 1 0.8',
                f'particle minecraft:reverse_portal {RIFT[0] + 0.5} {RIFT[1] + 2} {RIFT[2]} 1 2 1 0.3 400 force', f'function mg:{P}/xp {{n:200}}'])
BOSS = ['# Chaque seconde : déclenchement et suivi des boss',
        'scoreboard players remove $trspc mg.st 1', 'scoreboard players remove $trvc mg.st 1', 'scoreboard players remove $trrc mg.st 1',
        f'execute if score $trspa mg.st matches 1 unless entity @e[tag=mg.tvspino] run function mg:{P}/boss/spino_win',
        f'execute if score $trva mg.st matches 1 unless entity @e[tag=mg.trvarek] run function mg:{P}/boss/varek_win',
        f'execute if score $trra mg.st matches 1 unless entity @e[tag=mg.tvrex] run function mg:{P}/boss/rex_win',
        f'execute unless score $trspa mg.st matches 1 if score $trspc mg.st matches ..0 positioned {lx} {ly} {lz} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..22,scores={{mg.trch=40..}}] run function mg:{P}/boss/spino_start',
        f'execute unless score $trva mg.st matches 1 if score $trvc mg.st matches ..0 positioned {fx_} {fy_} {fz_} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..30,scores={{mg.trch=62..}}] run function mg:{P}/boss/varek_start',
        f'execute unless score $trra mg.st matches 1 if score $trrc mg.st matches ..0 positioned {cx_} {cy_} {cz_} if entity @a[tag=mg.tvw,gamemode=adventure,distance=..14,scores={{mg.trch=80..}}] run function mg:{P}/boss/rex_start',
        f'execute if score $trspa mg.st matches 1 run function mg:{P}/boss/spino',
        f'execute if score $trva mg.st matches 1 run function mg:{P}/boss/varek',
        f'execute if score $trra mg.st matches 1 run function mg:{P}/boss/rex']
w(f'{P}/bosses', BOSS)

# ================================================================ étapes « à un endroit » (chaque seconde)
QT = ['# Chaque seconde, @s : étapes de la campagne qui se valident en arrivant quelque part']
for n, nxt, (x, y, z), r in [(30, 32, STATION_C, 14), (50, 52, DELTA_C, 9), (60, 62, FORT_C, 30), (72, 75, BRIDGE_C, 9), (75, 80, CALD, 15)]:
    QT.append(f'execute if score @s mg.trch matches {n} positioned {x} {y} {z} if entity @s[distance=..{r}] run {chfn(nxt)}')
QT.append(f'execute if score @s mg.trch matches 85 positioned {RIFT[0] + 0.5} {RIFT[1]} {RIFT[2] + 0.5} if entity @s[distance=..3.5] run function mg:{P}/rift')
w(f'{P}/qtick', QT)

# ================================================================ PNJ, balises, modules, œufs : entités de la session
SU = ['# Session : PNJ du RPG, balises de voyage, modules de données, cellule, œufs d\'ambre, points d\'apparition, barres des boss',
      f'function mg:{P}/consts']
for nid, (key, name, col, (x, y, z), rot, prof) in NPCS.items():
    SU += [f'summon minecraft:villager {x} {y} {z} {{Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[{rot}f,0f],'
           f'VillagerData:{{profession:"{prof}",level:5,type:"minecraft:jungle"}},Offers:{{Recipes:[]}},CustomName:{js(TEXT(name, col))},CustomNameVisible:1b}}',
           f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.tv","mg.trnpc","mg.tvn"],width:1.1f,height:2.2f,response:1b}}',
           f'scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid {nid}', 'tag @e[tag=mg.tvn] remove mg.tvn',
           tdisp(x, y + 2.35, z, TEXT('💬 clic droit', 'gray'), 0.6)]
BEACONS = [(n, cx - 2, cy, cz) for n, ck, cname, cx, cy, cz in CAMPS]
BEACONS[0] = (1, COLONY_BEACON[0] + 0.5, COLONY_BEACON[1] + 1, COLONY_BEACON[2] + 0.5)
for n, x, y, z in BEACONS:
    SU += [f'summon minecraft:interaction {x} {y} {z} {{Tags:["mg.tv","mg.trbeacon"],width:1.2f,height:2.2f,response:1b}}',
           tdisp(x, y + 2.4, z, [TEXT('🌀 Balise de voyage\n', 'light_purple', bold=True), TEXT('clic droit', 'gray', bold=False)], 0.8)]
for k, (x, y, z) in enumerate(DATA_PTS, 1):
    SU += [f'summon minecraft:marker {x + 0.5} {y} {z + 0.5} {{Tags:["mg.tv","mg.trmod","mg.tvn"]}}', f'scoreboard players set @e[tag=mg.tvn,limit=1] mg.trnid {k}',
           'tag @e[tag=mg.tvn] remove mg.tvn',
           f'summon minecraft:item_display {x + 0.5} {y + 0.6} {z + 0.5} {{Tags:["mg.tv","mg.tvpdi"],item:{{id:"minecraft:recovery_compass",count:1}},Glowing:1b,glow_color_override:5636095,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
           tdisp(x + 0.5, y + 1.3, z + 0.5, TEXT('💾 Module de données', 'aqua', bold=True), 0.6)]
SU += [f'summon minecraft:marker {CELL[0] + 0.5} {CELL[1]} {CELL[2] + 0.5} {{Tags:["mg.tv","mg.trcell"]}}',
       tdisp(CELL[0] + 0.5, CELL[1] + 1.6, CELL[2] + 0.5, TEXT('🔋 Cellule d\'énergie volée', 'aqua', bold=True), 0.6)]
for (x, y, z) in EGGS:
    SU += [f'summon minecraft:item_display {x + 0.5} {y + 0.3} {z + 0.5} {{Tags:["mg.tv","mg.tvpdi"],item:{{id:"minecraft:sniffer_egg",count:1}},Glowing:1b,glow_color_override:16755200,{TR % (0, 0, 0, 0.5, 0.5, 0.5)}}}']
for (x, y, z, tags) in MARKERS:
    SU.append(f'summon minecraft:marker {x} {y} {z} {{Tags:[{tags}]}}')
SU += ['bossbar add mg:trspino {"text":"🦖 Spinosaure, reine du marais","color":"dark_aqua"}', 'bossbar set mg:trspino color blue', 'bossbar set mg:trspino style notched_10',
       'bossbar add mg:trrex {"text":"🦖 Le Roi Tyran","color":"dark_red"}', 'bossbar set mg:trrex color red', 'bossbar set mg:trrex style notched_20',
       'bossbar add mg:trvarek {"text":"⚔ Lieutenant Varek","color":"dark_red"}', 'bossbar set mg:trvarek color red', 'bossbar set mg:trvarek style notched_10',
       'bossbar set mg:trvarek max 140',
       'scoreboard players set $trspa mg.st 0', 'scoreboard players set $trva mg.st 0', 'scoreboard players set $trra mg.st 0',
       'scoreboard players set $trspc mg.st 0', 'scoreboard players set $trvc mg.st 0', 'scoreboard players set $trrc mg.st 0',
       'function mg:terra/bio_try', f'function mg:{P}/dg_setup', f'function mg:{P}/setup2']
w(f'{P}/setup', SU)
w(f'{P}/clear', ['# Fin de session : barres des boss, invocations (vex) retirées', 'bossbar remove mg:trspino', 'bossbar remove mg:trrex', 'bossbar remove mg:trvarek',
                 f'execute in {DIM} run kill @e[type=minecraft:vex,x=-260,y=-64,z=-260,dx=520,dy=400,dz=520]', 'scoreboard players set $trspa mg.st 0', 'scoreboard players set $trva mg.st 0',
                 'scoreboard players set $trra mg.st 0', f'function mg:{P}/dg_clear'])

# ================================================================ boucles : tick, seconde
w(f'{P}/npc_int', ['# @s (interaction d\'un PNJ) : le colon qui a cliqué lui parle', 'scoreboard players operation $npc mg.st = @s mg.trnid',
                   f'execute on target if entity @s[tag=mg.tvw] run function mg:{P}/npc', 'data remove entity @s interaction'])
w(f'{P}/npc', ['# @s parle au PNJ $npc'] + [f'execute if score $npc mg.st matches {nid} run return run function mg:{P}/npc_{key}' for nid, (key, *_r) in NPCS.items()])
w(f'{P}/beacon_int', ['# @s (balise) : fenêtre de voyage', f'execute on target if entity @s[tag=mg.tvw] run function mg:{P}/travel', 'data remove entity @s interaction'])
w(f'{P}/hurt', ['# @s (colon) vient d\'être blessé : le dinosaure qui l\'a mordu joue son attaque', 'scoreboard players set @s mg.trdt 0',
                'execute on attacker if entity @s[tag=mg.tvd] run scoreboard players set @s mg.tvat 8'])
w(f'{P}/tick', ['# Chaque tick (dimension) : PNJ, balises, choix, blessures, ramassages',
                f'execute as @e[type=minecraft:interaction,tag=mg.trnpc] if data entity @s interaction run function mg:{P}/npc_int',
                f'execute as @e[type=minecraft:interaction,tag=mg.trbeacon] if data entity @s interaction run function mg:{P}/beacon_int',
                f'execute as @a[tag=mg.tvw,scores={{mg.trtk=1..}}] run function mg:{P}/tk',
                f'execute as @a[tag=mg.tvw,scores={{mg.trdt=1..}}] run function mg:{P}/hurt',
                'scoreboard players remove @a[tag=mg.tvw,scores={mg.trsc=1..}] mg.trsc 1',
                f'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={{mg.trch=32}}] at @s if predicate mg:sneak run function mg:{P}/mod_try',
                f'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={{mg.trch=64}}] at @s if predicate mg:sneak run function mg:{P}/mod_try',
                'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trpk=1..}] unless predicate mg:sneak run scoreboard players set @s mg.trpk 0',
                f'execute if score $tvq5 mg.st matches 0 run function mg:{P}/eggs_tick', f'function mg:{P}/cl/tick', f'function mg:{P}/tick2',
                f'execute as @a[tag=mg.trcine] run function mg:{P}/cs/run',
                f'execute if score $tvq mg.st matches 0 as @a[tag=mg.tvw,tag=!mg.trcine,scores={{mg.tron=1}}] at @s run function mg:{P}/ind',
                f'execute if score $tvq mg.st matches 10 as @a[tag=mg.tvw,tag=!mg.trcine,scores={{mg.tron=1}}] at @s run function mg:{P}/ind'])
SECOND = ['# Chaque seconde (dimension) : régions, lieux, étapes, primes, population, capacités, boss',
          f'execute as @a[tag=mg.tvw,tag=!mg.trcine] run function mg:{P}/region', f'function mg:{P}/pois',
          f'execute as @a[tag=mg.tvw,tag=!mg.trcine] run function mg:{P}/qtick',
          '# première arrivée : cinématique d\'introduction (la carte est chargée)',
          f'execute as @a[tag=mg.tvw,tag=!mg.trcine,tag=!mg.trintro,scores={{mg.trch=0}}] run function mg:{P}/intro_go',
          'scoreboard players enable @a[tag=mg.tvw] mg.trtk']
for mob, (obj, fn) in {'kdilo': ('mg.tkdilo', 'k_dilo'), 'kcompy': ('mg.tkcompy', 'k_compy'), 'kptera': ('mg.tkptera', 'k_ptera'),
                       'ksix': ('mg.tksix', 'k_six'), 'kherb': ('mg.tkherb', 'k_herb2')}.items():
    SECOND.append(f'execute as @a[tag=mg.tvw,scores={{{obj}=1..}}] run function mg:{P}/{fn}')
SECOND += ['execute as @a[tag=mg.tvw,scores={mg.tkherb2=1..}] run function mg:terra/rpg/k_herb2',
           'execute as @a[tag=mg.tvw,scores={mg.tkherb3=1..}] run function mg:terra/rpg/k_herb2',
           'execute as @a[tag=mg.tvw,scores={mg.tkherb4=1..}] run function mg:terra/rpg/k_herb2',
           '# cycle de 6 s : une région complétée par seconde, puis nettoyage des dinosaures loin de tout joueur',
           'scoreboard players add $trq3 mg.st 1', 'execute if score $trq3 mg.st matches 6.. run scoreboard players set $trq3 mg.st 0']
for i, k in enumerate(('n', 'e', 'w', 's')):
    SECOND.append(f'execute if score $trq3 mg.st matches {i} if entity @a[tag=mg.tvw,scores={{mg.trrg={i + 1}}}] run function mg:{P}/pop_{k}')
SECOND += ['execute if score $trq3 mg.st matches 5 as @e[tag=mg.trr,tag=!mg.trboss] at @s unless entity @a[tag=mg.tvw,distance=..96] run tp @s ~ -400 ~',
           f'function mg:{P}/abilities', f'function mg:{P}/bosses', f'function mg:{P}/dungeons', f'function mg:{P}/cl/second', f'function mg:{P}/second2']
w(f'{P}/second', SECOND)

# ---------------------------------------------------------------- primes (XP, trophées)
def kfn(name, obj, lines, label):
    w(f'{P}/{name}', [f'# @s a abattu : {label}', f'scoreboard players operation $kk mg.st = @s {obj}', f'scoreboard players set @s {obj} 0'] + lines)


kfn('k_dilo', 'mg.tkdilo', ['scoreboard players operation @s mg.trvn += $kk mg.st', f'function mg:{P}/xpk {{n:20}}',
                            'title @s actionbar [{"text":"+1 glande à venin ","color":"green"},{"text":"dilophosaure abattu","color":"gray"}]', 'scoreboard players set @s mg.tval 30',
                            'scoreboard players add @s mg.tvc 15'], 'dilophosaure')
kfn('k_compy', 'mg.tkcompy', [f'function mg:{P}/xpk {{n:5}}', 'scoreboard players add @s mg.tvc 3'], 'compsognathus')
kfn('k_ptera', 'mg.tkptera', ['scoreboard players operation @s mg.trai += $kk mg.st', f'function mg:{P}/xpk {{n:25}}',
                              'title @s actionbar [{"text":"+1 aile ","color":"aqua"},{"text":"ptéranodon abattu","color":"gray"}]', 'scoreboard players set @s mg.tval 30',
                              'scoreboard players add @s mg.tvc 15'], 'ptéranodon')
kfn('k_six', 'mg.tksix', [f'function mg:{P}/xpk {{n:20}}', 'scoreboard players add @s mg.tvc 20',
                          'title @s actionbar [{"text":"+20 ₵ ","color":"green"},{"text":"renégat neutralisé","color":"gray"}]', 'scoreboard players set @s mg.tval 30'],
    'renégat')
w(f'{P}/k_herb2', ['# @s a tué un grand herbivore protégé (tricératops, stégosaure, ankylosaure, gallimimus)',
                   'scoreboard players set @s mg.tkherb 0', 'scoreboard players set @s mg.tkherb2 0', 'scoreboard players set @s mg.tkherb3 0',
                   'scoreboard players set @s mg.tkherb4 0', 'function mg:terra/k_herb'])
w(f'{P}/k_raptor', ['# Bonus RPG d\'un slasher abattu (appelé par terra/k_raptor avant la remise à zéro)', 'scoreboard players operation @s mg.trgr += @s mg.tvkr',
                    'scoreboard players operation $kx mg.st = @s mg.tvkr', 'scoreboard players operation $kx mg.st *= #12 mg.st',
                    'execute store result storage mg:terra s.n int 1 run scoreboard players get $kx mg.st', f'function mg:{P}/xpk with storage mg:terra s',
                    'execute if score @s mg.trch matches 10 run scoreboard players operation @s mg.trqp += @s mg.tvkr',
                    'execute if score @s mg.trch matches 10 if score @s mg.trqp matches ..2 run tellraw @s [{"text":"🦖 Premiers pas : ","color":"gold"},{"score":{"name":"@s","objective":"mg.trqp"},"color":"yellow","bold":true},{"text":" / 3 slashers","color":"yellow"}]',
                    f'execute if score @s mg.trch matches 10 if score @s mg.trqp matches 3.. run {chfn(15)}'])
w(f'{P}/xpm', ['$function mg:terra/rpg/xp {n:$(xp)}'])
w(f'{P}/k_carno', ['# Bonus RPG d\'un carnotaure abattu', 'scoreboard players add @s mg.trdn 2', f'function mg:{P}/xpk {{n:120}}', f'function mg:{P}/kc_hook',
                   'tellraw @s {"text":"  +2 dents de carnotaure (forge de Jo)","color":"red"}'])

# ================================================================ barre d'action hors mission : niveau, crédits, objectif de la campagne
HD = ['# @s : barre d\'action hors mission (niveau, crédits, objectif de la campagne)']
DIST = ',{"text":"  📍 ","color":"gold"},{"score":{"name":"@s","objective":"mg.trod"},"color":"yellow","bold":true},{"text":" m","color":"gold"}'
for n, obj in HUDQ:
    d = DIST if CH[n][2] else ''
    HD.append(f'execute if score @s mg.trch matches {n} run return run title @s actionbar [{CRED},{js(TEXT("📜 " + obj, "yellow"))}{d}]')
w(f'{P}/hud', HD)

# ================================================================ prédicats, objectifs, câblage (chargement, désinstallation)
for nm_, ch_ in (('tv_c20', 0.2), ('tv_c33', 0.33), ('tv_c50', 0.5)):
    with open(os.path.join(C.D, 'predicate', nm_ + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'condition': 'minecraft:random_chance', 'chance': ch_}, f, indent=2)
        f.write('\n')
C.objectives([(o, 'dummy') for o in ('mg.trlv', 'mg.trxp', 'mg.trch', 'mg.trqp', 'mg.trbs', 'mg.trpo', 'mg.trtv', 'mg.treg', 'mg.trwp', 'mg.trml',
                                     'mg.trar', 'mg.trmt', 'mg.trgr', 'mg.trdn', 'mg.trvn', 'mg.trec', 'mg.trai', 'mg.trrx', 'mg.trrg', 'mg.trpk',
                                     'mg.trsc', 'mg.trnid', 'mg.trcl', 'mg.trcd', 'mg.trdg')] +
             [('mg.trtk', 'trigger'), ('mg.trdt', 'minecraft.custom:minecraft.damage_taken'),
              ('mg.tkdilo', 'minecraft.killed:minecraft.zombie_villager'), ('mg.tkcompy', 'minecraft.killed:minecraft.silverfish'),
              ('mg.tkptera', 'minecraft.killed:minecraft.phantom'), ('mg.tksix', 'minecraft.killed:minecraft.pillager'),
              ('mg.tkherb', 'minecraft.killed:minecraft.iron_golem'), ('mg.tkherb2', 'minecraft.killed:minecraft.polar_bear'),
              ('mg.tkherb3', 'minecraft.killed:minecraft.panda'), ('mg.tkherb4', 'minecraft.killed:minecraft.pig')])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:terra built run schedule function mg:terra/world_build 200s',
        ['# Terra Nova RPG : régions construites une fois sur un monde déjà construit (avant la mise à jour du RPG)',
         'execute if score $setup mg.st matches 1 if data storage mg:terra built unless data storage mg:terra v2 run schedule function mg:terra/world_build2 210s'])
C.patch('desinstaller', 'scoreboard objectives remove mg.tvc',
        ['schedule clear mg:terra/rb_step', 'schedule clear mg:terra/world_build2', 'schedule clear mg:terra/bio_step', 'schedule clear mg:terra/rpg/setup_s',
         'bossbar remove mg:trspino', 'bossbar remove mg:trrex', 'bossbar remove mg:trvarek', 'bossbar remove mg:trdg0',
         'bossbar remove mg:trdg1', 'bossbar remove mg:trdg2', 'bossbar remove mg:trdg3',
         'data remove storage mg:terra v2', 'data remove storage mg:terra bio', 'data remove storage mg:terra s'])

# ================================================================ classes et donjons (tv_classes.py)
NETL_ITEM, TRAP_ITEM = NETL, TRAP
exec(open(os.path.join(os.path.dirname(os.path.abspath(C.__file__)), 'tv_classes.py'), encoding='utf-8').read())
w(f'{P}/cl/pick_tk', ['# @s : classe choisie dans la fenêtre ($tk 601..604)'] + [f'execute if score $tk mg.st matches {600 + n} run function mg:{P}/cl/pick_{n}' for n in range(1, 5)])

# ================================================================ cinématiques et indicateur d'objectif (tv_cine.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(C.__file__)), 'tv_cine.py'), encoding='utf-8').read())
w(f'{P}/intro_go', ['# @s arrive pour la première fois : cinématique d\'introduction', 'tag @s add mg.trintro', f'function mg:{P}/cs/intro'])
w(f'{P}/boss/wake', ['# Fin des cinématiques de boss : les boss se réveillent', 'execute in ' + DIM + ' as @e[tag=mg.trboss,tag=!mg.tralpha] run data merge entity @s {NoAI:0b}',
                     'execute in ' + DIM + ' as @e[tag=mg.trvarek] run data merge entity @s {NoAI:0b}'])
C.objectives([(o, 'dummy') for o in ('mg.trcs', 'mg.trct', 'mg.trox', 'mg.troy', 'mg.troz', 'mg.tron', 'mg.trod')])
C.patch('desinstaller', 'scoreboard objectives remove mg.tvc', ['schedule clear mg:terra/rpg/boss/wake'])

# ================================================================ 2e couche du RPG (tv_rpg2.py)
exec(open(os.path.join(os.path.dirname(os.path.abspath(C.__file__)), 'tv_rpg2.py'), encoding='utf-8').read())
