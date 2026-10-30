execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_arrow_1,tag=mg.flw] [{"text":"<"},{"text":"Flii","color":"green"},{"text":"> Last time you came to these woods some years back, you shot a ton of arrows everywhere. I'm still finding them here and there, but yeah, these belong to you.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_arrow_1,tag=mg.flw] [{"text":"<"},{"text":"Flii","color":"green"},{"text":"> I'm sure I'll find more by tomorrow, the amount of stray arrows stuck under leaves and into trees is absurd. Who were you even shooting at?","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_arrow_1,tag=mg.flw] arrow 8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_arrow_1,tag=mg.flw] add vendor_arrow_1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
