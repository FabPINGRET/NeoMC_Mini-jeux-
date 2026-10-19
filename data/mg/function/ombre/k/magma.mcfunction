# @s a vaincu : Cube de magma
advancement revoke @s only mg:ombre/k/magma
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 24
function mg:ombre/xpk {n:76}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..40 run scoreboard players add @s mg.olm6 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..40 run title @s actionbar [{"text":"+24 💰  ","color":"gold","bold":true},{"text":"+1 écaille de drake  ","color":"red"},{"text":"Cube de magma","color":"gray"}]
execute unless score $r mg.st matches ..40 run title @s actionbar [{"text":"+24 💰  ","color":"gold","bold":true},{"text":"Cube de magma","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p26 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_magma
scoreboard players set $kk mg.st 26
function mg:ombre/khook
