# @s a choisi une pose (mg.cmo)
scoreboard players operation $cmv mg.st = @s mg.cmo
scoreboard players reset @s mg.cmo
scoreboard players enable @s mg.cmo
execute unless score $cmv mg.st matches 1..6 run return 0
scoreboard players operation @s mg.cmpo = $cmv mg.st
scoreboard players set @s mg.cmst 0
scoreboard players operation $cmid mg.st = @s mg.cmid
execute if score $cmv mg.st matches 1 run function mg:cham/pose_1
execute if score $cmv mg.st matches 2 run function mg:cham/pose_2
execute if score $cmv mg.st matches 3 run function mg:cham/pose_3
execute if score $cmv mg.st matches 4 run function mg:cham/pose_4
execute if score $cmv mg.st matches 5 run function mg:cham/pose_5
execute if score $cmv mg.st matches 6 run function mg:cham/pose_6
execute at @s run playsound minecraft:entity.armor_stand.place player @s ~ ~ ~ 0.7 1.2
function mg:cham/hud
