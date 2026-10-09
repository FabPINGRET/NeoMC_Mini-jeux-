# @s : joueur, #k quilles renversées (#ln piste)
execute store result storage mg:bowl q.l int 1 run scoreboard players get @s mg.bln
function mg:bowl/w_load with storage mg:bowl q
tag @s remove mg.bnr
scoreboard players set #ev mg.st 0
execute if score @s mg.bp1n matches 1.. run scoreboard players operation @s mg.bp1s += #k mg.st
execute if score @s mg.bp1n matches 1.. run scoreboard players remove @s mg.bp1n 1
execute if score @s mg.bp2n matches 1.. run scoreboard players operation @s mg.bp2s += #k mg.st
execute if score @s mg.bp2n matches 1.. run scoreboard players remove @s mg.bp2n 1
execute if score @s mg.bp1n matches 0 if score @s mg.bp1f matches 1.. run function mg:bowl/p1_close
execute if score @s mg.bp1n matches 0 if score @s mg.bp1f matches 1.. run function mg:bowl/p1_close
scoreboard players operation @s mg.bfs += #k mg.st
execute store result storage mg:bowl w.f int 1 run scoreboard players get @s mg.bfr
execute if score @s mg.bfr matches 5 run function mg:bowl/r_last
execute if score @s mg.bfr matches ..4 run function mg:bowl/r_frame
scoreboard players operation @s mg.bsc = @s mg.bcu
execute if score @s mg.bp1f matches 1.. run scoreboard players operation @s mg.bsc += @s mg.bp1s
execute if score @s mg.bp2f matches 1.. run scoreboard players operation @s mg.bsc += @s mg.bp2s
scoreboard players operation @s mg.bsc += @s mg.bfs
execute store result storage mg:bowl w.t int 1 run scoreboard players get @s mg.bsc
function mg:bowl/render with storage mg:bowl w
function mg:bowl/w_save with storage mg:bowl w
function mg:bowl/announce
scoreboard players set @s mg.bph 3
scoreboard players set @s mg.btm 0
