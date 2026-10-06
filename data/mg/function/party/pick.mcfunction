# Tirage d'un mini-jeu parmi 13 ($mgid = id de lancement), affiché en titre
execute store result score $mgk mg.st run random value 1..13
execute if score $mgk mg.st matches 1 run scoreboard players set $mgid mg.st 1
execute if score $mgk mg.st matches 1 run title @a[tag=mg.mpp] title [{"text":"SPLEEF","color":"aqua","bold":true}]
execute if score $mgk mg.st matches 2 run scoreboard players set $mgid mg.st 2
execute if score $mgk mg.st matches 2 run title @a[tag=mg.mpp] title [{"text":"TNT RUN","color":"red","bold":true}]
execute if score $mgk mg.st matches 3 run scoreboard players set $mgid mg.st 20
execute if score $mgk mg.st matches 3 run title @a[tag=mg.mpp] title [{"text":"SPLEGG","color":"yellow","bold":true}]
execute if score $mgk mg.st matches 4 run scoreboard players set $mgid mg.st 21
execute if score $mgk mg.st matches 4 run title @a[tag=mg.mpp] title [{"text":"SPLEGG XXL","color":"gold","bold":true}]
execute if score $mgk mg.st matches 5 run scoreboard players set $mgid mg.st 22
execute if score $mgk mg.st matches 5 run title @a[tag=mg.mpp] title [{"text":"SUMO","color":"gold","bold":true}]
execute if score $mgk mg.st matches 6 run scoreboard players set $mgid mg.st 24
execute if score $mgk mg.st matches 6 run title @a[tag=mg.mpp] title [{"text":"SUMO COMPLEXE","color":"gold","bold":true}]
execute if score $mgk mg.st matches 7 run scoreboard players set $mgid mg.st 25
execute if score $mgk mg.st matches 7 run title @a[tag=mg.mpp] title [{"text":"DROPPER : TUBE COMMUN","color":"aqua","bold":true}]
execute if score $mgk mg.st matches 8 run scoreboard players set $mgid mg.st 27
execute if score $mgk mg.st matches 8 run title @a[tag=mg.mpp] title [{"text":"TNT TAG","color":"red","bold":true}]
execute if score $mgk mg.st matches 9 run scoreboard players set $mgid mg.st 28
execute if score $mgk mg.st matches 9 run title @a[tag=mg.mpp] title [{"text":"BLOCK PARTY","color":"light_purple","bold":true}]
execute if score $mgk mg.st matches 10 run scoreboard players set $mgid mg.st 29
execute if score $mgk mg.st matches 10 run title @a[tag=mg.mpp] title [{"text":"PLUIE D'ENCLUMES","color":"dark_gray","bold":true}]
execute if score $mgk mg.st matches 11 run scoreboard players set $mgid mg.st 42
execute if score $mgk mg.st matches 11 run title @a[tag=mg.mpp] title [{"text":"ENCLUMES + SOL TROUÉ","color":"red","bold":true}]
execute if score $mgk mg.st matches 12 run scoreboard players set $mgid mg.st 3
execute if score $mgk mg.st matches 12 run title @a[tag=mg.mpp] title [{"text":"ARÈNE PVP","color":"yellow","bold":true}]
execute if score $mgk mg.st matches 13 run scoreboard players set $mgid mg.st 56
execute if score $mgk mg.st matches 13 run title @a[tag=mg.mpp] title [{"text":"COURSE DE BATEAUX","color":"aqua","bold":true}]
execute as @a[tag=mg.mpp] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.5
