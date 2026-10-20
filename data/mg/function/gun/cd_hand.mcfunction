# @s tient une arme mg_gun : choisit la variante use_cooldown (limites : accroupi, Q, Neo GTA, lobby)
execute if score @s mg.grl matches 1.. if items entity @s weapon.mainhand *[custom_data~{gun:5,gcr:4b}] run return 0
execute if score @s mg.grl matches 1.. if items entity @s weapon.mainhand *[custom_data~{gun:5}] run return run function mg:gun/cd_set {n:5,s:0.05,m:4}
execute if score @s mg.grl matches 1.. run return run function mg:gun/cd_n
execute if score @s mg.gcd matches 1.. run return run function mg:gun/cd_n
execute if items entity @s weapon.mainhand *[custom_data~{gun:1}] if score @s mg.g1 matches ..1 run return run function mg:gun/cd_r {n:1,s:1.5,h:0.75}
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] if score @s mg.g2 matches ..1 run return run function mg:gun/cd_r {n:2,s:2,h:1}
execute if items entity @s weapon.mainhand *[custom_data~{gun:3}] if score @s mg.g3 matches ..1 run return run function mg:gun/cd_r {n:3,s:2.5,h:1.25}
execute if items entity @s weapon.mainhand *[custom_data~{gun:4}] if score @s mg.g4 matches ..1 run return run function mg:gun/cd_r {n:4,s:2,h:1}
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] if score @s mg.g5 matches ..1 run return run function mg:gun/cd_r {n:5,s:3,h:1.5}
execute if items entity @s weapon.mainhand *[custom_data~{gun:6}] if score @s mg.g6 matches ..1 run return run function mg:gun/cd_r {n:6,s:2.5,h:1.25}
execute if items entity @s weapon.mainhand *[custom_data~{gun:7}] if score @s mg.g7 matches ..1 run return run function mg:gun/cd_r {n:7,s:4,h:2}
execute if items entity @s weapon.mainhand *[custom_data~{gun:8}] if score @s mg.g8 matches ..1 run return run function mg:gun/cd_r {n:8,s:2,h:1}
function mg:gun/cd_n
