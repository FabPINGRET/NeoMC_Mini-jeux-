execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_blitzite_1,tag=mg.flw] [{"text":"<"},{"text":"U1-3","color":"aqua"},{"text":"> I'm already past my ","color":"white"},{"text":"Blitzite","color":"aqua"},{"text":" quota for today! Here, take some.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_blitzite_1,tag=mg.flw] [{"text":"<"},{"text":"U1-3","color":"aqua"},{"text":"> I'm going to try to get ahead of tomorrow's quota, so I can't give you any more right now.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_blitzite_1,tag=mg.flw] lapis_lazuli[custom_name={"color":"aqua","text":"Blitzite"},lore=["A shard of","frozen lightning"]] 16
execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_blitzite_1,tag=mg.flw] add vendor_blitzite_1

execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yuwunthri","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yuwunthri","color":"#825440"},{"text":"> I feel like a freak...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
