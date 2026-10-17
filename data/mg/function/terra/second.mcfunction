# Chaque seconde (dans la dimension) : colonie, soins, primes, missions, population de dinosaures, carnotaure
execute unless score $tvsu mg.st matches 1.. run return 0
execute if score $tvsu mg.st matches 2 run kill @e[tag=mg.tvp,tag=!mg.tvok]
tag @e[tag=mg.tvok] remove mg.tvok
scoreboard players set $tvsu mg.st 2
scoreboard players set #4 mg.st 4
scoreboard players set #10 mg.st 10
scoreboard players set #12 mg.st 12
function mg:terra/gate
scoreboard players enable @a[tag=mg.tvw] mg.tvms
effect give @a[tag=mg.tvw] minecraft:saturation infinite 0 true
effect give @a[tag=mg.tvw,x=9,y=64,z=11,dx=14,dy=5,dz=12] minecraft:regeneration 3 2 true
execute as @a[tag=mg.tvw,scores={mg.tvkr=1..}] run function mg:terra/k_raptor
execute as @a[tag=mg.tvw,scores={mg.tvkc=1..}] run function mg:terra/k_carno
execute as @a[tag=mg.tvw,scores={mg.tvkb=1..}] run function mg:terra/k_herb
execute as @a[tag=mg.tvw,scores={mg.tvkg=1..}] run function mg:terra/k_herb
execute as @a[tag=mg.tvcar] run function mg:terra/save_pos
execute as @a[tag=mg.tvcar,tag=!mg.tvout] run function mg:terra/m1_done
execute if score $tvo1 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=1},x=62.5,y=65,z=-73.5,distance=..8] run function mg:terra/d_start_1
execute if score $tvo1 mg.st matches 1 run function mg:terra/d_tick_1
execute if score $tvo2 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=2},x=-71.5,y=70,z=6.5,distance=..8] run function mg:terra/d_start_2
execute if score $tvo2 mg.st matches 1 run function mg:terra/d_tick_2
execute if score $tvo3 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=2,mg.tvmo=3},x=30.5,y=66,z=72.5,distance=..8] run function mg:terra/d_start_3
execute if score $tvo3 mg.st matches 1 run function mg:terra/d_tick_3
scoreboard players operation $tvq2 mg.st = $tvt mg.st
scoreboard players set #40 mg.st 40
scoreboard players operation $tvq2 mg.st %= #40 mg.st
execute if score $tvq2 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/hunt_loc
execute unless entity @a[tag=mg.tvw,scores={mg.tvm=4}] run tag @e[tag=mg.tvhunt] remove mg.tvhunt
execute unless entity @e[tag=mg.tvhunt] if entity @a[tag=mg.tvw,scores={mg.tvm=4}] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn
execute store result score $tvno mg.st if entity @a[tag=mg.tvout,gamemode=adventure]
execute store result score $tvnr mg.st if entity @e[tag=mg.tvraptor,tag=!mg.trr]
# slashers de la vallée : 3 par colon dehors + 6 (20 au plus)
scoreboard players operation $tvwr mg.st = $tvno mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation $tvwr mg.st *= #3 mg.st
scoreboard players add $tvwr mg.st 6
execute if score $tvwr mg.st matches 21.. run scoreboard players set $tvwr mg.st 20
scoreboard players remove $tvpk mg.st 1
scoreboard players remove $tvcc mg.st 1
execute if score $tvno mg.st matches 1.. if score $tvpk mg.st matches ..0 if score $tvnr mg.st < $tvwr mg.st run function mg:terra/pack_try
execute if score $tvno mg.st matches 1.. if score $tvcc mg.st matches ..0 unless entity @e[tag=mg.tvcarno] run function mg:terra/carno_try
scoreboard players operation $tvq3 mg.st = $tvt mg.st
scoreboard players set #60 mg.st 60
scoreboard players operation $tvq3 mg.st %= #60 mg.st
execute if score $tvq3 mg.st matches 0 as @e[tag=mg.tvraptor,tag=!mg.tvnetted] at @s unless entity @a[tag=mg.tvout,distance=..14] if entity @a[tag=mg.tvout,gamemode=adventure,distance=..56] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..56]
scoreboard players operation $tvq4 mg.st = $tvt mg.st
scoreboard players set #400 mg.st 400
scoreboard players operation $tvq4 mg.st %= #400 mg.st
execute if score $tvq4 mg.st matches 0 run function mg:terra/herb_fill
execute if score $tvq4 mg.st matches 200 as @e[tag=mg.tvhos,tag=!mg.tvhunt] at @s unless entity @a[tag=mg.tvw,distance=..80] run tp @s ~ -400 ~
execute as @e[tag=mg.tvhos,x=-28,y=58,z=-28,dx=56,dy=30,dz=56] at @s run function mg:terra/zap
execute as @e[tag=mg.tvherb,x=-28,y=58,z=-28,dx=56,dy=30,dz=56] unless predicate mg:has_passenger run tp @s @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1]
execute as @e[tag=mg.tvbrach] if predicate mg:has_passenger unless items entity @s saddle minecraft:saddle run function mg:terra/brach_saddle
execute as @e[tag=mg.tvcarno,tag=!mg.tvnetted] at @s unless entity @s[x=-28,y=58,z=-28,dx=56,dy=30,dz=56] run function mg:terra/carno_smash
execute unless entity @e[tag=mg.tvcarno] run bossbar set mg:tvcarno players
execute as @e[tag=mg.tvhunt,limit=1] at @s run function mg:terra/carno_bar
execute unless entity @e[tag=mg.tvhunt] as @e[tag=mg.tvcarno,limit=1] at @s run function mg:terra/carno_bar
execute store result score $tvr mg.st run random value 0..29
execute if score $tvr mg.st matches 0..9 as @e[tag=mg.tvraptor,sort=random,limit=1] at @s run playsound minecraft:entity.fox.screech hostile @a ~ ~ ~ 1.2 0.75
execute if score $tvr mg.st matches 10..12 as @e[tag=mg.tvcarno,sort=random,limit=1] at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.6
execute if score $tvr mg.st matches 13..15 as @e[tag=mg.tvbrach,sort=random,limit=1] at @s run playsound minecraft:entity.camel.ambient neutral @a ~ ~ ~ 2.5 0.45
execute if score $tvr mg.st matches 16..17 as @e[tag=mg.tvpachy,sort=random,limit=1] at @s run playsound minecraft:entity.goat.ambient neutral @a ~ ~ ~ 1.2 0.6
execute if score $tvr mg.st matches 18 as @a[tag=mg.tvout,sort=random,limit=1] at @s run playsound minecraft:entity.parrot.ambient ambient @s ~ ~8 ~ 0.6 0.8
# RPG (régions, campagne, boss) ; dinosaures d'une session précédente restés dans une zone non chargée : retirés
function mg:terra/rpg/second
execute as @e[tag=mg.tvd,tag=!mg.trmount] unless score @s mg.tvses = $tvses mg.st run tp @s ~ -400 ~
