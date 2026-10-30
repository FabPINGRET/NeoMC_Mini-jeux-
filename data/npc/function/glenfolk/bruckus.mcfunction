execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_apple_0,tag=mg.flw] [{"text":"<"},{"text":"Bruckus","color":"aqua"},{"text":"> Here, I've been picking these from the trees around the castle. They come with my special no worm guarantee!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_apple_0,tag=mg.flw] [{"text":"<"},{"text":"Bruckus","color":"aqua"},{"text":"> Apples don't grow on trees that fast. I'll have more by tomorrow though!","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_apple_0,tag=mg.flw] apple 8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_apple_0,tag=mg.flw] add vendor_apple_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
