# @s : robot — renvoie la balle tagguée mg.tnhit
scoreboard players set @s mg.tnt 10
function mg:tennis/robot_pick
execute as @e[tag=mg.tnhit] run function mg:tennis/shoot
tag @e[tag=mg.tnhit] remove mg.tnhit
