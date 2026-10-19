# @s a vaincu : Loup-garou
advancement revoke @s only mg:ombre/k/garou
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 12
function mg:ombre/xpk {n:34}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..30 run scoreboard players add @s mg.olm2 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..30 run title @s actionbar [{"text":"+12 💰  ","color":"gold","bold":true},{"text":"+1 soie d'araignée  ","color":"white"},{"text":"Loup-garou","color":"gray"}]
execute unless score $r mg.st matches ..30 run title @s actionbar [{"text":"+12 💰  ","color":"gold","bold":true},{"text":"Loup-garou","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_garou
scoreboard players set $kk mg.st 9
function mg:ombre/khook
