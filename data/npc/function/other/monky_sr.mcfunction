execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.fox.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Monky Sr.","color":"dark_green"},{"text":"> AHH OOOH OOOH!! (Welcome to Monkey Manor! We're all one big monkey family in the end. Stay here as long as you need, we're safe inside our tree.)","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
