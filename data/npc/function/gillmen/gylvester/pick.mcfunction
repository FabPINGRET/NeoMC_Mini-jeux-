execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if block -12 93 74 purple_wool run function npc:gillmen/gylvester/key
execute if block -12 93 74 red_wool run function npc:gillmen/gylvester/love
execute if block -12 93 74 brown_wool run function npc:gillmen/gylvester/pattern
execute if block -12 93 74 light_blue_wool run function npc:gillmen/gylvester/bard
execute if block -12 93 74 black_wool run function npc:gillmen/gylvester/abnormazoid
execute if block -12 93 74 yellow_wool run function npc:gillmen/gylvester/library
