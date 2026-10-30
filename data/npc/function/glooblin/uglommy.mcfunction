execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score plodark bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Uglommy","color":"light_purple"},{"text":"> I lost my eye in an accident in the ","color":"white"},{"text":"Alabaster Pools","color":"blue"},{"text":". I would've died if it weren't for one of their gods, ","color":"white"},{"text":"Plodark","color":"blue"},{"text":", intervening to spare my life. If you ever make it to the Pools, please find ","color":"white"},{"text":"Plodark's altar","color":"blue"},{"text":" and ","color":"white"},{"text":"perform a ritual of worship","color":"green"},{"text":" there for me. And make sure to come tell me about it! That would make me a ","color":"white"},{"text":"supremely happy Glooblin","color":"red"},{"text":".","color":"white"}]

execute if score plodark bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Uglommy","color":"light_purple"},{"text":"> You actually did it? You worshipped ","color":"white"},{"text":"Plodark","color":"blue"},{"text":" at his altar? That's fantastic, I'm ","color":"white"},{"text":"so, so happy","color":"red"},{"text":" you got to experience the warmth of his divine grace! Let me buy you an IPA or something. Hm? Oh, it stands for Icky Puddle Ale.","color":"white"}]

execute if score plodark bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

execute if score plodark bool matches 1 run setblock 10383 26 -249 redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
