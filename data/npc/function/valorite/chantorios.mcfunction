execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Chantorios","color":"#D47453"},{"text":"> Start a race anytime you want! If you haven't learned it already, the house always wins...","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
