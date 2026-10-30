execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Grinteldink","color":"#44BBFF"},{"text":"> What have we done to grieve Womwort so? I pray to whichever god I serve that they would give me a hint who they are!","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Grinteldink","color":"#44BBFF"},{"text":"> I should have known Womwort would never curse us like that. Thanks for taking care of that monster, I feel my memories returning and I suspect the other Froggadews are experiencing the same.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Grinteldink","color":"#44BBFF"},{"text":"> Oh, yes, this is delightful tea! My body is positively shivering with \"tea-spasms\" from the caffeine!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
