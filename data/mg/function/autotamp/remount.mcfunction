# @s (joueur en piste) n'est plus dans un bateau : nouveau bateau à sa place (dans la piste)
execute unless entity @s[x=-18,y=60,z=37382,dx=36,dy=12,dz=36] run function mg:autotamp/place
execute at @s run function mg:autotamp/boat
