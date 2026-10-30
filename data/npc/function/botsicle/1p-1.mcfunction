execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.sniffer.eat neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score bot_lycan bool matches 0 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"1P-1","color":"aqua"},{"text":"> When we're low on energy, we recharge at","color":"white"},{"text":" Blitzite","color":"aqua"},{"text":" power stations we each have in our houses. The beds are just for guests, though we rarely have any.","color":"white"},{"text":" bzzrt...","color":"gray","italic":true}]

execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wunpiwun","color":"#825440"},{"text":"> Guhhh...","color":"white"}]
execute if score bot_lycan bool matches 1 at @n[tag=npc,distance=0..] positioned ~ ~1 ~ as @p[tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wunpiwun","color":"#825440"},{"text":"> I hate having fur at night...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
