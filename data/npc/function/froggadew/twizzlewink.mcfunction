execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twizzlewink the Oracle","color":"#44BBFF"},{"text":"> You're right on time! I've been expecting you, hero, so I've prepared a ","color":"white"},{"text":"magic charm","color":"aqua"},{"text":" that will give you the Froggadew power to ","color":"white"},{"text":"enter other Froggadew's minds","color":"aqua"},{"text":". I have a ","color":"white"},{"text":"special thought","color":"light_purple"},{"text":" in my mind just for you, see if you can use the charm to see what it is!","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twizzlewink the Oracle","color":"#44BBFF"},{"text":"> You defeated the ","color":"white"},{"text":"Memory Contagion","color":"green"},{"text":", just as I foretold! I must warn you, whether you free the ","color":"white"},{"text":"Lord of Water ","color":"blue"},{"text":"or not is yet is not clear to me.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Twizzlewink the Oracle","color":"#44BBFF"},{"text":"> You freed the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":", good! The future is hazy from this point forward, I do not know what will happen.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
