# Plots (chaque tick) : créatif seulement sur son propre plot
execute as @a[tag=mg.inplot] unless entity @s[gamemode=creative] run tag @s remove mg.inplot
execute as @a[tag=mg.inplot] run function mg:plot/confine
execute as @a[tag=mg.inplot,tag=mg.plabel] run function mg:plot/label_try

# Murs réparés toutes les 5 s (un joueur en créatif peut casser une barrière)
scoreboard players add $pw mg.t 1
execute if score $pw mg.t matches 100.. as @a[tag=mg.inplot] run function mg:plot/walls_fix
execute if score $pw mg.t matches 100.. run scoreboard players set $pw mg.t 0
