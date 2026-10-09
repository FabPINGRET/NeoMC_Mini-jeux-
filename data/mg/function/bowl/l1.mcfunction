scoreboard players operation @s mg.br1 = #k mg.st
function mg:bowl/mk_a
function mg:bowl/mw with storage mg:bowl w
scoreboard players set @s mg.brl 2
execute if score #k mg.st matches 10 run tag @s add mg.bnr
execute if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1
execute if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1
execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4
execute unless score #k mg.st matches 10 run scoreboard players set @s mg.bxs 0
