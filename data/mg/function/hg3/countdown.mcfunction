scoreboard players operation $hgq mg.st = $hgt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $hgq mg.st %= #20 mg.st
execute unless score $hgq mg.st matches 0 run return 0
scoreboard players set $hgc mg.st 10
scoreboard players operation $hgs mg.st = $hgt mg.st
scoreboard players operation $hgs mg.st /= #20 mg.st
scoreboard players operation $hgc mg.st -= $hgs mg.st
title @a[tag=mg.play] title {"score":{"name":"$hgc","objective":"mg.st"},"color":"gold","bold":true}
execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4
