# @s a vaincu : Élémentaire de feu
advancement revoke @s only mg:ombre/k/feu
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 26
function mg:ombre/xpk {n:80}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm6 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+26 💰  ","color":"gold","bold":true},{"text":"+1 écaille de drake  ","color":"red"},{"text":"Élémentaire de feu","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+26 💰  ","color":"gold","bold":true},{"text":"Élémentaire de feu","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p25 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_feu
scoreboard players set $kk mg.st 25
function mg:ombre/khook
