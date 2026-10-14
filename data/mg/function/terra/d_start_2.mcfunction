# Défense de l'outpost Bravo : 90 s, vagues toutes les 15 s, carnotaure à mi-parcours
scoreboard players set $tvo2 mg.st 1
scoreboard players set $tvot2 mg.st 90
scoreboard players set $tvoi2 mg.st 100
scoreboard players set $tvow2 mg.st 3
scoreboard players set $tvoa2 mg.st 0
tellraw @a[tag=mg.tvw,x=-71.5,y=70,z=6.5,distance=..64] [{"text":"⚠ Les dinosaures attaquent l'outpost Bravo ! ","color":"red","bold":true},{"text":"Protège le générateur pendant 90 s.","color":"gray"}]
execute positioned -71.5 70 6.5 as @a[tag=mg.tvw,distance=..64] at @s run playsound minecraft:event.raid.horn hostile @s ~ ~ ~ 0.8 1.2
