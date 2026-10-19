# @s a vaincu : Forgeron calciné
advancement revoke @s only mg:ombre/k/a_forgeron
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 420
function mg:ombre/xpk {n:1050}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..100 run scoreboard players add @s mg.olm6 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..100 run title @s actionbar [{"text":"+420 💰  ","color":"gold","bold":true},{"text":"+1 écaille de drake  ","color":"red"},{"text":"Forgeron calciné","color":"gray"}]
execute unless score $r mg.st matches ..100 run title @s actionbar [{"text":"+420 💰  ","color":"gold","bold":true},{"text":"Forgeron calciné","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_a_forgeron
scoreboard players set $kk mg.st 44
function mg:ombre/khook
