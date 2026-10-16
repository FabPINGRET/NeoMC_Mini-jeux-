# Chaque seconde, @s (joueur) : région où il se trouve (0 vallée, 1 nord, 2 est, 3 ouest, 4 sud)
scoreboard players set $r mg.st 0
execute if entity @s[x=-96,y=-64,z=-256,dx=191,dy=400,dz=159] run scoreboard players set $r mg.st 1
execute if entity @s[x=96,y=-64,z=-96,dx=159,dy=400,dz=191] run scoreboard players set $r mg.st 2
execute if entity @s[x=-256,y=-64,z=-96,dx=159,dy=400,dz=191] run scoreboard players set $r mg.st 3
execute if entity @s[x=-96,y=-64,z=96,dx=191,dy=400,dz=159] run scoreboard players set $r mg.st 4
execute unless score @s mg.trrg = $r mg.st run function mg:terra/rpg/region_chg
