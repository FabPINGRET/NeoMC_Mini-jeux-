execute store result score $tvr mg.st run random value 0..3
execute if score $tvr mg.st matches 0 positioned -71.5 68 -9.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 1 positioned -55.5 67 6.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 2 positioned -71.5 63 22.5 run function mg:terra/d_raptor
execute if score $tvr mg.st matches 3 positioned -87.5 68 6.5 run function mg:terra/d_raptor
scoreboard players remove $tvn mg.st 1
execute if score $tvn mg.st matches 1.. run function mg:terra/d_wave_one_2
