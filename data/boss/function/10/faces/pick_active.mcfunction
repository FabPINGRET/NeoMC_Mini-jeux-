scoreboard players set boss_ta_active_face Value 0
scoreboard players set boss_ta_last_face Value 0

execute unless score boss_ta_last_face Value matches 1 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","1","exclude"]}
execute unless score boss_ta_last_face Value matches 2 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","2","exclude"]}
execute unless score boss_ta_last_face Value matches 3 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","3","exclude"]}
execute unless score boss_ta_last_face Value matches 4 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","4","exclude"]}
execute unless score boss_ta_last_face Value matches 5 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","5","exclude"]}
execute unless score boss_ta_last_face Value matches 6 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","6","exclude"]}
execute unless score boss_ta_last_face Value matches 7 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","7","exclude"]}
execute unless score boss_ta_last_face Value matches 8 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","8","exclude"]}
execute unless score boss_ta_last_face Value matches 9 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","9","exclude"]}
execute unless score boss_ta_last_face Value matches 10 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","10","exclude"]}
execute unless score boss_ta_last_face Value matches 11 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","11","exclude"]}
execute unless score boss_ta_last_face Value matches 12 run summon area_effect_cloud -11830 200 330 {Tags:["ta_face_temp","12","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=ta_face_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=ta_face_temp,tag=exclude,distance=0..]

execute if entity @e[tag=ta_face_temp,tag=1,distance=0..] run scoreboard players set boss_ta_active_face Value 1
execute if entity @e[tag=ta_face_temp,tag=2,distance=0..] run scoreboard players set boss_ta_active_face Value 2
execute if entity @e[tag=ta_face_temp,tag=3,distance=0..] run scoreboard players set boss_ta_active_face Value 3
execute if entity @e[tag=ta_face_temp,tag=4,distance=0..] run scoreboard players set boss_ta_active_face Value 4
execute if entity @e[tag=ta_face_temp,tag=5,distance=0..] run scoreboard players set boss_ta_active_face Value 5
execute if entity @e[tag=ta_face_temp,tag=6,distance=0..] run scoreboard players set boss_ta_active_face Value 6
execute if entity @e[tag=ta_face_temp,tag=7,distance=0..] run scoreboard players set boss_ta_active_face Value 7
execute if entity @e[tag=ta_face_temp,tag=8,distance=0..] run scoreboard players set boss_ta_active_face Value 8
execute if entity @e[tag=ta_face_temp,tag=9,distance=0..] run scoreboard players set boss_ta_active_face Value 9
execute if entity @e[tag=ta_face_temp,tag=10,distance=0..] run scoreboard players set boss_ta_active_face Value 10
execute if entity @e[tag=ta_face_temp,tag=11,distance=0..] run scoreboard players set boss_ta_active_face Value 11
execute if entity @e[tag=ta_face_temp,tag=12,distance=0..] run scoreboard players set boss_ta_active_face Value 12

kill @e[type=minecraft:area_effect_cloud,tag=ta_face_temp,distance=0..]

scoreboard players operation boss_ta_last_face Value = boss_ta_active_face Value
