scoreboard players add pretzel_emerald_clock Value 1

execute if score pretzel_emerald_clock Value matches 15 as @e[tag=pretzel_emerald_villager,sort=random,limit=1,distance=0..] at @s run function boss:mini/pretzel/utility/emerald_drop
execute if score pretzel_emerald_clock Value matches 15 run scoreboard players set pretzel_emerald_clock Value 0

execute as @e[tag=pretzel_emerald_display,distance=0..] at @s at @n[tag=pretzel_emerald_bomb,distance=0..] run tp @s ~ ~ ~

execute as @e[tag=pretzel_emerald_bomb,distance=0..] at @s unless block ~ ~-0.1 ~ air run scoreboard players add @s Value 1
execute as @e[tag=pretzel_emerald_bomb,distance=0..] at @s if block ~ ~-0.1 ~ air run particle minecraft:firework ~ ~ ~ 0.1 0 0.1 0 1


execute as @e[tag=pretzel_emerald_bomb,distance=0..] at @s if score @s Value matches 3 run summon firework_rocket ~ ~ ~ {LifeTime:0,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{explosions:[{shape:"burst",has_twinkle:true,has_trail:true,colors:[I;3710477],fade_colors:[I;16777215]}]}}}}
execute as @e[tag=pretzel_emerald_bomb,distance=0..] at @s if score @s Value matches 3 run kill @n[tag=pretzel_emerald_display,distance=0..]
execute as @e[tag=pretzel_emerald_bomb,distance=0..] at @s if score @s Value matches 3 run kill @s
