execute unless entity @a[tag=bossroom,tag=targeted,tag=mg.flw] run tag @r[tag=bossroom,gamemode=!spectator,tag=mg.flw] add targeted

# 1 - GUN
# 2 - SMACK
# 3 - PUNCH
# 4 - SUMMON
# 5 - BREATH
# 6 - CRYSTAL
# 7 - VORTEX

execute unless score boss:st_lastattack Value matches 1 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","1","exclude"]}
execute unless score boss:st_lastattack Value matches 2 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","2","exclude"]}
execute unless score boss:st_lastattack Value matches 2 if entity @e[tag=st_boss_walking_statue,distance=0..] run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","2","exclude"]}
execute unless score boss:st_lastattack Value matches 3 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","3","exclude"]}
execute unless score boss:st_lastattack Value matches 3 if entity @e[tag=st_boss_statue,distance=0..] run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","3","exclude"]}
execute unless score boss:st_lastattack Value matches 4 unless entity @e[tag=knucklehead,distance=0..] run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","4","exclude"]}
execute unless score boss:st_lastattack Value matches 4 unless entity @e[tag=knucklehead,distance=0..] run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","4","exclude"]}
execute unless score boss:st_lastattack Value matches 5 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","5","exclude"]}
execute unless score boss:st_lastattack Value matches 6 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","6","exclude"]}
execute unless score boss:st_lastattack Value matches 7 run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","7","exclude"]}

execute unless entity @e[tag=st_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -10472 -49 -383 {Tags:["st_attack_temp","1","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=st_attack_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=st_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=st_attack_temp,tag=1,distance=0..] as @e[tag=st_hand_loc,sort=random,limit=1,distance=0..] run function boss:7/attack/gun
execute if entity @e[tag=st_attack_temp,tag=2,distance=0..] as @e[tag=st_hand_loc,sort=random,limit=1,distance=0..] run function boss:7/attack/smack 
execute if entity @e[tag=st_attack_temp,tag=3,distance=0..] as @e[tag=st_hand_loc,sort=random,limit=1,distance=0..] run function boss:7/attack/punch 
execute if entity @e[tag=st_attack_temp,tag=4,distance=0..] as @e[tag=st_hand_loc,distance=0..] run function boss:7/attack/summon
execute if entity @e[tag=st_attack_temp,tag=5,distance=0..] run function boss:7/attack/breath
execute if entity @e[tag=st_attack_temp,tag=6,distance=0..] run function boss:7/attack/crystal
execute if entity @e[tag=st_attack_temp,tag=7,distance=0..] as @e[tag=st_hand_loc,distance=0..] run function boss:7/attack/vortex

execute if entity @e[tag=st_attack_temp,tag=1,distance=0..] run scoreboard players set boss:st_lastattack Value 1
execute if entity @e[tag=st_attack_temp,tag=2,distance=0..] run scoreboard players set boss:st_lastattack Value 2
execute if entity @e[tag=st_attack_temp,tag=3,distance=0..] run scoreboard players set boss:st_lastattack Value 3
execute if entity @e[tag=st_attack_temp,tag=4,distance=0..] run scoreboard players set boss:st_lastattack Value 4
execute if entity @e[tag=st_attack_temp,tag=5,distance=0..] run scoreboard players set boss:st_lastattack Value 5
execute if entity @e[tag=st_attack_temp,tag=6,distance=0..] run scoreboard players set boss:st_lastattack Value 6
execute if entity @e[tag=st_attack_temp,tag=7,distance=0..] run scoreboard players set boss:st_lastattack Value 7

kill @e[type=minecraft:area_effect_cloud,tag=st_attack_temp,distance=0..]
