# Trou 2 : par 3, 48 m — La Descente
scoreboard players set $gfpar mg.st 3
scoreboard players add $gfpc mg.st 3
scoreboard players set $gflim mg.st 1200
scoreboard players set $gfcx mg.st 243500
scoreboard players set $gfcz mg.st 34528500
tp @e[tag=mg.gftg] 243.5 65 34528.5
execute as @a[tag=mg.play] run function mg:golf/h2_ball
title @a[tag=mg.play] times 5 50 15
title @a[tag=mg.play] subtitle [{"text":"Par 3 · 48 m · La Descente","color":"white"}]
title @a[tag=mg.play] title [{"text":"⛳ Trou 2","color":"green","bold":true}]
tellraw @a[tag=mg.play] [{"text":"⛳ Trou 2/6","color":"green","bold":true},{"text":" — par 3, 48 m, « La Descente »","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2
