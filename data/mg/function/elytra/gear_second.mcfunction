# Toutes les 2 s (core/tick) : équipement du spawn rendu à qui le garde, objets jetés au sol détruits
execute as @e[type=minecraft:item] if items entity @s contents *[minecraft:custom_data~{mg_elyf:1b}] run kill @s
execute as @a[gamemode=adventure] if function mg:elytra/gear_keep run function mg:elytra/gear_check
