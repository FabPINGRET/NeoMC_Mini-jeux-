# @s a vaincu : Contremaître maudit
advancement revoke @s only mg:ombre/k/a_contremaitre
execute unless entity @s[tag=mg.olw] run return 0
scoreboard players add @s mg.olkt 1
scoreboard players add @s mg.olg 480
function mg:ombre/xpk {n:1200}
execute store result score $r mg.st run random value 1..100
execute if score $r mg.st matches ..100 run scoreboard players add @s mg.olm7 1
scoreboard players set @s mg.olal 30
execute if score $r mg.st matches ..100 run title @s actionbar [{"text":"+480 💰  ","color":"gold","bold":true},{"text":"+1 minerai de runite  ","color":"blue"},{"text":"Contremaître maudit","color":"gray"}]
execute unless score $r mg.st matches ..100 run title @s actionbar [{"text":"+480 💰  ","color":"gold","bold":true},{"text":"Contremaître maudit","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/k/new_a_contremaitre
scoreboard players set $kk mg.st 45
function mg:ombre/khook
