execute store result score $ec mg.st if entity @e[type=minecraft:enderman,tag=mg.mob]
execute if score $ec mg.st matches 6.. run return 0
execute at @r[tag=mg.play] run summon minecraft:enderman ~3 ~ ~ {Tags:["mg.mob","mg.agro"],PersistenceRequired:1b,AngerTime:2400}
execute at @r[tag=mg.play] run summon minecraft:enderman ~-3 ~ ~ {Tags:["mg.mob","mg.agro"],PersistenceRequired:1b,AngerTime:2400}
function mg:mobarena/ship/anger
tag @e[tag=mg.agro] remove mg.agro
