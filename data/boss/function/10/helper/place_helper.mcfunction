function boss:10/rand_spread

execute positioned -11830 277 330 run tag @e[tag=boss_ta_rand,sort=nearest,limit=45,distance=0..] add boss_ta_helper_loc
execute positioned -11830 277 330 run tag @e[tag=boss_ta_rand,sort=nearest,limit=40,distance=0..] remove boss_ta_helper_loc

execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tag @e[tag=boss_ta_helper_loc,sort=nearest,limit=4,distance=0..] remove boss_ta_helper_loc

execute as @n[tag=boss_ta_helper_loc,distance=0..] at @s run summon marker ~ 217 ~ {NoGravity:1b,Silent:1b,Tags:["boss_ta_helper"]}

tag @e[tag=boss_ta_rand,distance=0..] remove boss_ta_helper_loc

execute if score boss:ta BossHealth matches 6 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> You must lure that fiend over to the white smoke... I can force its form to dissipate..."}
execute if score boss:ta BossHealth matches 3..5 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> You must lure it over here now..."}
execute if score boss:ta BossHealth matches 2 at @n[tag=boss_ta_helper,distance=0..] run tellraw @a[tag=mg.flw] {"text":"<?> You must lure it over here now... I'm sorry..."}

execute at @n[tag=boss_ta_helper,distance=0..] run playsound minecraft:entity.allay.ambient_without_item neutral @a[tag=mg.flw] ~ ~ ~ 5 0.5 
