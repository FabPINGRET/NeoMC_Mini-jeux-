# @s porte sa caisse : elle flotte au-dessus de sa tête
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[type=minecraft:item_display,tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run tp @s ~ ~2.2 ~ ~ 0
