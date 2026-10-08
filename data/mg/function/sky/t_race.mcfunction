# Modes 1-2 : chrono, joueurs, combat, limite de 4 minutes
scoreboard players operation $es mg.st = $skt mg.st
scoreboard players operation $es mg.st /= #20 mg.st
scoreboard players operation $ecs mg.st = $skt mg.st
scoreboard players operation $ecs mg.st %= #20 mg.st
scoreboard players operation $ecs mg.st *= #5 mg.st
execute as @a[tag=mg.play] at @s run function mg:sky/r_player
execute if score $elm mg.st matches 2 run function mg:sky/t_combat
execute if score $skt mg.st matches 3600 run tellraw @a[tag=mg.play] [{"text":"🪽 Plus qu'une minute !","color":"gold"}]
execute if score $state mg.st matches 2 if score $skt mg.st matches 4800.. run function mg:sky/r_timeout
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw
