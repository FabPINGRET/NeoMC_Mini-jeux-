# Monstres apparus dans la zone s (marqués mg.trnew) : PV et dégâts ×3, une chance sur 10 d'élite
execute as @e[tag=mg.trnew] run attribute @s minecraft:max_health modifier add mg:trzone 2 add_multiplied_base
execute as @e[tag=mg.trnew] run attribute @s minecraft:attack_damage modifier add mg:trzone 1.2 add_multiplied_base
execute as @e[tag=mg.trnew] store result entity @s Health float 1 run attribute @s minecraft:max_health get
scoreboard players set @e[tag=mg.trnew] mg.trzm 6
execute if predicate mg:tv_c10 as @e[tag=mg.trnew,tag=mg.tvhos,sort=random,limit=1] run function mg:terra/rpg/elite
