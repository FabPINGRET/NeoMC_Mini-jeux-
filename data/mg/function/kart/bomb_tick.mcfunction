# Bob-omb (@s) : vol en cloche, se pose, clignote, explose au contact ou à la fin de la mèche
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run function mg:kart/bomb_boom
execute if score @s mg.kvy matches 1.. run scoreboard players remove @s mg.kvy 1
execute unless entity @s[tag=mg.kland] if score @s mg.kvy matches 1.. run tp @s ^ ^0.35 ^1.0
execute unless entity @s[tag=mg.kland] if score @s mg.kvy matches 0 run tp @s ^ ^-0.45 ^0.8
execute unless entity @s[tag=mg.kland] at @s unless block ~ ~-0.3 ~ #mg:kart_pass run tag @s add mg.kland
particle minecraft:small_flame ~ ~0.45 ~ 0.03 0.03 0.03 0 1
scoreboard players operation $kbl mg.st = @s mg.t
scoreboard players operation $kbl mg.st %= #k8 mg.st
execute if score $kbl mg.st matches 0 run item replace entity @s contents with minecraft:red_concrete
execute if score $kbl mg.st matches 4 run item replace entity @s contents with minecraft:black_concrete
execute if score @s mg.t matches ..50 if entity @e[type=minecraft:block_display,tag=mg.kart,distance=..1.8] run function mg:kart/bomb_boom
