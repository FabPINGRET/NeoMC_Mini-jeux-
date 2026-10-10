function mg:master/times with storage mg:ms t
$title @a[tag=mg.play] title [{"text":"$(m)","color":"gold","bold":true},{"text":"$(t)","color":"white","bold":true}]
title @a[tag=mg.play] subtitle ""
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 1.6
