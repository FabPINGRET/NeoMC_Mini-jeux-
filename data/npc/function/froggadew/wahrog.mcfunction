execute if score beat_wahrog bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if score beat_wahrog bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.lightning_bolt.thunder neutral @a[tag=mg.flw] ~ ~ ~ 1 1
#PRE MEMORY RESTORATION
execute if score beat_wahrog bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> It gnaws at me like a rat in the walls, the crackling, the crackling in the soft parts of the mind where the thoughts are sweetest and the brainmeat fattest. It will kill me, my head will burst like glass! Crackle-crackle, the last sound I will hear echoes through my skull even now.","color":"white"}]
execute if score beat_wahrog bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> ...","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
