# 🚩 Capture the Flag — tick
scoreboard players add $cft mg.st 1
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:ctf/respawn
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..72}] run function mg:ctf/respawn
# drapeau ROUGE
execute as @e[type=minecraft:marker,tag=mg.cfpr] at @a[tag=mg.cfcr,limit=1] run tp @s ~ ~ ~
execute if score $cfr mg.st matches 0 positioned -35 82 21600 as @a[tag=mg.play,team=mg_blue,distance=..2,limit=1,sort=nearest] run function mg:ctf/take_red
execute if score $cfr mg.st matches 2 as @e[tag=mg.cfdr] at @s as @a[tag=mg.play,team=mg_blue,distance=..1.6,limit=1,sort=nearest] run function mg:ctf/take_red
execute if score $cfr mg.st matches 2 as @e[tag=mg.cfdr] at @s if entity @a[tag=mg.play,team=mg_red,distance=..1.6] run function mg:ctf/return_red
execute if score $cfr mg.st matches 2 run scoreboard players remove $cfrt mg.st 1
execute if score $cfr mg.st matches 2 if score $cfrt mg.st matches ..0 run function mg:ctf/return_red
execute as @a[tag=mg.cfcr] at @s run particle minecraft:dust{color:[1.0,0.0,0.0],scale:1.5} ~ ~2.3 ~ 0.2 0.2 0.2 0 2
execute as @e[tag=mg.cfdr] at @s run particle minecraft:end_rod ~ ~1 ~ 0.1 0.5 0.1 0.01 1
execute if score $cfr mg.st matches 0 positioned -35 82 21600 as @a[tag=mg.cfcb,team=mg_red,distance=..2.5,limit=1] run function mg:ctf/capture_red
# drapeau BLEU
execute as @e[type=minecraft:marker,tag=mg.cfpb] at @a[tag=mg.cfcb,limit=1] run tp @s ~ ~ ~
execute if score $cfb mg.st matches 0 positioned 35 82 21600 as @a[tag=mg.play,team=mg_red,distance=..2,limit=1,sort=nearest] run function mg:ctf/take_blue
execute if score $cfb mg.st matches 2 as @e[tag=mg.cfdb] at @s as @a[tag=mg.play,team=mg_red,distance=..1.6,limit=1,sort=nearest] run function mg:ctf/take_blue
execute if score $cfb mg.st matches 2 as @e[tag=mg.cfdb] at @s if entity @a[tag=mg.play,team=mg_blue,distance=..1.6] run function mg:ctf/return_blue
execute if score $cfb mg.st matches 2 run scoreboard players remove $cfbt mg.st 1
execute if score $cfb mg.st matches 2 if score $cfbt mg.st matches ..0 run function mg:ctf/return_blue
execute as @a[tag=mg.cfcb] at @s run particle minecraft:dust{color:[0.0,0.0,1.0],scale:1.5} ~ ~2.3 ~ 0.2 0.2 0.2 0 2
execute as @e[tag=mg.cfdb] at @s run particle minecraft:end_rod ~ ~1 ~ 0.1 0.5 0.1 0.01 1
execute if score $cfb mg.st matches 0 positioned 35 82 21600 as @a[tag=mg.cfcr,team=mg_blue,distance=..2.5,limit=1] run function mg:ctf/capture_blue
execute if score $cft mg.st matches 10800 run tellraw @a[tag=mg.play] {"text":"🚩 Plus qu'une minute !","color":"gold"}
execute if score $state mg.st matches 2 if score $cft mg.st matches 12000.. run function mg:ctf/timeout
execute store result score $cfn mg.st if entity @a[tag=mg.play,team=mg_red]
execute store result score $cfm mg.st if entity @a[tag=mg.play,team=mg_blue]
execute if score $state mg.st matches 2 if score $cfn mg.st matches 0 if score $cfm mg.st matches 1.. run return run function mg:core/win_blue
execute if score $state mg.st matches 2 if score $cfm mg.st matches 0 if score $cfn mg.st matches 1.. run return run function mg:core/win_red
execute if score $state mg.st matches 2 if score $cfm mg.st matches 0 if score $cfn mg.st matches 0 run function mg:core/draw
