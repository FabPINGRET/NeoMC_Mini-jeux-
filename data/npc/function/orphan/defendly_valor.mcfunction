execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Defendly","color":"aqua"},{"text":"> Ho there, hero. Oi'm afraid this is as far as Oi can dig wifout alerting those guards. It's gotta be up to yew to sneak past 'em all sneaky-loik. Good luck.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
