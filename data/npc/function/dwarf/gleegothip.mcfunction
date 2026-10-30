execute positioned -267 41 -52 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -267 41 -52 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gleegothip","color":"dark_aqua"},{"text":"> Heard Grudgrumlin say he was hearing weird humming noises comin' from the ","color":"white"},{"text":"closet","color":"dark_aqua"},{"text":" in his apartment. Wonder if someone is hidin' in there. Creepy!","color":"white"}]

setblock -9762 80 418 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
