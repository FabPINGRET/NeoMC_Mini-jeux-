# @s a vaincu : Elfe noir
advancement revoke @s only mg:ombre/k/elfe
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 10
function mg:ombre/xpk {n:26}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..25 run scoreboard players add @s mg.olm2 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..25 run title @s actionbar [{"text":"+10 💰  ","color":"gold","bold":true},{"text":"+1 soie d'araignée  ","color":"white"},{"text":"Elfe noir","color":"gray"}]
execute unless score $r mg.st matches ..25 run title @s actionbar [{"text":"+10 💰  ","color":"gold","bold":true},{"text":"Elfe noir","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_elfe
scoreboard players set $kk mg.st 8
function mg:ombre/khook
