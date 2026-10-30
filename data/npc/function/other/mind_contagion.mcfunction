execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] if entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] positioned ~ ~1 ~ run tellraw @a[distance=..8,tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua","bold":true},{"text":"> Pathetic invader, I will not deal with you until everyone is here.","color":"white","bold":false}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] if entity @a[distance=..8,gamemode=!spectator,tag=mg.flw] unless entity @a[distance=8..,gamemode=!spectator,tag=mg.flw] run function npc:overworld_cutscene/mind_contagion/0

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
