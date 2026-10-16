# Chaque tick (dimension) : PNJ, balises, choix, blessures, ramassages
execute as @e[type=minecraft:interaction,tag=mg.trnpc] if data entity @s interaction run function mg:terra/rpg/npc_int
execute as @e[type=minecraft:interaction,tag=mg.trbeacon] if data entity @s interaction run function mg:terra/rpg/beacon_int
execute as @a[tag=mg.tvw,scores={mg.trtk=1..}] run function mg:terra/rpg/tk
execute as @a[tag=mg.tvw,scores={mg.trdt=1..}] run function mg:terra/rpg/hurt
scoreboard players remove @a[tag=mg.tvw,scores={mg.trsc=1..}] mg.trsc 1
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trch=32}] at @s if predicate mg:sneak run function mg:terra/rpg/mod_try
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trch=64}] at @s if predicate mg:sneak run function mg:terra/rpg/mod_try
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trpk=1..}] unless predicate mg:sneak run scoreboard players set @s mg.trpk 0
execute if score $tvq5 mg.st matches 0 run function mg:terra/rpg/eggs_tick
function mg:terra/rpg/cl/tick
function mg:terra/rpg/tick2
execute as @a[tag=mg.trcine] run function mg:terra/rpg/cs/run
execute if score $tvq mg.st matches 0 as @a[tag=mg.tvw,tag=!mg.trcine,scores={mg.tron=1}] at @s run function mg:terra/rpg/ind
execute if score $tvq mg.st matches 10 as @a[tag=mg.tvw,tag=!mg.trcine,scores={mg.tron=1}] at @s run function mg:terra/rpg/ind
