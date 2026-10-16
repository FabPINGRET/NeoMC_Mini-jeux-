# 💣 Bomberman — tick
scoreboard players add $yc mg.st 1
execute as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{ybomb:1b}] at @s align xz positioned ~0.5 65 ~0.5 run function mg:bman/place
scoreboard players reset @a[scores={mg.qs=1..}] mg.qs
scoreboard players remove @a[scores={mg.yh=1..}] mg.yh 1
execute as @e[type=minecraft:marker,tag=mg.yb] at @s run function mg:bman/bomb_tick
execute as @e[type=minecraft:marker,tag=mg.yf] at @s run function mg:bman/flame_tick
execute as @e[type=minecraft:item_display,tag=mg.yp] at @s run function mg:bman/pu_tick
scoreboard players operation $yq mg.st = $yc mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $yq mg.st %= #20 mg.st
execute if score $yq mg.st matches 0 run function mg:bman/second
execute if score $yc mg.st matches 3000 run function mg:bman/sudden
execute if score $yc mg.st matches 3000.. run scoreboard players operation $yq mg.st = $yc mg.st
scoreboard players set #12 mg.st 12
execute if score $yc mg.st matches 3000.. run scoreboard players operation $yq mg.st %= #12 mg.st
execute if score $yc mg.st matches 3000.. if score $yq mg.st matches 0 run function mg:bman/rain
execute if score $state mg.st matches 2 run function mg:bman/check
execute if score $state mg.st matches 2 if score $yc mg.st matches 4800.. run function mg:bman/time_up
