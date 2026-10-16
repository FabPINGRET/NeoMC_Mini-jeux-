# @s a jeté (Q) une arme : elle revient et se recharge
scoreboard players reset @s mg.zdr
data modify storage mg:zm du set from entity @s UUID
execute as @e[type=minecraft:item,distance=..8] if items entity @s contents *[custom_data~{mg_gun:1b}] run function mg:zx/drop_mine
execute as @e[type=minecraft:item,distance=..8] if items entity @s contents *[custom_data~{zrpg:1b}] run function mg:zx/drop_mine
execute unless entity @e[type=minecraft:item,tag=mg.zdi] run return 0
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:1}] run function mg:gun/reload_1
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:2}] run function mg:gun/reload_2
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:3}] run function mg:gun/reload_3
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:4}] run function mg:gun/reload_4
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:5}] run function mg:gun/reload_5
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:6}] run function mg:gun/reload_6
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:7}] run function mg:gun/reload_7
execute if items entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents *[custom_data~{gun:8}] run function mg:gun/reload_8
scoreboard players set $zq mg.st 0
execute unless items entity @s weapon.mainhand * run scoreboard players set $zq mg.st 1
execute if score $zq mg.st matches 1 run item replace entity @s weapon.mainhand from entity @e[type=minecraft:item,tag=mg.zdi,limit=1] contents
execute if score $zq mg.st matches 1 run kill @e[type=minecraft:item,tag=mg.zdi,limit=1]
tag @s add mg.zdp
execute as @e[type=minecraft:item,tag=mg.zdi] run data merge entity @s {PickupDelay:0s}
execute as @e[type=minecraft:item,tag=mg.zdi] run tp @s @a[tag=mg.zdp,limit=1]
tag @s remove mg.zdp
tag @e[type=minecraft:item,tag=mg.zdi] remove mg.zdi
