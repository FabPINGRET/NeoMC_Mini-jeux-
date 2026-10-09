scoreboard players operation @s mg.br2 = #k mg.st
execute if score @s mg.br1 matches 10 run return run function mg:bowl/l2_after_x
scoreboard players operation #q mg.st = @s mg.br1
scoreboard players operation #q mg.st += #k mg.st
execute if score #q mg.st matches 10 run data modify storage mg:bowl w.b set value "/"
execute unless score #q mg.st matches 10 run function mg:bowl/mk_b
function mg:bowl/mw with storage mg:bowl w
execute if score #q mg.st matches 10 run scoreboard players set #ev mg.st 2
execute if score #q mg.st matches 10 run tag @s add mg.bnr
execute if score #q mg.st matches 10 run return run scoreboard players set @s mg.brl 3
execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4
function mg:bowl/last_end
