# @s a fait un clic droit avec un bâton (corde ou dynamite)
scoreboard players reset @s mg.fnu
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{fn_rope:1b}] run return run function mg:filon/rope
execute if items entity @s weapon.mainhand *[minecraft:custom_data~{fn_dyn:1b}] run return run function mg:filon/dyn
execute if items entity @s weapon.offhand *[minecraft:custom_data~{fn_rope:1b}] run return run function mg:filon/rope
execute if items entity @s weapon.offhand *[minecraft:custom_data~{fn_dyn:1b}] run return run function mg:filon/dyn
