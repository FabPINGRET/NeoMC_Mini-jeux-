# @s (scientifique) : fusée de détection
playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1 1
particle minecraft:firework ~ ~3 ~ 0.4 2 0.4 0.05 40 force
particle minecraft:glow ~ ~1 ~ 6 1 6 0 60
effect give @e[tag=mg.tvd,distance=..40] minecraft:glowing 10 0 true
execute if score $rk mg.st matches 1 run effect give @a[tag=mg.tvw,distance=..8] minecraft:regeneration 6 1
execute if score $rk mg.st matches 2.. run effect give @a[tag=mg.tvw,distance=..8] minecraft:regeneration 6 2
execute if score $rk mg.st matches 3.. run effect give @a[tag=mg.tvw,distance=..8] minecraft:absorption 20 1
