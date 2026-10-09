# Toutes les 0,5 s : musique pour ceux qui entrent, coupée pour ceux qui sortent, animation
execute in mg:gta as @a[tag=mg.gtw,tag=!mg.gclub,x=-70,y=64,z=32423,dx=20,dy=8,dz=14] at @s run function mg:gta/club_in
execute as @a[tag=mg.gclub] at @s unless entity @s[x=-70,y=64,z=32423,dx=20,dy=8,dz=14] run function mg:gta/club_out
execute if entity @a[tag=mg.gclub] run function mg:gta/club_fx
