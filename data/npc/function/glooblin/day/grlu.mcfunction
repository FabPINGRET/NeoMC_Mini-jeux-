execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grlu","color":"light_purple"},{"text":"> When I was a child, my friends and I would explore","color":"white"},{"text":" Sticky Hollow ","color":"light_purple"},{"text":"to try and find the ","color":"white"},{"text":"magic spell ","color":"light_purple"},{"text":"rumored to be hidden within its depths. Now, the ","color":"white"},{"text":"Lord of Spores","color":"light_purple"},{"text":" is trapped there by a monster.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
