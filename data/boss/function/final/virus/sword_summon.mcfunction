summon marker -12384 124 380 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12366 124 373 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12359 124 355 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12366 124 337 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12384 124 330 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12402 124 337 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12409 124 355 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12402 124 373 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}

tag @e[tag=wv_lord,limit=1,sort=random,distance=0..] add wv_lordsword_chosen

scoreboard players set lordsword_mode bool 0

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=flame] run function boss:final/virus/model/lord_sword/flame
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=forest] run function boss:final/virus/model/lord_sword/forest
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=spores] run function boss:final/virus/model/lord_sword/spores
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=stone] run function boss:final/virus/model/lord_sword/stone
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=ice] run function boss:final/virus/model/lord_sword/ice
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=water] run function boss:final/virus/model/lord_sword/water
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] if entity @s[tag=valor] run function boss:final/virus/model/lord_sword/valor

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=flame] run playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] ~ ~ ~ 1 1.4 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=flame] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> Sword for you, hero!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=flame] run tag @e[tag=wv_lord,tag=flame,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=forest] run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=forest] run playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] ~ ~ ~ 1 1 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=forest] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Hurl this at it!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=forest] run tag @e[tag=wv_lord,tag=forest,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=spores] run playsound minecraft:entity.silverfish.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=spores] run playsound minecraft:entity.puffer_fish.blow_up neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=spores] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> Hit it with the power of spores!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=spores] run tag @e[tag=wv_lord,tag=spores,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=stone] run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=stone] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Take this!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=stone] run tag @e[tag=wv_lord,tag=stone,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=ice] run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=ice] run playsound minecraft:block.trial_spawner.spawn_item_begin neutral @a[tag=mg.flw] ~ ~ ~ 1 1 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=ice] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> Use this sword, friend!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=ice] run tag @e[tag=wv_lord,tag=ice,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=water] run playsound minecraft:entity.drowned.ambient_water neutral @a[tag=mg.flw] ~ ~ ~ 1 2 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=water] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> Over here, a blade of water!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=water] run tag @e[tag=wv_lord,tag=water,distance=0..] add override

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=valor] run playsound minecraft:entity.shulker.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2 1
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=valor] run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Valor","color":"yellow"},{"text":"> Launch this at its stinky face!","color":"white"}]
execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s if entity @s[tag=valor] run tag @e[tag=wv_lord,tag=valor,distance=0..] add override

schedule function floaty:sched/boss/final/virus/lord_end_override 20t replace

tag @e[tag=wv_lord,distance=0..] remove wv_lordsword_chosen
kill @e[tag=wv_lordsword_option,distance=0..]
