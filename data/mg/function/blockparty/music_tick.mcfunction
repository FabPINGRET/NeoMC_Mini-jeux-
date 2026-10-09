# Avance la musique d'un tick
scoreboard players add $bmt mg.st 1
execute if score $bmt mg.st >= $bms mg.st run function mg:blockparty/music_step
