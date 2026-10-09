# @s : caisse d'un véhicule détruit (son cheval ou son ghast est mort) : explosion
function mg:bomber/boom/r2
execute as @e[tag=mg.gtg,distance=..3.5] run damage @s 8 minecraft:explosion
particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force
particle minecraft:flame ~ ~1 ~ 1.2 0.8 1.2 0.1 50 force
particle minecraft:large_smoke ~ ~1.5 ~ 1 1 1 0.05 40 force
particle minecraft:lava ~ ~1 ~ 1 0.5 1 0 15 force
playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.7
