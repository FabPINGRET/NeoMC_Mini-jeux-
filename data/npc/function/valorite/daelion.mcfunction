execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Daelion","color":"#D47453"},{"text":"> Ever since our ","color":"white"},{"text":"Seven Lords","color":"gold"},{"text":" were overthrown by the","color":"white"},{"text":" World Virus","color":"dark_aqua"},{"text":" and that horrible ","color":"white"},{"text":"Morbex","color":"dark_aqua"},{"text":" started ruling from ","color":"white"},{"text":"Valor Tower","color":"gold"},{"text":", our city has been in decline. Without the ","color":"white"},{"text":"Seven Lords","color":"gold"},{"text":"... we're powerless.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
