# 1er lancer sans strike
scoreboard players operation @s mg.br1 = #k mg.st
function mg:bowl/mk_a
data modify storage mg:bowl w.b set value ""
data modify storage mg:bowl w.c set value ""
function mg:bowl/mw with storage mg:bowl w
scoreboard players set @s mg.brl 2
execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4
