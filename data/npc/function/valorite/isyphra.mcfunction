execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Isyphra","color":"#D47453"},{"text":"> For centuries, this tower was a symbol of peace and harmony in the Isles. Now, until the ","color":"white"},{"text":"World Virus","color":"dark_aqua"},{"text":" is driven away forever, as long as even one Lord stands free, this tower is a symbol of courage and hope.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
