# @s : talents de la classe (modificateurs mg:olcl)
attribute @s minecraft:max_health modifier remove mg:olcl
attribute @s minecraft:armor modifier remove mg:olcl
attribute @s minecraft:movement_speed modifier remove mg:olcl
attribute @s minecraft:safe_fall_distance modifier remove mg:olcl
attribute @s minecraft:knockback_resistance modifier remove mg:olcl
execute if score @s mg.olcl matches 1 run attribute @s minecraft:max_health modifier add mg:olcl 6 add_value
execute if score @s mg.olcl matches 1 run attribute @s minecraft:armor modifier add mg:olcl 2 add_value
execute if score @s mg.olcl matches 1 run attribute @s minecraft:knockback_resistance modifier add mg:olcl 0.3 add_value
execute if score @s mg.olcl matches 2 run attribute @s minecraft:movement_speed modifier add mg:olcl 0.12 add_multiplied_base
execute if score @s mg.olcl matches 2 run attribute @s minecraft:safe_fall_distance modifier add mg:olcl 6 add_value
execute if score @s mg.olcl matches 4 run attribute @s minecraft:max_health modifier add mg:olcl 4 add_value
