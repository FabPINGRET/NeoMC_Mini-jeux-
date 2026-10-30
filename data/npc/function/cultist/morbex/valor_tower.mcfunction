tag @a[tag=mg.flw] remove stealth_area
#Stops stealth section
setblock -9765 252 426 minecraft:redstone_block

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..8,tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> I will not deal with you until everyone is up here, close enough to hear me.","color":"white","bold":false}]

execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord Morbex","color":"dark_aqua","bold":true},{"text":"> You have the power of the ","color":"white","bold":false},{"text":"Bell of Life","color":"gold"},{"text":" emanating from you, I can smell it. That power drew us across many worlds.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned 10022 95 -98 run kill @n[tag=boss_marker,distance=..3]

#track player eyes
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run setblock 10017 91 -105 minecraft:redstone_block
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run stopsound @a[tag=mg.flw] record
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run scoreboard players set @a[tag=mg.flw] SoundtrackOverride 1
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run tag @a[tag=mg.flw] add no_warp
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run fill 10023 94 -97 10023 94 -98 air
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run setblock 10022 93 -86 minecraft:chiseled_deepslate
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run schedule function floaty:sched/npc/overworld_cutscene/valor_morbex/0 8s
execute positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] at @e[sort=nearest,limit=1,tag=npc,distance=0..] run function music:morbex


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
