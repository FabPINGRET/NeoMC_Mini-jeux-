# @s a vaincu : Goule
advancement revoke @s only mg:ombre/k/goule
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 4
function mg:ombre/xpk {n:12}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..10 run scoreboard players add @s mg.olm1 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..10 run title @s actionbar [{"text":"+4 💰  ","color":"gold","bold":true},{"text":"+1 peau de bête  ","color":"gold"},{"text":"Goule","color":"gray"}]
execute unless score $r mg.st matches ..10 run title @s actionbar [{"text":"+4 💰  ","color":"gold","bold":true},{"text":"Goule","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_goule
scoreboard players set $kk mg.st 3
function mg:ombre/khook
