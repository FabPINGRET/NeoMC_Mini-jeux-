# Objet utilisé (clic droit) par @s
scoreboard players reset @s mg.qs
execute if score @s mg.kit matches 0 run return 0
scoreboard players operation $kuse mg.st = @s mg.kit
scoreboard players set @s mg.kit 0
clear @s minecraft:warped_fungus_on_a_stick
execute if score $kuse mg.st matches 1 run function mg:kart/use_banana
execute if score $kuse mg.st matches 2 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 3 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 4 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 5 run function mg:kart/use_star
execute if score $kuse mg.st matches 6 run function mg:kart/use_lightning
