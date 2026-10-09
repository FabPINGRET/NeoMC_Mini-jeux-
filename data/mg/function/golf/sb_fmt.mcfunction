# @s : texte de sa ligne au tableau
execute store result storage mg:golf f.t int 1 run scoreboard players get @s mg.gft
scoreboard players operation $gfrel mg.st = @s mg.gft
scoreboard players operation $gfrel mg.st -= $gfpc mg.st
execute store result storage mg:golf f.n int 1 run scoreboard players get $gfrel mg.st
data modify storage mg:golf f.p set value ""
data modify storage mg:golf f.c set value "green"
execute if score $gfrel mg.st matches 0 run data modify storage mg:golf f.p set value "±"
execute if score $gfrel mg.st matches 0 run data modify storage mg:golf f.c set value "white"
execute if score $gfrel mg.st matches 1.. run data modify storage mg:golf f.p set value "+"
execute if score $gfrel mg.st matches 1.. run data modify storage mg:golf f.c set value "red"
function mg:golf/sb_set with storage mg:golf f
