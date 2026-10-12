# @s : joueur avec un chapeau choisi, à sa position (chaque tick)
execute if entity @s[tag=mg.surv] run return run function mg:hat/strip
execute if entity @s[gamemode=spectator] run return run function mg:hat/strip
execute if predicate mg:invisible run return run function mg:hat/strip
execute if items entity @s container.* *[minecraft:custom_data~{mg_hat:1b}] run clear @s *[minecraft:custom_data~{mg_hat:1b}]
execute if items entity @s player.crafting.* *[minecraft:custom_data~{mg_hat:1b}] run clear @s *[minecraft:custom_data~{mg_hat:1b}]
execute if items entity @s weapon.offhand *[minecraft:custom_data~{mg_hat:1b}] run item replace entity @s weapon.offhand with minecraft:air
execute if items entity @s player.cursor *[minecraft:custom_data~{mg_hat:1b}] run item replace entity @s player.cursor with minecraft:air
execute unless items entity @s armor.head * run function mg:hat/wear
execute if entity @s[tag=mg.hatd] if items entity @s armor.head *[minecraft:custom_data~{mg_hat:1b}] run function mg:hat/unfollow
execute if items entity @s armor.head *[minecraft:custom_data~{mg_hat:1b}] run return 0
# casque de jeu sur la tête : le chapeau suit la tête
function mg:hat/follow
