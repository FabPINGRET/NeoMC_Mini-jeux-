execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Pleepy","color":"#44BBFF"},{"text":"> After losing our memories, we gathered in the temple of Womwort, god of forgetting. And lo and behold, his sanctum is sealed off! We need to get inside so we can make the proper sacrifices and ritual auto-spankings to please His Forgetfulship.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Pleepy","color":"#44BBFF"},{"text":"> We've let Womwort's sanctum be defiled by a monster! It's going to take soooo many auto-spankings to sate his wrath now.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Pleepy","color":"#44BBFF"},{"text":"> The entire time you were in Frogcrates's mind rescuing the","color":"white"},{"text":" Lord","color":"blue"},{"text":", I was in Womwort's sanctum performing the ninety thousand ritual auto-spankings he required of me.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
