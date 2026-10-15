# Habillage des animaux tourné comme eux (chaque tick), puis cycle des chutes et ambiance du thème (chaque seconde)
execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle rotated as @s on passengers if entity @s[tag=mg.thrid] run rotate @s ~ 0
scoreboard players add $tht mg.st 1
execute if score $tht mg.st matches ..19 run return 0
scoreboard players set $tht mg.st 0
function mg:lobby/theme/fall_tick
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/fx
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/fx
