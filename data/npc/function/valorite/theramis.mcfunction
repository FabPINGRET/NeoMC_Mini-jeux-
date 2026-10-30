execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute unless block 9942 58 -174 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Theramis","color":"#D47453"},{"text":"> Welcome to the Dark Isles Great Museum! Our collection includes fascinating exhibits from many regions in the ","color":"white"},{"text":"Dark Isles","color":"dark_purple"},{"text":", both near and far. Please take your time and enjoy our exhibition!","color":"white"}]
execute if block 9942 58 -174 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Theramis","color":"#D47453"},{"text":"> Welcome to the Dark Isles Great Museum! Our collection includes fascinating exhibits from many regions in the ","color":"white"},{"text":"Dark Isles","color":"dark_purple"},{"text":", both near and far. One of our wax models is missing though, sorry for the inconvenience.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
