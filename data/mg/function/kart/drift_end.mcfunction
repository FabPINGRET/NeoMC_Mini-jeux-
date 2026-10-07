execute if score @s mg.kdr matches 55.. if score @s mg.kbo matches ..27 run scoreboard players set @s mg.kbo 28
execute if score @s mg.kdr matches 25..54 if score @s mg.kbo matches ..13 run scoreboard players set @s mg.kbo 14
execute if score @s mg.kdr matches 25.. at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..20] ~ ~ ~ 0.8 1.4
scoreboard players set @s mg.kdr 0
