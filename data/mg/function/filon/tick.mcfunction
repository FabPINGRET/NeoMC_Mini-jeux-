# Chaque tick (joueurs présents) : clics, triggers, objets, morts, sécurité
execute as @e[type=minecraft:interaction,tag=mg.fni,x=-60,y=0,z=45930,dx=136,dy=200,dz=136] if data entity @s interaction run function mg:filon/click
scoreboard players enable @a[tag=mg.fnw] mg.fnt
execute as @a[tag=mg.fnw,scores={mg.fnt=1..}] run function mg:filon/cmd
execute as @a[tag=mg.fnw,scores={mg.fnu=1..}] at @s run function mg:filon/use
execute as @a[tag=mg.fnw,scores={mg.fnd=1..}] run function mg:filon/died
scoreboard players reset @a[tag=mg.fnw] mg.fnk
# dans la mine ou en surface
tag @a[tag=mg.fnw] remove mg.fnin
tag @a[tag=mg.fnw,x=0,y=39,z=46000,dx=15,dy=64,dz=15] add mg.fnin
execute as @a[tag=mg.fnw,tag=!mg.fnin] at @s if entity @s[y=-64,dy=159] run function mg:filon/to_surface
execute as @a[tag=mg.fnw] at @s unless entity @s[x=-60,y=0,z=45930,dx=136,dy=200,dz=136] run function mg:filon/to_surface
execute if score $fnpvp mg.st matches 1 run team leave @a[tag=mg.fnw,tag=mg.fnin]
execute if score $fnpvp mg.st matches 1 run team join mg_fn @a[tag=mg.fnw,tag=!mg.fnin]
