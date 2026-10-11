# @s vise : zoom selon l'arme en main
attribute @s minecraft:movement_speed modifier remove mg:aim
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.3 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.35 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.25 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.6 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.9 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.45 add_multiplied_total
execute if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run return run attribute @s minecraft:movement_speed modifier add mg:aim -0.5 add_multiplied_total
