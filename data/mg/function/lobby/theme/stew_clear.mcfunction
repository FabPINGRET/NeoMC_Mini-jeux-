# Retire les modificateurs, le tag mini-moi / lapin / flash, le lapin et le chrono du ragoût chez @s (silencieux ; jamais les valeurs de base)
attribute @s minecraft:scale modifier remove mg:thstew
attribute @s minecraft:gravity modifier remove mg:thstew
attribute @s minecraft:jump_strength modifier remove mg:thstew
attribute @s minecraft:movement_speed modifier remove mg:thstew
attribute @s minecraft:step_height modifier remove mg:thstew
attribute @s minecraft:friction_modifier modifier remove mg:thstew
attribute @s minecraft:air_drag_modifier modifier remove mg:thstew
attribute @s minecraft:bounciness modifier remove mg:thstew
execute if entity @s[tag=mg.thbun] run effect clear @s minecraft:invisibility
execute if entity @s[tag=mg.thbun] run scoreboard players operation $thbi mg.st = @s mg.thbn
execute if entity @s[tag=mg.thbun] as @e[type=minecraft:rabbit,tag=mg.thbun] if score @s mg.thbn = $thbi mg.st run kill @s
tag @s remove mg.thmini
tag @s remove mg.thbun
tag @s remove mg.thzap
scoreboard players reset @s mg.ths
