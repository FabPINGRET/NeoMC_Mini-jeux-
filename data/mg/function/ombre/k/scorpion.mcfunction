# @s a vaincu : Scorpion des sables
advancement revoke @s only mg:ombre/k/scorpion
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 20
function mg:ombre/xpk {n:60}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm5 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+20 💰  ","color":"gold","bold":true},{"text":"+1 ambre solaire  ","color":"yellow"},{"text":"Scorpion des sables","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+20 💰  ","color":"gold","bold":true},{"text":"Scorpion des sables","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p20 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_scorpion
scoreboard players set $kk mg.st 20
function mg:ombre/khook
