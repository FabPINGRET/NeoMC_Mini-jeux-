# ⛳ Golf — tick
execute unless score $gfok mg.st matches 1 run return run title @a[tag=mg.play] actionbar {"text":"⛳ Préparation du parcours…","color":"green"}
execute if score $gfh mg.st matches 0 run function mg:golf/hole_next
execute as @a[tag=mg.play] at @s run function mg:golf/ptick
scoreboard players reset @a[tag=mg.play] mg.qs
execute as @e[type=minecraft:item_display,tag=mg.gfmv] at @s run function mg:golf/ball
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run return run function mg:core/draw
execute if score $gfw mg.st matches 1.. run return run function mg:golf/between
scoreboard players add $gft mg.st 1
scoreboard players operation $gfr mg.st = $gflim mg.st
scoreboard players operation $gfr mg.st -= $gft mg.st
execute if score $gfr mg.st matches 300 run tellraw @a[tag=mg.play] {"text":"⏱ Plus que 15 secondes pour finir le trou !","color":"gold"}
execute if score $gfr mg.st matches ..0 as @a[tag=mg.play,scores={mg.gfs=0..1}] run function mg:golf/timeout
execute store result score $gfa mg.st if entity @a[tag=mg.play,scores={mg.gfs=0..1}]
execute if score $gfa mg.st matches 0 run function mg:golf/hole_done
