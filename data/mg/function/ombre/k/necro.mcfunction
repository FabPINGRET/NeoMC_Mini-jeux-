# @s a vaincu : Nécromancien
advancement revoke @s only mg:ombre/k/necro
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 50
function mg:ombre/xpk {n:150}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..40 run scoreboard players add @s mg.olm8 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..40 run title @s actionbar [{"text":"+50 💰  ","color":"gold","bold":true},{"text":"+1 essence d'ombre  ","color":"dark_purple"},{"text":"Nécromancien","color":"gray"}]
execute unless score $r mg.st matches ..40 run title @s actionbar [{"text":"+50 💰  ","color":"gold","bold":true},{"text":"Nécromancien","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_necro
scoreboard players set $kk mg.st 35
function mg:ombre/khook
