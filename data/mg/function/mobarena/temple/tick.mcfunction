# Le Temple des Profondeurs — tick
kill @e[distance=0..,type=minecraft:slime,tag=!mg.mob]
# Gardiens : ralentissement + fatigue de minage chaque seconde
scoreboard players operation $m1 mg.st = $bt mg.st
scoreboard players operation $m1 mg.st %= $k20 mg.st
execute if score $m1 mg.st matches 0 as @e[type=minecraft:guardian,tag=mg.mob] at @s if entity @a[tag=mg.play,distance=..14] run function mg:mobarena/temple/curse
execute if entity @e[tag=mg.boss] run function mg:mobarena/temple/boss_tick
