execute if score @s mg.kdr matches 80.. if score @s mg.kbo matches ..47 run scoreboard players set @s mg.kbo 48
execute if score @s mg.kdr matches 45..79 if score @s mg.kbo matches ..31 run scoreboard players set @s mg.kbo 32
execute if score @s mg.kdr matches 20..44 if score @s mg.kbo matches ..17 run scoreboard players set @s mg.kbo 18
execute if score @s mg.kdr matches 20.. at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.8 1.4
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 8
