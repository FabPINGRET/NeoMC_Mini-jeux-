# Habillage des animaux tourné comme eux (chaque tick), puis cycle des chutes et ambiance du thème (chaque seconde)
execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle rotated as @s on passengers if entity @s[tag=mg.thrid] run rotate @s ~ 0
execute as @e[type=minecraft:interaction,tag=mg.thnpci] if data entity @s interaction run function mg:lobby/theme/npc_use
execute as @e[type=minecraft:interaction,tag=mg.thnpci] if data entity @s attack run function mg:lobby/theme/npc_use
execute as @a[tag=mg.thbun] at @s run function mg:lobby/theme/stew_rabbit_tp
execute as @a[tag=mg.thzap] at @s run particle minecraft:electric_spark ~ ~0.2 ~ 0.2 0.1 0.2 0 2 normal
scoreboard players add $tht mg.st 1
execute if score $tht mg.st matches ..19 run return 0
scoreboard players set $tht mg.st 0
function mg:lobby/theme/npc_second
function mg:lobby/theme/fall_tick
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/fx
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/fx
