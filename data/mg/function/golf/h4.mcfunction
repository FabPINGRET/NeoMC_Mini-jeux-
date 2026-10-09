# Trou 4 : par 3, 44 m — L'Île
scoreboard players set $gfpar mg.st 3
scoreboard players add $gfpc mg.st 3
scoreboard players set $gflim mg.st 1200
scoreboard players set $gfcx mg.st 384500
scoreboard players set $gfcz mg.st 34582500
tp @e[tag=mg.gftg] 384.5 66 34582.5
execute as @a[tag=mg.play] run function mg:golf/h4_ball
title @a[tag=mg.play] times 5 50 15
title @a[tag=mg.play] subtitle [{"text":"Par 3 · 44 m · L'Île","color":"white"}]
title @a[tag=mg.play] title [{"text":"⛳ Trou 4","color":"green","bold":true}]
tellraw @a[tag=mg.play] [{"text":"⛳ Trou 4/6","color":"green","bold":true},{"text":" — par 3, 44 m, « L'Île »","color":"gray"},{"text":" (green en île : vise juste !)","color":"aqua"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2
