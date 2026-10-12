# @s : chapeau retiré (invisible, spectateur, survie) ; remis par mg:hat/guard dès que possible
clear @s *[minecraft:custom_data~{mg_hat:1b}]
execute if entity @s[tag=mg.hatd] run function mg:hat/unfollow
