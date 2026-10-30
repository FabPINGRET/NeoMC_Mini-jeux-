execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ant","color":"green"},{"text":"> You managed to get over here! Climb these roots to the base of the Blade Willow, there are usually swords growing under there.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
