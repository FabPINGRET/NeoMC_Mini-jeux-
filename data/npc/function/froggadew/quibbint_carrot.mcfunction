execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_golden_carrot_1,tag=mg.flw] [{"text":"<"},{"text":"Quibbint","color":"#44BBFF"},{"text":"> What's better than a carrot? A carrot made of inert metal you get to put inside your body!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_golden_carrot_1,tag=mg.flw] [{"text":"<"},{"text":"Quibbint","color":"#44BBFF"},{"text":"> I need to make more carrots become golded before I can give you more.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_golden_carrot_1,tag=mg.flw] golden_carrot 10
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_golden_carrot_1,tag=mg.flw] add vendor_golden_carrot_1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
