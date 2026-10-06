# Le rayon touche de la neige (position = bloc visé) : le bloc disparaît
setblock ~ ~ ~ minecraft:air
# XXL : cratère 3x3 (neige uniquement)
execute if score $sg mg.st matches 1 run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:snow_block
particle minecraft:snowflake ~ ~ ~ 0.3 0.3 0.3 0.05 20
particle minecraft:poof ~ ~ ~ 0.2 0.2 0.2 0.02 4
playsound minecraft:block.snow.break master @a ~ ~ ~ 1.2 1
