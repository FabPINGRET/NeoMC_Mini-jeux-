execute at @n[tag=frostbyte_volley_pos,distance=0..] as @a[gamemode=!spectator,distance=..3,tag=mg.flw] run damage @s 16 minecraft:dragon_breath by @n[tag=boss_fs_name,distance=0..]
execute at @n[tag=frostbyte_volley_pos,distance=0..] run particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.5 0.5 0.5 0 50
execute at @n[tag=frostbyte_volley_pos,distance=0..] run particle explosion ~ ~ ~ 0.1 0.1 0.1 0 1
execute at @n[tag=frostbyte_volley_pos,distance=0..] run playsound minecraft:entity.generic.explode hostile @a[tag=mg.flw] ~ ~ ~ 2 1

execute as @n[tag=frostbyte_volley_pos,distance=0..] at @s positioned ^ ^ ^-1 run summon item ~ ~ ~ {Invulnerable:1b,Item:{id:"minecraft:lapis_lazuli",count:5,components:{"minecraft:custom_name":{"color":"aqua","text":"Blitzite"},"minecraft:lore":["A shard of","frozen lightning"]}}}


kill @e[tag=frostbyte_volley,distance=0..]
kill @e[tag=frostbyte_volley_pos,distance=0..]


scoreboard players set boss:fs_motor Value 2
function boss:8/target/rigid
function boss:8/position/random_position

setblock -10825 67 365 minecraft:redstone_block

#Stop Volley Tick
setblock -10828 67 372 minecraft:air
