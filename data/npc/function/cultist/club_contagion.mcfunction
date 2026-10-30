execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tag @s add germ_club_caught

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> The plan for conquering the","color":"white"},{"text":" Bell of Life","color":"gold"},{"text":" is almost at a close. Once it is completed, there will be nothing standing in our way! Aren't you excited?","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> REMOVE YOURSELF, INVADER!","color":"white"}]

execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> The","color":"white"},{"text":" Mind Contagion","color":"dark_aqua"},{"text":" is gone! He is completely out of our heads! I talked it over with some of the other","color":"white"},{"text":" Ex-Germ Eaters ","color":"#D47453"},{"text":"and we think we're going to form an improv comedy troupe now that we're free. The Germ Eater cult is no more.","color":"white"}]

execute if entity @a[tag=germ_club_caught,tag=mg.flw] run schedule function floaty:sched/main_quest/germ_club_caught 1s replace

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
