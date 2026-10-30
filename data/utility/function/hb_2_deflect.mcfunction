execute if score @s HBWard matches 10 run playsound minecraft:block.honey_block.break player @a[tag=mg.flw] ~ ~ ~ 1 0.1
particle minecraft:sweep_attack ~ ~1 ~ 3 3 3 0 10
particle minecraft:cherry_leaves ~ ~1 ~ 3 3 3 0 10

execute as @e[type=#minecraft:hb_projectiles,distance=..5,scores={HBDeflectCD=0}] unless entity @s[type=minecraft:arrow,nbt={inGround:1b}] unless entity @s[type=minecraft:spectral_arrow,nbt={inGround:1b}] unless entity @s[type=minecraft:trident,nbt={inGround:1b}] on origin if entity @s[type=!minecraft:player] run effect give @s minecraft:slowness 1 100 true

execute as @e[type=#minecraft:hb_projectiles,distance=..5,scores={HBDeflectCD=0}] unless entity @s[type=minecraft:arrow,nbt={inGround:1b}] unless entity @s[type=minecraft:spectral_arrow,nbt={inGround:1b}] unless entity @s[type=minecraft:trident,nbt={inGround:1b}] at @s run function utility:hb_2_flip_motion
