# @s : bonus au sol (ramassé en entrant dans sa case)
tag @s add mg.ypt
execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0,limit=1] run function mg:bman/pu_take
tag @s remove mg.ypt
