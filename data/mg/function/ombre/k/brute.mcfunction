# @s a vaincu : Brute calcinée
advancement revoke @s only mg:ombre/k/brute
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 32
function mg:ombre/xpk {n:96}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm6 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+32 💰  ","color":"gold","bold":true},{"text":"+1 écaille de drake  ","color":"red"},{"text":"Brute calcinée","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+32 💰  ","color":"gold","bold":true},{"text":"Brute calcinée","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p27 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_brute
scoreboard players set $kk mg.st 27
function mg:ombre/khook
