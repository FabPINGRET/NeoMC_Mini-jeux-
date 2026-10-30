summon rabbit -10340 90 446 {CustomNameVisible:0b,PersistenceRequired:1b,Health:12f,RabbitType:99,Tags:["pretzel_rabbit","enemy","new"],CustomName:"Rabbit",attributes:[{id:"minecraft:max_health",base:12}]}

execute store result score pretzel_rabbit_name Value run random value 1..12
execute if score pretzel_rabbit_name Value matches 1 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Glrr"
execute if score pretzel_rabbit_name Value matches 2 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Jimothy O'Boole"
execute if score pretzel_rabbit_name Value matches 3 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Sur Fritzel"
execute if score pretzel_rabbit_name Value matches 4 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Phillipe"
execute if score pretzel_rabbit_name Value matches 5 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Iendar"
execute if score pretzel_rabbit_name Value matches 6 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Scorzonera Plunt"
execute if score pretzel_rabbit_name Value matches 7 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Mangelwurzel Plunt-Vulgaris"
execute if score pretzel_rabbit_name Value matches 8 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Yung Crimple"
execute if score pretzel_rabbit_name Value matches 9 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Skli"
execute if score pretzel_rabbit_name Value matches 10 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Yahn Buggenhichler"
execute if score pretzel_rabbit_name Value matches 11 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Snarthity Russet Tuber O’Summ"
execute if score pretzel_rabbit_name Value matches 12 run data modify entity @n[tag=pretzel_rabbit,tag=new,distance=0..] CustomName set value "Parsnipius BerDangleton"

tag @e[tag=pretzel_rabbit,distance=0..] remove new

playsound minecraft:entity.rabbit.attack hostile @a[tag=mg.flw] -10340 89 446 2 0.1
particle item{item:"carrot"} -10340 90.5 446 0.3 0.3 0.3 0.2 100

schedule function floaty:sched/boss/mini/pretzel/schedule_attack 3s
