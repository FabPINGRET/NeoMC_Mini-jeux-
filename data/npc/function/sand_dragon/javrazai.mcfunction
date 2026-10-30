execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute if block 116 35 159 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Javrazai","color":"gold"},{"text":"> Welcome to my archery course! It's lonely at the top; I haven't met anyone who's been able to match my skill with a bow. I see you have one though, so you're welcome to try and beat my score! If you can demonstrate your skill and get ","color":"white"},{"text":"40 points in 1 minute","color":"green"},{"text":", I'll let you be my best friend, and I'll be","color":"white"},{"text":" so, so happy","color":"red"},{"text":"!","color":"white"}]
execute if block 116 35 159 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Javrazai","color":"gold"},{"text":"> Welcome to my archery course, bestie! I'm","color":"white"},{"text":" so happy","color":"red"},{"text":" you're here, feel free to play my archery course again anytime you want!","color":"white"}]

execute if block 116 35 159 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
