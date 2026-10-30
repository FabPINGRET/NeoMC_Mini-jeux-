execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5

execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_blitzite_3,tag=mg.flw] [{"text":"<"},{"text":"Y10-1","color":"aqua"},{"text":"> I've got some ","color":"white"},{"text":"Blitzite","color":"aqua"},{"text":" for you! Thank you for your service to our people.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_blitzite_3,tag=mg.flw] [{"text":"<"},{"text":"Y10-1","color":"aqua"},{"text":"> I'm waiting for another shipment from the mines, come back tomorrow!","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]

execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_blitzite_3,tag=mg.flw] lapis_lazuli[custom_name={"color":"aqua","text":"Blitzite"},lore=["A shard of","frozen lightning"]] 16
execute at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_blitzite_3,tag=mg.flw] add vendor_blitzite_3

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
