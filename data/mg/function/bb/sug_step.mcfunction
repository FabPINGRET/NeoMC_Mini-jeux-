execute store result score $bbr mg.st run random value 0..9999
scoreboard players operation $bbr mg.st %= $bbsl mg.st
execute store result storage mg:c i int 1 run scoreboard players get $bbr mg.st
function mg:bb/sug_move with storage mg:c
scoreboard players remove $bbsl mg.st 1
scoreboard players remove $bbsk mg.st 1
execute if score $bbsk mg.st matches 1.. run function mg:bb/sug_step
