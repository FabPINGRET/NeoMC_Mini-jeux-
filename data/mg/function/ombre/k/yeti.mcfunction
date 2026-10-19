# @s a vaincu : Yéti
advancement revoke @s only mg:ombre/k/yeti
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 18
function mg:ombre/xpk {n:55}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..40 run scoreboard players add @s mg.olm3 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..40 run title @s actionbar [{"text":"+18 💰  ","color":"gold","bold":true},{"text":"+1 éclat de givre  ","color":"aqua"},{"text":"Yéti","color":"gray"}]
execute unless score $r mg.st matches ..40 run title @s actionbar [{"text":"+18 💰  ","color":"gold","bold":true},{"text":"Yéti","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_yeti
scoreboard players set $kk mg.st 13
function mg:ombre/khook
