# @s recloue une planche (à la position de la fenêtre) : +10 pts, 20 fois par manche au plus
execute as @e[type=minecraft:marker,tag=mg.zwin,sort=nearest,limit=1] run function mg:zx/win_up
execute if score @s mg.zrp matches ..19 run scoreboard players add @s mg.zpt 10
execute if score @s mg.zrp matches ..19 if score $zdp mg.st matches 1.. run scoreboard players add @s mg.zpt 10
scoreboard players add @s mg.zrp 1
playsound minecraft:block.wood.place player @a ~ ~ ~ 1 0.8
playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.4 1.6
