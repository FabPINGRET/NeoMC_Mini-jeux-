particle minecraft:explosion_emitter -11144 58 430 0 0 0 0 1
particle minecraft:reverse_portal -11144 58 430 0 0 0 1 50
execute positioned -11144 58 430 as @a[distance=..4,tag=mg.flw] run damage @s 30 minecraft:dragon_breath
playsound minecraft:entity.dragon_fireball.explode hostile @a[tag=mg.flw] -11144 58 430 4 0.5
