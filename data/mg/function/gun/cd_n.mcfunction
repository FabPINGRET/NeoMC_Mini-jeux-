# Variante normale (hors dernière balle) : retire l'overlay de recharge ; Sniper : overlay de cadence
execute unless items entity @s weapon.mainhand *[custom_data~{gun:5}] unless items entity @s weapon.mainhand *[custom_data~{gcr:1b}] unless items entity @s weapon.mainhand *[custom_data~{gcr:2b}] run return 0
execute if items entity @s weapon.mainhand *[custom_data~{gun:1,gcr:1b}] run return run function mg:gun/cd_set {n:1,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:1,gcr:2b}] run return run function mg:gun/cd_set {n:1,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:2,gcr:1b}] run return run function mg:gun/cd_set {n:2,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:2,gcr:2b}] run return run function mg:gun/cd_set {n:2,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:3,gcr:1b}] run return run function mg:gun/cd_set {n:3,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:3,gcr:2b}] run return run function mg:gun/cd_set {n:3,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:4,gcr:1b}] run return run function mg:gun/cd_set {n:4,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:4,gcr:2b}] run return run function mg:gun/cd_set {n:4,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] unless entity @s[tag=mg.zdbl] unless items entity @s weapon.mainhand *[custom_data~{gcr:0b}] run return run function mg:gun/cd_set {n:5,s:1.5,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] if entity @s[tag=mg.zdbl] unless items entity @s weapon.mainhand *[custom_data~{gcr:3b}] run return run function mg:gun/cd_set {n:5,s:1,m:3}
execute if items entity @s weapon.mainhand *[custom_data~{gun:6,gcr:1b}] run return run function mg:gun/cd_set {n:6,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:6,gcr:2b}] run return run function mg:gun/cd_set {n:6,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:7,gcr:1b}] run return run function mg:gun/cd_set {n:7,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:7,gcr:2b}] run return run function mg:gun/cd_set {n:7,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:8,gcr:1b}] run return run function mg:gun/cd_set {n:8,s:0.05,m:0}
execute if items entity @s weapon.mainhand *[custom_data~{gun:8,gcr:2b}] run return run function mg:gun/cd_set {n:8,s:0.05,m:0}
