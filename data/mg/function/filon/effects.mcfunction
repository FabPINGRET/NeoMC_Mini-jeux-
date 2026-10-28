# @s : hâte selon son niveau, vision nocturne (rafraîchies chaque seconde)
execute if score @s mg.fnha matches 0 run effect give @s minecraft:haste 3 0 true
execute if score @s mg.fnha matches 1 run effect give @s minecraft:haste 3 1 true
execute if score @s mg.fnha matches 2 run effect give @s minecraft:haste 3 2 true
effect give @s minecraft:night_vision 15 0 true
