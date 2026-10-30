execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score moonlight_contagion bool matches 0 if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"6R-1","color":"aqua"},{"text":"> Can you understand us at night? We try to talk, but it just comes out as a gutteral moan. Like we're speaking another ","color":"white"},{"text":"language ","color":"green"},{"text":"or something...","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score moonlight_contagion bool matches 1 if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"6R-1","color":"aqua"},{"text":"> Lightning bolts freeze solid here because of how cold it is, but you seem totally fine. That's weird, I can't really compute a good explanation for that fact.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]

execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Sixarwun","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Sixarwun","color":"#825440"},{"text":"> At least this squishy body doesn't rust...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
