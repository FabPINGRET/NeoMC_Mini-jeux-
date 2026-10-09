# @s (équipe adverse) prend le drapeau BLEU
scoreboard players set $cfb mg.st 1
kill @e[tag=mg.cfdb]
setblock 35 82 21600 minecraft:air
tag @s add mg.cfcb
kill @e[tag=mg.cfpb]
execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.cfp","mg.cfpb"]}
item replace entity @s armor.head with minecraft:blue_banner
effect give @s minecraft:glowing infinite 0 true
tellraw @a[tag=mg.play] [{"text":"🚩 ","color":"blue"},{"selector":"@s","color":"red"},{"text":" a pris le drapeau BLEU !","color":"blue","bold":true}]
execute as @a[tag=mg.play,team=mg_blue] at @s run playsound minecraft:block.note_block.didgeridoo master @s ~ ~ ~ 1 0.6
execute as @a[tag=mg.play,team=mg_red] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5
