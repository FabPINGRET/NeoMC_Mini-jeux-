# Le Cœur I.A. Corrompu
function mg:mobarena/hp_check
scoreboard players add $bc mg.st 1
execute at @e[tag=mg.boss] run particle minecraft:electric_spark ~ ~1.8 ~ 1 1.8 1 0.3 8
execute if entity @e[tag=mg.boss,tag=!mg.ph2] run function mg:mobarena/ship/ph1_tick
execute if entity @e[tag=mg.boss,tag=!mg.ph2] if score $bh2 mg.st <= $bmax mg.st run function mg:mobarena/ship/phase2
execute if entity @e[tag=mg.boss,tag=mg.ph2] run function mg:mobarena/ship/ph2_tick
