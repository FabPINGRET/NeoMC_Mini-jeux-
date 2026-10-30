execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"B11-8","color":"aqua"},{"text":"> The road behind my house leads to the ","color":"white"},{"text":"Isle of Smoke","color":"yellow"},{"text":". The air there is toxic to breathe, which isn't a problem for us","color":"white"},{"text":" Botsicles","color":"aqua"},{"text":" but most living beings will quickly perish from it. I strongly advise not going.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Beewunwunate","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Beewunwunate","color":"#825440"},{"text":"> Ohh, I'm gonna throw up. I've never done that before...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value
