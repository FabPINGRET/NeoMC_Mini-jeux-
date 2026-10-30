execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION, CAVE CLOSED
execute if block 10185 50 115 minecraft:lapis_block if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Flobbint","color":"#44BBFF"},{"text":"> The Oracle is in that sealed cave, pondering where the memories of the Froggadews went. The closer I am to the ","color":"white"},{"text":"Alabaster Pools","color":"blue"},{"text":", the worse my memory gets, so I decided to just come with her to this remote place.","color":"white"}]

#PRE MEMORY RESTORATION, CAVE OPEM
execute if block 10185 50 115 air if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Flobbint","color":"#44BBFF"},{"text":"> You know, the Oracle foretold that someone would come unseal that cave. I hope she sees the return of the memories of the Froggadews in the near future. The closer I am to the ","color":"white"},{"text":"Alabaster Pools","color":"blue"},{"text":", the worse my memory gets, so I decided to just come with her to this remote place.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Flobbint","color":"#44BBFF"},{"text":"> Is it safe to return to the ","color":"white"},{"text":"Alabaster Pools","color":"blue"},{"text":"?","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Flobbint","color":"#44BBFF"},{"text":"> Is it safe to return to the","color":"white"},{"text":" Alabaster Pools","color":"blue"},{"text":"? It is? That's great! I will soon. I just want to breathe in a bit more of this intoxicating silence.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
