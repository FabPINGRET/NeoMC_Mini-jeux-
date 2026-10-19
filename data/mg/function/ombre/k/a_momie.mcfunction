# @s a vaincu : Momie royale
advancement revoke @s only mg:ombre/k/a_momie
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 360
function mg:ombre/xpk {n:900}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..100 run scoreboard players add @s mg.olm5 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..100 run title @s actionbar [{"text":"+360 💰  ","color":"gold","bold":true},{"text":"+1 ambre solaire  ","color":"yellow"},{"text":"Momie royale","color":"gray"}]
execute unless score $r mg.st matches ..100 run title @s actionbar [{"text":"+360 💰  ","color":"gold","bold":true},{"text":"Momie royale","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_a_momie
scoreboard players set $kk mg.st 43
function mg:ombre/khook
