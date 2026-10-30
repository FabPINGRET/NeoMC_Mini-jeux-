summon marker ^ ^ ^10 {NoGravity:1b,Silent:1b,Tags:["boss_ta_future_loc"]}
execute at @n[tag=boss_ta_face_loc,distance=0..] run summon marker ~ ~ ~ {NoGravity:1b,Silent:1b,Tags:["boss_ta_pred_origin","new"]}
execute as @n[tag=boss_ta_pred_origin,tag=new,distance=0..] at @s facing entity @n[tag=boss_ta_future_loc,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
tag @n[tag=boss_ta_pred_origin,tag=new,distance=0..] remove new
kill @n[tag=boss_ta_future_loc,distance=0..]
