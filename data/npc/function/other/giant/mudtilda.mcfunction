execute positioned 10356 40 -200 run playsound minecraft:entity.witch.celebrate neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned 10356 40 -200 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mudtilda","color":"gold"},{"text":"> Is that an arrow scar I see? This dross-turbid pool of molten filth might be an answer to prayer for you, little Glooblin. I am the master of all things grubby and soiled, and this is my ","color":"white"},{"text":"Grime Forge","color":"gold"},{"text":". Use it freely, coat your garments in mucky magic.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
