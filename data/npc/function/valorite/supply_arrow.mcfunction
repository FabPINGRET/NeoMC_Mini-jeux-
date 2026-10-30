execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_arrow_4,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> If you've never used these before, it's pretty simple. Point and shoot. Make sure the safety on your bow is turned off first, of course.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_arrow_4,tag=mg.flw] [{"text":"<"},{"text":"Thalagos","color":"#D47453"},{"text":"> You've taken your fair share of arrows for the day.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_arrow_4,tag=mg.flw] arrow 16
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_arrow_4,tag=mg.flw] add vendor_arrow_4


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
