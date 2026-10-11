execute if entity @e[tag=mg.evb] run tellraw @a {"text":"👑 Le Roi Zombie retourne dans son trou...","color":"gray"}
scoreboard players set $evbest mg.st 0
execute as @a[tag=mg.evl] run scoreboard players operation $evbest mg.st > @s mg.evd
execute if score $evbest mg.st matches 1.. as @a[tag=mg.evl] if score @s mg.evd = $evbest mg.st run tag @s add mg.evwin
execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win
tag @a remove mg.evwin
