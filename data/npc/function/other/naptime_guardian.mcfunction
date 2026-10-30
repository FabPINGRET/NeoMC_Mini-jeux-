execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..8,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Naptime Guardian","color":"gold"},{"text":"> ...","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..8,gamemode=!spectator,tag=mg.flw] run setblock -11560 189 -326 minecraft:redstone_block
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..8,gamemode=!spectator,tag=mg.flw] positioned -11546 205 -336 run kill @n[tag=boss_marker,distance=..3]


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Naptime Guardian","color":"gold"},{"text":"> ...\n","color":"white"},{"text":"It seems to be waiting for everyone to be here first...","color":"gray","italic":true}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
