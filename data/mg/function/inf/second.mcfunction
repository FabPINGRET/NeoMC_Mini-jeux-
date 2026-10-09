scoreboard players set $inl mg.st 180
scoreboard players operation $ins2 mg.st = $ift mg.st
scoreboard players operation $ins2 mg.st /= #20 mg.st
scoreboard players operation $inl mg.st -= $ins2 mg.st
title @a[tag=mg.play,tag=mg.inf] actionbar [{"text":"🧟 Survivants : ","color":"dark_green"},{"score":{"name":"$ins","objective":"mg.st"},"color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run title @a[tag=mg.play] actionbar [{"text":"🧪 Entraînement : ","color":"yellow"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]
execute if score $inl mg.st matches 60 run tellraw @a[tag=mg.play] {"text":"🧪 Plus qu'une minute !","color":"gold"}
execute if score $inl mg.st matches 60 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8
