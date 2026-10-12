# Chaque seconde : sans resource pack, hors saison, objets perdus, présentoirs orphelins
scoreboard players set $hatt mg.st 0
execute unless score $rp mg.st matches 1 run clear @a *[minecraft:custom_data~{mg_hat:1b}]
execute unless score $rp mg.st matches 1 run kill @e[type=minecraft:item_display,tag=mg.hatf]
execute unless score $rp mg.st matches 1 run tag @a remove mg.hatd
# galerie absente ou recouverte (construction du spawn par étapes, monde déjà installé) : reconstruite
execute if score $setup mg.st matches 1 if data storage mg:lobby v6 unless block -34 44 8 minecraft:polished_deepslate run function mg:hat/build
execute if score $setup mg.st matches 1 if data storage mg:lobby v6 unless block -33 48 9 minecraft:air run function mg:hat/build
execute as @a unless score @s mg.hat matches 1.. run clear @s *[minecraft:custom_data~{mg_hat:1b}]
execute unless score $theme mg.st matches 1 as @a[scores={mg.hat=29..32}] run function mg:hat/off_season
execute unless score $theme mg.st matches 2 as @a[scores={mg.hat=33..35}] run function mg:hat/off_season
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{mg_hat:1b}] run kill @s
tag @e[type=minecraft:item_display,tag=mg.hatf] add mg.hato
execute as @a[tag=mg.hatd] run function mg:hat/keep
kill @e[type=minecraft:item_display,tag=mg.hato]
