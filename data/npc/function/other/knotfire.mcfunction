execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.attack neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> You have come to pay me tribute, good. I require you to bring all of your companions here first.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] run function npc:overworld_cutscene/knotfire/0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
