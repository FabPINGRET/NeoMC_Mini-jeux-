# L'Abomination Toxique
function mg:mobarena/hp_check
scoreboard players add $bc mg.st 1
execute at @e[tag=mg.boss] run particle minecraft:sneeze ~ ~2 ~ 1.4 1.8 1.4 0 6
execute at @e[tag=mg.boss,tag=mg.shield] run particle minecraft:end_rod ~ ~1.8 ~ 1.8 2 1.8 0.02 6
# Phase 1 : nuage de peste persistant sous un joueur toutes les 5 s
scoreboard players operation $m1 mg.st = $bc mg.st
scoreboard players operation $m1 mg.st %= $k100 mg.st
execute if score $m1 mg.st matches 0 at @r[tag=mg.play] run function mg:mobarena/lab/cloud_big
# Phase 2 à 50 % des PV : bouclier + quatre alambics à briser
execute if entity @e[tag=mg.boss,tag=!mg.ph2] if score $bh2 mg.st <= $bmax mg.st run function mg:mobarena/lab/phase2
execute at @e[type=minecraft:slime,tag=mg.alembic] run particle minecraft:sneeze ~ ~1.8 ~ 0.6 0.8 0.6 0 3
execute store result score $al mg.st if entity @e[type=minecraft:slime,tag=mg.alembic]
execute if entity @e[tag=mg.boss,tag=mg.shield] if score $al mg.st matches 0 run function mg:mobarena/lab/unshield
