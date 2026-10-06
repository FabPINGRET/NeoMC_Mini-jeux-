scoreboard players set $gl mg.st 1
title @a[tag=mg.play] actionbar [{"text":"◉ ","color":"yellow"},{"text":"Plus que 3 monstres : ils sont surlignés à travers les murs !","color":"gold"}]
tellraw @a[tag=mg.play] [{"text":"[Mob Arena] ","color":"dark_green","bold":true},{"text":"Plus que 3 monstres ou moins : ils sont maintenant surlignés, même à travers les murs.","color":"yellow"}]
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 0.7 1.5
