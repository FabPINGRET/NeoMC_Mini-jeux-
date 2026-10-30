# Terra Nova : objets, portail du lobby, entrée / sortie / session ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : DIM, EXITA, FAR, FL, FL_REGIONS, HERBS, MED, OUTPOSTS, OUT_H, PADS, PX, PZ, SPAWN, SPAWNS, TR, WALL, js, top, w

# ================================================================ objets
WF = 'minecraft:warped_fungus_on_a_stick'


def nm(t, c):
    return js({'text': t, 'color': c, 'italic': False, 'bold': True})


def lo(*ls):
    return '[' + ','.join(js({'text': l, 'color': 'gray', 'italic': False}) for l in ls) + ']'


PROD = (f'minecraft:stick[custom_data={{tv:1}},item_model="minecraft:blaze_rod",custom_name={nm("⚡ Bâton électrique", "yellow")},'
        f'lore={lo("Mêlée : étourdit le dinosaure touché", "(lenteur V + faiblesse, 3 s)")},'
        'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:tvprod",amount:5.0,operation:"add_value",slot:"mainhand"}]]')
RIFLE1 = (f'{WF}[custom_data={{tv:2}},item_model="minecraft:crossbow",unbreakable={{}},custom_name={nm("🔫 Fusil à impulsions", "aqua")},'
          f'lore={lo("Clic droit : tir (maintenir = rafale)", "Attention à la surchauffe !")}]')
RIFLE2 = (f'{WF}[custom_data={{tv:3}},item_model="minecraft:crossbow",unbreakable={{}},enchantment_glint_override=true,'
          f'custom_name={nm("🔫 Fusil à impulsions Mk2", "gold")},lore={lo("Plus puissant, chauffe moins vite", "Clic droit : tir")}]')
SONIC = (f'{WF}[custom_data={{tv:4}},item_model="minecraft:goat_horn",unbreakable={{}},use_cooldown={{seconds:4f,cooldown_group:"mg:tvsonic"}},custom_name={nm("📢 Canon sonique", "aqua")},'   # 4 s = mg.tvsc 80 ticks (terra/sonic)
         f'lore={lo("Clic droit : onde de choc en cône (8 blocs)", "Repousse et ralentit, recharge 4 s")}]')
NETL = (f'{WF}[custom_data={{tv:5}},item_model="minecraft:fishing_rod",unbreakable={{}},custom_name={nm("🕸 Lance-filets", "white")},'
        f'lore={lo("Clic droit : immobilise un dinosaure 5 s", "Filets en vente au dépôt")}]')
TRAP = (f'{WF}[custom_data={{tv:6}},item_model="minecraft:tripwire_hook",unbreakable={{}},custom_name={nm("⚙ Pièges au sol", "gray")},'
        f'lore={lo("Clic droit : pose un piège à tes pieds", "Le premier prédateur qui marche dessus est bloqué 6 s")}]')
HOME = (f'{WF}[custom_data={{tv:9}},item_model="minecraft:bell",unbreakable={{}},custom_name={nm("📡 Rappel à la colonie", "green")},'
        f'lore={lo("Clic droit : retour à la colonie en 5 s", "Annulé si tu prends un coup")}]')
SADDLE = (f'minecraft:saddle[custom_name={nm("🐴 Selle de brachiosaure", "yellow")},'
          f'lore={lo("Clic droit sur un brachiosaure pour la poser,", "puis clic droit pour monter (Z/Q/S/D, espace = élan)")}]')
MEDK = f'minecraft:golden_apple[custom_name={nm("✚ Trousse de soins", "red")}]'
UNIF_C = f'minecraft:leather_chestplate[dyed_color=9140827,unbreakable={{}},custom_name={nm("Uniforme de colon", "gold")}]'
UNIF_B = f'minecraft:leather_boots[dyed_color=5915971,unbreakable={{}},custom_name={nm("Bottes de colon", "gold")}]'
ARM = {s: f'minecraft:chainmail_{p}[unbreakable={{}},custom_data={{tvarm:1b}},custom_name={nm("🛡 Armure de patrouille", "dark_aqua")}]'
       for s, p in [('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings')]}

w('terra/loc', ['# @s : 📡 localisateur (boussole) vers $(x) $(y) $(z) (macro), en case 9 de la barre',
                'clear @s minecraft:compass[minecraft:custom_data~{tvloc:1b}]',
                f'$item replace entity @s hotbar.8 with minecraft:compass[custom_data={{tvloc:1b}},lodestone_tracker={{target:{{pos:[I;$(x),$(y),$(z)],dimension:"{DIM}"}},tracked:false}},'
                f'custom_name={nm("📡 Localisateur", "aqua")},lore={lo("Indique la colonie ou l’objectif de ta mission")}]',
                '$scoreboard players set @s mg.trox $(x)', '$scoreboard players set @s mg.troy $(y)', '$scoreboard players set @s mg.troz $(z)',
                'scoreboard players set @s mg.tron 1'])
LOC_HOME = 'function mg:terra/loc {x:0,y:65,z:0}'
w('terra/kit', ['# @s : équipement (paliers du RPG gardés : mêlée, fusil, armure, scanner, sifflet)', 'clear @s',
                'function mg:terra/rpg/kit', f'item replace entity @s hotbar.7 with {HOME}', 'function mg:terra/rpg/qloc',
                'effect give @s minecraft:saturation infinite 0 true'])

# ================================================================ portail du lobby (monde des mini-jeux)
def part(tags, blk, tx, ty, tz, sx, sy, sz, at='~ ~ ~', extra=''):
    if '"mg.tvp"' in tags:
        tags += ',"mg.tvok"'
    return (f'summon minecraft:block_display {at} {{Tags:[{tags}],block_state:{{Name:"minecraft:{blk}"}},teleport_duration:2,'
            f'{TR % (tx, ty, tz, sx, sy, sz)}{extra}}}')


RAPTOR = [('green_terracotta', -0.28, 0.75, -0.55, 0.56, 0.5, 1.05), ('green_terracotta', -0.14, 1.05, 0.35, 0.28, 0.45, 0.3),
          ('green_terracotta', -0.2, 1.38, 0.4, 0.4, 0.32, 0.6), ('lime_terracotta', -0.15, 1.3, 0.98, 0.3, 0.16, 0.2),
          ('yellow_concrete', -0.21, 1.55, 0.74, 0.42, 0.06, 0.08), ('white_concrete', -0.13, 1.28, 1.0, 0.26, 0.04, 0.16),
          ('green_terracotta', -0.12, 0.88, -1.45, 0.24, 0.24, 0.92), ('black_terracotta', -0.07, 0.92, -1.85, 0.14, 0.14, 0.42),
          ('black_terracotta', -0.29, 1.0, -0.3, 0.58, 0.1, 0.12), ('black_terracotta', -0.29, 1.0, 0.1, 0.58, 0.1, 0.12),
          ('brown_terracotta', -0.26, 0.0, -0.15, 0.13, 0.78, 0.2), ('brown_terracotta', 0.13, 0.0, -0.15, 0.13, 0.78, 0.2),
          ('brown_terracotta', -0.24, 0.85, 0.42, 0.08, 0.25, 0.08), ('brown_terracotta', 0.16, 0.85, 0.42, 0.08, 0.25, 0.08)]
CARNO = [('red_terracotta', -0.8, 1.4, -1.3, 1.6, 1.3, 2.5), ('orange_terracotta', -0.7, 1.3, -1.0, 1.4, 0.15, 1.9),
         ('red_terracotta', -0.45, 2.2, 1.0, 0.9, 0.8, 0.6), ('red_terracotta', -0.6, 2.45, 1.4, 1.2, 0.95, 1.4),
         ('brown_terracotta', -0.5, 2.15, 1.5, 1.0, 0.3, 1.2), ('white_concrete', -0.48, 2.42, 2.78, 0.96, 0.08, 0.06),
         ('black_terracotta', -0.6, 3.38, 1.6, 0.25, 0.35, 0.25), ('black_terracotta', 0.35, 3.38, 1.6, 0.25, 0.35, 0.25),
         ('yellow_concrete', -0.62, 2.95, 2.2, 1.24, 0.12, 0.12), ('red_terracotta', -0.4, 1.8, -3.3, 0.8, 0.7, 2.0),
         ('red_terracotta', -0.2, 1.9, -4.4, 0.4, 0.4, 1.1), ('brown_terracotta', -0.8, 0.0, -0.6, 0.5, 1.5, 0.7),
         ('brown_terracotta', 0.3, 0.0, -0.6, 0.5, 1.5, 0.7), ('red_terracotta', -0.75, 1.7, 1.0, 0.15, 0.4, 0.15),
         ('red_terracotta', 0.6, 1.7, 1.0, 0.15, 0.4, 0.15), ('black_terracotta', -0.1, 2.7, -1.1, 0.2, 0.15, 2.0)]
BRACH = [('light_gray_terracotta', -1.3, 2.4, -2.0, 2.6, 2.0, 4.0), ('white_terracotta', -1.2, 2.3, -1.6, 2.4, 0.15, 3.2),
         ('light_gray_terracotta', -0.45, 3.8, 1.7, 0.9, 2.4, 0.9), ('light_gray_terracotta', -0.4, 6.0, 2.2, 0.8, 2.2, 0.8),
         ('light_gray_terracotta', -0.5, 8.0, 2.0, 1.0, 0.7, 1.6), ('black_concrete', -0.52, 8.4, 3.0, 1.04, 0.1, 0.1),
         ('light_gray_terracotta', -0.35, 2.9, -4.6, 0.7, 0.7, 2.7), ('light_gray_terracotta', -0.2, 2.9, -6.6, 0.4, 0.4, 2.1),
         ('gray_terracotta', -1.25, 0.0, -1.8, 0.75, 2.5, 0.75), ('gray_terracotta', 0.5, 0.0, -1.8, 0.75, 2.5, 0.75),
         ('gray_terracotta', -1.25, 0.0, 0.9, 0.75, 2.5, 0.75), ('gray_terracotta', 0.5, 0.0, 0.9, 0.75, 2.5, 0.75),
         ('gray_terracotta', -1.31, 3.3, -0.5, 2.62, 0.4, 0.6)]
PACHY = [('brown_terracotta', -0.38, 0.65, -0.65, 0.76, 0.6, 1.25), ('brown_terracotta', -0.2, 0.95, 0.5, 0.4, 0.4, 0.3),
         ('orange_terracotta', -0.28, 1.05, 0.65, 0.56, 0.45, 0.5), ('white_terracotta', -0.24, 1.48, 0.68, 0.48, 0.22, 0.42),
         ('black_terracotta', -0.3, 1.4, 0.62, 0.6, 0.06, 0.06), ('black_concrete', -0.29, 1.25, 1.1, 0.58, 0.06, 0.06),
         ('brown_terracotta', -0.13, 0.85, -1.55, 0.26, 0.26, 0.95), ('brown_terracotta', -0.3, 0.0, -0.1, 0.16, 0.7, 0.22),
         ('brown_terracotta', 0.14, 0.0, -0.1, 0.16, 0.7, 0.22)]

PB = ['# Portail de Terra Nova au lobby : construit par le hub (mg:hub/build, tools/lobby/gen_hub.py)', 'function mg:hub/build']
w('terra/portal_build', PB)
w('terra/spawn_clean', ['# Abords du portail : plus de découpe au spawn, le portail est au hub (tools/lobby/gen_hub.py)', 'data modify storage mg:lobby tvclean set value 1b'])
ENTER_SEL = (f'tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,'
             f'gamemode=adventure,x={PX},y=64,z={PZ - 1},dx=0,dy=2,dz=2')
w('terra/lobby_tick', ['# Chaque tick (core/tick, monde des mini-jeux) : portail de Terra Nova, session du monde',
                       f'execute if score $setup mg.st matches 1 as @a[{ENTER_SEL}] run function mg:terra/enter',
                       f'particle minecraft:dust{{color:[0.3,0.85,0.25],scale:1.1}} {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 3',
                       f'particle minecraft:spore_blossom_air {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 2',
                       f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {PX} 63 {PZ} minecraft:chiseled_tuff_bricks run function mg:terra/portal_build',
                       'execute unless score $tvw mg.st matches 1 if entity @a[tag=mg.tvw] run function mg:terra/session_start',
                       'execute if score $tvw mg.st matches 1 unless entity @a[tag=mg.tvw] run function mg:terra/session_end',
                       f'execute if score $tvw mg.st matches 1 in {DIM} run function mg:terra/tick'])
w('terra/pre_tick', ['# Avant la survie (core/tick) : un joueur de Terra Nova sorti de la dimension sans passer par la sortie perd ses tags',
                     f'execute as @a[tag=mg.tvw] at @s unless dimension {DIM} run function mg:terra/strayed'])
w('terra/strayed', ['# @s a quitté Terra Nova autrement (téléportation…) : retour au lobby complet, sauf s\'il est déjà dans une partie',
                     'tag @s remove mg.tvw', 'tag @s remove mg.surv', 'function mg:terra/mis_clear', 'function mg:terra/traps_clear', 'function mg:terra/untag',
                     'function mg:terra/rpg/leave',
                     'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] in minecraft:overworld run function mg:core/reset_player',
                     'attribute @s minecraft:fall_damage_multiplier base set 0'])
w('terra/traps_clear', ['# @s part : ses pièges disparaissent', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                        'execute as @e[tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run kill @s', 'execute as @e[tag=mg.tvtrapd] if score @s mg.tvo = $own mg.st run kill @s'])

# ================================================================ entrée, sortie, session
w('terra/enter', ['# @s entre dans le portail de Terra Nova (contexte : monde des mini-jeux)',
                  'execute unless data storage mg:terra built run return run function mg:terra/not_ready',
                  'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Terra Nova sera accessible après.","color":"red"}',
                  'function mg:lobkart/leave', 'function mg:parkour/quit',
                  'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
                  'tag @s add mg.surv', 'tag @s add mg.tvw',
                  'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc',
                  'execute if score $state mg.st matches 0 run function mg:vote/refresh',
                  'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
                  'attribute @s minecraft:fall_damage_multiplier base set 1',
                  'function mg:terra/join', 'function mg:core/heal',
                  f'execute in {DIM} run spawnpoint @s {int(MED[0])} {MED[1]} {int(MED[2])}',
                  f'execute in {DIM} run tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]} 180 0',
                  'scoreboard players set @s mg.tvnet 0', 'scoreboard players set @s mg.tvtr 0', 'tag @s remove mg.trkb',
                  'function mg:terra/kit', 'function mg:terra/rpg/cl/bonus',
                  'title @s times 10 60 20', 'title @s title {"text":"TERRA NOVA","color":"green","bold":true}', 'function mg:terra/rpg/enter',
                  'title @s subtitle {"text":"Il y a 85 millions d\'années…","color":"gray"}',
                  'tellraw @s ' + js([{'text': '🦖 TERRA NOVA', 'color': 'green', 'bold': True}, {'text': ' : bienvenue dans la colonie, colon !', 'color': 'yellow'}]),
                  'tellraw @s ' + js([{'text': ' 📋 Missions : ', 'color': 'gold'}, {'text': 'tableau sur le mur du QG (nord-est de la place), récompenses en crédits ₵', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🛒 Équipement : ', 'color': 'aqua'}, {'text': 'dépôt au nord-ouest (canon sonique, filets, pièges, armure…)', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🔫 Armes : ', 'color': 'yellow'}, {'text': 'bâton électrique (étourdit), fusil à impulsions (clic droit, gare à la surchauffe)', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' ✚ Infirmerie : ', 'color': 'red'}, {'text': 'au sud-est, soigne. Mort = -10 % de tes crédits', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🚪 Sortir : ', 'color': 'light_purple'}, {'text': 'portail du temps (sud-ouest) ou Échap → ≡ Menu', 'color': 'gray'}]),
                  'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.8'])
w('terra/not_ready', ['# Terra Nova pas encore construite : on recule le joueur', f'tp @s {PX + 3}.5 64 {PZ}.5 90 0',
                      'tellraw @s {"text":"🚧 Terra Nova est en construction (quelques minutes après le démarrage du serveur). Réessaie bientôt !","color":"yellow"}'])
w('terra/menu_go', ['# @s : « Aller à Terra Nova » du menu Échap (trigger mg.sv 7), d\'où qu\'on soit hors partie',
                    'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup","color":"red"}',
                    'execute unless data storage mg:terra built run return run tellraw @s {"text":"🚧 Terra Nova est en construction, réessaie bientôt.","color":"yellow"}',
                    'execute if entity @s[tag=mg.tvw] run return run tellraw @s {"text":"Tu es déjà à Terra Nova.","color":"gray"}',
                    'execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Terra Nova sera accessible après.","color":"red"}',
                    'execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Terra Nova sera accessible après.","color":"red"}',
                    'execute if entity @s[tag=mg.surv] run function mg:survie/leave',
                    'execute in minecraft:overworld run function mg:terra/enter'])
w('terra/join', ['# @s : réglages d\'arrivée (les crédits sont gardés d\'une visite à l\'autre)',
                 'execute unless score @s mg.tvpid matches 1.. run scoreboard players add $tvpn mg.st 1',
                 'execute unless score @s mg.tvpid matches 1.. run scoreboard players operation @s mg.tvpid = $tvpn mg.st',
                 'execute unless score @s mg.tvc matches -2147483648.. run scoreboard players set @s mg.tvc 0',
                 'function mg:terra/mis_clear',
                 'scoreboard players set @s mg.tvh 0', 'scoreboard players set @s mg.tvcd 0', 'scoreboard players set @s mg.tvsc 0',
                 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tval 0', 'scoreboard players set @s mg.deaths 0',
                 'scoreboard players set @s mg.tvkr 0', 'scoreboard players set @s mg.tvkc 0', 'scoreboard players set @s mg.tvkb 0',
                 'scoreboard players set @s mg.tvkg 0', 'scoreboard players set @s mg.tvdd 0', 'scoreboard players reset @s mg.tvq',
                 'scoreboard players enable @s mg.tvms', 'tag @s remove mg.tvoh', 'tag @s remove mg.tvout',
                 'team add mg_tv', 'team modify mg_tv friendlyFire false', 'team modify mg_tv color dark_green', 'team join mg_tv @s',
                 'function mg:terra/rpg/join'])
w('terra/untag', ['# @s : plus joueur de Terra Nova (tags, titres, recharges)', 'tag @s remove mg.tvout', 'tag @s remove mg.tvoh', 'tag @s remove mg.tvin2',
                  'title @s clear', 'title @s reset', 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tvh 0',
                  'effect clear @s minecraft:slowness', 'team leave @s'])
w('terra/leave', ['# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)',
                  'execute unless entity @s[tag=mg.tvw] run return 0',
                  'tag @s remove mg.tvw', 'tag @s remove mg.surv', 'function mg:terra/mis_clear', 'function mg:terra/traps_clear', 'function mg:terra/untag',
                  'function mg:terra/rpg/leave', 'function mg:core/reset_player', 'attribute @s minecraft:fall_damage_multiplier base set 0',
                  'tellraw @s [{"text":"⌂ Retour au lobby. Tes crédits restent à Terra Nova : ","color":"gold"},'
                  '{"score":{"name":"@s","objective":"mg.tvc"},"color":"green","bold":true},{"text":" ₵","color":"green"}]'])
w('terra/session_start', ['# Premier joueur à Terra Nova : chargement de la carte, entités dans 1,5 s',
                          'scoreboard players set $tvw mg.st 1', 'scoreboard players add $tvses mg.st 1', 'scoreboard players set $tvt mg.st 0', 'scoreboard players set $tvsu mg.st 0',
                          f'execute in {DIM} run forceload add {FL}'] + [f'execute in {DIM} run forceload add {f}' for f in FL_REGIONS.values()] +
  ['schedule function mg:terra/session_setup 30t', 'schedule function mg:terra/rpg/setup_s 100t'])
w('terra/rpg/setup_s', ['# Session : entités du RPG (régions chargées)', 'execute unless score $tvw mg.st matches 1 run return 0',
                        f'execute in {DIM} run function mg:terra/rpg/setup'])
w('terra/session_setup', ['# Session : entités de Terra Nova (dans la dimension)',
                          'execute unless score $tvw mg.st matches 1 run return 0', f'execute in {DIM} run function mg:terra/setup_in'])
w('terra/session_end', ['# Plus personne à Terra Nova : entités retirées, outposts réparés, plus de chargement forcé',
                        'scoreboard players set $tvw mg.st 0', 'scoreboard players set $tvsu mg.st 0', 'schedule clear mg:terra/session_setup',
                        'function mg:terra/clear', 'team remove mg_tv'] +
  [f'execute in {DIM} run function mg:terra/out_build_{k}' for k in range(1, 4)] +
  [f'execute in {DIM} run forceload remove {FL}'] + [f'execute in {DIM} run forceload remove {f}' for f in FL_REGIONS.values()] +
  ['schedule clear mg:terra/rpg/setup_s'])
w('terra/clear', ['# Retire tout ce que Terra Nova a posé (entités, objets au sol, barres)', 'kill @e[tag=mg.tv]', 'function mg:terra/rpg/clear',
                  f'execute in {DIM} run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                  f'execute in {DIM} run kill @e[type=minecraft:experience_orb,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                  'bossbar remove mg:tvcarno'] + [f'bossbar remove mg:tvo{k}' for k in range(1, 4)] +
  [f'scoreboard players set $tvo{k} mg.st 0' for k in range(1, 4)])
RULES = [f'execute in {DIM} run difficulty normal', f'execute in {DIM} run gamerule spawn_mobs false',
         f'execute in {DIM} run gamerule mob_griefing false', f'execute in {DIM} run gamerule keep_inventory true',
         f'execute in {DIM} run gamerule immediate_respawn true', f'execute in {DIM} run gamerule advance_time false',
         f'execute in {DIM} run gamerule advance_weather false', f'execute in {DIM} run time set 2000', f'execute in {DIM} run weather clear']
w('terra/rules', ['# Règles du monde de Terra Nova (propres à la dimension sur Paper) : jour fixe, pas d\'apparitions naturelles, inventaire gardé'] + RULES)

# ---------------------------------------------------------------- entités de la session
def tdisp(x, y, z, text, scale=1.0, bg=1140850688, extra=''):
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.tv"],billboard:"vertical",text:{js(text)},background:{bg},'
            f'{TR % (0, 0, 0, scale, scale, scale)}{extra}}}')


PAD = {'sonic': (1, '📢 Canon sonique', 'aqua', 150, 'minecraft:goat_horn'), 'mk2': (2, '🔫 Fusil à impulsions Mk2', 'gold', 220, 'minecraft:crossbow'),
       'net': (3, '🕸 Lance-filets (+3 filets)', 'white', 80, 'minecraft:fishing_rod'), 'netx': (4, '🕸 Filets ×3', 'white', 25, 'minecraft:cobweb'),
       'trap': (5, '⚙ Pièges au sol ×3', 'gray', 45, 'minecraft:tripwire_hook'), 'med': (6, '✚ Trousses de soins ×2', 'red', 15, 'minecraft:golden_apple'),
       'armor': (7, '🛡 Armure de patrouille', 'dark_aqua', 100, 'minecraft:chainmail_chestplate'),
       'saddle': (8, '🐴 Selle de brachiosaure', 'yellow', 40, 'minecraft:saddle')}
SU = ['# Session (dans la dimension) : panneaux, présentoirs, tableau, marqueurs, herbivores, barres',
      '# reste d\'une session interrompue (/reload, arrêt du serveur) : tout est retiré avant', 'function mg:terra/clear', 'function mg:terra/shop_fix',
      'execute as @a[tag=mg.tvw] run function mg:terra/mis_clear', 'function mg:terra/rules',
      f'summon minecraft:marker {EXITA[0] + 0.5} 65 {EXITA[1] + 0.5} {{Tags:["mg.tv","mg.tvexit"]}}',
      tdisp(0.5, 73, 0.5, [{'text': 'TERRA NOVA\n', 'color': 'green', 'bold': True}, {'text': 'Colonie humaine · il y a 85 millions d\'années', 'color': 'gray', 'bold': False}], 3.0),
      tdisp(-7.4, 70.4, -17.5, {'text': '🛒 DÉPÔT D\'ÉQUIPEMENT', 'color': 'aqua', 'bold': True}, 1.3),
      tdisp(9.4, 71.4, -17.5, {'text': '🏛 QG DE COMMANDEMENT', 'color': 'gold', 'bold': True}, 1.3),
      tdisp(7.4, 70.6, 17.5, [{'text': '✚ INFIRMERIE\n', 'color': 'red', 'bold': True}, {'text': 'reste à l\'intérieur pour te soigner', 'color': 'gray', 'bold': False}], 1.3),
      tdisp(EXITA[0] + 0.5, 72.6, EXITA[1] + 0.5, [{'text': '🌀 Portail du temps\n', 'color': 'light_purple', 'bold': True}, {'text': 'retour au spawn', 'color': 'gray', 'bold': False}], 1.2),
      tdisp(0.5, 75.6, -WALL + 0.5, {'text': '🚪 PORTE NORD', 'color': 'yellow', 'bold': True}, 1.5),
      tdisp(0.5, 75.6, WALL + 0.5, {'text': '🚪 PORTE SUD', 'color': 'yellow', 'bold': True}, 1.5),
      f'summon minecraft:text_display 8.4 67.4 -22.5 {{Tags:["mg.tv"],Rotation:[90f,0f],text:{js([{"text": "📋 MISSIONS\n", "color": "gold", "bold": True}, {"text": "clic droit sur le tableau", "color": "gray", "bold": False}])},background:-1442840576,{TR % (0, 0, 0, 1.2, 1.2, 1.2)}}}',
      'summon minecraft:interaction 8.8 65 -22.5 {Tags:["mg.tv","mg.tvboard"],width:2.6f,height:3.2f,response:1b}',
      'summon minecraft:villager -15.5 65 -22.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],'
      'VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},'
      f'CustomName:{js({"text": "🛒 Intendant", "color": "gold"})},CustomNameVisible:1b}}',
      'summon minecraft:villager 20.5 65 17.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[90f,0f],'
      'VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},'
      f'CustomName:{js({"text": "✚ Médecin", "color": "red"})},CustomNameVisible:1b}}']
for (x, key) in PADS:
    code, lab, col, price, it = PAD[key]
    SU += [f'summon minecraft:item_display {x + 0.5} 66.7 -21.5 {{Tags:["mg.tv","mg.tvpdi"],item:{{id:"{it}",count:1}},billboard:"fixed",{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}',
           tdisp(x + 0.5, 67.55, -21.5, [{'text': lab + '\n', 'color': col, 'bold': True}, {'text': f'{price} ₵', 'color': 'green', 'bold': False}], 0.45),
           f'summon minecraft:interaction {x + 0.5} 65 -21.5 {{Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}}',
           f'scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk {code}', 'tag @e[tag=mg.tvn] remove mg.tvn']
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    SU.append(tdisp(ox + 0.5, OUT_H[name] + 5, oz + 0.5, [{'text': f'📡 Outpost {name}\n', 'color': 'aqua', 'bold': True}, {'text': 'générateur de la colonie', 'color': 'gray', 'bold': False}], 1.2))
for (x, z) in SPAWNS:
    SU.append(f'summon minecraft:marker {x + 0.5} {top(x, z)} {z + 0.5} {{Tags:["mg.tv","mg.tvsp"{",\"mg.tvfar\"" if (x, z) in FAR else ""}]}}')
for (x, z) in HERBS:
    SU.append(f'summon minecraft:marker {x + 0.5} {top(x, z)} {z + 0.5} {{Tags:["mg.tv","mg.tvhp"]}}')
for i, (x, z) in enumerate(HERBS):
    SU.append(f'execute positioned {x + 0.5} {top(x, z)} {z + 0.5} run function mg:terra/dino/{"brachio" if i < 3 else "pachy"}')
SU += ['bossbar add mg:tvcarno {"text":"🦖 Carnotaure","color":"red"}', 'bossbar set mg:tvcarno color red', 'bossbar set mg:tvcarno style notched_10',
       'bossbar set mg:tvcarno max 160', 'bossbar set mg:tvcarno players']
for k, (name, _, _) in enumerate(OUTPOSTS, 1):
    SU += [f'bossbar add mg:tvo{k} {js({"text": f"🛡 Outpost {name}", "color": "aqua"})}', f'bossbar set mg:tvo{k} color blue',
           f'bossbar set mg:tvo{k} style notched_10', f'bossbar set mg:tvo{k} max 100', f'bossbar set mg:tvo{k} players',
           f'scoreboard players set $tvo{k} mg.st 0']
SU += ['# équipe des colons recréée (session_end la retire ; un joueur reconnecté n\'est pas repassé par enter)',
       'team add mg_tv', 'team modify mg_tv friendlyFire false', 'team modify mg_tv color dark_green', 'team join mg_tv @a[tag=mg.tvw]',
       'scoreboard players set $tvcc mg.st 90', 'scoreboard players set $tvpk mg.st 3', 'scoreboard players set $tvsu mg.st 1']
w('terra/setup_in', SU)
