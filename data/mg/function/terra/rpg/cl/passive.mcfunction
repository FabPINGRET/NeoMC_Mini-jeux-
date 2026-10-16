# @s : talents de sa classe (modificateurs mg:trcl*), retirés puis remis
attribute @s minecraft:max_health modifier remove mg:trcl
attribute @s minecraft:armor modifier remove mg:trcl
attribute @s minecraft:movement_speed modifier remove mg:trcl
attribute @s minecraft:jump_strength modifier remove mg:trcl
attribute @s minecraft:safe_fall_distance modifier remove mg:trcl
attribute @s minecraft:attack_damage modifier remove mg:trcl
execute if score @s mg.trcl matches 1 run attribute @s minecraft:max_health modifier add mg:trcl 6 add_value
execute if score @s mg.trcl matches 1 run attribute @s minecraft:armor modifier add mg:trcl 2 add_value
execute if score @s mg.trcl matches 2 run attribute @s minecraft:movement_speed modifier add mg:trcl 0.15 add_multiplied_base
execute if score @s mg.trcl matches 2 run attribute @s minecraft:jump_strength modifier add mg:trcl 0.1 add_value
execute if score @s mg.trcl matches 2 run attribute @s minecraft:safe_fall_distance modifier add mg:trcl 6 add_value
execute if score @s mg.trcl matches 2 run attribute @s minecraft:attack_damage modifier add mg:trcl 2 add_value
