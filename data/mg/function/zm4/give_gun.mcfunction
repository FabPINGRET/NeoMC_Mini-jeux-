# @s reçoit l'arme $zgn : recharge si déjà possédée, sinon 2e emplacement (3e avec Mule Kick), sinon remplace l'arme en main
execute if score $zgn mg.st matches 11 run return run function mg:zx/monkey_give
execute if score $zgn mg.st matches 12 run return run function mg:zx/bat_give
execute if score $zgn mg.st matches 10 if items entity @s container.* *[custom_data~{zrpg:1b}] run return 0
execute if score $zgn mg.st matches 1 if items entity @s container.* *[custom_data~{gun:1}] run return run scoreboard players set @s mg.g1 8
execute if score $zgn mg.st matches 2 if items entity @s container.* *[custom_data~{gun:2}] run return run scoreboard players set @s mg.g2 30
execute if score $zgn mg.st matches 3 if items entity @s container.* *[custom_data~{gun:3}] run return run scoreboard players set @s mg.g3 4
execute if score $zgn mg.st matches 4 if items entity @s container.* *[custom_data~{gun:4}] run return run scoreboard players set @s mg.g4 10
execute if score $zgn mg.st matches 5 if items entity @s container.* *[custom_data~{gun:5}] run return run scoreboard players set @s mg.g5 5
execute if score $zgn mg.st matches 6 if items entity @s container.* *[custom_data~{gun:6}] run return run scoreboard players set @s mg.g6 20
execute if score $zgn mg.st matches 7 if items entity @s container.* *[custom_data~{gun:7}] run return run scoreboard players set @s mg.g7 60
execute if score $zgn mg.st matches 8 if items entity @s container.* *[custom_data~{gun:8}] run return run scoreboard players set @s mg.g8 6
execute unless items entity @s hotbar.2 * run return run function mg:zm4/put {slot:"hotbar.2"}
execute if entity @s[tag=mg.zmu] unless items entity @s hotbar.3 * run return run function mg:zm4/put {slot:"hotbar.3"}
execute if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run return run function mg:zm4/put {slot:"weapon.mainhand"}
execute if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] run return run function mg:zm4/put {slot:"weapon.mainhand"}
function mg:zm4/put {slot:"hotbar.2"}
