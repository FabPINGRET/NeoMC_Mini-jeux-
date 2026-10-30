execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gathion","color":"#D47453"},{"text":"> Don't mind the Master of Faces. He's just method acting, we're pretty sure.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
