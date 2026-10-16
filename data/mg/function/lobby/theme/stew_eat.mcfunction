# 🎃 Ragoût mystère consommé (advancement mg:theme_stew ; @s = joueur) : ricanement, puis effet tiré au hasard
advancement revoke @s only mg:theme_stew
# hors thème, en partie, en survie ou occupé ailleurs : consommé sans effet
execute unless score $theme mg.st matches 1.. run return 0
execute if entity @s[tag=mg.surv] run return 0
execute if entity @s[tag=mg.play] run return 0
execute if entity @s[tag=mg.ely] run return 0
execute if entity @s[tag=mg.xso] run return 0
execute if entity @s[tag=mg.lk] run return 0
execute if entity @s[tag=mg.inplot] run return 0
execute if entity @s[tag=mg.visit] run return 0
execute at @s run playsound minecraft:entity.witch.ambient neutral @a[distance=..16] ~ ~ ~ 1 1
execute store result score $thr mg.st run random value 1..8
execute if score $thr mg.st matches 1 run return run effect give @s minecraft:invisibility 20 0
execute if score $thr mg.st matches 2 run return run effect give @s minecraft:glowing 10 0
execute if score $thr mg.st matches 3 run return run effect give @s minecraft:nausea 8 0
execute if score $thr mg.st matches 4 run return run effect give @s minecraft:levitation 5 0
execute if score $thr mg.st matches 5 run return run function mg:lobby/theme/stew_mini
execute if score $thr mg.st matches 6 run return run function mg:lobby/theme/stew_moon
execute if score $thr mg.st matches 7 run return run function mg:lobby/theme/stew_burp
execute if score $thr mg.st matches 8 run return run function mg:lobby/theme/stew_wind
