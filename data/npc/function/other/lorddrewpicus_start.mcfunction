execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Drewpy","color":"red"},{"text":"> Yep, that's how you talk to people! If you ever need to show or give an NPC something, talk to them with that item in your","color":"white"},{"text":" main hand","color":"gold"},{"text":". Also, when you see this symbol: \"","color":"white"},{"text":"⇒","color":"light_purple"},{"text":"\" it means the speaker isn't finished talking and will have more to say shortly. I hope you enjoy my adventure!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
