# @s a vaincu : Gardien noyé
advancement revoke @s only mg:ombre/k/a_noye
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 300
function mg:ombre/xpk {n:760}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..100 run scoreboard players add @s mg.olm4 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..100 run title @s actionbar [{"text":"+300 💰  ","color":"gold","bold":true},{"text":"+1 fiole de venin  ","color":"dark_green"},{"text":"Gardien noyé","color":"gray"}]
execute unless score $r mg.st matches ..100 run title @s actionbar [{"text":"+300 💰  ","color":"gold","bold":true},{"text":"Gardien noyé","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_a_noye
scoreboard players set $kk mg.st 42
function mg:ombre/khook
