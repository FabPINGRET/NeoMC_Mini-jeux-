# Entretien chaque seconde : retour des reconnectés, pions remis en place, affichage, ambiance
scoreboard players set $mpu mg.st 0
execute as @a[tag=mg.mpp,tag=mg.out,tag=!mg.spectate] run function mg:party/rejoin
execute unless score $mph mg.st matches 3 as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpview] run function mg:party/place
execute if score $mph mg.st matches 3 as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpview,tag=!mg.mpcur] run function mg:party/place
execute at @e[type=minecraft:text_display,tag=mg.mpstar] run particle minecraft:end_rod ~ ~-2 ~ 0.5 1 0.5 0.02 12
particle minecraft:large_smoke 38 98 15040 2 2 2 0.02 25 force
particle minecraft:lava 38 93 15040 2 0.5 2 0 6 force
execute as @a[tag=mg.mpp,tag=!mg.mpcur,tag=!mg.mpview] run title @s actionbar [{"text":"★ ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpk"},"color":"yellow"},{"text":"    ● ","color":"gold"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold"},{"text":"    ","color":"gray"},{"text":"🎲🎲×","color":"aqua"},{"score":{"name":"@s","objective":"mg.mid"},"color":"aqua"},{"text":"  🎲🎲🎲×","color":"light_purple"},{"score":{"name":"@s","objective":"mg.mit"},"color":"light_purple"},{"text":"  🔀×","color":"yellow"},{"score":{"name":"@s","objective":"mg.mip"},"color":"yellow"},{"text":"    Tour ","color":"gray"},{"score":{"name":"$mpround","objective":"mg.st"},"color":"white"},{"text":"/","color":"gray"},{"score":{"name":"$mpmax","objective":"mg.st"},"color":"white"}]
