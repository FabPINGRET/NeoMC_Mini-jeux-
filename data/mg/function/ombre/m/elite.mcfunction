# @s devient une élite : PV ×2,5, contour doré, affixe, butin à sa mort
tag @s add mg.olelite
attribute @s minecraft:max_health modifier add mg:olelite 1.5 add_multiplied_total
attribute @s minecraft:attack_damage modifier add mg:olelite 0.3 add_multiplied_base
execute store result entity @s Health float 1 run attribute @s minecraft:max_health get
data merge entity @s {Glowing:1b,CustomNameVisible:1b}
team join mg_olel @s
execute store result score $r mg.st run random value 1..4
execute if score $r mg.st matches 1 run effect give @s minecraft:speed infinite 1 true
execute if score $r mg.st matches 2 run attribute @s minecraft:scale modifier add mg:olelite 0.3 add_multiplied_base
execute if score $r mg.st matches 2 run attribute @s minecraft:knockback_resistance base set 1
execute if score $r mg.st matches 3 run effect give @s minecraft:regeneration infinite 1 true
execute if score $r mg.st matches 4 run effect give @s minecraft:resistance infinite 0 true
tag @s add mg.olelnm
