title @s times 5 25 10
title @s title {"text":"SPARE !","color":"aqua","bold":true}
title @s subtitle {"text":"/ toutes les quilles en 2 lancers","color":"gray"}
tellraw @a[tag=mg.play] [{"text":"🎳 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" fait un ","color":"gray"},{"text":"SPARE","color":"aqua","bold":true},{"text":" !","color":"gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.7 1.4
execute if score #ln mg.st matches 0 run particle minecraft:happy_villager -24.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 1 run particle minecraft:happy_villager -17.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 2 run particle minecraft:happy_villager -10.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 3 run particle minecraft:happy_villager -3.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 4 run particle minecraft:happy_villager 3.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 5 run particle minecraft:happy_villager 10.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 6 run particle minecraft:happy_villager 17.5 66 35177 1.2 0.6 1.2 0.15 30 force
execute if score #ln mg.st matches 7 run particle minecraft:happy_villager 24.5 66 35177 1.2 0.6 1.2 0.15 30 force
