# @s = interaction cliquée
execute on target run tag @s add mg.zbuyer
data remove entity @s interaction
execute unless entity @a[tag=mg.zbuyer,tag=mg.play,tag=!mg.zdead] run return run tag @a remove mg.zbuyer
execute if entity @s[tag=mg.zb1] run scoreboard players set $zc mg.st 750
execute if entity @s[tag=mg.zb1] if function mg:zm/pay run function mg:zm/door_1
execute if entity @s[tag=mg.zb2] run scoreboard players set $zc mg.st 750
execute if entity @s[tag=mg.zb2] if function mg:zm/pay run function mg:zm/door_2
execute if entity @s[tag=mg.zb3] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb3] if function mg:zm/pay run function mg:zm/door_3
execute if entity @s[tag=mg.zb4] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb4] if function mg:zm/pay run function mg:zm/door_4
execute if entity @s[tag=mg.zb11] run scoreboard players set $zc mg.st 500
execute if entity @s[tag=mg.zb11] if function mg:zm/pay run function mg:zm/buy_gun {n:4}
execute if entity @s[tag=mg.zb12] run scoreboard players set $zc mg.st 500
execute if entity @s[tag=mg.zb12] if function mg:zm/pay run function mg:zm/buy_gun {n:3}
execute if entity @s[tag=mg.zb13] run scoreboard players set $zc mg.st 1000
execute if entity @s[tag=mg.zb13] if function mg:zm/pay run function mg:zm/buy_gun {n:2}
execute if entity @s[tag=mg.zb20] run scoreboard players set $zc mg.st 950
execute if entity @s[tag=mg.zb20] if function mg:zm/pay run function mg:zm/box
execute if entity @s[tag=mg.zb21] if entity @a[tag=mg.zbuyer,tag=mg.zjug] run return run function mg:zm/already
execute if entity @s[tag=mg.zb21] run scoreboard players set $zc mg.st 2500
execute if entity @s[tag=mg.zb21] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/jug
execute if entity @s[tag=mg.zb22] if entity @a[tag=mg.zbuyer,tag=mg.zsc] run return run function mg:zm/already
execute if entity @s[tag=mg.zb22] run scoreboard players set $zc mg.st 3000
execute if entity @s[tag=mg.zb22] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/cola
tag @a remove mg.zbuyer
