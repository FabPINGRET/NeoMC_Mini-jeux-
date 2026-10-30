execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.attack neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Knotfire","color":"green"},{"text":"> I am Knotfire, eternal spirit of ","color":"white"},{"text":"control","color":"green"},{"text":". If you would pay me tribute, climb the ","color":"white"},{"text":"great ascent ","color":"green"},{"text":"and find me in my chambers. I will await your supplication, small one.","color":"white"}]

setblock -33 -21 1608 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
