# @s (équipe adverse) prend le drapeau ROUGE
scoreboard players set $cfr mg.st 1
kill @e[tag=mg.cfdr]
setblock -35 82 21600 minecraft:air
tag @s add mg.cfcr
kill @e[tag=mg.cfpr]
execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.cfp","mg.cfpr"]}
item replace entity @s armor.head with minecraft:red_banner
effect give @s minecraft:glowing infinite 0 true
tellraw @a[tag=mg.play] [{"text":"🚩 ","color":"red"},{"selector":"@s","color":"blue"},{"text":" a pris le drapeau ROUGE !","color":"red","bold":true}]
execute as @a[tag=mg.play,team=mg_red] at @s run playsound minecraft:block.note_block.didgeridoo master @s ~ ~ ~ 1 0.6
execute as @a[tag=mg.play,team=mg_blue] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5
