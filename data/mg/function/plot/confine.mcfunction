# Garde @s dans son plot (survol des murs, chute sous le sol) : retour au centre sinon
execute store result score $dx mg.t run data get entity @s Pos[0]
execute store result score $dy mg.t run data get entity @s Pos[1]
execute store result score $dz mg.t run data get entity @s Pos[2]
scoreboard players operation $dx mg.t -= @s mg.pcx
scoreboard players operation $dz mg.t -= @s mg.pcz
execute unless score $dx mg.t matches -12..12 run return run function mg:plot/tp_home
execute unless score $dz mg.t matches -12..12 run return run function mg:plot/tp_home
execute if score $dy mg.t matches ..49 run function mg:plot/tp_home
