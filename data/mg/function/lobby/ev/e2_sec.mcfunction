execute unless score $theme mg.st matches 1..2 run bossbar set mg:ev name {"text":"💰 Pluie de pièces","color":"gold","bold":true}
execute if score $theme mg.st matches 1 run bossbar set mg:ev name {"text":"🍬 Chasse aux bonbons","color":"gold","bold":true}
execute if score $theme mg.st matches 2 run bossbar set mg:ev name {"text":"🎁 Chasse aux cadeaux","color":"red","bold":true}
execute store result bossbar mg:ev value run scoreboard players get $evt mg.st
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute as @a[tag=mg.evl] run function mg:lobby/ev/e2_count
