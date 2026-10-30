execute at @e[sort=nearest,limit=2,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"One-Eyed Emerson","color":"aqua"},{"text":"> Hey man, when was the last time you checked yourself for lumps?","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Awug Grumbler","color":"aqua"},{"text":"> Gosh bro, it's been a long time, let me go do that, thanks bro you maybe just saved my life.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"One-Eyed Emerson","color":"aqua"},{"text":"> No problem man, I love you bro. Hero, you should check yourself for lumps too.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
