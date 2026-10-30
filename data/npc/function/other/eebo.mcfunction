execute positioned -11544 199 -185 run playsound minecraft:entity.strider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute unless block -11538 187 -183 chest positioned -11544 199 -185 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Eebo","color":"gold"},{"text":"> He crawled out of my painting. He looked just like me! He said he was my brother... Oh, I cannot go in the ","color":"white"},{"text":"basement","color":"green"},{"text":" anymore. My brother, he haunts it...","color":"white"}]

execute if block -11538 187 -183 chest positioned -11544 199 -185 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Eebo","color":"gold"},{"text":"> Turns out Dark Eebo is a nice guy. He just needs some help.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
