# Survie (chaque tick) : commandes, retours depuis le Nether, entretien du monde des mini-jeux
scoreboard players enable @a mg.sv
execute as @a[scores={mg.sv=1..}] run function mg:survie/cmd
execute as @a[tag=mg.surv] at @s if dimension minecraft:overworld run function mg:survie/from_overworld
scoreboard players reset @a[tag=mg.surv] mg.cs
scoreboard players reset @a[tag=mg.surv] mg.us
scoreboard players reset @a[tag=mg.surv] mg.wc
scoreboard players reset @a[tag=mg.surv] mg.fw
scoreboard players reset @a[tag=mg.surv] mg.qs

# Monde des mini-jeux : objets au sol supprimés (sauf ceux du Bedwars en cours), plus d'orbes d'XP
execute if score $game mg.st matches 4 in minecraft:overworld run tag @e[type=minecraft:item,x=-60,y=-64,z=1140,dx=120,dy=384,dz=120] add mg.keep
execute in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:item,distance=0..,tag=!mg.keep]
execute in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:experience_orb,distance=0..]

scoreboard players add $svt mg.st 1
execute if score $svt mg.st matches 10 run function mg:survie/sweep_mobs
execute if score $svt mg.st matches 20.. run function mg:survie/second
