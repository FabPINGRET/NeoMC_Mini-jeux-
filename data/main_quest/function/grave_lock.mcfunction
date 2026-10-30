execute as @p[gamemode=!spectator,tag=mg.flw] if items entity @s weapon.mainhand minecraft:trial_key run tag @s add grave_key

execute as @p[tag=mg.flw] if entity @s[tag=!grave_key] run tellraw @s [{"text":"This can only be unlocked with a "},{"text":"Grave Key","color":"yellow","bold":true}]

execute as @p[tag=mg.flw] if entity @s[tag=grave_key] run setblock ~ ~1 ~ raw_gold_block
execute as @p[tag=mg.flw] if entity @s[tag=grave_key] run setblock ~ ~1 ~-1 air 
execute as @p[tag=mg.flw] if entity @s[tag=grave_key] run setblock ~ ~2 ~ minecraft:black_candle[lit=true,candles=4]
execute as @p[tag=mg.flw] if entity @s[tag=grave_key] run clear @s minecraft:trial_key 1

execute if block 9999 59 246 minecraft:raw_gold_block if block 9995 59 246 minecraft:raw_gold_block if block 9999 59 242 minecraft:raw_gold_block if block 9995 59 242 minecraft:raw_gold_block run setblock 9997 58 244 air
execute if block 9999 59 246 minecraft:raw_gold_block if block 9995 59 246 minecraft:raw_gold_block if block 9999 59 242 minecraft:raw_gold_block if block 9995 59 242 minecraft:raw_gold_block run fill 9998 64 243 9996 62 243 minecraft:raw_gold_block
execute if block 9999 59 246 minecraft:raw_gold_block if block 9995 59 246 minecraft:raw_gold_block if block 9999 59 242 minecraft:raw_gold_block if block 9995 59 242 minecraft:raw_gold_block run playsound minecraft:zelda.secret master @a[tag=mg.flw] 9997 58 244 1 1 1
execute if block 9999 59 246 minecraft:raw_gold_block if block 9995 59 246 minecraft:raw_gold_block if block 9999 59 242 minecraft:raw_gold_block if block 9995 59 242 minecraft:raw_gold_block run advancement grant @a[tag=mg.flw] only main_quest:quest_10
execute if block 9999 59 246 minecraft:raw_gold_block if block 9995 59 246 minecraft:raw_gold_block if block 9999 59 242 minecraft:raw_gold_block if block 9995 59 242 minecraft:raw_gold_block run scoreboard players set $fla28 mg.fla 1

tag @a[tag=mg.flw] remove grave_key
