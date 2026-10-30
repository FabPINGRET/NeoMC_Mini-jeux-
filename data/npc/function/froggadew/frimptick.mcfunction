execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frimptick","color":"#44BBFF"},{"text":"> I think I went to the Temple Cavern to pray recently? Maybe? Hmmm...","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frimptick","color":"#44BBFF"},{"text":"> The Temple Cavern is a cool feature of our Isle, but I prefer it up here with the fountains and the sky and all that good stuff.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Frimptick","color":"#44BBFF"},{"text":"> The Temple Cavern is a cool feature of our Isle, but I prefer it up here with the fountains and the sky and all that good stuff.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
