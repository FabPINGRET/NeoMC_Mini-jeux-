# @s a vaincu : Archer desséché
advancement revoke @s only mg:ombre/k/desseche
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 18
function mg:ombre/xpk {n:58}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..30 run scoreboard players add @s mg.olm5 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..30 run title @s actionbar [{"text":"+18 💰  ","color":"gold","bold":true},{"text":"+1 ambre solaire  ","color":"yellow"},{"text":"Archer desséché","color":"gray"}]
execute unless score $r mg.st matches ..30 run title @s actionbar [{"text":"+18 💰  ","color":"gold","bold":true},{"text":"Archer desséché","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p21 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_desseche
scoreboard players set $kk mg.st 21
function mg:ombre/khook
