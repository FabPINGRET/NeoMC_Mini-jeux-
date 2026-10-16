# @s : sa monture disparaît
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.trmount] if score @s mg.tvo = $own mg.st at @s run tp @s ~ -400 ~
