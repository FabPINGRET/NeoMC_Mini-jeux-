execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_bread_3,tag=mg.flw] [{"text":"<"},{"text":"Xerandros","color":"#D47453"},{"text":"> Here's some fresh-steamed bread! It's a Valorforge street food classic that you can't afford to miss!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_bread_3,tag=mg.flw] [{"text":"<"},{"text":"Xerandros","color":"#D47453"},{"text":"> I ALREADY GAVE YOU BREAD TODAY, GUY! Geez louise, some people...","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_bread_3,tag=mg.flw] bread 6
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_bread_3,tag=mg.flw] add vendor_bread_3


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
