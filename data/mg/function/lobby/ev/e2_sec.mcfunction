bossbar set mg:ev name {"text":"💰 Pluie de pièces","color":"gold","bold":true}
execute store result bossbar mg:ev value run scoreboard players get $evt mg.st
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute in minecraft:overworld run function mg:lobby/ev/e2_coin
execute as @a[tag=mg.evl] run function mg:lobby/ev/e2_count
