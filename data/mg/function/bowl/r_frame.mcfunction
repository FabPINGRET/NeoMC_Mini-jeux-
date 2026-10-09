# @s : lancer dans un frame normal
execute if score @s mg.brl matches 1 if score #k mg.st matches 10 run return run function mg:bowl/r_strike
execute if score @s mg.brl matches 1 run return run function mg:bowl/r_first
scoreboard players operation #q mg.st = @s mg.br1
scoreboard players operation #q mg.st += #k mg.st
execute if score #q mg.st matches 10 run return run function mg:bowl/r_spare
function mg:bowl/mk_b
function mg:bowl/mw with storage mg:bowl w
scoreboard players set #ev mg.st 0
execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4
scoreboard players operation @s mg.bcu += @s mg.bfs
execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bfr
execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu
function mg:bowl/cw with storage mg:bowl q
scoreboard players set @s mg.bxs 0
function mg:bowl/next_frame
