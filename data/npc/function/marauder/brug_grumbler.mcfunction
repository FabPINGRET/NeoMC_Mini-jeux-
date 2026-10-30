execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brug Grumbler","color":"aqua"},{"text":"> I eated a hexbug nano and it’s in there buzzing so loud.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
