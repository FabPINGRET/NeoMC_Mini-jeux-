title @s times 5 30 10
title @s title {"text":"STRIKE !","color":"gold","bold":true}
title @s subtitle {"text":"✖ toutes les quilles d'un coup","color":"yellow"}
tellraw @a[tag=mg.play] [{"text":"🎳 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" fait un ","color":"gray"},{"text":"STRIKE","color":"gold","bold":true},{"text":" !","color":"gray"}]
playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2
execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 1
execute if score #ln mg.st matches 0 run particle minecraft:firework -24.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 1 run particle minecraft:firework -17.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 2 run particle minecraft:firework -10.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 3 run particle minecraft:firework -3.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 4 run particle minecraft:firework 3.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 5 run particle minecraft:firework 10.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 6 run particle minecraft:firework 17.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 7 run particle minecraft:firework 24.5 66 35177 1.2 0.6 1.2 0.15 60 force
execute if score #ln mg.st matches 0 run particle minecraft:totem_of_undying -24.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 1 run particle minecraft:totem_of_undying -17.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 2 run particle minecraft:totem_of_undying -10.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 3 run particle minecraft:totem_of_undying -3.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 4 run particle minecraft:totem_of_undying 3.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 5 run particle minecraft:totem_of_undying 10.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 6 run particle minecraft:totem_of_undying 17.5 66 35177 1.2 0.6 1.2 0.15 40 force
execute if score #ln mg.st matches 7 run particle minecraft:totem_of_undying 24.5 66 35177 1.2 0.6 1.2 0.15 40 force
