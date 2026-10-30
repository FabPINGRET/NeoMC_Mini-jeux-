execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score BetterEconomy bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dorsa","color":"yellow"},{"text":"> Sorry, salmon is just too expensive to source these days. I wish I had some for you, but I don't.","color":"white"}]

execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_salmon_0,tag=mg.flw] [{"text":"<"},{"text":"Dorsa","color":"yellow"},{"text":"> Fresh, buttery salmon for you! Don't give me that look, it's not like I'm selling Gillmen meat. These are fish, they're completely different.","color":"white"}]
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_salmon_0,tag=mg.flw] [{"text":"<"},{"text":"Dorsa","color":"yellow"},{"text":"> I'll need to catch more to restock, come back tomorrow!","color":"white"}]

execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_salmon_0,tag=mg.flw] cooked_salmon 8
execute if score BetterEconomy bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_salmon_0,tag=mg.flw] add vendor_salmon_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
