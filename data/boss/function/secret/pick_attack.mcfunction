#COLORBALL
#KEYSTARS
#SUMMON
#BOMBS
#FLOOR
#TURRETS
#KEYRING SPAWN
#KEYRING LAUNCH

execute if score sc_boss_countdown Value matches 3.. unless score keygod_lastattack Value matches 1 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","1","exclude"]}
execute if score sc_boss_countdown Value matches 4.. unless score keygod_lastattack Value matches 1 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","1","exclude"]}
execute if score sc_boss_countdown Value matches 5.. unless score keygod_lastattack Value matches 1 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","1","exclude"]}
execute if score sc_boss_countdown Value matches 6.. unless score keygod_lastattack Value matches 1 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","1","exclude"]}
execute if score sc_boss_countdown Value matches 7.. unless score keygod_lastattack Value matches 1 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","1","exclude"]}
execute unless score keygod_lastattack Value matches 2 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","2","exclude"]}
execute if score sc_boss_color bool matches 0 unless entity @e[tag=illock,tag=red,distance=0..] unless score keygod_lastattack Value matches 3 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","3","exclude"]}
execute if score sc_boss_color bool matches 1 unless entity @e[tag=illock,tag=blue,distance=0..] unless score keygod_lastattack Value matches 3 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","3","exclude"]}
execute unless score keygod_lastattack Value matches 4 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","4","exclude"]}
execute unless score keygod_lastattack Value matches 5 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","5","exclude"]}
execute unless score keygod_lastattack Value matches 6 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","6","exclude"]}
execute if entity @e[tag=sc_keyring_pos,distance=0..] unless score keygod_lastattack Value matches 7 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","7","exclude"]}
execute if entity @e[tag=sc_keyring_pos,distance=0..] unless score keygod_lastattack Value matches 7 run summon area_effect_cloud -12471 180 -171 {Tags:["keygod_attack_temp","7","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=keygod_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=keygod_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=keygod_attack_temp,tag=1,distance=0..] run function boss:secret/attack/do_colorball
execute if entity @e[tag=keygod_attack_temp,tag=1,distance=0..] run scoreboard players set keygod_lastattack Value 1
execute if entity @e[tag=keygod_attack_temp,tag=2,distance=0..] run function boss:secret/attack/do_keystars
execute if entity @e[tag=keygod_attack_temp,tag=2,distance=0..] run scoreboard players set keygod_lastattack Value 2
execute if entity @e[tag=keygod_attack_temp,tag=3,distance=0..] run function boss:secret/attack/do_summon
execute if entity @e[tag=keygod_attack_temp,tag=3,distance=0..] run scoreboard players set keygod_lastattack Value 3
execute if entity @e[tag=keygod_attack_temp,tag=4,distance=0..] run function boss:secret/attack/do_bombs
execute if entity @e[tag=keygod_attack_temp,tag=4,distance=0..] run scoreboard players set keygod_lastattack Value 4
execute if entity @e[tag=keygod_attack_temp,tag=5,distance=0..] run function boss:secret/attack/do_floor
execute if entity @e[tag=keygod_attack_temp,tag=5,distance=0..] run scoreboard players set keygod_lastattack Value 5
execute if entity @e[tag=keygod_attack_temp,tag=6,distance=0..] run function boss:secret/attack/do_turrets
execute if entity @e[tag=keygod_attack_temp,tag=6,distance=0..] run scoreboard players set keygod_lastattack Value 6
execute if entity @e[tag=keygod_attack_temp,tag=7,distance=0..] run function boss:secret/attack/do_ring_launch
execute if entity @e[tag=keygod_attack_temp,tag=7,distance=0..] run scoreboard players set keygod_lastattack Value 7


kill @e[type=minecraft:area_effect_cloud,tag=keygod_attack_temp,distance=0..]

scoreboard players add sc_boss_countdown Value 1
