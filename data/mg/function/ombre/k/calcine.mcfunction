# @s a vaincu : Chevalier calciné
advancement revoke @s only mg:ombre/k/calcine
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 30
function mg:ombre/xpk {n:94}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm6 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+30 💰  ","color":"gold","bold":true},{"text":"+1 écaille de drake  ","color":"red"},{"text":"Chevalier calciné","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+30 💰  ","color":"gold","bold":true},{"text":"Chevalier calciné","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p28 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_calcine
scoreboard players set $kk mg.st 28
function mg:ombre/khook
