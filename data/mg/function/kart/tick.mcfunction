# Kart (état 2, jeu 61)
scoreboard players add $ktime mg.st 1
scoreboard players enable @a[tag=mg.play] mg.kv
execute as @a[tag=mg.play] run function mg:kart/drive
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc

execute as @e[type=minecraft:item_display,tag=mg.kbox,tag=!mg.kboff] at @s if entity @e[type=minecraft:block_display,tag=mg.kart,distance=..2.3] run function mg:kart/box_hit
execute as @e[type=minecraft:item_display,tag=mg.kboff] run function mg:kart/box_wait
execute as @e[type=minecraft:item_display,tag=mg.kshell] at @s run function mg:kart/shell_tick
execute as @e[type=minecraft:item_display,tag=mg.kban] at @s run function mg:kart/banana_tick
execute as @e[type=minecraft:item_display,tag=mg.kblue] at @s run function mg:kart/blue_tick
execute as @e[type=minecraft:item_display,tag=mg.kbomb] at @s run function mg:kart/bomb_tick
execute as @e[type=minecraft:item_display,tag=mg.kfake] at @s run function mg:kart/fake_tick

scoreboard players add $kph mg.st 1
execute if score $kph mg.st matches 4.. run function mg:kart/every4

execute store result score $kn mg.st if entity @a[tag=mg.play]
execute store result score $kfn mg.st if entity @a[tag=mg.play,tag=mg.kfin]
execute if score $kn mg.st matches 1.. if score $kfn mg.st = $kn mg.st run return run function mg:kart/end
execute if score $kend mg.st matches 1.. if score $ktime mg.st >= $kend mg.st run return run function mg:kart/end
execute if score $ktime mg.st matches 8400.. run return run function mg:kart/end
execute unless entity @a[tag=mg.play] run function mg:core/draw
