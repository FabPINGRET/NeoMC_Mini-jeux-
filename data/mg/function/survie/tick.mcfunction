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
execute if score $game mg.st matches 204 in minecraft:overworld run tag @e[type=minecraft:item,x=-43,y=40,z=34757,dx=86,dy=90,dz=86] add mg.keep
execute if score $game mg.st matches 205 in minecraft:overworld run tag @e[type=minecraft:item,x=-53,y=40,z=34947,dx=106,dy=90,dz=106] add mg.keep
execute if score $game mg.st matches 202 in minecraft:overworld run tag @e[type=minecraft:item,x=-43,y=40,z=34357,dx=86,dy=90,dz=86] add mg.keep
execute if score $game mg.st matches 203 in minecraft:overworld run tag @e[type=minecraft:item,x=-53,y=40,z=34547,dx=106,dy=90,dz=106] add mg.keep
execute if score $game mg.st matches 94 in minecraft:overworld run tag @e[type=minecraft:item,x=-43,y=40,z=22357,dx=86,dy=90,dz=86] add mg.keep
execute if score $game mg.st matches 95 in minecraft:overworld run tag @e[type=minecraft:item,x=-53,y=40,z=22747,dx=106,dy=90,dz=106] add mg.keep
execute in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:item,distance=0..,tag=!mg.keep]
execute in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:experience_orb,distance=0..]

scoreboard players add $svt mg.st 1
execute if score $svt mg.st matches 10 run function mg:survie/sweep_mobs
execute if score $svt mg.st matches 20.. run function mg:survie/second
