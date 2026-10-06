# Fin de mèche (@s = mouton, à sa position)

# --- Spéciaux sans explosion ---
execute if entity @s[tag=mg.k_nausea] run return run function mg:sheepwar/boom_nausea
execute if entity @s[tag=mg.k_freeze] run return run function mg:sheepwar/boom_freeze
execute if entity @s[tag=mg.k_blind] run return run function mg:sheepwar/boom_blind
execute if entity @s[tag=mg.k_fire] run return run function mg:sheepwar/boom_fire

execute if entity @s[tag=mg.k_mitra] run function mg:sheepwar/boom_mitra_step
execute if entity @s[tag=mg.k_mitra] run return run kill @s

# --- Super / ULTRA explosif (explosion_power = puissance ; TNT normal = 4) ---
execute if entity @s[tag=mg.k_super] run summon minecraft:tnt ~ ~ ~ {fuse:0s,explosion_power:5f}
execute if entity @s[tag=mg.k_ultra] run summon minecraft:tnt ~ ~ ~ {fuse:0s,explosion_power:9f}
execute if entity @s[tag=mg.k_ultra] run particle minecraft:explosion_emitter ~ ~1 ~ 2 1 2 0 6
execute if entity @s[tag=mg.k_ultra] run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 3 0.5
execute if entity @s[tag=mg.k_super] run return run kill @s
execute if entity @s[tag=mg.k_ultra] run return run kill @s

# --- Mouton normal et mouton de l'espace : explosion ---
summon minecraft:tnt ~ ~ ~ {fuse:0s}
execute if entity @s[tag=mg.k_space] run particle minecraft:end_rod ~ ~1 ~ 1 1 1 0.3 60
particle minecraft:explosion ~ ~0.5 ~ 0.5 0.5 0.5 0 10
kill @s
