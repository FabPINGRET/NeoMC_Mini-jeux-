# @s (cacheur) s'accroupit : copie l'objet qu'il regarde (5 blocs max)
scoreboard players set $phf mg.st 0
scoreboard players set $phr mg.st 25
execute at @s anchored eyes positioned ^ ^ ^0.2 run function mg:ph/copy_ray
execute if score $phf mg.st matches 0 run title @s actionbar {"text":"Regarde un objet du manoir (tonneau, citrouille, enclume…)","color":"gray"}
execute if score $phf mg.st matches 1 run function mg:ph/apply
execute if score $phf mg.st matches 1 at @s run playsound minecraft:entity.illusioner.mirror_move player @s ~ ~ ~ 0.6 1.4
execute if score $phf mg.st matches 1 at @s run particle minecraft:poof ~ ~0.5 ~ 0.3 0.3 0.3 0.02 8
