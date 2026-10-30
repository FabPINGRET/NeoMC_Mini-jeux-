execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.wither_skeleton.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Skqenic","color":"dark_aqua"},{"text":"> The Smoke Doctor's ","color":"white"},{"text":"tiny planets ","color":"green"},{"text":"were inspired by the Pebbos's magic circles. If you can use a magic circle, you should be able to enter a tiny planet in a similar way. Just look at it up close, and ","color":"white"},{"text":"sneak","color":"green"},{"text":".","color":"white"}]

scoreboard players set can_planet bool 1

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
