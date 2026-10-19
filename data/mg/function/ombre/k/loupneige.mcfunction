# @s a vaincu : Loup des neiges
advancement revoke @s only mg:ombre/k/loupneige
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 10
function mg:ombre/xpk {n:30}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm3 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+10 💰  ","color":"gold","bold":true},{"text":"+1 éclat de givre  ","color":"aqua"},{"text":"Loup des neiges","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+10 💰  ","color":"gold","bold":true},{"text":"Loup des neiges","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_loupneige
scoreboard players set $kk mg.st 12
function mg:ombre/khook
