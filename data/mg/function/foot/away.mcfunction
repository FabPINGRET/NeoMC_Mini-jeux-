# @s (mg.ftr, mg.ftb ou mg.ftin) : toujours sur le terrain ? Oui (et en overworld) : rien ; non : plus compté, plus d'équipe
execute if entity @s[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] at @s if dimension minecraft:overworld run return 0
tag @s remove mg.ftin
function mg:foot/cleanup
scoreboard players reset @s mg.ft
tag @s remove mg.ftlt
