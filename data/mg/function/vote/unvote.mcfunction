# @s = joueur : retire son vote
scoreboard players reset @s mg.vc
function mg:vote/refresh
tellraw @s [{"text":"✖ Vote retiré.","color":"gray"}]
