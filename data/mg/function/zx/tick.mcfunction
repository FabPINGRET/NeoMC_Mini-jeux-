# Zombies, chaque tick : bonus en cours, bonus au sol, grenades singe, roquettes, réparation des fenêtres
execute if score $zik mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"💀 Fin de la mort instantanée","color":"gray"}
execute if score $zik mg.st matches 1.. run scoreboard players remove $zik mg.st 1
execute if score $zdp mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"✖2 Fin des points doubles","color":"gray"}
execute if score $zdp mg.st matches 1.. run scoreboard players remove $zdp mg.st 1
execute if score $zfs mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🔥 Fin de la vente de feu","color":"gray"}
execute if score $zfs mg.st matches 1.. run scoreboard players remove $zfs mg.st 1
# (exécuté depuis le centre de la carte par zm/tick : sélecteurs bornés à 80 blocs)
execute as @e[type=minecraft:item_display,tag=mg.zpu,distance=..80] at @s run function mg:zx/pu_one
execute as @e[type=minecraft:snowball,tag=!mg.zms,distance=..80] if data entity @s Item.components."minecraft:custom_data".monkey at @s run function mg:zx/mk_new
execute as @e[type=minecraft:marker,tag=mg.zmt,distance=..80] run function mg:zx/mk_follow
execute as @e[type=minecraft:item_display,tag=mg.zmk,distance=..80] at @s run function mg:zx/mk_tick
execute as @e[type=minecraft:item_display,tag=mg.zrk,distance=..80] at @s run function mg:zx/rk_tick
scoreboard players add $zxt mg.st 1
execute if score $zxt mg.st matches 10.. run function mg:zx/win_fix_all
execute as @e[type=minecraft:item,distance=..80] if items entity @s contents *[custom_data~{mg_gun:1b}] run function mg:zx/q_item
execute as @e[type=minecraft:item,distance=..80] if items entity @s contents *[custom_data~{zrpg:1b}] run function mg:zx/q_item
scoreboard players reset @a[scores={mg.zdr=1..}] mg.zdr
scoreboard players set $zxon mg.st 2
