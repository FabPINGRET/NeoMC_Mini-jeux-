# Entretien chaque seconde : retour des reconnectés, pions remis en place, affichage
scoreboard players set $mpu mg.st 0
execute as @a[tag=mg.mpp,tag=mg.out,tag=!mg.spectate] run function mg:party/rejoin
execute unless score $mph mg.st matches 3 as @a[tag=mg.mpp,tag=mg.play] run function mg:party/place
execute if score $mph mg.st matches 3 as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpcur] run function mg:party/place
execute at @e[type=minecraft:text_display,tag=mg.mpstar] run particle minecraft:end_rod ~ ~-2 ~ 0.5 1 0.5 0.02 12
execute as @a[tag=mg.mpp,tag=!mg.mpcur] run title @s actionbar [{"text":"★ ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpk"},"color":"yellow"},{"text":"    ● ","color":"gold"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold"},{"text":"    Tour ","color":"gray"},{"score":{"name":"$mpround","objective":"mg.st"},"color":"white"},{"text":"/","color":"gray"},{"score":{"name":"$mpmax","objective":"mg.st"},"color":"white"}]
