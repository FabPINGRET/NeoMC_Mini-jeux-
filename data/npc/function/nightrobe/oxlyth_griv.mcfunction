scoreboard players set whisper_quest_2 bool 0

execute if score whisper_5 bool matches 2 if score whisper_6 bool matches 2 if score whisper_7 bool matches 2 run scoreboard players set whisper_quest_2 bool 1

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score whisper_quest_2 bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Oxlyth-Griv","color":"light_purple"},{"text":"> There's spacial magic happening on this isle, I can sense it! Annoyingly, I can also sense ","color":"white"},{"text":"three pesky Whispers","color":"light_purple"},{"text":" hiding somewhere in the ","color":"white"},{"text":"Dark Isles","color":"light_purple"},{"text":", disturbing the hyper-dimensional peace. If you can ","color":"white"},{"text":"find and kill all three","color":"light_purple"},{"text":", I'll give you a ","color":"white"},{"text":"unique plant","color":"green"},{"text":" I found here. I suspect the Whispers are all in parts of these Isles you've already visited...","color":"white"}]

execute if score whisper_quest_2 bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Oxlyth-Griv","color":"light_purple"},{"text":"> You've done it! The Whisper-stench is no more. I can now study this isle's secrets in peace. Thank you, hero. Here's the ","color":"white"},{"text":"plant ","color":"green"},{"text":"I promised you!","color":"white"}]
execute if score whisper_quest_2 bool matches 1 run setblock 10182 35 240 redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

