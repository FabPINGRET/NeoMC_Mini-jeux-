summon marker -12384 124 380 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12366 124 373 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12359 124 355 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12366 124 337 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12384 124 330 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12402 124 337 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12409 124 355 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}
summon marker -12402 124 373 {NoGravity:1b,Silent:1b,Tags:["wv_lordsword_option"]}

tag @e[tag=wv_lord,tag=flame,distance=0..] add wv_lordsword_chosen

scoreboard players set lordsword_mode bool 0

execute as @n[tag=wv_lordsword_chosen,distance=0..] at @s at @n[tag=wv_lordsword_option,distance=0..] run function boss:final/virus/model/lord_sword/flame
execute as @n[tag=wv_lord,tag=flame,distance=0..] at @s run playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] ~ ~ ~ 1 1.4 1
execute as @n[tag=wv_lord,tag=flame,distance=0..] at @s run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> This thing looks tough, try using my ","color":"white"},{"text":"power","color":"green"},{"text":" as a blade against it. Once you're wielding a Lord's power, you can unleash it by ","color":"white"},{"text":"sneaking","color":"light_purple"},{"text":". We seven will forge blades of power for you as fast as we can!","color":"white"}]
execute as @n[tag=wv_lord,tag=flame,distance=0..] at @s run tag @s add override
schedule function floaty:sched/boss/final/virus/lord_end_override 20t replace

tag @e[tag=wv_lord,distance=0..] remove wv_lordsword_chosen
kill @e[tag=wv_lordsword_option,distance=0..]
