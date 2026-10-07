# L'Émissaire du Kraken
function mg:mobarena/hp_check
scoreboard players add $bc mg.st 1
# Répulsion : tous les joueurs à moins de 11 blocs sont repoussés
execute as @e[tag=mg.boss,limit=1] at @s as @a[tag=mg.play,distance=..11] at @s facing entity @e[tag=mg.boss,limit=1] feet rotated ~ 0 run tp @s ^ ^ ^-0.8
execute at @e[tag=mg.boss] run particle minecraft:bubble ~ ~2 ~ 2 2 2 0.1 10
# Rayon laser continu sur le joueur le plus proche (2 PV tous les 15 ticks)
scoreboard players operation $m1 mg.st = $bc mg.st
scoreboard players operation $m1 mg.st %= $k15 mg.st
execute if score $m1 mg.st matches 0 as @e[tag=mg.boss,limit=1] at @s positioned ~ ~2.5 ~ facing entity @p[tag=mg.play] eyes run function mg:mobarena/temple/beam
execute as @e[tag=mg.boss,limit=1] at @s positioned ~ ~2.5 ~ facing entity @p[tag=mg.play] eyes run function mg:mobarena/temple/beam_vis
# Phase 2
execute if entity @e[tag=mg.boss,tag=!mg.ph2] if score $bh2 mg.st <= $bmax mg.st run function mg:mobarena/temple/phase2
execute store result score $tn mg.st if entity @e[type=minecraft:slime,tag=mg.tent]
execute if entity @e[tag=mg.boss,tag=mg.shield] if score $tn mg.st matches 0 run function mg:mobarena/temple/unshield
execute at @e[tag=mg.boss,tag=mg.shield] run particle minecraft:end_rod ~ ~2 ~ 2.5 2.5 2.5 0.02 8
