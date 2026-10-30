execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION, PRE PUZZLE
execute if block 10670 78 -74 minecraft:lapis_block if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Meekwy","color":"#44BBFF"},{"text":"> We high priests agree that if we see the whole picture of who we each serve, it might jog our memory enough to let other important details through. We set up this wall to try visualize it, but so far we haven't made much progress.","color":"white"}]

#PRE MEMORY RESTORATION, POST PUZZLE
execute if block 10670 78 -74 minecraft:air if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Meekwy","color":"#44BBFF"},{"text":"> Who is that in Womwort's sanctum?","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Meekwy","color":"#44BBFF"},{"text":"> I... I can remember again! Oh no, how long has it been? How long since ","color":"white"},{"text":"Frogcrates","color":"aqua"},{"text":" hid the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":"?","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Meekwy","color":"#44BBFF"},{"text":"> The high priests are celebrating in my mind right now if you want to drop in and say hi. In the meantime, as an offering of thanks to Womwort, I will sacrifice one memory to him. I don't remember how often I do this.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
