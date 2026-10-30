execute if score mr_nippy bool matches 0 run scoreboard players set mr_nippy bool 1
execute if block 9780 51 34 minecraft:redstone_block if block 9781 51 25 minecraft:redstone_block if block 9783 51 25 minecraft:redstone_block if block 9785 51 25 minecraft:redstone_block run scoreboard players set mr_nippy bool 2


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.snow_golem.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score mr_nippy bool matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mr. Nippy","color":"aqua"},{"text":"> You know what's worse than being inanimate? Not having any friends! I started this club as a place where inanimate people could meet and gather, but I haven't been able to spread the word. If ","color":"white"},{"text":"four","color":"red"},{"text":" other inanimate friends showed up, I'd be a ","color":"white"},{"text":"very, very happy snowman","color":"red"},{"text":"! Maybe a ","color":"white"},{"text":"scarecrow","color":"gold"},{"text":" somewhere would want to join! Or a ","color":"white"},{"text":"garden gnome","color":"red"},{"text":", or a ","color":"white"},{"text":"wax model","color":"green"},{"text":", or a ","color":"white"},{"text":"training dummy","color":"aqua"},{"text":"!","color":"white"}]

execute if score mr_nippy bool matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mr. Nippy","color":"aqua"},{"text":"> Wow, for the first time in my life, I'm surrounded by friends! Inanimate fellas who understand the struggle! Thank you, I'm a ","color":"white"},{"text":"very, very happy snowman","color":"red"},{"text":" now. We're going to organize and lobby for Object Rights together soon. Down with the living! Haha just yanking your chain, you're one of the good ones.","color":"white"}]

execute if score mr_nippy bool matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force
execute if score mr_nippy bool matches 2 run setblock 9785 51 31 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
