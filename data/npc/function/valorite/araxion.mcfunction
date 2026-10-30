execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Araxion","color":"#D47453"},{"text":"> A little man just dug through the wall with frightening speed. All he said to me was \"hello, you've got a beautiful light-up hat, I don't have no parents,\" or something to that effect, before zipping away down that hole and into the tunnels beneath ","color":"white"},{"text":"Valor Tower","color":"red"},{"text":".","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
