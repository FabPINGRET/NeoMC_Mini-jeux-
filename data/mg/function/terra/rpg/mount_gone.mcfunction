# @s : sa monture disparaît (le joueur descend d'abord, puis la monture est envoyée sous le monde et retirée)
ride @s dismount
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.trmount] if score @s mg.tvo = $own mg.st at @s run tp @s ~ -400 ~
execute as @e[tag=mg.trmount] if score @s mg.tvo = $own mg.st run kill @s
