execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_apple_1,tag=mg.flw] [{"text":"<"},{"text":"Mrs. Ladybug","color":"green"},{"text":"> Hi sweetie, have some apples! They're on the house, consider them a thank you for cleansing our shrine a few years ago. Stop by tomorrow, I'd love to give you more when I have them!","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_apple_1,tag=mg.flw] [{"text":"<"},{"text":"Mrs. Ladybug","color":"green"},{"text":"> I'm all out of apples for now sweetie, but please come back tomorrow! Thanks for being a lovely example of courage to our children.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_apple_1,tag=mg.flw] apple 10
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_apple_1,tag=mg.flw] add vendor_apple_1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
