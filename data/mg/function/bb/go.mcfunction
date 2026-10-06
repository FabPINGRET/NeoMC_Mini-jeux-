# Build Battle — départ
scoreboard players set $bbt mg.st 0
execute if score $bbm mg.st matches 1 run function mg:bb/master_start
execute unless score $bbm mg.st matches 1 run function mg:bb/word_random
