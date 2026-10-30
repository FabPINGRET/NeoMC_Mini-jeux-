execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.zoglin.angry neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ unless entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..9,gamemode=!spectator,tag=mg.flw] run function npc:overworld_cutscene/memory_contagion/0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[distance=9..,gamemode=!spectator,tag=mg.flw] run tellraw @a[distance=..9,tag=mg.flw] [{"text":"<"},{"text":"?","color":"green"},{"text":"> Everyone needs to gather around close...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

##execute at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ unless entity @a[distance=7..,gamemode=!spectator] if entity @a[distance=..7,gamemode=!spectator] run setblock -11545 124 544 minecraft:redstone_block
##execute at @e[sort=nearest,limit=1,tag=npc] positioned ~ ~1 ~ if entity @a[distance=7..,gamemode=!spectator] run tellraw @a[distance=..7] {"text":"Gather everyone close first...","color":"aqua"}
