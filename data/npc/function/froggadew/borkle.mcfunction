execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Borkle","color":"#44BBFF"},{"text":"> Whoa, you're not a Froggadew! We don't get many non-Froggadews here. Or do we? I don't remember...","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Borkle","color":"#44BBFF"},{"text":"> It's usually pretty difficult for non-Froggadews to get to the ","color":"white"},{"text":"Pools","color":"blue"},{"text":". Most people can't jump that high!","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Borkle","color":"#44BBFF"},{"text":"> It's usually pretty difficult for non-Froggadews to get to the","color":"white"},{"text":" Pools","color":"blue"},{"text":". Most people can't jump that high!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
