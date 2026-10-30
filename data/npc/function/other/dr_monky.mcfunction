execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.fox.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dr. Monky","color":"dark_green"},{"text":"> OOH OOH AHHHH EEEH AHHH! (If you've never lived in a tree, it's a lot of fun! Except for the days when you wake up covered in sap and bugs.)","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
