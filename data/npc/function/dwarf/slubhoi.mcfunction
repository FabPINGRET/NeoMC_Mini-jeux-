execute positioned -253 44 -72 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -253 44 -72 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slubhoi","color":"dark_aqua"},{"text":"> Hot springs are one of those things you never realized you needed until you dipped your little toesies into one.","color":"white"}]

setblock -9762 80 420 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
