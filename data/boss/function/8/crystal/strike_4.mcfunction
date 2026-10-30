execute positioned ~ 89 ~ as @a[gamemode=!spectator,distance=..4,tag=mg.flw] run damage @s 22 minecraft:dragon_breath by @n[tag=boss_fs_name,distance=0..]

summon lightning_bolt ~ 89 ~

particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ 89.5 ~ 1.5 0.3 1.5 0 75 force
particle explosion ~ 89.5 ~ 1.5 0.3 1.5 0 5 force
playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ 89 ~ 1 1.8

execute as @a[gamemode=!spectator,tag=mg.flw] run summon item ~ 89 ~ {Invulnerable:1b,Item:{id:"minecraft:lapis_lazuli",count:1,components:{"minecraft:custom_name":{"color":"aqua","text":"Blitzite"},"minecraft:lore":["A shard of","frozen lightning"]}}}

kill @e[tag=frostbyte_crystal,tag=4,distance=0..]
