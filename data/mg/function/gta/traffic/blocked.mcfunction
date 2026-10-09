# @s : obstacle devant (joueur, passant, voiture) : arrêt, klaxon au bout de 3 s
execute if score @s mg.gtw8 matches 60 run playsound minecraft:block.note_block.didgeridoo neutral @a ~ ~ ~ 1.5 1.6
execute if score @s mg.gtw8 matches 63 run playsound minecraft:block.note_block.didgeridoo neutral @a ~ ~ ~ 1.5 1.6
execute if score @s mg.gtw8 matches 300.. run return run function mg:gta/traffic/despawn
execute at @s run function mg:gta/traffic/sync
