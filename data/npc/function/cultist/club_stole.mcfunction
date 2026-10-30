execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tag @s add germ_club_caught

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Some of us just returned from a mission to steal a strange","color":"white"},{"text":" orb ","color":"white"},{"text":"from the ","color":"white"},{"text":"Nightrobes","color":"light_purple"},{"text":". I don't ask why it's important, I don't need to know, but I believe the plan is to steal 3 remaining orbs from","color":"white"},{"text":" Floaty Isles","color":"yellow"},{"text":" leaders.","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> REMOVE YOURSELF, INVADER!","color":"white"}]

execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> I'm working on my jock character, how's this? \"Uh, hey man, what kind of weird sport ball are you playing over there? A book? Never played that one before! Can you dunk it?\"","color":"white"}]

execute if entity @a[tag=germ_club_caught,tag=mg.flw] run schedule function floaty:sched/main_quest/germ_club_caught 1s replace

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
