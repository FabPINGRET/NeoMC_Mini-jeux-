execute store result score $tvr mg.st run random value 0..3
execute if score $tvr mg.st matches 0 positioned 30.5 63 56.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 1 positioned 46.5 63 72.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 2 positioned 30.5 71 87.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 3 positioned 14.5 65 72.5 run function mg:terra/d_raptor
scoreboard players remove $tvn mg.st 1
execute if score $tvn mg.st matches 1.. run function mg:terra/d_wave_one_3
