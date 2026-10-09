# @s reçoit l'arme $zgn : recharge si déjà possédée, sinon 2e emplacement, sinon remplace l'arme en main
execute if score $zgn mg.st matches 1 if items entity @s container.* *[custom_data~{gun:1}] run return run scoreboard players set @s mg.g1 8
execute if score $zgn mg.st matches 2 if items entity @s container.* *[custom_data~{gun:2}] run return run scoreboard players set @s mg.g2 30
execute if score $zgn mg.st matches 3 if items entity @s container.* *[custom_data~{gun:3}] run return run scoreboard players set @s mg.g3 4
execute if score $zgn mg.st matches 4 if items entity @s container.* *[custom_data~{gun:4}] run return run scoreboard players set @s mg.g4 10
execute if score $zgn mg.st matches 5 if items entity @s container.* *[custom_data~{gun:5}] run return run scoreboard players set @s mg.g5 5
execute if score $zgn mg.st matches 6 if items entity @s container.* *[custom_data~{gun:6}] run return run scoreboard players set @s mg.g6 20
execute unless items entity @s hotbar.2 * run return run function mg:zm2/put {slot:"hotbar.2"}
execute if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run return run function mg:zm2/put {slot:"weapon.mainhand"}
function mg:zm2/put {slot:"hotbar.2"}
