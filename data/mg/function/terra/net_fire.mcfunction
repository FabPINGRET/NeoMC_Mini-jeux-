# @s : lance-filets (un filet par tir)
execute if score @s mg.tvnet matches ..0 run return run function mg:terra/no_net
scoreboard players remove @s mg.tvnet 1
playsound minecraft:entity.fishing_bobber.throw player @a ~ ~ ~ 1 0.6
scoreboard players set $tvr mg.st 0
execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/net_ray
