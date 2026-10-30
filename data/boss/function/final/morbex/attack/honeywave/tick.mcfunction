execute as @e[tag=morbex_honey,distance=0..] at @s run tp @s ~ ~2 ~
execute as @e[tag=morbex_honey,distance=0..] at @s store result score @s Value run data get entity @n[tag=morbex_honey,distance=0..] Pos[1]
execute as @e[tag=morbex_honey,distance=0..] at @s if score @s Value matches 134.. run fill ~-1 134 ~-1 ~1 134 ~1 honey_block replace #minecraft:hb_passthrough
execute as @e[tag=morbex_honey,distance=0..] at @s if score @s Value matches 134.. run playsound minecraft:item.bottle.fill_dragonbreath hostile @a[tag=mg.flw] ~ 123 ~ 3 1.4
execute as @e[tag=morbex_honey,distance=0..] at @s if score @s Value matches 134.. run kill @s
