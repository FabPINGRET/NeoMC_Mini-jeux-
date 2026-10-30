execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"4Z-1","color":"aqua"},{"text":"> Have you met anyone who wants to ","color":"white"},{"text":"trade","color":"yellow"},{"text":" you for things? I've run a few simulations, and the most likely outcome of trading with all of them is receipt of an","color":"white"},{"text":" item ","color":"yellow"},{"text":"that can make your","color":"white"},{"text":" bow never run out of arrows","color":"green"},{"text":". Probability is quirky like that.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Forziwun","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Forziwun","color":"#825440"},{"text":"> Is it normal to feel gurgling in your tummy if you're alive...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
