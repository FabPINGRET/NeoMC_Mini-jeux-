execute store result score $tvr mg.st run random value 0..3
execute if score $tvr mg.st matches 0 positioned 62.5 70 -87.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 1 positioned 78.5 65 -73.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 2 positioned 62.5 60 -57.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 3 positioned 46.5 68 -73.5 run function mg:terra/d_raptor
scoreboard players remove $tvn mg.st 1
execute if score $tvn mg.st matches 1.. run function mg:terra/d_wave_one_1
