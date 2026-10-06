# @s = maître ; mg.bw = 11..18
scoreboard players operation $bbr mg.st = @s mg.bw
scoreboard players remove $bbr mg.st 11
execute store result storage mg:c i int 1 run scoreboard players get $bbr mg.st
function mg:bb/word_sug_m with storage mg:c
function mg:bb/word_apply
