attribute @s minecraft:max_health modifier remove mg:olst
attribute @s minecraft:attack_damage modifier remove mg:olst
attribute @s minecraft:movement_speed modifier remove mg:olst
$attribute @s minecraft:max_health modifier add mg:ollv $(lv) add_value
$attribute @s minecraft:max_health modifier add mg:olst $(v) add_value
$attribute @s minecraft:attack_damage modifier add mg:olst $(f) add_value
$attribute @s minecraft:movement_speed modifier add mg:olst $(a) add_multiplied_base
