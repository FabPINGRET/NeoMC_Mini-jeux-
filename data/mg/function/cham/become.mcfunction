# @s devient caméléon : invisible, corps en blocs (6 morceaux) et zone touchable
clear @s
scoreboard players add $cmc mg.st 1
scoreboard players operation @s mg.cmid = $cmc mg.st
effect give @s minecraft:invisibility infinite 0 true
effect give @s minecraft:saturation infinite 0 true
effect give @s minecraft:resistance infinite 3 true
effect give @s minecraft:regeneration infinite 2 true
scoreboard players set @s mg.cmpo 1
scoreboard players set @s mg.cmpt 1
scoreboard players set @s mg.cmdl 2
scoreboard players set @s mg.cmtc 0
scoreboard players set @s mg.cmst 0
scoreboard players set @s mg.cmq 0
scoreboard players enable @s mg.cmp
scoreboard players enable @s mg.cmo
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk1","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:green_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,1.4f,-0.25f],scale:[0.5f,0.5f,0.5f]}}
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk2","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:lime_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,0.7f,-0.13f],scale:[0.5f,0.7f,0.26f]}}
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk3","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:lime_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,0.7f,-0.12f],scale:[0.24f,0.7f,0.24f]}}
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk4","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:lime_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.26f,0.7f,-0.12f],scale:[0.24f,0.7f,0.24f]}}
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk5","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:green_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.25f,0.0f,-0.12f],scale:[0.24f,0.7f,0.24f]}}
execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmd","mg.cmk6","mg.cmnew"],teleport_duration:1,block_state:{Name:"minecraft:green_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.01f,0.0f,-0.12f],scale:[0.24f,0.7f,0.24f]}}
execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.cmi","mg.cmnew"],width:0.8f,height:1.9f}
scoreboard players operation @e[tag=mg.cmnew] mg.cmid = @s mg.cmid
tag @e[tag=mg.cmnew] remove mg.cmnew
attribute @s minecraft:scale base set 1
item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={chm:1},item_model="mg:cham_palette",custom_name={"text":"🎨 Palette","color":"green","bold":true,"italic":false},lore=[{"text":"Clic droit : choisir la partie du corps et sa matière","color":"gray","italic":false}],unbreakable={}]
item replace entity @s hotbar.1 with minecraft:warped_fungus_on_a_stick[custom_data={chm:2},item_model="mg:cham_pipette",custom_name={"text":"💧 Pipette","color":"aqua","bold":true,"italic":false},lore=[{"text":"Clic droit sur un bloc : copie sa matière sur la partie choisie","color":"gray","italic":false}],unbreakable={}]
item replace entity @s hotbar.2 with minecraft:warped_fungus_on_a_stick[custom_data={chm:3},item_model="mg:cham_pose",custom_name={"text":"🧍 Poses","color":"yellow","bold":true,"italic":false},lore=[{"text":"Clic droit : debout, assis, boule, à plat, plaqué au mur, bloc","color":"gray","italic":false}],unbreakable={}]
item replace entity @s hotbar.3 with minecraft:warped_fungus_on_a_stick[custom_data={chm:4},item_model="mg:cham_decoy",custom_name={"text":"👥 Leurre","color":"light_purple","bold":true,"italic":false},lore=[{"text":"Clic droit : pose une copie de toi (2 par manche)","color":"gray","italic":false}],unbreakable={}]
item replace entity @s hotbar.4 with minecraft:warped_fungus_on_a_stick[custom_data={chm:5},item_model="mg:cham_taunt",custom_name={"text":"📢 Narguer","color":"gold","bold":true,"italic":false},lore=[{"text":"Clic droit : un sifflet bien fort, +5 points (recharge 8 s)","color":"gray","italic":false}],unbreakable={}]
