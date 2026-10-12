# @s (bonus) pris par le joueur le plus proche (mg.zpk)
tag @a[tag=mg.play,tag=!mg.zdead,distance=..1.8,sort=nearest,limit=1] add mg.zpk
execute if score @s mg.zpy matches 1 run title @a[tag=mg.play] title {"text":"💀 MORT INSTANTANÉE","color":"white","bold":true}
execute if score @s mg.zpy matches 1 run title @a[tag=mg.play] subtitle {"text":"un coup suffit pendant 30 s","color":"gray"}
execute if score @s mg.zpy matches 1 run tellraw @a[tag=mg.play] [{"text":"🎁 ","color":"white"},{"selector":"@a[tag=mg.zpk]","color":"yellow"},{"text":" a pris : ","color":"gray"},{"text":"💀 MORT INSTANTANÉE","color":"white","bold":true}]
execute if score @s mg.zpy matches 2 run title @a[tag=mg.play] title {"text":"💥 KABOOM","color":"red","bold":true}
execute if score @s mg.zpy matches 2 run title @a[tag=mg.play] subtitle {"text":"tous les zombies explosent, +400 pts","color":"gray"}
execute if score @s mg.zpy matches 2 run tellraw @a[tag=mg.play] [{"text":"🎁 ","color":"red"},{"selector":"@a[tag=mg.zpk]","color":"yellow"},{"text":" a pris : ","color":"gray"},{"text":"💥 KABOOM","color":"red","bold":true}]
execute if score @s mg.zpy matches 3 run title @a[tag=mg.play] title {"text":"✖2 POINTS DOUBLES","color":"yellow","bold":true}
execute if score @s mg.zpy matches 3 run title @a[tag=mg.play] subtitle {"text":"pendant 30 s","color":"gray"}
execute if score @s mg.zpy matches 3 run tellraw @a[tag=mg.play] [{"text":"🎁 ","color":"yellow"},{"selector":"@a[tag=mg.zpk]","color":"yellow"},{"text":" a pris : ","color":"gray"},{"text":"✖2 POINTS DOUBLES","color":"yellow","bold":true}]
execute if score @s mg.zpy matches 4 run title @a[tag=mg.play] title {"text":"🪚 CHARPENTIER","color":"gold","bold":true}
execute if score @s mg.zpy matches 4 run title @a[tag=mg.play] subtitle {"text":"toutes les fenêtres réparées, +200 pts","color":"gray"}
execute if score @s mg.zpy matches 4 run tellraw @a[tag=mg.play] [{"text":"🎁 ","color":"gold"},{"selector":"@a[tag=mg.zpk]","color":"yellow"},{"text":" a pris : ","color":"gray"},{"text":"🪚 CHARPENTIER","color":"gold","bold":true}]
execute if score @s mg.zpy matches 5 run title @a[tag=mg.play] title {"text":"🔥 VENTE DE FEU","color":"light_purple","bold":true}
execute if score @s mg.zpy matches 5 run title @a[tag=mg.play] subtitle {"text":"boîte mystère à 10 pts pendant 30 s","color":"gray"}
execute if score @s mg.zpy matches 5 run tellraw @a[tag=mg.play] [{"text":"🎁 ","color":"light_purple"},{"selector":"@a[tag=mg.zpk]","color":"yellow"},{"text":" a pris : ","color":"gray"},{"text":"🔥 VENTE DE FEU","color":"light_purple","bold":true}]
execute if score @s mg.zpy matches 1 run function mg:zx/pu_ik
execute if score @s mg.zpy matches 2 run function mg:zx/pu_kaboom
execute if score @s mg.zpy matches 3 run scoreboard players set $zdp mg.st 600
execute if score @s mg.zpy matches 4 run function mg:zx/pu_carp
execute if score @s mg.zpy matches 5 run scoreboard players set $zfs mg.st 600
execute as @a[tag=mg.play] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.6 1.4
tag @a remove mg.zpk
kill @s
