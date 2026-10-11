execute unless entity @e[tag=mg.evb] run return run function mg:lobby/ev/e1_dead
bossbar set mg:ev name [{"text":"👑 Roi Zombie","color":"red","bold":true},{"text":"  (tape-le !)","color":"gray"}]
execute store result bossbar mg:ev value run data get entity @e[tag=mg.evb,limit=1] Health
scoreboard players operation $evm mg.st = $evt mg.st
scoreboard players operation $evm mg.st %= #ev10 mg.st
execute if score $evm mg.st matches 0 if score $evt mg.st matches 1..170 at @e[tag=mg.evb,limit=1] run function mg:lobby/ev/e1_minions
