execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[distance=..10,gamemode=!spectator,tag=mg.flw] unless items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> This clubhouse is for ","color":"white"},{"text":"Germ Eaters only","color":"dark_aqua"},{"text":"! You're obviously not one, so scram!","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[distance=..10,gamemode=!spectator,tag=mg.flw] if items entity @s armor.head minecraft:player_head[minecraft:custom_name] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Come right in, ","color":"white"},{"text":"Germ Eater","color":"dark_aqua"},{"text":". Were you stationed at the obelisk?","color":"white"}]
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @p[distance=..10,gamemode=!spectator,tag=mg.flw] if items entity @s armor.head minecraft:player_head[minecraft:custom_name] run setblock 10105 56 -178 minecraft:redstone_torch


execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> The worst thing an improv comedian can say is \"no,\" so come right in! Oh, to be clear, I mean like just in the context of improv. I was trying to do like, a friendly quip, but it came across wrong. It's important to say \"no\" to things sometimes obviously. Obviously.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
