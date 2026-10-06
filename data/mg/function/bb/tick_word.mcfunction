# Le Maître choisit (60 s max)
scoreboard players add $bbt mg.st 1
execute as @a[tag=mg.play,scores={mg.bi=0..}] run function mg:bb/confine
execute as @a[tag=mg.play,scores={mg.bi=-1}] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.bi=-1,mg.t=..50}] run tp @s -639.5 65 13650.5
scoreboard players operation $bbq mg.st = $bbt mg.st
scoreboard players operation $bbq mg.st %= $bbc20 mg.st
execute if score $bbq mg.st matches 0 run title @a[tag=mg.bm] actionbar [{"text":"✎ Écris le thème dans ton livre puis valide, ou clique une idée dans le chat","color":"gold"}]
execute if score $bbq mg.st matches 0 run title @a[tag=mg.play,tag=!mg.bm] actionbar [{"text":"✎ Le Maître du mot choisit le thème…","color":"gray"}]
execute unless entity @a[tag=mg.bm,tag=mg.play] run return run function mg:bb/word_timeout
execute if score $bbt mg.st matches 1200.. run function mg:bb/word_timeout
