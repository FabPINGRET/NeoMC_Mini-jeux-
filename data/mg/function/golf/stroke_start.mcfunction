# @s : début d'un coup (balle à l'arrêt) : jauge à zéro, replacé à côté de sa balle, distance au trou
scoreboard players set @s mg.gfs 0
scoreboard players set @s mg.gfp 0
scoreboard players set @s mg.gfq 1
scoreboard players set @s mg.gfk 12
scoreboard players reset @s mg.qs
function mg:golf/own
function mg:golf/place
function mg:golf/dist
tag @e[tag=mg.gfmy] remove mg.gfmy
