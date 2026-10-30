execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_blitzite_0,tag=mg.flw] [{"text":"<"},{"text":"3L-3","color":"aqua"},{"text":"> Let me give you some freshly mined ","color":"white"},{"text":"Blitzite","color":"aqua"},{"text":"! This amount is enough to keep your batteries charged for weeks.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_blitzite_0,tag=mg.flw] [{"text":"<"},{"text":"3L-3","color":"aqua"},{"text":"> I already gave you ","color":"white"},{"text":"Blitzite","color":"aqua"},{"text":" today! Come back another day when I've had time to mine for more.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_blitzite_0,tag=mg.flw] lapis_lazuli[custom_name={"color":"aqua","text":"Blitzite"},lore=["A shard of","frozen lightning"]] 16
execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_blitzite_0,tag=mg.flw] add vendor_blitzite_0

execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thrielthree","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thrielthree","color":"#825440"},{"text":"> This body doesn't have any servos... How am I supposed to move without any servos...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
