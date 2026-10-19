# @s a vaincu : Seigneur des cryptes
advancement revoke @s only mg:ombre/k/a_crypte
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 120
function mg:ombre/xpk {n:300}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..100 run scoreboard players add @s mg.olm1 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..100 run title @s actionbar [{"text":"+120 💰  ","color":"gold","bold":true},{"text":"+1 peau de bête  ","color":"gold"},{"text":"Seigneur des cryptes","color":"gray"}]
execute unless score $r mg.st matches ..100 run title @s actionbar [{"text":"+120 💰  ","color":"gold","bold":true},{"text":"Seigneur des cryptes","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_a_crypte
scoreboard players set $kk mg.st 39
function mg:ombre/khook
