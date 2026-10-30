# BOSSBAR MATH
scoreboard players set boss:attestor BossHealth 175
execute as @a[tag=in_trial_well_3,tag=mg.flw] run scoreboard players add boss:attestor BossHealth 50

scoreboard players operation boss:attestor_half BossHealth = boss:attestor BossHealth
scoreboard players operation boss:attestor_half BossHealth /= 2 Value
scoreboard players operation boss:attestor_quarter BossHealth = boss:attestor_half BossHealth
scoreboard players operation boss:attestor_quarter BossHealth /= 2 Value

scoreboard players operation boss:attestor_third BossHealth = boss:attestor BossHealth
scoreboard players operation boss:attestor_third BossHealth /= 3 Value
scoreboard players operation boss:attestor_two_thirds BossHealth = boss:attestor_third BossHealth
scoreboard players operation boss:attestor_two_thirds BossHealth *= 2 Value

execute store result bossbar boss:attestor max run scoreboard players get boss:attestor BossHealth
execute store result bossbar boss:attestor value run scoreboard players get boss:attestor BossHealth
bossbar set boss:attestor players @a[tag=mg.flw]

execute store result entity @n[tag=a_golem,distance=0..] attributes[{id:"minecraft:max_health"}].base double 1 run scoreboard players get boss:attestor BossHealth
execute store result entity @n[tag=a_golem,distance=0..] Health float 1 run scoreboard players get boss:attestor BossHealth
