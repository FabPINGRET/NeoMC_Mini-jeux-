# Redonne la canne menu (admin) ou vote (autres) SEULEMENT si elle manque (@s = joueur)
execute if entity @s[tag=mg.admin] if items entity @s hotbar.* minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_menu:1b}] run return 0
execute if entity @s[tag=mg.admin] if items entity @s container.* minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_menu:1b}] run return 0
execute if entity @s[tag=mg.admin] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_menu:1b}] run return 0
execute unless entity @s[tag=mg.admin] if items entity @s hotbar.* minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_vote:1b}] run return 0
execute unless entity @s[tag=mg.admin] if items entity @s container.* minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_vote:1b}] run return 0
execute unless entity @s[tag=mg.admin] if items entity @s weapon.offhand minecraft:carrot_on_a_stick[minecraft:custom_data~{mg_vote:1b}] run return 0
function mg:core/give_menu
