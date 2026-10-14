# Défense de l'outpost Alpha : 90 s, vagues toutes les 15 s, carnotaure à mi-parcours
scoreboard players set $tvo1 mg.st 1
scoreboard players set $tvot1 mg.st 90
scoreboard players set $tvoi1 mg.st 100
scoreboard players set $tvow1 mg.st 3
scoreboard players set $tvoa1 mg.st 0
tellraw @a[tag=mg.tvw,x=62.5,y=65,z=-73.5,distance=..64] [{"text":"⚠ Les dinosaures attaquent l'outpost Alpha ! ","color":"red","bold":true},{"text":"Protège le générateur pendant 90 s.","color":"gray"}]
execute positioned 62.5 65 -73.5 as @a[tag=mg.tvw,distance=..64] at @s run playsound minecraft:event.raid.horn hostile @s ~ ~ ~ 0.8 1.2
