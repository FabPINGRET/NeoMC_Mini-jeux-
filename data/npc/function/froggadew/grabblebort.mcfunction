execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

execute if block 10654 71 48 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grabblebort","color":"#44BBFF"},{"text":"> I heard a song once, in the farthest northeastern parts of ","color":"white"},{"text":"Moldsap","color":"light_purple"},{"text":". It was the most beautiful song I'd ever heard, but now I cannot remember the tune nor find the source of the song. If only I could hear it once again, I'd be ","color":"white"},{"text":"super, super happy","color":"red"},{"text":".","color":"white"}]

execute unless block 10654 71 48 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grabblebort","color":"#44BBFF"},{"text":"> That song, you found it! What a beautiful thing! My heart is so moved by it, I cannot explain why it smites me so. I'm an ","color":"white"},{"text":"utterly, utterly happy","color":"red"},{"text":" Froggadew.","color":"white"}]

execute unless block 10654 71 48 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
