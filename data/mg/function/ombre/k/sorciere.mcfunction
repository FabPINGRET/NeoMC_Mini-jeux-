# @s a vaincu : Sorcière des marais
advancement revoke @s only mg:ombre/k/sorciere
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 16
function mg:ombre/xpk {n:45}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..35 run scoreboard players add @s mg.olm4 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..35 run title @s actionbar [{"text":"+16 💰  ","color":"gold","bold":true},{"text":"+1 fiole de venin  ","color":"dark_green"},{"text":"Sorcière des marais","color":"gray"}]
execute unless score $r mg.st matches ..35 run title @s actionbar [{"text":"+16 💰  ","color":"gold","bold":true},{"text":"Sorcière des marais","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_sorciere
scoreboard players set $kk mg.st 14
function mg:ombre/khook
