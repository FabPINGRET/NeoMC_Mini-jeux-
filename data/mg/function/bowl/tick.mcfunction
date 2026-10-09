# 🎳 Bowling — tick
scoreboard players add $bt mg.st 1
scoreboard players set #km1 mg.st -1
scoreboard players set $bsub mg.st 0
function mg:bowl/phys
scoreboard players set $bsub mg.st 1
function mg:bowl/phys
execute as @e[type=minecraft:item_display,tag=mg.bball] run function mg:bowl/pos
execute as @e[type=minecraft:block_display,tag=mg.bpmv] run function mg:bowl/pos_pin
execute as @a[tag=mg.play,tag=mg.bwl] at @s run function mg:bowl/ptick
scoreboard players reset @a[scores={mg.blu=1..}] mg.blu
scoreboard players reset @a[tag=mg.play,scores={mg.qs=1..}] mg.qs
kill @e[type=minecraft:item,x=-34,y=60,z=35130,dx=67,dy=20,dz=54]
execute if score $bt mg.st matches 6000 run tellraw @a[tag=mg.play] {"text":"🎳 Plus qu'une minute !","color":"gold"}
execute if score $state mg.st matches 2 if score $bt mg.st matches 7200.. run return run function mg:bowl/finish
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute store result score #n mg.st if entity @a[tag=mg.play,tag=mg.bwl,scores={mg.bph=..8}]
execute if score $alive mg.st matches 1.. if score #n mg.st matches 0 run scoreboard players add $bend mg.st 1
execute if score $state mg.st matches 2 if score $bend mg.st matches 60.. run return run function mg:bowl/finish
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
