# @s a vaincu : Ours des glaces
advancement revoke @s only mg:ombre/k/ours
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 12
function mg:ombre/xpk {n:40}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..40 run scoreboard players add @s mg.olm3 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..40 run title @s actionbar [{"text":"+12 💰  ","color":"gold","bold":true},{"text":"+1 éclat de givre  ","color":"aqua"},{"text":"Ours des glaces","color":"gray"}]
execute unless score $r mg.st matches ..40 run title @s actionbar [{"text":"+12 💰  ","color":"gold","bold":true},{"text":"Ours des glaces","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_ours
scoreboard players set $kk mg.st 11
function mg:ombre/khook
