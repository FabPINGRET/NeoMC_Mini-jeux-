# Défense de l'outpost Charlie : 90 s, vagues toutes les 15 s, carnotaure à mi-parcours
scoreboard players set $tvo3 mg.st 1
scoreboard players set $tvot3 mg.st 90
scoreboard players set $tvoi3 mg.st 100
scoreboard players set $tvow3 mg.st 3
scoreboard players set $tvoa3 mg.st 0
tellraw @a[tag=mg.tvw,x=30.5,y=66,z=72.5,distance=..64] [{"text":"⚠ Les dinosaures attaquent l'outpost Charlie ! ","color":"red","bold":true},{"text":"Protège le générateur pendant 90 s.","color":"gray"}]
execute positioned 30.5 66 72.5 as @a[tag=mg.tvw,distance=..64] at @s run playsound minecraft:event.raid.horn hostile @s ~ ~ ~ 0.8 1.2
