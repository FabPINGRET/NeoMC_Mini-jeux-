execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tag @s add germ_club_caught

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=!vendor_pumpkin_pie_1,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Every good clubhouse needs an in-house pastry chef, and by the power of the","color":"white"},{"text":" Mind Contagion","color":"dark_aqua"},{"text":", that's what I am compelled to be! Take these pies I made, I live to serve.","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=vendor_pumpkin_pie_1,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> I live to serve the","color":"white"},{"text":" Contagion","color":"dark_aqua"},{"text":", I live to serve the collective. I must bake more pies!","color":"white"}]

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> REMOVE YOURSELF, INVADER!","color":"white"}]

execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_pumpkin_pie_1,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> During my time as a brainwashed cultist, I got a lot of practice making pies. Pies have a lot of comedy potential, thankfully. Have some!","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_pumpkin_pie_1,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> More pies are in the oven. I wonder if any of my fellow performers would let me throw one at them during our act.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!germ_club_caught,tag=!vendor_pumpkin_pie_1,tag=mg.flw] pumpkin_pie 16
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!germ_club_caught,tag=!vendor_pumpkin_pie_1,tag=mg.flw] add vendor_pumpkin_pie_1

execute if entity @a[tag=germ_club_caught,tag=mg.flw] run schedule function floaty:sched/main_quest/germ_club_caught 1s replace

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
