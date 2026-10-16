# Fin du Labyrinthe géant
schedule clear mg:maze/build
kill @e[type=!minecraft:player,x=-50,y=55,z=41050,dx=106,dy=40,dz=100]
effect clear @a minecraft:night_vision
clear @a minecraft:compass
team leave @a[team=mg_sq]
scoreboard players reset * mg.jid
scoreboard players reset * mg.jc
scoreboard players reset * mg.je
scoreboard players reset * mg.jk
function mg:maze/sas
forceload remove -51 41049 57 41150
