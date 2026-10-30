execute if score banana_of_temptation bool matches 0 run damage @a[sort=nearest,limit=1,gamemode=!spectator,tag=mg.flw] 10000 minecraft:indirect_magic by @e[tag=banana_of_temptation,limit=1,distance=0..]

execute if score banana_of_temptation bool matches 1 as @p[gamemode=!spectator,tag=mg.flw] at @s rotated ~ 0 positioned ^ ^ ^0.1 run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["b_of_t_check","front"]}
execute if score banana_of_temptation bool matches 1 as @p[gamemode=!spectator,tag=mg.flw] at @s rotated ~ 0 positioned ^ ^ ^-0.1 run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["b_of_t_check","back"]}
execute if score banana_of_temptation bool matches 1 positioned -193 45 -146 run kill @n[tag=b_of_t_check,distance=0..]
execute if score banana_of_temptation bool matches 1 if entity @e[tag=b_of_t_check,tag=back,distance=0..] run damage @a[sort=nearest,limit=1,gamemode=!spectator,tag=mg.flw] 10000 minecraft:indirect_magic by @e[tag=banana_of_temptation,limit=1,distance=0..]

execute if score banana_of_temptation bool matches 1 if entity @e[tag=b_of_t_check,tag=front,distance=0..] run give @p[gamemode=!spectator,tag=mg.flw] flint[custom_model_data={strings:["30"]},custom_name={"bold":true,"color":"yellow","text":"The Banana of Temptation"},lore=["It's the most dangerous","object you've ever held..."]] 1
execute if score banana_of_temptation bool matches 1 if entity @e[tag=b_of_t_check,tag=front,distance=0..] run setblock -190 39 -149 air
execute if score banana_of_temptation bool matches 1 if entity @e[tag=b_of_t_check,tag=front,distance=0..] run fill -191 45 -147 -193 48 -145 air
execute if score banana_of_temptation bool matches 1 if entity @e[tag=b_of_t_check,tag=front,distance=0..] run setblock -192 45 -146 minecraft:polished_deepslate_wall

kill @e[tag=b_of_t_check,distance=0..]
