particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1
playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.8
execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..4] run function mg:kart/owner_hit_big
kill @s
