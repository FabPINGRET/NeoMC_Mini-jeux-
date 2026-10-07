particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1
playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.9
execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..4.5] run function mg:kart/owner_hit
kill @s
