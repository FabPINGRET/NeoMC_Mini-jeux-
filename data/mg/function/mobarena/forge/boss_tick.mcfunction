# Le Golem de Basalte
function mg:mobarena/hp_check
scoreboard players add $bc mg.st 1
execute at @e[tag=mg.boss] run particle minecraft:flame ~ ~1.5 ~ 1 1.5 1 0.03 6
execute at @e[tag=mg.boss] run particle minecraft:smoke ~ ~3 ~ 0.6 0.6 0.6 0.02 3
# Phase 1 : onde de choc toutes les 5 s (annoncée 1 s avant)
scoreboard players operation $m1 mg.st = $bc mg.st
scoreboard players operation $m1 mg.st %= $k100 mg.st
execute if score $m1 mg.st matches 80 at @e[tag=mg.boss] run particle minecraft:flame ~ ~0.3 ~ 6 0.1 6 0.02 120
execute if score $m1 mg.st matches 80 at @e[tag=mg.boss] run playsound minecraft:block.anvil.land master @a ~ ~ ~ 1 0.5
execute if score $m1 mg.st matches 0 as @e[tag=mg.boss,limit=1] at @s run function mg:mobarena/forge/shock
# Phase 2 : pluie de météorites
execute if entity @e[tag=mg.boss,tag=!mg.ph2] if score $bh2 mg.st <= $bmax mg.st run function mg:mobarena/forge/phase2
scoreboard players operation $m2 mg.st = $bc mg.st
scoreboard players operation $m2 mg.st %= $k20 mg.st
execute if entity @e[tag=mg.boss,tag=mg.ph2] if score $m2 mg.st matches 0 run function mg:mobarena/forge/meteor_spawn
