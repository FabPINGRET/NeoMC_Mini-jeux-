# Lancement effectif (@s = demandeur, mg.go = id)

scoreboard players operation $game mg.st = @s mg.go
scoreboard players reset @s mg.go
# [variantes] ids 100..196 : carte d'un autre jeu + difficulté ($ar, $dif) ; $ar = 0 → carte native
scoreboard players set $ar mg.st 0
scoreboard players set $dif mg.st 2
execute if score $game mg.st matches 100..196 run function mg:var/remap
scoreboard players operation $rgid mg.st = $game mg.st
# Kart : 61 = Circuit Champignon, 62 = Royaume Koopa → jeu 61 + circuit $ktr
scoreboard players set $ktr mg.st 1
execute if score $game mg.st matches 62 run scoreboard players set $ktr mg.st 2
scoreboard players set $kbat mg.st 0
execute if score $game mg.st matches 63 run scoreboard players set $kbat mg.st 1
execute if score $game mg.st matches 63 run scoreboard players set $ktr mg.st 3
execute if score $game mg.st matches 63 run scoreboard players set $game mg.st 61
execute if score $game mg.st matches 62 run scoreboard players set $game mg.st 61

# TNT Tag : 27 = carte au hasard, 67 = classique, 68 Collines, 69 Canyon, 70 Village perché → jeu 27 + carte $ttm (0..3)
execute if score $game mg.st matches 27 store result score $ttm mg.st run random value 0..3
execute if score $game mg.st matches 67..70 run scoreboard players operation $ttm mg.st = $game mg.st
execute if score $game mg.st matches 67..70 run scoreboard players remove $ttm mg.st 67
execute if score $game mg.st matches 67..70 run scoreboard players set $game mg.st 27
# Bedwars : 4 = carte au hasard, 71 = classique, 72 Caldeira, 73 Hanami, 74 Banquise → jeu 4 + carte $bwm (0..3)
execute if score $game mg.st matches 4 store result score $bwm mg.st run random value 0..3
execute if score $game mg.st matches 71..74 run scoreboard players operation $bwm mg.st = $game mg.st
execute if score $game mg.st matches 71..74 run scoreboard players remove $bwm mg.st 71
execute if score $game mg.st matches 71..74 run scoreboard players set $game mg.st 4
# Élytra : 75 course d'anneaux, 76 course + combat, 77 survie en vol, 78 mode au hasard → jeu 75 + mode $elm (1..3)
execute if score $game mg.st matches 78 store result score $elm mg.st run random value 1..3
execute if score $game mg.st matches 75..77 run scoreboard players operation $elm mg.st = $game mg.st
execute if score $game mg.st matches 75..77 run scoreboard players remove $elm mg.st 74
execute if score $game mg.st matches 75..78 run scoreboard players set $game mg.st 75

# Block Party : 28 = carrés, 91 = bandes, 92 = mixte → jeu 28 + sol $bpm (0..2)
execute if score $game mg.st matches 28 run scoreboard players set $bpm mg.st 0
execute if score $game mg.st matches 91 run scoreboard players set $bpm mg.st 1
execute if score $game mg.st matches 92 run scoreboard players set $bpm mg.st 2
execute if score $game mg.st matches 91..92 run scoreboard players set $game mg.st 28
# Infection : 217 Bunker, 218 Laboratoire, 219 Manoir = joueurs contre mobs → jeu 98 / 211 / 213 + $infm 1
scoreboard players set $infm mg.st 0
execute if score $game mg.st matches 217..219 run scoreboard players set $infm mg.st 1
execute if score $game mg.st matches 217 run scoreboard players set $game mg.st 98
execute if score $game mg.st matches 218 run scoreboard players set $game mg.st 211
execute if score $game mg.st matches 219 run scoreboard players set $game mg.st 213

# Mini Party : 59 = 8 tours, 60 = 15 tours. Un jeu lancé hors Mini Party ($mpl) met fin à la partie en cours
execute unless score $mpl mg.st matches 1 run scoreboard players set $mp mg.st 0
execute if score $game mg.st matches 59 run scoreboard players set $mpmax mg.st 8
execute if score $game mg.st matches 60 run scoreboard players set $mpmax mg.st 15
execute if score $game mg.st matches 60 run scoreboard players set $game mg.st 59

# Mob Arena à thème : 8 nether, 9 end, 10 ultra hard, 11 volant, 12 araignée → jeu 6 + thème $mt (1..5)
scoreboard players set $sm mg.st 0
execute if score $game mg.st matches 14 run scoreboard players set $sm mg.st 1
execute if score $game mg.st matches 14 run scoreboard players set $game mg.st 7
execute if score $game mg.st matches 15..19 run scoreboard players operation $sm mg.st = $game mg.st
execute if score $game mg.st matches 15..19 run scoreboard players remove $sm mg.st 13
execute if score $game mg.st matches 15..19 run scoreboard players set $game mg.st 7
scoreboard players set $sg mg.st 0
execute if score $game mg.st matches 42 run scoreboard players set $sg mg.st 2
execute if score $game mg.st matches 42 run scoreboard players set $game mg.st 29
execute if score $game mg.st matches 21 run scoreboard players set $sg mg.st 1
execute if score $game mg.st matches 24 run scoreboard players set $sg mg.st 1
execute if score $game mg.st matches 25 run scoreboard players set $sg mg.st 1
execute if score $game mg.st matches 25 run scoreboard players set $game mg.st 23
execute if score $game mg.st matches 24 run scoreboard players set $game mg.st 22
execute if score $game mg.st matches 21 run scoreboard players set $game mg.st 20
scoreboard players set $pbm mg.st 0
execute if score $game mg.st matches 54 run scoreboard players set $pbm mg.st 1
execute if score $game mg.st matches 55 run scoreboard players set $pbm mg.st 2
execute if score $game mg.st matches 54..55 run scoreboard players set $game mg.st 36
scoreboard players set $om mg.st 0
execute if score $game mg.st matches 52 run scoreboard players set $om mg.st 1
execute if score $game mg.st matches 53 run scoreboard players set $om mg.st 2
execute if score $game mg.st matches 52..53 run scoreboard players set $game mg.st 26
scoreboard players set $qm mg.st 0
execute if score $game mg.st matches 43 run scoreboard players set $qm mg.st 5
execute if score $game mg.st matches 43 run scoreboard players set $game mg.st 31
execute if score $game mg.st matches 46 run scoreboard players set $qm mg.st 6
execute if score $game mg.st matches 46 run scoreboard players set $game mg.st 31
execute if score $game mg.st matches 49 run scoreboard players set $qm mg.st 7
execute if score $game mg.st matches 49 run scoreboard players set $game mg.st 31
execute if score $game mg.st matches 32..35 run scoreboard players operation $qm mg.st = $game mg.st
execute if score $game mg.st matches 32..35 run scoreboard players remove $qm mg.st 31
execute if score $game mg.st matches 32..35 run scoreboard players set $game mg.st 31
# Quake sniper : 79 = Ravin, 80 = Tours → $qm 8 / 9
execute if score $game mg.st matches 79 run scoreboard players set $qm mg.st 8
execute if score $game mg.st matches 80 run scoreboard players set $qm mg.st 9
execute if score $game mg.st matches 79..80 run scoreboard players set $game mg.st 31
# Course d'élytres : 66 = parcours au hasard, 81..82 = parcours 1..2 (81 Canyon du Couchant, 82 Pic Blanc) → jeu 66 + parcours $xc (0 = au hasard)
scoreboard players set $xc mg.st 0
execute if score $game mg.st matches 81..82 run scoreboard players operation $xc mg.st = $game mg.st
execute if score $game mg.st matches 81..82 run scoreboard players remove $xc mg.st 80
execute if score $game mg.st matches 81..82 run scoreboard players set $game mg.st 66
scoreboard players set $pm mg.st 0
execute if score $game mg.st matches 44..45 run scoreboard players set $pm mg.st 1
execute if score $game mg.st matches 47..48 run scoreboard players set $pm mg.st 2
execute if score $game mg.st matches 48 run scoreboard players set $game mg.st 13
execute if score $game mg.st matches 47 run scoreboard players set $game mg.st 3
execute if score $game mg.st matches 50..51 run scoreboard players set $pm mg.st 3
execute if score $game mg.st matches 51 run scoreboard players set $game mg.st 13
execute if score $game mg.st matches 50 run scoreboard players set $game mg.st 3
execute if score $game mg.st matches 45 run scoreboard players set $game mg.st 13
execute if score $game mg.st matches 44 run scoreboard players set $game mg.st 3
scoreboard players set $pc mg.st 0
execute if score $game mg.st matches 13 run scoreboard players set $pc mg.st 1
execute if score $game mg.st matches 13 run scoreboard players set $game mg.st 3
scoreboard players set $mt mg.st 0
execute if score $game mg.st matches 37..41 run scoreboard players operation $mt mg.st = $game mg.st
execute if score $game mg.st matches 37..41 run scoreboard players remove $mt mg.st 31
execute if score $game mg.st matches 37..41 run scoreboard players set $game mg.st 6
execute if score $game mg.st matches 8..12 run scoreboard players operation $mt mg.st = $game mg.st
execute if score $game mg.st matches 8..12 run scoreboard players remove $mt mg.st 7
execute if score $game mg.st matches 8..12 run scoreboard players set $game mg.st 6

# Participants = tous les joueurs initialisés hors pause et hors survie (Mini Party en cours : seulement ses participants)
execute unless score $mpl mg.st matches 1 run tag @a[tag=mg.init,tag=!mg.spectate,tag=!mg.surv] add mg.play
execute if score $mpl mg.st matches 1 run tag @a[tag=mg.init,tag=mg.mpp,tag=!mg.spectate,tag=!mg.surv] add mg.play
tag @a remove mg.out
execute store result score $n0 mg.st if entity @a[tag=mg.play]
execute if score $n0 mg.st matches 0 run tellraw @s [{"text":"Aucun participant (tout le monde est en pause ou en survie).","color":"red"}]
execute if score $n0 mg.st matches 0 run return run scoreboard players set $game mg.st 0
execute as @a[tag=mg.play,tag=mg.inplot] run function mg:plot/leave_game
execute as @a[tag=mg.play,tag=mg.visit] run function mg:plot/leave_game
# Activités du spawn : un participant en kart libre ou en élytres en sort sur place (avant la téléportation de prepare)
execute as @a[tag=mg.play,tag=mg.lk] run function mg:lobkart/leave
execute as @a[tag=mg.play,tag=mg.ely] run function mg:elytra/stop_quiet
execute as @a[tag=mg.play,tag=mg.elyf] run function mg:elytra/free_stop

# État : compte à rebours de 10 s
scoreboard players set $state mg.st 1
function mg:vote/clear
clear @a[tag=!mg.surv] minecraft:warped_fungus_on_a_stick
clear @a[tag=!mg.surv] minecraft:blaze_rod
clear @a[tag=!mg.surv] minecraft:wind_charge
clear @a[tag=!mg.surv] minecraft:snowball
scoreboard players reset @a mg.qs
scoreboard players reset @a mg.fw
scoreboard players reset @a mg.wc
scoreboard players reset @a mg.wd
scoreboard players set $timer mg.st 200
scoreboard players set @a mg.deaths 0
scoreboard players reset @a mg.us
tag @a remove mg.win

# Annonce
execute if score $game mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SPLEEF","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"TNT RUN","color":"red","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 3 if score $pm mg.st matches 1 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"POUSSIÈRE","color":"gold","bold":true},{"text":" (style Dust : Long A, Mid, tunnels B)","color":"gray"}]
execute if score $game mg.st matches 3 if score $pm mg.st matches 2 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"MIRAGE","color":"aqua","bold":true},{"text":" (style Mirage : Appartements, Mid, Fenêtre, Jungle)","color":"gray"}]
execute if score $game mg.st matches 3 if score $pm mg.st matches 3 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"NUKETOWN","color":"green","bold":true},{"text":" (style Nuketown : deux maisons face à face, bus au milieu)","color":"gray"}]
execute if score $game mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie d'","color":"gray"},{"text":"ARÈNE PVP","color":"yellow","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 4 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"BEDWARS","color":"light_purple","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 4 if score $bwm mg.st matches 1 run function mg:bedwars/map/info_1
execute if score $game mg.st matches 4 if score $bwm mg.st matches 2 run function mg:bedwars/map/info_2
execute if score $game mg.st matches 4 if score $bwm mg.st matches 3 run function mg:bedwars/map/info_3
execute if score $game mg.st matches 4 if score $bwm mg.st matches 0 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"CLASSIQUE","color":"light_purple","bold":true},{"text":" (4 îles de pierre autour du diamant)","color":"gray"}]
execute if score $game mg.st matches 75 if score $elm mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🪽 ÉLYTRA : COURSE D'ANNEAUX","color":"aqua","bold":true},{"text":" (20 anneaux dans l'ordre, premier arrivé gagne) !","color":"gray"}]
execute if score $game mg.st matches 75 if score $elm mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🪽 ÉLYTRA : COURSE + COMBAT","color":"red","bold":true},{"text":" (arc et charges de vent : un adversaire touché chute) !","color":"gray"}]
execute if score $game mg.st matches 75 if score $elm mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🪽 ÉLYTRA : SURVIE EN VOL","color":"light_purple","bold":true},{"text":" (reste en l'air dans la zone qui rétrécit, dernier en vol gagne) !","color":"gray"}]
execute if score $game mg.st matches 5 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 3 — BASTIONS","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 4 — CUBES VOXEL","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 5 — PYRAMIDES INVERSÉES","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 4 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 6 — ARCHIPEL BICOLORE","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 5 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 7 — DOUBLE CANYON","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 if score $sm mg.st matches 6 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 8 — NUAGES VOXEL","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 7 unless score $sm mg.st matches 1..6 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SHEEP WAR 2 — FORTERESSES","color":"white","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 20 if score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SPLEGG XXL","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 20 unless score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SPLEGG","color":"yellow","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 22 if score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SUMO — ARÈNE COMPLEXE","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 22 unless score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"SUMO","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 23 if score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"THE DROPPER — TUBE COMMUN","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 65 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⬇ DROPPER : DÉFI","color":"aqua","bold":true},{"text":" (même puits pour tous, niveau au hasard, premier à 3 manches) !","color":"gray"}]
execute if score $game mg.st matches 66 run function mg:elyrace/announce
execute if score $game mg.st matches 64 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⬇ THE DROPPER : AVENTURE","color":"aqua","bold":true},{"text":" (10 niveaux à thème, le premier qui les finit gagne) !","color":"gray"}]
execute if score $game mg.st matches 23 unless score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"THE DROPPER","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 26 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"ONE IN THE CHAMBER","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 26 if score $om mg.st matches 1 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"CHÂTEAU","color":"gold","bold":true},{"text":" (41×41 : donjon à étage, quatre tours à échelles)","color":"gray"}]
execute if score $game mg.st matches 26 if score $om mg.st matches 2 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"GRANDE FORÊT","color":"dark_green","bold":true},{"text":" (71×71 : collines, arbres, ruines, tours de guet)","color":"gray"}]
execute if score $game mg.st matches 27 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"TNT TAG","color":"red","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 27 if score $ttm mg.st matches 1 run function mg:tnttag/map/info_1
execute if score $game mg.st matches 27 if score $ttm mg.st matches 2 run function mg:tnttag/map/info_2
execute if score $game mg.st matches 27 if score $ttm mg.st matches 3 run function mg:tnttag/map/info_3
execute if score $game mg.st matches 27 if score $ttm mg.st matches 0 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"CLASSIQUE","color":"red","bold":true},{"text":" (arène plate 31×31, piliers et murets)","color":"gray"}]
execute if score $game mg.st matches 28 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"BLOCK PARTY","color":"light_purple","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 29 if score $sg mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"PLUIE D'ENCLUMES — SOL TROUÉ","color":"red","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 29 unless score $sg mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"PLUIE D'ENCLUMES","color":"dark_gray","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 30 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"TURF WARS","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 0 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — NÉON","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — VOLCAN XL","color":"red","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — JUNGLE XL","color":"dark_green","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — DÉSERT","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 5 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — POUSSIÈRE (style Dust)","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 6 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — MIRAGE (style Mirage)","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 7 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — NUKETOWN (style Nuketown)","color":"green","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 4 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"QUAKECRAFT — GLACIER (MINI)","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 8 run tellraw @a [{"selector": "@s", "color": "yellow"}, {"text": " lance une partie de ", "color": "gray"}, {"text": "QUAKECRAFT — RAVIN (SNIPER)", "color": "gold", "bold": true}, {"text": " : deux plateaux face à face, railgun longue portée !", "color": "gray"}]
execute if score $game mg.st matches 31 if score $qm mg.st matches 9 run tellraw @a [{"selector": "@s", "color": "yellow"}, {"text": " lance une partie de ", "color": "gray"}, {"text": "QUAKECRAFT — TOURS (SNIPER)", "color": "green", "bold": true}, {"text": " : 9 tours dans une grande plaine, railgun longue portée !", "color": "gray"}]
execute if score $game mg.st matches 36 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"PAINTBALL","color":"gold","bold":true},{"text":" — Orange contre Bleu !","color":"gray"}]
execute if score $game mg.st matches 36 if score $pbm mg.st matches 1 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"MINI-TERRAIN","color":"gold","bold":true},{"text":" (31×41, 1 min 30 : parties rapides)","color":"gray"}]
execute if score $game mg.st matches 36 if score $pbm mg.st matches 2 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"GRAND TERRAIN","color":"gold","bold":true},{"text":" (81×101, 3 min : grosse bataille)","color":"gray"}]
execute if score $game mg.st matches 56 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"COURSE DE BATEAUX SUR GLACE","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 84 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⚡ TRON","color":"aqua","bold":true},{"text":" : laisse un mur derrière toi, ne touche aucun mur !","color":"gray"}]
execute if score $game mg.st matches 85 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏍 TRON MOTO","color":"gold","bold":true},{"text":" : à cheval, laisse un mur derrière toi, ne touche aucun mur !","color":"gray"}]
execute if score $game mg.st matches 86 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL","color":"gold","bold":true},{"text":" : tiens le sommet seul, 60 points pour gagner !","color":"gray"}]
execute if score $game mg.st matches 87 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL — ÉQUIPES","color":"gold","bold":true},{"text":" : rouges contre bleus, 90 points sur le sommet !","color":"gray"}]
execute if score $game mg.st matches 88 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏰 THE TOWERS","color":"gold","bold":true},{"text":" : rouges contre bleus, saute dans le puits adverse (5 points) !","color":"gray"}]
execute if score $game mg.st matches 89 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🚚 CONVOI","color":"gold","bold":true},{"text":" : rouges contre bleus, escortez ou bloquez le convoi (2 manches) !","color":"gray"}]
execute if score $game mg.st matches 90 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🚚 CONVOI — COOP","color":"gold","bold":true},{"text":" : escortez le convoi à travers les monstres !","color":"gray"}]
execute if score $game mg.st matches 93 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🚩 CAPTURE THE FLAG","color":"gold","bold":true},{"text":" : rouges contre bleus, 3 captures pour gagner !","color":"gray"}]
execute if score $game mg.st matches 94 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⛏ MINI UHC RUN","color":"gold","bold":true},{"text":" : farm, PvP, zone qui rétrécit — 5 min !","color":"gray"}]
execute if score $game mg.st matches 95 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏹 MINI HUNGER GAMES","color":"gold","bold":true},{"text":" : coffres, corne d'abondance, dernier en vie — 5 min !","color":"gray"}]
execute if score $game mg.st matches 97 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧟 ZOMBIES","color":"dark_green","bold":true},{"text":" : survivez à 10 manches dans le bunker !","color":"gray"}]
execute if score $game mg.st matches 98 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧪 INFECTION","color":"dark_green","bold":true},{"text":" : survivants armés contre zombies contagieux, 3 min !","color":"gray"}]
execute if score $game mg.st matches 96 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🎭 PROP HUNT","color":"gold","bold":true},{"text":" : cachez-vous en objets, les chercheurs arrivent dans 30 s !","color":"gray"}]
execute if score $game mg.st matches 99 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"💣 BOMBARDIER","color":"red","bold":true},{"text":" : largue des bombes sur la ville, le plus de dégâts gagne !","color":"gray"}]
execute if score $game mg.st matches 200 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⚡ TRON — XXL","color":"aqua","bold":true},{"text":" : laisse un mur derrière toi, ne touche aucun mur !","color":"gray"}]
execute if score $game mg.st matches 201 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏍 TRON MOTO — XXL","color":"gold","bold":true},{"text":" : à cheval, laisse un mur derrière toi, ne touche aucun mur !","color":"gray"}]
execute if score $game mg.st matches 202 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⛏ MINI UHC RUN — Désert","color":"gold","bold":true},{"text":" : farm, PvP, zone qui rétrécit — 5 min !","color":"gray"}]
execute if score $game mg.st matches 203 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏹 MINI HUNGER GAMES — Jungle","color":"gold","bold":true},{"text":" : coffres, corne d'abondance, dernier en vie — 5 min !","color":"gray"}]
execute if score $game mg.st matches 204 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⛏ MINI UHC RUN — Taïga enneigée","color":"gold","bold":true},{"text":" : farm, PvP, zone qui rétrécit — 5 min !","color":"gray"}]
execute if score $game mg.st matches 205 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🏹 MINI HUNGER GAMES — Canyon","color":"gold","bold":true},{"text":" : coffres, corne d'abondance, dernier en vie — 5 min !","color":"gray"}]
execute if score $game mg.st matches 206 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL — Pyramide","color":"gold","bold":true},{"text":" : tiens le sommet seul, 60 points pour gagner !","color":"gray"}]
execute if score $game mg.st matches 207 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL — ÉQUIPES — Pyramide","color":"gold","bold":true},{"text":" : rouges contre bleus, 90 points sur le sommet !","color":"gray"}]
execute if score $game mg.st matches 208 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL — Glacier","color":"gold","bold":true},{"text":" : tiens le sommet seul, 60 points pour gagner !","color":"gray"}]
execute if score $game mg.st matches 209 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"👑 KING OF THE HILL — ÉQUIPES — Glacier","color":"gold","bold":true},{"text":" : rouges contre bleus, 90 points sur le sommet !","color":"gray"}]
execute if score $game mg.st matches 210 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧟 ZOMBIES — Laboratoire","color":"dark_green","bold":true},{"text":" : survivez à 10 manches dans le bunker !","color":"gray"}]
execute if score $game mg.st matches 211 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧪 INFECTION — Laboratoire","color":"dark_green","bold":true},{"text":" : survivants armés contre zombies contagieux, 3 min !","color":"gray"}]
execute if score $game mg.st matches 212 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧟 ZOMBIES — Manoir","color":"dark_green","bold":true},{"text":" : survivez à 10 manches dans le bunker !","color":"gray"}]
execute if score $game mg.st matches 213 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🧪 INFECTION — Manoir","color":"dark_green","bold":true},{"text":" : survivants armés contre zombies contagieux, 3 min !","color":"gray"}]
execute if score $game mg.st matches 198 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🦎 MECCHA CHAMELEON","color":"green","bold":true},{"text":" : peignez-vous aux couleurs du décor, les chasseurs arrivent dans 45 s !","color":"gray"}]
execute if score $game mg.st matches 216 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🎾 TENNIS","color":"yellow","bold":true},{"text":" : 1 contre 1, chacun son court : premier à 3 jeux !","color":"gray"}]
execute if score $game mg.st matches 214 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"🎳 BOWLING","color":"light_purple","bold":true},{"text":" : chacun sa piste, 5 frames, le meilleur total gagne !","color":"gray"}]
execute if score $game mg.st matches 215 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance ","color":"gray"},{"text":"⛳ GOLF","color":"green","bold":true},{"text":" : 6 trous façon Wii Sports, le moins de coups gagne !","color":"gray"}]
execute if score $game mg.st matches 57 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"BUILD BATTLE","color":"green","bold":true},{"text":" — thème aléatoire, puis vote !","color":"gray"}]
execute if score $game mg.st matches 83 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"📞 TÉLÉPHONE","color":"gold","bold":true},{"text":" : mot → construction → devinette → construction → devinette !","color":"gray"}]
execute if score $game mg.st matches 58 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"BUILD BATTLE — MAÎTRE DU MOT","color":"dark_aqua","bold":true},{"text":" : un joueur donne le thème !","color":"gray"}]
execute if score $game mg.st matches 61 if score $ktr mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une course de ","color":"gray"},{"text":"🏎 KART","color":"gold","bold":true},{"text":" sur le Circuit Champignon (3 tours, objets) !","color":"gray"}]
execute if score $game mg.st matches 61 if score $ktr mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une course de ","color":"gray"},{"text":"🏎 KART","color":"gold","bold":true},{"text":" dans le Royaume Koopa (3 tours, pièges, objets) !","color":"gray"}]
execute if score $game mg.st matches 61 if score $ktr mg.st matches 3 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"🎈 BATAILLE DE KARTS","color":"red","bold":true},{"text":" dans la Forteresse Bob-omb (3 ballons chacun, dernier en lice gagne) !","color":"gray"}]
execute if score $game mg.st matches 59 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"MINI PARTY","color":"gold","bold":true},{"text":" : plateau, dé, étoiles et mini-jeux (","color":"gray"},{"score":{"name":"$mpmax","objective":"mg.st"},"color":"yellow"},{"text":" tours) !","color":"gray"}]
execute if score $game mg.st matches 6 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"MOB ARENA","color":"dark_green","bold":true},{"text":" !","color":"gray"}]
execute if score $pc mg.st matches 1 run tellraw @a [{"text":"Mode ","color":"gray"},{"text":"CLASSES","color":"gold","bold":true},{"text":" : choisis ta classe d'équipement pendant le compte à rebours !","color":"gray"}]
execute if score $mt mg.st matches 1 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"NETHER","color":"red","bold":true},{"text":" — piglins, blazes, Roi Piglin","color":"gray"}]
execute if score $mt mg.st matches 2 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"END","color":"dark_purple","bold":true},{"text":" — endermen, shulkers, l'Ombre du Vide","color":"gray"}]
execute if score $mt mg.st matches 3 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"ULTRA HARD","color":"dark_red","bold":true},{"text":" — monstres boostés, Broyeur puis Warden. Bonne chance.","color":"gray"}]
execute if score $mt mg.st matches 4 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"VOLANT","color":"aqua","bold":true},{"text":" — phantoms, vex, ghasts, Seigneur des Cieux","color":"gray"}]
execute if score $mt mg.st matches 6 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"LA CATHÉDRALE MAUDITE","color":"dark_red","bold":true},{"text":" — 20 vagues, squelettes archers, zombies en fer, chauves-souris Wither, Comte de Sang","color":"gray"}]
execute if score $mt mg.st matches 7 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"LE LABORATOIRE ALCHIMIQUE","color":"green","bold":true},{"text":" — 20 vagues, zombies speed, sorcières, creepers chargés, Abomination Toxique","color":"gray"}]
execute if score $mt mg.st matches 8 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"LE TEMPLE DES PROFONDEURS","color":"aqua","bold":true},{"text":" — 20 vagues, noyés au trident, gardiens, Émissaire du Kraken","color":"gray"}]
execute if score $mt mg.st matches 9 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"LA FORGE DU TITAN","color":"gold","bold":true},{"text":" — 20 vagues, piglins furieux, cubes de magma, blazes, Golem de Basalte","color":"gray"}]
execute if score $mt mg.st matches 10 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"LE VAISSEAU CYBERNÉTIQUE","color":"light_purple","bold":true},{"text":" — 20 vagues, endermites, shulkers, phantoms, Cœur I.A. Corrompu","color":"gray"}]
execute if score $mt mg.st matches 5 run tellraw @a [{"text":"Thème : ","color":"gray"},{"text":"ARAIGNÉE","color":"dark_green","bold":true},{"text":" — araignées, jockeys, Reine Araignée, Arachnarque","color":"gray"}]
execute if score $n0 mg.st matches 1 run tellraw @a [{"text":"(Mode test solo : pas de victoire automatique — menu → Arrêter pour finir)","color":"dark_gray","italic":true}]

# [variantes] annonce de la variante puis $game = jeu réel
execute if score $ar mg.st matches 1.. run function mg:var/start
# Préparation de l'arène + téléportation
execute if score $game mg.st matches 1 run function mg:spleef/prepare
execute if score $game mg.st matches 2 run function mg:tntrun/prepare
execute if score $game mg.st matches 3 run function mg:pvp/prepare
execute if score $game mg.st matches 4 run function mg:bedwars/prepare
execute if score $game mg.st matches 5 run function mg:sheepwar/prepare
execute if score $game mg.st matches 6 run function mg:mobarena/prepare
execute if score $game mg.st matches 20 run function mg:splegg/prepare
execute if score $game mg.st matches 22 run function mg:sumo/prepare
execute if score $game mg.st matches 23 run function mg:dropper/prepare
execute if score $game mg.st matches 64 run function mg:dropadv/prepare
execute if score $game mg.st matches 65 run function mg:dropadv/c_prepare
execute if score $game mg.st matches 66 run function mg:elyrace/prepare
execute if score $state mg.st matches 3 run return 0
execute if score $game mg.st matches 26 run function mg:oitc/prepare
execute if score $game mg.st matches 27 run function mg:tnttag/prepare
execute if score $game mg.st matches 28 run function mg:blockparty/prepare
execute if score $game mg.st matches 29 run function mg:anvil/prepare
execute if score $game mg.st matches 30 run function mg:turf/prepare
execute if score $game mg.st matches 31 run function mg:quake/prepare
execute if score $game mg.st matches 36 run function mg:paintball/prepare
execute if score $game mg.st matches 56 run function mg:icerace/prepare
execute if score $game mg.st matches 57..58 run function mg:bb/prepare
execute if score $game mg.st matches 215 run function mg:golf/prepare
execute if score $game mg.st matches 214 run function mg:bowl/prepare
execute if score $game mg.st matches 216 run function mg:tennis/prepare
execute if score $game mg.st matches 198 run function mg:cham/prepare
execute if score $game mg.st matches 212..213 run function mg:zmode3/prepare
execute if score $game mg.st matches 210..211 run function mg:zmode2/prepare
execute if score $game mg.st matches 208..209 run function mg:koth3/prepare
execute if score $game mg.st matches 206..207 run function mg:koth2/prepare
execute if score $game mg.st matches 204..205 run function mg:survival3/prepare
execute if score $game mg.st matches 202..203 run function mg:survival2/prepare
execute if score $game mg.st matches 200..201 run function mg:tronxl/prepare
execute if score $game mg.st matches 99 run function mg:bomber/prepare
execute if score $game mg.st matches 96 run function mg:ph/prepare
execute if score $game mg.st matches 97..98 run function mg:zmode/prepare
execute if score $game mg.st matches 94..95 run function mg:survival/prepare
execute if score $game mg.st matches 93 run function mg:ctf/prepare
execute if score $game mg.st matches 89..90 run function mg:convoy/prepare
execute if score $game mg.st matches 88 run function mg:tower/prepare
execute if score $game mg.st matches 86..87 run function mg:koth/prepare
execute if score $game mg.st matches 84..85 run function mg:tron/prepare
execute if score $game mg.st matches 83 run function mg:tel/prepare
execute if score $game mg.st matches 59 run function mg:party/prepare
execute if score $game mg.st matches 61 run function mg:kart/prepare
execute if score $game mg.st matches 75 run function mg:sky/prepare
execute if score $game mg.st matches 7 unless score $sm mg.st matches 1..6 run function mg:sheepwar2/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 1 run function mg:sheepwar3/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 2 run function mg:sheepwar4/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 3 run function mg:sheepwar5/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 4 run function mg:sheepwar6/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 5 run function mg:sheepwar7/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 6 run function mg:sheepwar8/prepare

# Gel pendant le compte à rebours
execute as @a[tag=mg.play] run function mg:core/freeze
effect give @a[tag=mg.play] minecraft:resistance 15 255 true
title @a[tag=mg.play] title [{"text":"Préparez-vous !","color":"gold"}]
title @a[tag=mg.play] subtitle [{"text":"Début dans 10 secondes...","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
# Rappel aux joueurs en pause (après prepare : une partie annulée, $state 3, n'en envoie pas ; pas en Mini Party, $mpl)
execute unless score $mpl mg.st matches 1 unless score $mp mg.st matches 1 unless score $state mg.st matches 3 run tellraw @a[tag=mg.init,tag=mg.spectate,tag=!mg.surv] [{"text":"⏸ Partie lancée sans toi (pause). ","color":"gray"},{"text":"[▶ Reprendre les parties]","color":"green","click_event":{"action":"run_command","command":"trigger mg.opt set 1"},"hover_event":{"action":"show_text","value":"Désactiver la pause : tu seras téléporté aux prochaines parties"}}]
execute unless score $mpl mg.st matches 1 if score $mp mg.st matches 1 unless score $state mg.st matches 3 run tellraw @a[tag=mg.init,tag=mg.spectate,tag=!mg.surv] [{"text":"⏸ Partie lancée sans toi (pause). ","color":"gray"},{"text":"[▶ Reprendre les parties]","color":"green","click_event":{"action":"run_command","command":"trigger mg.opt set 1"},"hover_event":{"action":"show_text","value":"La Mini Party se joue sans toi ; tu seras téléporté aux parties suivantes"}}]
