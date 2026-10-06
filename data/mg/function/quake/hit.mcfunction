# Joueur touché (@s = victime ; le tireur porte le tag mg.qsh)
scoreboard players add @a[tag=mg.qsh,limit=1] mg.qk 1
execute as @a[tag=mg.qsh,limit=1] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.5
title @a[tag=mg.qsh,limit=1] actionbar [{"text":"⚡ Kill ! ","color":"aqua","bold":true},{"selector":"@s","color":"red"},{"text":"  —  ","color":"gray"},{"score":{"name":"@a[tag=mg.qsh,limit=1]","objective":"mg.qk"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$qg","objective":"mg.st"},"color":"gray"}]
tellraw @s [{"text":"☠ Touché par ","color":"gray"},{"selector":"@a[tag=mg.qsh,limit=1]","color":"aqua"}]
execute at @s run particle minecraft:firework ~ ~1 ~ 0.3 0.5 0.3 0.15 40
execute at @s run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 0.6 1.6
execute as @a[tag=mg.qsh,limit=1] run function mg:quake/gren_chance
execute if score @s mg.ks matches 3.. run tellraw @a[tag=mg.play] [{"text":"✖ ","color":"red"},{"selector":"@a[tag=mg.qsh,limit=1]","color":"aqua"},{"text":" met fin à la série de ","color":"gray"},{"selector":"@s","color":"red"},{"text":" (","color":"gray"},{"score":{"name":"@s","objective":"mg.ks"},"color":"gold"},{"text":" kills)","color":"gray"}]
execute as @a[tag=mg.qsh,limit=1] run function mg:quake/streak
function mg:quake/die
