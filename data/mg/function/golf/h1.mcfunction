# Trou 1 : par 4, 86 m — Le Grand Chêne
scoreboard players set $gfpar mg.st 4
scoreboard players add $gfpc mg.st 4
scoreboard players set $gflim mg.st 1500
scoreboard players set $gfcx mg.st 220500
scoreboard players set $gfcz mg.st 34594500
tp @e[tag=mg.gftg] 220.5 65 34594.5
execute as @a[tag=mg.play] run function mg:golf/h1_ball
title @a[tag=mg.play] times 5 50 15
title @a[tag=mg.play] subtitle [{"text":"Par 4 · 86 m · Le Grand Chêne","color":"white"}]
title @a[tag=mg.play] title [{"text":"⛳ Trou 1","color":"green","bold":true}]
tellraw @a[tag=mg.play] [{"text":"⛳ Trou 1/6","color":"green","bold":true},{"text":" — par 4, 86 m, « Le Grand Chêne »","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2
