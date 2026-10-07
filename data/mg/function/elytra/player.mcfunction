# Parcours d'élytra, chaque tick (@s = joueur tagué mg.ely, positionné)
execute if entity @s[tag=mg.play] run return run function mg:elytra/stop_quiet
execute if entity @s[tag=mg.surv] run return run function mg:elytra/stop_quiet
execute if score @s mg.est matches 0 if predicate mg:gliding run function mg:elytra/go
execute if score @s mg.est matches 0 run title @s actionbar [{"text":"Saute de la plateforme et ouvre tes élytres !","color":"aqua"}]
execute if score @s mg.est matches 1 run scoreboard players add @s mg.et 1
execute if score @s mg.est matches 1 if predicate mg:gliding run scoreboard players set @s mg.eg 0
execute if score @s mg.est matches 1 unless predicate mg:gliding run scoreboard players add @s mg.eg 1

# Anneaux, dans l'ordre
execute if score @s mg.ec matches 0 if entity @s[x=-17,y=167,z=-47,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 1 if entity @s[x=13,y=163,z=-47,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 2 if entity @s[x=43,y=157,z=-17,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 3 if entity @s[x=43,y=153,z=13,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 4 if entity @s[x=13,y=147,z=43,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 5 if entity @s[x=-17,y=143,z=43,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 6 if entity @s[x=-47,y=137,z=13,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 7 if entity @s[x=-47,y=133,z=-17,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 8.. run return run function mg:elytra/finish

# Échecs : sous le parcours, trop loin, ou posé plus de 2 s
execute unless entity @s[y=118,dy=400] run return run function mg:elytra/fail
execute unless entity @s[x=-76,y=-64,z=-76,dx=152,dy=500,dz=152] run return run function mg:elytra/fail
execute if score @s mg.eg matches 40.. run return run function mg:elytra/fail

# Guide lumineux vers le prochain anneau + chrono
execute if score @s mg.ec matches 0 run particle minecraft:end_rod -14.5 169.5 -44.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 1 run particle minecraft:end_rod 15.5 165.5 -44.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 2 run particle minecraft:end_rod 45.5 159.5 -14.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 3 run particle minecraft:end_rod 45.5 155.5 15.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 4 run particle minecraft:end_rod 15.5 149.5 45.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 5 run particle minecraft:end_rod -14.5 145.5 45.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 6 run particle minecraft:end_rod -44.5 139.5 15.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 7 run particle minecraft:end_rod -44.5 135.5 -14.5 1 1 1 0.01 3 force @s
execute if score @s mg.est matches 1 run function mg:elytra/hud
