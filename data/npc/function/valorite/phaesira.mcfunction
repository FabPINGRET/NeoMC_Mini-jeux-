execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if score Inventory Amulet matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phaesira","color":"#D47453"},{"text":"> Scary how monsters started appearing","color":"white"},{"text":" inside some buildings at night","color":"light_purple"},{"text":". Nothing feels safe now that the ","color":"white"},{"text":"Seven Lords","color":"gold"},{"text":" are gone. Especially our own ","color":"white"},{"text":"Lord of Flame","color":"red"},{"text":". We Valorites knew he always had our backs.","color":"white"}]

execute if score Inventory Amulet matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Phaesira","color":"#D47453"},{"text":"> Scary how monsters started appearing","color":"white"},{"text":" inside some buildings at night","color":"light_purple"},{"text":". Nothing feels safe now, even though the ","color":"white"},{"text":"Lord of Flame","color":"red"},{"text":" is back in charge. We Valorites know he always has our backs.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
