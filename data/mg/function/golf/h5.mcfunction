# Trou 5 : par 4, 105 m — Le Coude
scoreboard players set $gfpar mg.st 4
scoreboard players add $gfpc mg.st 4
scoreboard players set $gflim mg.st 1500
scoreboard players set $gfcx mg.st 332500
scoreboard players set $gfcz mg.st 34682500
tp @e[tag=mg.gftg] 332.5 65 34682.5
execute as @a[tag=mg.play] run function mg:golf/h5_ball
title @a[tag=mg.play] times 5 50 15
title @a[tag=mg.play] subtitle [{"text":"Par 4 · 105 m · Le Coude","color":"white"}]
title @a[tag=mg.play] title [{"text":"⛳ Trou 5","color":"green","bold":true}]
tellraw @a[tag=mg.play] [{"text":"⛳ Trou 5/6","color":"green","bold":true},{"text":" — par 4, 105 m, « Le Coude »","color":"gray"},{"text":" (dogleg : le trou tourne à droite, les arbres bloquent le raccourci)","color":"aqua"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2
