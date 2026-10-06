# Lancement effectif (@s = demandeur, mg.go = id)

scoreboard players operation $game mg.st = @s mg.go
scoreboard players reset @s mg.go

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

# Participants = tous les joueurs initialisés non-spectateurs
tag @a[tag=mg.init,tag=!mg.spectate] add mg.play
tag @a remove mg.out
execute store result score $n0 mg.st if entity @a[tag=mg.play]
execute if score $n0 mg.st matches 0 run tellraw @s [{"text":"Aucun participant (tout le monde est en mode spectateur).","color":"red"}]
execute if score $n0 mg.st matches 0 run return run scoreboard players set $game mg.st 0

# État : compte à rebours de 10 s
scoreboard players set $state mg.st 1
function mg:vote/clear
clear @a minecraft:warped_fungus_on_a_stick
clear @a minecraft:blaze_rod
clear @a minecraft:wind_charge
clear @a minecraft:snowball
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
execute if score $game mg.st matches 23 unless score $sg mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"THE DROPPER","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 26 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"ONE IN THE CHAMBER","color":"gold","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 26 if score $om mg.st matches 1 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"CHÂTEAU","color":"gold","bold":true},{"text":" (41×41 : donjon à étage, quatre tours à échelles)","color":"gray"}]
execute if score $game mg.st matches 26 if score $om mg.st matches 2 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"GRANDE FORÊT","color":"dark_green","bold":true},{"text":" (71×71 : collines, arbres, ruines, tours de guet)","color":"gray"}]
execute if score $game mg.st matches 27 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"TNT TAG","color":"red","bold":true},{"text":" !","color":"gray"}]
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
execute if score $game mg.st matches 36 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une partie de ","color":"gray"},{"text":"PAINTBALL","color":"gold","bold":true},{"text":" — Orange contre Bleu !","color":"gray"}]
execute if score $game mg.st matches 36 if score $pbm mg.st matches 1 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"MINI-TERRAIN","color":"gold","bold":true},{"text":" (31×41, 3 min : parties rapides)","color":"gray"}]
execute if score $game mg.st matches 36 if score $pbm mg.st matches 2 run tellraw @a [{"text":"Carte : ","color":"gray"},{"text":"GRAND TERRAIN","color":"gold","bold":true},{"text":" (81×101, 6 min : grosse bataille)","color":"gray"}]
execute if score $game mg.st matches 56 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance une ","color":"gray"},{"text":"COURSE DE BATEAUX SUR GLACE","color":"aqua","bold":true},{"text":" !","color":"gray"}]
execute if score $game mg.st matches 57 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"BUILD BATTLE","color":"green","bold":true},{"text":" — thème aléatoire, puis vote !","color":"gray"}]
execute if score $game mg.st matches 58 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"BUILD BATTLE — MAÎTRE DU MOT","color":"dark_aqua","bold":true},{"text":" : un joueur donne le thème !","color":"gray"}]
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
execute if score $game mg.st matches 26 run function mg:oitc/prepare
execute if score $game mg.st matches 27 run function mg:tnttag/prepare
execute if score $game mg.st matches 28 run function mg:blockparty/prepare
execute if score $game mg.st matches 29 run function mg:anvil/prepare
execute if score $game mg.st matches 30 run function mg:turf/prepare
execute if score $game mg.st matches 31 run function mg:quake/prepare
execute if score $game mg.st matches 36 run function mg:paintball/prepare
execute if score $game mg.st matches 56 run function mg:icerace/prepare
execute if score $game mg.st matches 57..58 run function mg:bb/prepare
execute if score $game mg.st matches 7 unless score $sm mg.st matches 1..6 run function mg:sheepwar2/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 1 run function mg:sheepwar3/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 2 run function mg:sheepwar4/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 3 run function mg:sheepwar5/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 4 run function mg:sheepwar6/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 5 run function mg:sheepwar7/prepare
execute if score $game mg.st matches 7 if score $sm mg.st matches 6 run function mg:sheepwar8/prepare

# Gel pendant le compte à rebours
effect give @a[tag=mg.play] minecraft:slowness 15 255 true
effect give @a[tag=mg.play] minecraft:resistance 15 255 true
title @a[tag=mg.play] title [{"text":"Préparez-vous !","color":"gold"}]
title @a[tag=mg.play] subtitle [{"text":"Début dans 10 secondes...","color":"gray"}]
execute as @a at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
