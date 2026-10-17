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
execute if entity @s[tag=mg.pkr] run return 0
execute at @s run playsound minecraft:entity.witch.ambient neutral @a[distance=..16] ~ ~ ~ 1 1
execute store result score $thr mg.st run random value 1..12
execute if score $thr mg.st matches 1 run title @s actionbar {"text":"👻 Invisible ! (45 s)","color":"gray"}
execute if score $thr mg.st matches 1 run return run effect give @s minecraft:invisibility 45 0
execute if score $thr mg.st matches 2 run title @s actionbar {"text":"✨ Tu brilles à travers les murs ! (30 s)","color":"yellow"}
execute if score $thr mg.st matches 2 run return run effect give @s minecraft:glowing 30 0
execute if score $thr mg.st matches 3 run title @s actionbar {"text":"😵 Le monde tourne… (15 s)","color":"dark_green"}
execute if score $thr mg.st matches 3 run return run effect give @s minecraft:nausea 15 0
execute if score $thr mg.st matches 4 run title @s actionbar {"text":"🎈 Tu t'envoles… et tu redescends en douceur (10 s)","color":"light_purple"}
execute if score $thr mg.st matches 4 run effect give @s minecraft:slow_falling 18 0
execute if score $thr mg.st matches 4 run return run effect give @s minecraft:levitation 10 0
execute if score $thr mg.st matches 5 run return run function mg:lobby/theme/stew_mini
execute if score $thr mg.st matches 6 run return run function mg:lobby/theme/stew_moon
execute if score $thr mg.st matches 7 run return run function mg:lobby/theme/stew_burp
execute if score $thr mg.st matches 8 run return run function mg:lobby/theme/stew_wind
execute if score $thr mg.st matches 9 run return run function mg:lobby/theme/stew_rabbit
execute if score $thr mg.st matches 10 run return run function mg:lobby/theme/stew_flash
execute if score $thr mg.st matches 11 run return run function mg:lobby/theme/stew_skate
execute if score $thr mg.st matches 12 run return run function mg:lobby/theme/stew_bounce
