# Œil du faucon
playsound minecraft:entity.parrot.imitate.phantom player @a ~ ~ ~ 1 1.5
effect give @s minecraft:speed 10 1
execute as @e[tag=mg.olm,distance=..30] run function mg:ombre/cl/mark
function mg:ombre/cl/end
