# Cri de guerre
playsound minecraft:event.raid.horn player @a ~ ~ ~ 1 1.3
particle minecraft:angry_villager ~ ~2 ~ 1.5 0.5 1.5 0 15
effect give @a[tag=mg.olw,distance=..8] minecraft:strength 8 0
effect give @a[tag=mg.olw,distance=..8] minecraft:resistance 8 0
execute as @e[tag=mg.olm,distance=..10] run damage @s 0.01 minecraft:generic by @a[tag=mg.olcast,limit=1]
function mg:ombre/cl/end
