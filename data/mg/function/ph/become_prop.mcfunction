# @s devient cacheur : invisible, petit, un objet au hasard
clear @s
scoreboard players add $phc mg.st 1
scoreboard players operation @s mg.pid = $phc mg.st
effect give @s minecraft:invisibility infinite 0 true
effect give @s minecraft:saturation infinite 0 true
attribute @s minecraft:scale base set 0.5
execute store result score @s mg.php run random value 1..30
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.phd","mg.phnew"],teleport_duration:1,block_state:{Name:"minecraft:barrel"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,0f,-0.5f],scale:[1f,1f,1f]}}
execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.phi","mg.phnew"],width:1.02f,height:1.02f}
scoreboard players operation @e[tag=mg.phnew] mg.pid = @s mg.pid
tag @e[tag=mg.phnew] remove mg.phnew
function mg:ph/apply
