# Survie (chaque tick) : commandes, retours depuis le Nether, entretien du monde des mini-jeux
scoreboard players enable @a mg.sv
execute as @a[scores={mg.sv=1..}] run function mg:survie/cmd
execute as @a[tag=mg.surv,tag=!mg.fnw] at @s if dimension minecraft:overworld run function mg:survie/from_overworld
# Monde de survie régénéré : les joueurs qui y étaient repartent du point de départ (inventaire gardé)
execute as @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw,tag=!mg.fnw,tag=!mg.svg2,scores={mg.svid=1..}] run function mg:survie/regen_now
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
execute if score $fnw mg.st matches 1 in minecraft:overworld run tag @e[type=minecraft:item,x=-60,y=0,z=45930,dx=136,dy=200,dz=136] add mg.keep
execute if score $state mg.st matches 2 as @a[tag=mg.play,scores={mg.zdr=1..}] at @s run tag @e[type=minecraft:item,distance=..8] add mg.keep
# nettoyage toutes les 5 ticks (0,25 s : aucun ramassage possible avant 10 ticks) : deux parcours de toutes les entités du monde en moins
scoreboard players operation #sv5 mg.st = $svt mg.st
scoreboard players operation #sv5 mg.st %= #5 mg.st
execute if score #sv5 mg.st matches 0 in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:item,distance=0..,tag=!mg.keep]
execute if score #sv5 mg.st matches 0 in minecraft:overworld positioned 0 0 0 run kill @e[type=minecraft:experience_orb,distance=0..]

scoreboard players add $svt mg.st 1
execute if score $svt mg.st matches 10 run function mg:survie/sweep_mobs
execute if score $svt mg.st matches 20.. run function mg:survie/second
