execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.strider.happy neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block 329 78 1612 white_wool at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thribyx-Oth","color":"light_purple"},{"text":"> Some ","color":"white"},{"text":"weird guy","color":"yellow"},{"text":" gave this to the Mindczar. There is a very clever magic about it.","color":"white"}]

execute if block 329 78 1612 red_wool at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thribyx-Oth","color":"light_purple"},{"text":"> A group of ","color":"white"},{"text":"creepy weirdos","color":"dark_aqua"},{"text":" broke in and stole the orb from its display case! I overheard them saying they were taking it ","color":"white"},{"text":"back to their clubhouse","color":"dark_aqua"},{"text":". I didn't realize it was valuable enough for someone to want to steal it...","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
