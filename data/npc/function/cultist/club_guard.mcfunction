execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tag @s add germ_club_caught

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Were you there when ","color":"white"},{"text":"Lord Morbex","color":"dark_aqua"},{"text":" lost control of ","color":"white"},{"text":"Valor Tower","color":"red"},{"text":"? It was crazy, the ","color":"white"},{"text":"Floaty Isles' champion","color":"yellow"},{"text":" sneaked right past me in the basement tunnels and I didn't even know. I got demoted because of that.","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=germ_club_caught,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> REMOVE YOURSELF, INVADER!","color":"white"}]

execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> I hope","color":"white"},{"text":" Valorforge","color":"red"},{"text":" is still doing well. So many of us citizens fell into the ","color":"white"},{"text":"Contagion's","color":"dark_aqua"},{"text":" mental trap, myself included of course.","color":"white"}]

execute if entity @a[tag=germ_club_caught,tag=mg.flw] run schedule function floaty:sched/main_quest/germ_club_caught 1s replace

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
