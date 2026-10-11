execute if entity @e[type=minecraft:husk,tag=mg.evm,limit=6] run return 0
summon minecraft:husk ~1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}
summon minecraft:husk ~-1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}
playsound minecraft:entity.zombie.ambient hostile @a ~ ~ ~ 2 0.5
particle minecraft:large_smoke ~ ~2 ~ 1 1 1 0.05 30
