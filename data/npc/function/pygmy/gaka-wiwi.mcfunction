execute if score @n[tag=sync_snake,tag=1,distance=0..] Value = @n[tag=sync_snake,tag=2,distance=0..] Value if score @n[tag=sync_snake,tag=2,distance=0..] Value = @n[tag=sync_snake,tag=3,distance=0..] Value if score @n[tag=sync_snake,tag=3,distance=0..] Value = @n[tag=sync_snake,tag=4,distance=0..] Value if score @n[tag=sync_snake,tag=4,distance=0..] Value = @n[tag=sync_snake,tag=5,distance=0..] Value if score @n[tag=sync_snake,tag=5,distance=0..] Value = @n[tag=sync_snake,tag=6,distance=0..] Value if score @n[tag=sync_snake,tag=6,distance=0..] Value = @n[tag=sync_snake,tag=7,distance=0..] Value run setblock 10423 40 199 redstone_block

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.axolotl.idle_air neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute unless block 10423 40 199 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gaka-Wiwi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"I'm trying to train these snakes to ","color":"white","italic":false},{"text":"dance in sync","color":"green","italic":false},{"text":" with one another, but they're being so frustrating! If only they would all move and sway in unison, I would be a ","color":"white","italic":false},{"text":"very happy Pygmy","color":"red","italic":false},{"text":"...","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]

execute if block 10423 40 199 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gaka-Wiwi","color":"#C29D62"},{"text":"> ","color":"white"},{"text":"*nuk-tuk* ","color":"gray","italic":true},{"text":"No way! They're dancing together! How did you convince them so quickly? Well, however you did it, you've made me a ","color":"white","italic":false},{"text":"very happy Pygmy","color":"red","italic":false},{"text":" today.","color":"white","italic":false},{"text":" *tuk-nuk* ","color":"gray","italic":true}]


execute if block 10423 40 199 redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.2 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:pygmy/pose/repose

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
