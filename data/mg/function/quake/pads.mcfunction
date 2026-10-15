# Quakecraft (cartes verticales) : tremplins — slime = petit saut, émeraude = grand saut
execute as @a[tag=mg.play,gamemode=adventure] at @s if block ~ ~-0.3 ~ minecraft:slime_block run function mg:quake/pad {a:5}
execute as @a[tag=mg.play,gamemode=adventure] at @s if block ~ ~-0.3 ~ minecraft:emerald_block run function mg:quake/pad {a:9}
