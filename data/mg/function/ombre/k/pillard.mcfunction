# @s a vaincu : Pillard du désert
advancement revoke @s only mg:ombre/k/pillard
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 24
function mg:ombre/xpk {n:64}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..30 run scoreboard players add @s mg.olm5 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..30 run title @s actionbar [{"text":"+24 💰  ","color":"gold","bold":true},{"text":"+1 ambre solaire  ","color":"yellow"},{"text":"Pillard du désert","color":"gray"}]
execute unless score $r mg.st matches ..30 run title @s actionbar [{"text":"+24 💰  ","color":"gold","bold":true},{"text":"Pillard du désert","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p23 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_pillard
scoreboard players set $kk mg.st 23
function mg:ombre/khook
