# Trou 3 : par 5, 128 m — La Rivière
scoreboard players set $gfpar mg.st 5
scoreboard players add $gfpc mg.st 5
scoreboard players set $gflim mg.st 1800
scoreboard players set $gfcx mg.st 384500
scoreboard players set $gfcz mg.st 34520500
tp @e[tag=mg.gftg] 384.5 65 34520.5
execute as @a[tag=mg.play] run function mg:golf/h3_ball
title @a[tag=mg.play] times 5 50 15
title @a[tag=mg.play] subtitle [{"text":"Par 5 · 128 m · La Rivière","color":"white"}]
title @a[tag=mg.play] title [{"text":"⛳ Trou 3","color":"green","bold":true}]
tellraw @a[tag=mg.play] [{"text":"⛳ Trou 3/6","color":"green","bold":true},{"text":" — par 5, 128 m, « La Rivière »","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2
