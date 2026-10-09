# @s prend un objet à la villa ($gpt) : seulement s'il a déjà été acheté une fois
execute if score $gpt mg.st matches 31 unless data storage mg:gta unl.t21 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 31 run scoreboard players set $gpt mg.st 21
execute if score $gpt mg.st matches 32 unless data storage mg:gta unl.t22 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 32 run scoreboard players set $gpt mg.st 22
execute if score $gpt mg.st matches 33 unless data storage mg:gta unl.t23 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 33 run scoreboard players set $gpt mg.st 23
execute if score $gpt mg.st matches 34 unless data storage mg:gta unl.t24 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 34 run scoreboard players set $gpt mg.st 24
execute if score $gpt mg.st matches 35 unless data storage mg:gta unl.t25 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 35 run scoreboard players set $gpt mg.st 25
execute if score $gpt mg.st matches 42 unless data storage mg:gta unl.t2 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 42 run scoreboard players set $gpt mg.st 2
execute if score $gpt mg.st matches 43 unless data storage mg:gta unl.t3 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 43 run scoreboard players set $gpt mg.st 3
execute if score $gpt mg.st matches 44 unless data storage mg:gta unl.t4 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 44 run scoreboard players set $gpt mg.st 4
execute if score $gpt mg.st matches 45 unless data storage mg:gta unl.t5 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 45 run scoreboard players set $gpt mg.st 5
execute if score $gpt mg.st matches 46 unless data storage mg:gta unl.t6 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 46 run scoreboard players set $gpt mg.st 6
execute if score $gpt mg.st matches 47 unless data storage mg:gta unl.t7 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 47 run scoreboard players set $gpt mg.st 7
execute if score $gpt mg.st matches 49 unless data storage mg:gta unl.t9 run return run function mg:gta/villa_locked
execute if score $gpt mg.st matches 49 run scoreboard players set $gpt mg.st 9
scoreboard players set $gvilla mg.st 1
scoreboard players set $gok mg.st 1
function mg:gta/pad_give
scoreboard players set $gvilla mg.st 0
