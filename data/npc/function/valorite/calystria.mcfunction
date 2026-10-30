execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if block 9937 73 -69 minecraft:suspicious_sand at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Calystria","color":"#D47453"},{"text":"> Welcome to Brickworks Incorporated! Unfortunately, our ","color":"white"},{"text":"main pipe","color":"green"},{"text":" is clogged, so our assembly line is at a standstill. If someone could get up there and unclog it, we could make bricks again and I'd be ","color":"white"},{"text":"so, so happy","color":"red"},{"text":"!","color":"white"}]

execute unless block 9937 73 -69 minecraft:suspicious_sand at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Calystria","color":"#D47453"},{"text":"> You unclogged our ","color":"white"},{"text":"main pipe","color":"green"},{"text":", and our assembly line is working again! I'm ","color":"white"},{"text":"so, so happy","color":"red"},{"text":" Brickworks Incorporated is back in business. Time to make bricks and waste them! We're gonna waste all the bricks we make until we get a buyer. Until then, we're just gonna waste them, all the bricks are gonna get destroyed and thrown away and just totally, completely wasted.","color":"white"}]

execute unless block 9937 73 -69 minecraft:suspicious_sand run setblock 9936 54 -55 minecraft:redstone_block

execute unless block 9937 73 -69 minecraft:suspicious_sand at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
