execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if block 150 45 -259 mangrove_roots at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mite-Mite","color":"green"},{"text":"> The Blade Willow is right through this tunnel, but the roots have grown too thick here, so you probably won't be able to squeeze through. I'm almost positive there's another way to reach it though, from one of the colony's","color":"white"},{"text":" four other entrances","color":"green"},{"text":"...","color":"white"}]
execute if block 150 45 -259 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mite-Mite","color":"green"},{"text":"> You got to the other side, good! I'll make sure those roots don't grow back again in the future, consider it a lesson learned.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
