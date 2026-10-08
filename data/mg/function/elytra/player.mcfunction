# Parcours d'élytra, chaque tick (@s = joueur tagué mg.ely, positionné)
execute if entity @s[tag=mg.play] run return run function mg:elytra/stop_quiet
execute if entity @s[tag=mg.surv] run return run function mg:elytra/stop_quiet
execute unless score @s mg.ecr matches 1..2 run scoreboard players set @s mg.ecr 1
execute if score @s mg.est matches 0 if predicate mg:gliding run function mg:elytra/go
execute if score @s mg.est matches 0 run title @s actionbar [{"text":"Saute de la plateforme et ouvre tes élytres !","color":"aqua"}]
execute if score @s mg.est matches 1 run scoreboard players add @s mg.et 1
execute if score @s mg.est matches 1 if predicate mg:gliding run scoreboard players set @s mg.eg 0
execute if score @s mg.est matches 1 unless predicate mg:gliding run scoreboard players add @s mg.eg 1
execute if score @s mg.ecr matches 1 run return run function mg:elytra/rings1
execute if score @s mg.ecr matches 2 run return run function mg:elytra/rings2
