# (OP) Construit le parcours Élytra (modes 1-2) et l'arène de survie (mode 3), section par section (asynchrone)
execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : construction déjà en cours.","color":"yellow"}]
scoreboard players set $skbm mg.st 1
scoreboard players set $skbs mg.st 0
scoreboard players set $skw mg.st 0
scoreboard players set $skbn mg.st 164
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : construction du décor (28 sections)...","color":"gray"}]
schedule function mg:sky/b_next 1t
