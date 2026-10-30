# tick de la carte Scourge (minecraft:tick) : à appeler `execute in mg:floaty positioned 1274 209 181 run`
execute as @e[tag=biome,distance=0..] at @s run fillbiome ~-4 -64 ~-4 ~4 312 ~4 plains
execute as @e[tag=biome,distance=0..] at @s positioned ~6 ~ ~ run fillbiome ~-4 -64 ~-4 ~4 312 ~4 plains
execute as @e[tag=biome,distance=0..] at @s positioned ~-6 ~ ~ run fillbiome ~-4 -64 ~-4 ~4 312 ~4 plains
execute as @e[tag=biome,distance=0..] at @s positioned ~ ~ ~6 run fillbiome ~-4 -64 ~-4 ~4 312 ~4 plains
execute as @e[tag=biome,distance=0..] at @s positioned ~ ~ ~-6 run fillbiome ~-4 -64 ~-4 ~4 312 ~4 plains

#XP SET TO 0
xp set @a[tag=mg.flw] 0 levels

# SNEAK CHECK
execute as @a[tag=mg.flw] run scoreboard players operation @s sneak_last = @s sneak_time
execute as @a[tag=mg.flw] if score @s sneak_time > 0 Value run scoreboard players remove @s sneak_time 1
execute as @a[tag=mg.flw] if score @s sneak_time > 10 Value run scoreboard players set @s sneak_time 0

scoreboard players remove @a[scores={sneak_speed_timer=1..},tag=mg.flw] sneak_speed_timer 1
execute as @a[scores={sneak_speed_timer=..0},tag=mg.flw] run attribute @s minecraft:sneaking_speed base reset

# NPC CARRY

tp @e[type=minecraft:phantom,distance=0..] ~ -500 ~
execute as @a[gamemode=survival,tag=mg.flw] run gamemode adventure @s

# CEILING CHECK
execute as @a[tag=mg.flw] at @s if entity @s[y=319,dy=5000] run tellraw @s [{"text":"<?> You are too high, my Hero. Come back down."}]
execute as @a[tag=mg.flw] at @s if entity @s[y=319,dy=5000] run tp @s ~ ~-50 ~

# JUMP FLAG
execute as @a[tag=mg.flw] at @s if score @s jump_flag_buffer matches 1.. run scoreboard players set @s jump_flag 0
scoreboard players set @a[tag=mg.flw] jump_flag_buffer 0
execute as @a[tag=mg.flw] at @s if score @s jump_flag matches 1.. if score @s jump_flag_buffer matches 0 run scoreboard players set @s jump_flag_buffer 1

# MAKE ITEMS INVULNERABLE
execute as @e[type=item,distance=0..] run data merge entity @s {Invulnerable:1b}

# BELL
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:mace",count:1,components:{"minecraft:custom_name":"Knowledge & Learning"}}}] run playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] 142 59 -54 1 0.1
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:mace",count:1,components:{"minecraft:custom_name":"Knowledge & Learning"}}}] at @s run particle minecraft:enchant ~ ~1.8 ~ 0.3 0.3 0.3 0 50
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:mace",count:1,components:{"minecraft:custom_name":"Knowledge & Learning"}}}] run item replace entity @s weapon.mainhand from block 142 56 -54 container.0
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={equipment:{offhand:{id:"minecraft:mace",components:{"minecraft:custom_name":"Knowledge & Learning"}}}}] run playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] 142 59 -54 1 0.1
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={equipment:{offhand:{id:"minecraft:mace",components:{"minecraft:custom_name":"Knowledge & Learning"}}}}] at @s run particle minecraft:enchant ~ ~1.8 ~ 0.3 0.3 0.3 0 50
execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={equipment:{offhand:{id:"minecraft:mace",components:{"minecraft:custom_name":"Knowledge & Learning"}}}}] run item replace entity @s weapon.offhand from block 142 56 -54 container.0

execute as @a[scores={BellRung=1..},tag=mg.flw] run effect give @s minecraft:instant_health 3 100 true
execute as @a[scores={BellRung=1..},tag=mg.flw] run effect give @s minecraft:regeneration 3 100 true
execute as @a[scores={BellRung=1..},tag=mg.flw] run effect give @s minecraft:saturation 3 255 true
execute as @a[scores={BellRung=1..},tag=mg.flw] run effect clear @s poison
execute as @a[scores={BellRung=1..},tag=mg.flw] run effect clear @s slowness
execute as @a[scores={BellRung=1..},tag=mg.flw] run effect clear @s wither
execute as @a[scores={BellRung=1..},tag=mg.flw] run tellraw @s {"text":"A warmth pierces your heart and knits you back together completely...","italic":true,"color":"gray"}
scoreboard players set @a[tag=mg.flw] BellRung 0

# CUTSCENE
#title @a[tag=cutscene] actionbar {"text":"[🎬]","color":"white"}

# CARROT-ON-A-STICK TICK
execute if entity @a[scores={CarrotStick=1..},tag=mg.flw] run function utility:00carrot_tick

# HORN TICK
execute if entity @a[scores={horn_blow=1..},tag=mg.flw] run function utility:horn_blow_tick

# TRI-ASPECT AMULET
execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["2"]}] run effect give @s minecraft:fire_resistance 1 100 true
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["2"]}] run effect give @s minecraft:fire_resistance 1 100 true

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["3"]}] run effect give @s minecraft:fire_resistance 1 100 true
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["3"]}] run effect give @s minecraft:fire_resistance 1 100 true

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["5"]}] run effect give @s minecraft:fire_resistance 1 100 true
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["5"]}] run effect give @s minecraft:fire_resistance 1 100 true

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["4"]}] run effect give @s minecraft:water_breathing 1 100 true
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["4"]}] run effect give @s minecraft:water_breathing 1 100 true

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["6"]}] run effect give @s minecraft:water_breathing 1 100 true
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["6"]}] run effect give @s minecraft:water_breathing 1 100 true

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["7"]}] run effect clear @s minecraft:poison
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["7"]}] run effect clear @s minecraft:poison

execute as @a[tag=mg.flw] if items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["7"]}] run effect clear @s minecraft:wither
execute as @a[tag=mg.flw] if items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["7"]}] run effect clear @s minecraft:wither


# Smoke Biome Poisoning
execute as @a[tag=mg.flw] at @s unless items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["7"]}] unless items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["7"]}] if biome ~ ~ ~ minecraft:smoke run effect give @s minecraft:wither 3 0 true
execute as @a[tag=mg.flw] at @s unless items entity @s container.* carrot_on_a_stick[custom_model_data={strings:["7"]}] unless items entity @s weapon.offhand carrot_on_a_stick[custom_model_data={strings:["7"]}] if biome ~ ~ ~ minecraft:smoke run damage @s 5 minecraft:wither

# WALKING STATUE CHECK
execute as @e[tag=walking_statue,type=zombie,distance=0..] at @s if block ~ ~-0.1 ~ lime_glazed_terracotta run function utility:walking_statue_end

#SHRINK AND GROW TIMERS
execute as @a[tag=mg.flw] if score @s shrink_timer matches 0.. run scoreboard players remove @s shrink_timer 1
execute as @a[tag=mg.flw] if score @s grow_timer matches 0.. run scoreboard players remove @s grow_timer 1
execute as @a[scores={grow_timer=38},tag=mg.flw] run attribute @s scale base set 2
execute as @a[scores={grow_timer=36},tag=mg.flw] run attribute @s scale base set 3
execute as @a[scores={grow_timer=34},tag=mg.flw] run attribute @s scale base set 4
execute as @a[scores={grow_timer=32},tag=mg.flw] run attribute @s scale base set 5
execute as @a[scores={grow_timer=30},tag=mg.flw] run attribute @s scale base set 6
execute as @a[scores={grow_timer=28},tag=mg.flw] run attribute @s scale base set 7
execute as @a[scores={grow_timer=26},tag=mg.flw] run attribute @s scale base set 8
execute as @a[scores={grow_timer=25},tag=mg.flw] run attribute @s scale base set 0.1
execute as @a[scores={grow_timer=18},tag=mg.flw] run attribute @s scale base set 0.2
execute as @a[scores={grow_timer=16},tag=mg.flw] run attribute @s scale base set 0.3
execute as @a[scores={grow_timer=14},tag=mg.flw] run attribute @s scale base set 0.4
execute as @a[scores={grow_timer=12},tag=mg.flw] run attribute @s scale base set 0.5
execute as @a[scores={grow_timer=10},tag=mg.flw] run attribute @s scale base set 0.6
execute as @a[scores={grow_timer=8},tag=mg.flw] run attribute @s scale base set 0.7
execute as @a[scores={grow_timer=6},tag=mg.flw] run attribute @s scale base set 0.8
execute as @a[scores={grow_timer=4},tag=mg.flw] run attribute @s scale base set 0.9
execute as @a[scores={grow_timer=2},tag=mg.flw] run attribute @s scale base set 1


execute as @a[scores={shrink_timer=38},tag=mg.flw] run attribute @s scale base set 0.9
execute as @a[scores={shrink_timer=36},tag=mg.flw] run attribute @s scale base set 0.8
execute as @a[scores={shrink_timer=34},tag=mg.flw] run attribute @s scale base set 0.7
execute as @a[scores={shrink_timer=32},tag=mg.flw] run attribute @s scale base set 0.6
execute as @a[scores={shrink_timer=30},tag=mg.flw] run attribute @s scale base set 0.5
execute as @a[scores={shrink_timer=28},tag=mg.flw] run attribute @s scale base set 0.4
execute as @a[scores={shrink_timer=26},tag=mg.flw] run attribute @s scale base set 0.3
execute as @a[scores={shrink_timer=25},tag=mg.flw] run attribute @s scale base set 8
execute as @a[scores={shrink_timer=18},tag=mg.flw] run attribute @s scale base set 7
execute as @a[scores={shrink_timer=16},tag=mg.flw] run attribute @s scale base set 6
execute as @a[scores={shrink_timer=14},tag=mg.flw] run attribute @s scale base set 5
execute as @a[scores={shrink_timer=12},tag=mg.flw] run attribute @s scale base set 4
execute as @a[scores={shrink_timer=10},tag=mg.flw] run attribute @s scale base set 3
execute as @a[scores={shrink_timer=8},tag=mg.flw] run attribute @s scale base set 2.5
execute as @a[scores={shrink_timer=6},tag=mg.flw] run attribute @s scale base set 2
execute as @a[scores={shrink_timer=4},tag=mg.flw] run attribute @s scale base set 1.5
execute as @a[scores={shrink_timer=2},tag=mg.flw] run attribute @s scale base set 1


# WEIGHTLESS ARROW CHECK

execute as @e[type=arrow,tag=!air_arrow_countdown,distance=0..] if entity @s[nbt={weapon:{components:{"minecraft:custom_data":{air_scale:1}}}}] run scoreboard players set @s Countdown 60
execute as @e[type=arrow,tag=!air_arrow_countdown,distance=0..] if entity @s[nbt={weapon:{components:{"minecraft:custom_data":{air_scale:1}}}}] run data modify entity @s NoGravity set value 1b
execute as @e[type=arrow,distance=0..] if entity @s[nbt={weapon:{components:{"minecraft:custom_data":{air_scale:1}}}}] run tag @s add air_arrow_countdown
execute as @e[type=arrow,tag=air_arrow_countdown,distance=0..] run scoreboard players remove @s Countdown 1
execute as @e[type=arrow,tag=air_arrow_countdown,distance=0..] if score @s Countdown matches ..0 run data modify entity @s NoGravity set value 0b

# ICE CANNON CHECK

execute as @a[tag=mg.flw] if items entity @s weapon.mainhand minecraft:crossbow[minecraft:custom_data={ice_cannon:1b},minecraft:charged_projectiles=[{id:"minecraft:arrow"}]] run item replace entity @s weapon.mainhand from block -9761 272 425 container.1
execute as @a[tag=mg.flw] if items entity @s weapon.offhand minecraft:crossbow[minecraft:custom_data={ice_cannon:1b},minecraft:charged_projectiles=[{id:"minecraft:arrow"}]] run item replace entity @s weapon.offhand from block -9761 272 425 container.1

# PRETZEL ITEM CHECK

execute as @a[tag=mg.flw] if items entity @s weapon.* minecraft:spider_eye run effect give @s minecraft:night_vision 1 0 true

# VYRN'S ENFEEBLEMENT CHECK

execute as @a[tag=vyrn,tag=mg.flw] at @s if score @s shield_block matches 1.. run particle infested ^ ^1 ^1.5 0.5 0.5 0.5 0.5 50
execute as @a[tag=vyrn,tag=mg.flw] at @s if score @s shield_block matches 1.. run playsound minecraft:item.lodestone_compass.lock player @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @a[tag=vyrn,tag=mg.flw] at @s if score @s shield_block matches 1.. positioned ^ ^ ^1.5 run effect give @e[tag=enemy,distance=..1.5] minecraft:weakness 2 0 false
scoreboard players set @a[tag=mg.flw] shield_block 0

# HB2 WARD
scoreboard players add @e[type=#minecraft:hb_projectiles,distance=0..] HBDeflectCD 0
scoreboard players remove @e[type=#minecraft:hb_projectiles,scores={HBDeflectCD=1..},distance=0..] HBDeflectCD 1
execute as @a[scores={HBWard=1..},tag=mg.flw] at @s run function utility:hb_2_deflect
scoreboard players remove @a[scores={HBWard=1..},tag=mg.flw] HBWard 1

# Reduce projectile reflection cooldowns.
scoreboard players remove @e[type=#minecraft:hb_projectiles,scores={HBDeflectCD=1..},distance=0..] HBDeflectCD 1

# TIME VALUE
execute in mg:floaty store result score Time Value run time query day
execute if score Time Value matches 2999 run function music:overworld/9am
execute if score Time Value matches 8999 run function music:overworld/3pm
execute if score Time Value matches 14999 run function music:overworld/9pm
execute if score Time Value matches 20999 run function music:overworld/3am


# ENEMY STUFF
execute as @e[tag=s_elemental,distance=0..] at @s run particle block{block_state:"minecraft:sand"} ~ ~ ~ 0.2 0 0.2 0 6 force
execute as @e[tag=r_soul,distance=0..] at @s positioned ~ ~1.75 ~ run particle minecraft:totem_of_undying ^ ^ ^-0.25 0.2 0.1 0.2 0 1 normal
