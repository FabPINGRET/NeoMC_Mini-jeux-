# Neo GTA, monde : construction de la ville, portail du lobby, entrée / sortie / session : exécuté par gen_gta.py (exec) à sa place d'origine.
# Utilise : AREA, DIM, FL, FL2, HX, INTER, js, NA, NG, NH, NP, NZ, OLD_P, PX, PZ, TR, VFRONT, VY, w, YT, Z

# ---------------------------------------------------------------- construction et réparation de la ville (dans mg:gta)
WB = ['# Une étape de construction de Neo City par tick ($gwb), dans la dimension mg:gta. Planifiée.',
      'scoreboard players add $gwb mg.st 1']
WB += [f'execute if score $gwb mg.st matches {i} in {DIM} run function mg:bomber/b/g{i}' for i in range(1, NG + 1)]
WB += [f'execute if score $gwb mg.st matches {NG + i} in {DIM} run function mg:bomber/b/p{i}' for i in range(1, NP + 1)]
WB += [f'execute if score $gwfull mg.st matches 1 if score $gwb mg.st matches {NG + NP + i} in {DIM} run function mg:gta/villa/p{i}' for i in range(1, NH['parts'] + 1)]   # Neo Hills : construction complète seulement
WB += [f'execute if score $gwb mg.st matches {NG + NP + NH["parts"] + 1} run function mg:gta/wb_done',
       f'execute if score $gwb mg.st matches ..{NG + NP + NH["parts"]} run schedule function mg:gta/wb_step 1t']
w('gta/wb_step', WB)
w('gta/wb_done', ['# Ville prête : murs invisibles, drapeau, plus de chargement forcé si personne ne joue',
                  f'execute in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                  f'execute in {DIM} run function mg:gta/walls',
                  f'execute in {DIM} if block 0 58 {Z} minecraft:stone run data modify storage mg:gta built set value 1b',
                  f'execute unless score $gtw mg.st matches 1 in {DIM} run forceload remove {FL}',
                  f'execute unless score $gtw mg.st matches 1 in {DIM} run forceload remove {FL2}'])
w('gta/world_build', ['# Première construction de Neo City (ou reconstruction complète)',
                      f'execute in {DIM} run forceload add {FL}', f'execute in {DIM} run forceload add {FL2}', 'scoreboard players set $gwb mg.st 0',
                      'scoreboard players set $gwfull mg.st 1',
                      'schedule function mg:gta/wb_step 40t'])
w('gta/walls', ['# Bord de la carte et plafond des hélicos (barrières)',
                f'fill -{HX} {YT} {Z - HX} {HX} {YT} {Z + HX} minecraft:barrier',
                f'fill {-HX - 1} 57 {Z - HX - 1} {-HX - 1} {YT - 1} {Z + HX + 1} minecraft:barrier',
                f'fill {HX + 1} 65 {Z - HX - 1} {HX + 1} {YT - 1} {Z + HX + 1} minecraft:barrier',
                f'fill {-HX} 57 {Z - HX - 1} {NA[0] - 1} {YT - 1} {Z - HX - 1} minecraft:barrier',   # nord : ouvert sur Neo Hills
                f'fill {NA[2] + 1} 57 {Z - HX - 1} {HX} {YT - 1} {Z - HX - 1} minecraft:barrier',
                f'fill {-HX} 57 {Z + HX + 1} {HX} {YT - 1} {Z + HX + 1} minecraft:barrier',
                # Neo Hills : trouée dans le mur nord (avenue 20), enceinte et plafond du domaine
                f'fill 17 65 {Z - HX - 1} 23 65 {Z - HX - 1} minecraft:polished_andesite_slab',
                f'fill {NA[0] - 1} 57 {Z + NZ} {NA[0] - 1} {YT - 1} {Z - HX - 2} minecraft:barrier',
                f'fill {NA[2] + 1} 57 {Z + NZ} {NA[2] + 1} {YT - 1} {Z - HX - 2} minecraft:barrier',
                f'fill {NA[0] - 1} 57 {Z + NZ} {NA[2] + 1} {YT - 1} {Z + NZ} minecraft:barrier',
                f'fill {NA[0] - 1} {YT} {Z + NZ} {NA[2] + 1} {YT} {Z - HX - 2} minecraft:barrier'])

# ---------------------------------------------------------------- portail du lobby (monde des mini-jeux)
PB = ['# Portail de Neo GTA au lobby (avenue nord, côté est), reconstruit par mg:gta/lobby_tick s\'il disparaît',
      'kill @e[tag=mg.gtap]',
      f'fill {OLD_P[0] - 4} 64 {OLD_P[1] - 4} {OLD_P[0] + 4} 73 {OLD_P[1] + 4} minecraft:air',
      f'fill {OLD_P[0] - 4} 63 {OLD_P[1] - 4} {OLD_P[0] + 4} 63 {OLD_P[1] + 4} minecraft:grass_block',
      f'fill {PX - 4} 64 {PZ - 4} {PX + 4} 73 {PZ + 4} minecraft:air',
      f'fill {PX - 4} 63 {PZ - 4} {PX + 4} 63 {PZ + 4} minecraft:polished_blackstone_bricks',
      f'fill {PX - 3} 63 {PZ - 3} {PX + 3} 63 {PZ + 3} minecraft:black_concrete',
      f'fill {PX - 4} 63 {PZ} {PX - 1} 63 {PZ} minecraft:yellow_concrete']
for k in range(-4, 5, 2):                                     # bandes jaunes et noires (chantier) sur le pourtour
    PB += [f'setblock {PX + k} 63 {PZ - 4} minecraft:yellow_concrete', f'setblock {PX + k} 63 {PZ + 4} minecraft:yellow_concrete',
           f'setblock {PX - 4} 63 {PZ + k} minecraft:yellow_concrete', f'setblock {PX + 4} 63 {PZ + k} minecraft:yellow_concrete']
PB += [f'fill {PX} 64 {PZ - 2} {PX} 69 {PZ - 2} minecraft:black_concrete', f'fill {PX} 64 {PZ + 2} {PX} 69 {PZ + 2} minecraft:black_concrete',
       f'fill {PX} 70 {PZ - 2} {PX} 70 {PZ + 2} minecraft:black_concrete',
       f'fill {PX} 64 {PZ - 3} {PX} 70 {PZ - 3} minecraft:yellow_concrete', f'fill {PX} 64 {PZ + 3} {PX} 70 {PZ + 3} minecraft:yellow_concrete',
       f'fill {PX} 71 {PZ - 3} {PX} 71 {PZ + 3} minecraft:yellow_concrete',
       f'setblock {PX} 72 {PZ - 3} minecraft:redstone_lamp[lit=true]', f'setblock {PX} 72 {PZ + 3} minecraft:redstone_lamp[lit=true]',
       f'setblock {PX - 1} 71 {PZ - 3} minecraft:end_rod[facing=west]', f'setblock {PX - 1} 71 {PZ + 3} minecraft:end_rod[facing=west]',
       f'setblock {PX} 63 {PZ} minecraft:chiseled_polished_blackstone',
       # haie de l'avenue ouverte devant le portail, passage pavé jusqu'à l'avenue (x 4 à 8)
       f'fill 4 64 {PZ - 1} {PX - 1} 66 {PZ + 1} minecraft:air', f'fill 4 63 {PZ - 1} {PX - 5} 63 {PZ + 1} minecraft:stone_bricks',
       f'setblock {PX - 3} 64 {PZ - 4} minecraft:iron_bars', f'setblock {PX - 3} 65 {PZ - 4} minecraft:iron_bars', f'setblock {PX - 3} 66 {PZ - 4} minecraft:lantern',
       f'setblock {PX - 3} 64 {PZ + 4} minecraft:iron_bars', f'setblock {PX - 3} 65 {PZ + 4} minecraft:iron_bars', f'setblock {PX - 3} 66 {PZ + 4} minecraft:lantern',
       f'summon minecraft:text_display {PX - 0.6} 72.6 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "🚓 NEO GTA", "color": "gold", "bold": True})},'
       f'background:-1442840576,{TR % (0, 0, 0, 2.6, 2.6, 2.6)}}}',
       f'summon minecraft:text_display {PX - 0.6} 72.15 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "Monde GTA libre : armes, voitures, hélicos, police", "color": "gray"})},'
       f'background:0,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
       f'summon minecraft:text_display {PX - 0.6} 64.4 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "▶ entre dans le portail", "color": "yellow"})},'
       f'background:0,{TR % (0, 0, 0, 0.8, 0.8, 0.8)}}}']
# petit taxi garé à côté du portail
for (blk, tx, ty, tz, sx, sy, sz) in [('yellow_concrete', -0.95, 0.05, -1.7, 1.9, 0.75, 3.4), ('black_concrete', -0.8, 0.8, -0.9, 1.6, 0.65, 1.7),
                                       ('yellow_concrete', -0.3, 1.45, -0.3, 0.6, 0.2, 0.6), ('black_concrete', -1.0, 0.0, -1.25, 0.25, 0.45, 0.6),
                                       ('black_concrete', 0.75, 0.0, -1.25, 0.25, 0.45, 0.6), ('black_concrete', -1.0, 0.0, 0.85, 0.25, 0.45, 0.6),
                                       ('black_concrete', 0.75, 0.0, 0.85, 0.25, 0.45, 0.6)]:
    PB.append(f'summon minecraft:block_display {PX + 2.5} 64 {PZ + 0.5} {{Tags:["mg.gtap"],block_state:{{Name:"minecraft:{blk}"}},{TR % (tx, ty, tz, sx, sy, sz)}}}')
PB.append('function mg:gta/spawn_clean')
w('gta/portal_build', PB)
# restes de l'arbre écrasé par le portail + bordure de l'avenue nord dégagée devant le portail (on voit qu'on peut passer)
w('gta/spawn_clean', ['# Abords du portail de Neo City au spawn : feuillage/troncs coupés autour du portail, bordure de l\'avenue (x 4) dégagée',
                      f'fill {PX - 4} 64 {PZ - 8} {PX + 4} 76 {PZ + 8} minecraft:air replace #minecraft:leaves',
                      f'fill {PX - 4} 64 {PZ - 8} {PX + 4} 76 {PZ + 8} minecraft:air replace #minecraft:logs',
                      # haie, banc et lampadaire de la bordure est de l'avenue, de z {PZ - 7} à {PZ + 4} (avant la place)
                      f'fill 4 64 {PZ - 7} 4 72 {PZ + 4} minecraft:air',
                      # bordure pavée face au portail, raccord avec le passage existant
                      f'fill 4 63 {PZ - 4} 4 63 {PZ + 4} minecraft:stone_bricks',
                      f'fill 4 63 {PZ - 1} {PX - 5} 63 {PZ + 1} minecraft:stone_bricks',
                      'data modify storage mg:lobby gtaclean set value 1b'])
w('gta/lobby_tick', ['# Chaque tick (core/tick, monde des mini-jeux) : portail de Neo City, session du monde GTA',
                     f'execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x={PX},y=64,z={PZ - 1},dx=0,dy=2,dz=2] run function mg:gta/enter',
                     f'particle minecraft:dust{{color:[1.0,0.82,0.1],scale:1.1}} {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 3',
                     f'particle minecraft:portal {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0.3 4',
                     f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {PX} 63 {PZ} minecraft:chiseled_polished_blackstone run function mg:gta/portal_build',
                     'execute unless score $gtw mg.st matches 1 if entity @a[tag=mg.gtw] run function mg:gta/session_start',
                     'execute if score $gtw mg.st matches 1 unless entity @a[tag=mg.gtw] run function mg:gta/session_end',
                     'execute if score $gtw mg.st matches 1 run function mg:gta/tick'])
w('gta/pre_tick', ['# Avant la survie (core/tick) : un joueur du GTA sorti de la dimension sans passer par la sortie perd ses tags',
                   f'execute as @a[tag=mg.gtw] at @s unless dimension {DIM} run function mg:gta/strayed'])
w('gta/strayed', ['# @s a quitté Neo City autrement (téléportation…) : il n\'est plus considéré comme joueur du GTA',
                  'tag @s remove mg.gtw', 'tag @s remove mg.surv', 'function mg:gta/untag'])

# ---------------------------------------------------------------- entrée, sortie, session
P_LINES = ['# @s : à un carrefour au hasard de Neo City (dans la dimension du contexte)',
           f'execute store result score $gr mg.st run random value 0..{len(INTER) - 1}']
P_LINES += [f'execute if score $gr mg.st matches {i} run tp @s {x + 0.5} 65 {Z + z + 0.5}' for i, (x, z) in enumerate(INTER)]
w('gta/place', P_LINES)
w('gta/enter', ['# @s entre dans le portail de Neo City',
                'execute unless data storage mg:gta built run return run function mg:gta/not_ready',
                'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Neo GTA sera accessible après.","color":"red"}',
                'function mg:lobkart/leave', 'function mg:parkour/quit',
                'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
                'tag @s add mg.surv', 'tag @s add mg.gtw',
                'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc',
                'execute if score $state mg.st matches 0 run function mg:vote/refresh',
                'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
                'attribute @s minecraft:fall_damage_multiplier base set 1',
                'function mg:gta/join', 'function mg:core/heal',
                f'execute in {DIM} run spawnpoint @s {VFRONT[0]} {VY} {Z + VFRONT[1]}',
                f'execute in {DIM} run tp @s {VFRONT[0] + 0.5} {VY} {Z + VFRONT[1] + 0.5} 180 0',
                'function mg:gta/kit',
                'title @s times 10 50 20', 'title @s title {"text":"NEO GTA","color":"gold","bold":true}',
                'title @s subtitle {"text":"Deviens le plus riche de Neo City","color":"gray"}',
                'tellraw @s ' + js([{'text': '🚓 NEO GTA', 'color': 'gold', 'bold': True}, {'text': ' : deviens le plus riche de la ville', 'color': 'yellow'}]),
                'tellraw @s ' + js([{'text': ' 💵 Gagner : ', 'color': 'green'}, {'text': 'accroupi + arme en main pour braquer passants, commerces, banque ; missions au 📱', 'color': 'gray'}]),
                'tellraw @s ' + js([{'text': ' 🔫 Armes : ', 'color': 'gold'}, {'text': 'clic gauche tirer, clic droit viser, accroupi recharger', 'color': 'gray'}]),
                'tellraw @s ' + js([{'text': ' 🔫 Dépenser : ', 'color': 'aqua'}, {'text': 'armurerie et concession au parc, tout ce qui est acheté est gratuit à la villa', 'color': 'gray'}]),
                'tellraw @s ' + js([{'text': ' ★ Police : ', 'color': 'red'}, {'text': 'chaque crime = étoile, une de moins toutes les 15 s', 'color': 'gray'}]),
                'tellraw @s ' + js([{'text': ' 🚪 Sortir : ', 'color': 'yellow'}, {'text': 'Échap → ≡ Menu', 'color': 'gray'}]),
                'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6'])
w('gta/not_ready', ['# Neo City pas encore construite : on recule le joueur', f'tp @s {PX - 3}.5 64 {PZ + 0.5} -90 0',
                    'tellraw @s {"text":"🚧 Neo GTA est en construction (environ 2 minutes après le démarrage du serveur). Réessaie bientôt !","color":"yellow"}'])
w('gta/menu_go', ['# @s : « Aller dans Neo GTA » du menu Échap (trigger mg.sv 4), d\'où qu\'on soit hors partie',
                  'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup","color":"red"}',
                  'execute if entity @s[tag=mg.gtw] run return run tellraw @s {"text":"Tu es déjà dans Neo GTA.","color":"gray"}',
                  'execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Neo GTA sera accessible après.","color":"red"}',
                  'execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Neo GTA sera accessible après.","color":"red"}',
                  'execute if entity @s[tag=mg.surv] run function mg:survie/leave',
                  'execute in minecraft:overworld run function mg:gta/enter'])
w('gta/join', ['# @s : réglages d\'arrivée (les dollars sont gardés d\'une visite à l\'autre)',
               'tag @s add mg.gtg', 'execute unless score @s mg.gta matches -2147483648.. run scoreboard players set @s mg.gta 0',
               'scoreboard players set @s mg.gwl 0', 'scoreboard players set @s mg.gwt 0', 'scoreboard players set @s mg.grk 0',
               'scoreboard players add $bidn mg.st 1', 'scoreboard players operation @s mg.bid = $bidn mg.st',
               'scoreboard players reset @s mg.gkp', 'scoreboard players reset @s mg.gkv', 'scoreboard players reset @s mg.gks',
               'scoreboard players reset @s mg.gkw', 'scoreboard players reset @s mg.gqs', 'scoreboard players set @s mg.deaths 0',
               'function mg:gun/reset', 'scoreboard players set @s mg.gtl 0', 'scoreboard players set @s mg.gal 0', 'tag @s remove mg.gdrv',
               'team join mg_gciv @s'])
w('gta/untag', ['# @s : plus joueur du GTA (tags, sons, titres, étoiles, mission)', 'function mg:gta/mis_clean', 'tag @s remove mg.gtg', 'tag @s remove mg.gclub', 'tag @s remove mg.gdrv',
                'tag @s remove mg.gscope', 'tag @s remove mg.grd', 'tag @s remove mg.gro', 'stopsound @s record',
                'title @s clear', 'title @s reset', 'scoreboard players reset @s mg.gwl', 'scoreboard players reset @s mg.gwt',
                'function mg:gun/reset', 'team leave @s'])
w('gta/leave', ['# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)',
                'execute unless entity @s[tag=mg.gtw] run return 0',
                'tag @s remove mg.gtw', 'tag @s remove mg.surv', 'function mg:gta/untag',
                'function mg:core/reset_player', 'attribute @s minecraft:fall_damage_multiplier base set 0',
                'tellraw @s [{"text":"⌂ Retour au lobby. Tes dollars restent à Neo City : ","color":"gold"},'
                '{"score":{"name":"@s","objective":"mg.gta"},"color":"green","bold":true},{"text":" $","color":"green"}]'])
w('gta/session_start', ['# Premier joueur à Neo City : chargement de la ville, entités dans 1,5 s',
                        'scoreboard players set $gtw mg.st 1', 'scoreboard players set $gtt mg.st 0',
                        f'execute in {DIM} run forceload add {FL}', f'execute in {DIM} run forceload add {FL2}', 'schedule function mg:gta/session_setup 30t'])
w('gta/session_setup', ['# Session : entités de Neo City (dans la dimension)',
                        'execute unless score $gtw mg.st matches 1 run return 0', f'execute in {DIM} run function mg:gta/setup_in'])
w('gta/session_end', ['# Plus personne à Neo City : entités retirées, ville réparée en tâche de fond, puis plus de chargement forcé',
                      'scoreboard players set $gtw mg.st 0', 'scoreboard players set $gsu mg.st 0', 'schedule clear mg:gta/session_setup', 'function mg:gta/clear',
                      'function mg:gta/bars_remove', 'team remove mg_gciv',
                      f'scoreboard players set $gwb mg.st {NG}', 'scoreboard players set $gwfull mg.st 0', 'schedule function mg:gta/wb_step 20t'])
w('gta/clear', ['# Retire tout ce que le GTA a posé (entités, objets au sol, flèches)', 'kill @e[tag=mg.gta]',
                f'execute in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                f'execute in {DIM} run kill @e[type=minecraft:item,{AREA}]',
                f'execute in {DIM} run kill @e[type=#minecraft:arrows,{AREA}]',
                f'execute in {DIM} run kill @e[type=minecraft:experience_orb,{AREA}]'])
