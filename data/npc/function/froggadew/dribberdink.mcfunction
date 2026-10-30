execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dribberdink","color":"#44BBFF"},{"text":"> I think the memory loss is a targeted curse. The priests and Frogcrates are getting hit the hardest, but don't get me wrong, I'm being affected too. For example, I can't remember what \"hat\" means.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dribberdink","color":"#44BBFF"},{"text":"> I remembered what \"hat\" means! It means like, y'know, like for your head? Like on top of it? Nevermind, I can see I'm not impressing you.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dribberdink","color":"#44BBFF"},{"text":"> I remembered what \"hat\" means! It means like, y'know, like for your head? Like on top of it? Nevermind, I can see I'm not impressing you.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
