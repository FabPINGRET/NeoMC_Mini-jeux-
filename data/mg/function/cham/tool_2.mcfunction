# Pipette : premier bloc solide regardé (6 blocs)
scoreboard players set $cmf mg.st 0
scoreboard players set $cmr mg.st 30
execute anchored eyes positioned ^ ^ ^0.2 run function mg:cham/pip_ray
execute if score $cmf mg.st matches 0 run title @s actionbar {"text":"💧 Rien à copier ici : vise un mur, un sol ou un meuble","color":"gray"}
