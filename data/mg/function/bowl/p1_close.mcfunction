# @s : le plus ancien frame en attente est complet → cumul, case remplie, l'attente suivante remonte
scoreboard players operation @s mg.bcu += @s mg.bp1s
execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bp1f
execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu
function mg:bowl/cw with storage mg:bowl q
scoreboard players operation @s mg.bp1f = @s mg.bp2f
scoreboard players operation @s mg.bp1s = @s mg.bp2s
scoreboard players operation @s mg.bp1n = @s mg.bp2n
scoreboard players set @s mg.bp2f 0
scoreboard players set @s mg.bp2s 0
scoreboard players set @s mg.bp2n 0
