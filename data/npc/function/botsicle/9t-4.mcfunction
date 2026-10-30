execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"9T-4","color":"aqua"},{"text":"> The","color":"white"},{"text":" Windbite Tundra","color":"aqua"},{"text":" is a cold place! Cold enough that even the lightning bolts freeze solid. If you dig underground, you can find ancient frozen lightning that's been compressed over millions of years. We mine it for ","color":"white"},{"text":"Blitzite","color":"aqua"},{"text":" crystals!","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ninetifor","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ninetifor","color":"#825440"},{"text":"> I'm a monster...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
