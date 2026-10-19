# @s a vaincu : Rejeton
advancement revoke @s only mg:ombre/k/arachneen
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 2
function mg:ombre/xpk {n:6}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..10 run scoreboard players add @s mg.olm2 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..10 run title @s actionbar [{"text":"+2 💰  ","color":"gold","bold":true},{"text":"+1 soie d'araignée  ","color":"white"},{"text":"Rejeton","color":"gray"}]
execute unless score $r mg.st matches ..10 run title @s actionbar [{"text":"+2 💰  ","color":"gold","bold":true},{"text":"Rejeton","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p17 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_arachneen
scoreboard players set $kk mg.st 47
function mg:ombre/khook
