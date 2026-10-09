# 3e lancer (bonus) du dernier frame
scoreboard players operation #q mg.st = @s mg.br2
scoreboard players operation #q mg.st += #k mg.st
execute if score @s mg.br1 matches 10 unless score @s mg.br2 matches 10 if score #q mg.st matches 10 run data modify storage mg:bowl w.c set value "/"
execute if score @s mg.br1 matches 10 unless score @s mg.br2 matches 10 if score #q mg.st matches 10 run scoreboard players set #ev mg.st 2
execute unless data storage mg:bowl w{c:"/"} run function mg:bowl/mk_c
execute unless data storage mg:bowl w{c:"/"} if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1
execute unless data storage mg:bowl w{c:"/"} if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1
function mg:bowl/mw with storage mg:bowl w
function mg:bowl/last_end
