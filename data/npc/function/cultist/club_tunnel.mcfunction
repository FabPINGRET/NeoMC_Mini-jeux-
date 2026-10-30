execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tag @s add germ_club_caught

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> The ","color":"white"},{"text":"Mind Contagion","color":"dark_aqua"},{"text":", I feel his glory swimming through my brain like silver eels! What an incredible feeling...","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> REMOVE YOURSELF, INVADER!","color":"white"}]

execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> I hate knowing that","color":"white"},{"text":" thing","color":"dark_aqua"},{"text":" had control over my mind for so long. What does that say about the strength of my will compared to others? Improv comedy is a good escape as any.","color":"white"}]

execute if entity @a[tag=germ_club_caught,tag=mg.flw] run schedule function floaty:sched/main_quest/germ_club_caught 1s replace

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
