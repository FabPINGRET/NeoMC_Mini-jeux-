# 🎄 Noël : un animal du thème à cet endroit (appelé par lobby/theme/spot)
summon minecraft:snow_golem ~ ~ ~ {Tags:["mg.thx","mg.thmob","mg.th_snowman"],PersistenceRequired:1b,Invulnerable:1b,DeathLootTable:"minecraft:empty",NoAI:1b,Pumpkin:0b}
execute as @e[type=minecraft:snow_golem,tag=mg.th_snowman,distance=..0.1] store result entity @s Rotation[0] float 1 run random value 0..359
