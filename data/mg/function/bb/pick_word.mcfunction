# Choisit un mot au hasard dans mg:bb words → mg:bb word
execute store result score $bbnw mg.st run data get storage mg:bb words
execute store result score $bbr mg.st run random value 0..9999
scoreboard players operation $bbr mg.st %= $bbnw mg.st
execute store result storage mg:c i int 1 run scoreboard players get $bbr mg.st
function mg:bb/pick_word_m with storage mg:c
