# @s = pack, position exécutée = le pack : particules, ramassage par le joueur le plus proche à 1 PV
execute if predicate {condition:"minecraft:random_chance",chance:0.15} run particle minecraft:heart ~ ~0.5 ~ 0.25 0.25 0.25 0 1
execute store success score #tmhs mg.st if entity @a[tag=mg.play,gamemode=adventure,distance=..1.3,scores={mg.tmhp=..1}]
execute if score #tmhs mg.st matches 1 as @p[tag=mg.play,gamemode=adventure,distance=..1.3,scores={mg.tmhp=..1}] run function mg:tdm/pack_take
execute if score #tmhs mg.st matches 1 run kill @s
