# Objet utilisé par @s (son kart porte mg.kk)
execute if score @s mg.kit matches 0 run return 0
scoreboard players operation $kuse mg.st = @s mg.kit
# objets à charges : on en consomme une, l'objet reste tant qu'il en reste
execute if score $kuse mg.st matches 8..11 run function mg:kart/use_charge
execute if score $kuse mg.st matches 12 run return run function mg:kart/use_golden
execute unless score $kuse mg.st matches 8..11 run scoreboard players set @s mg.kit 0
execute if score @s mg.kit matches 0 run clear @s minecraft:warped_fungus_on_a_stick
execute if score $kuse mg.st matches 1 run function mg:kart/use_banana
execute if score $kuse mg.st matches 2 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 3 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 4 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 5 run function mg:kart/use_star
execute if score $kuse mg.st matches 6 run function mg:kart/use_lightning
execute if score $kuse mg.st matches 7 run function mg:kart/use_blue
execute if score $kuse mg.st matches 8 run function mg:kart/use_banana
execute if score $kuse mg.st matches 9 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 10 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 11 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 13 run function mg:kart/use_bomb
execute if score $kuse mg.st matches 14 run function mg:kart/use_bill
execute if score $kuse mg.st matches 15 run function mg:kart/use_blooper
execute if score $kuse mg.st matches 16 run function mg:kart/use_horn
execute if score $kuse mg.st matches 17 run function mg:kart/use_boo
execute if score $kuse mg.st matches 18 run function mg:kart/use_fake
execute if score $kuse mg.st matches 19 run function mg:kart/use_mega
