# 🦖 Terra Nova : chaque tick tant qu'un joueur y est (contexte : dimension mg:terranova)
scoreboard players add $tvt mg.st 1
scoreboard players operation $tvq mg.st = $tvt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $tvq mg.st %= #20 mg.st
execute as @a[tag=mg.tvw,scores={mg.tvq=1..}] at @s run function mg:terra/use
scoreboard players reset @a[scores={mg.tvq=1..}] mg.tvq
execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:1}] at @s run function mg:terra/prod_hit
execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:12}] at @s run function mg:terra/prod_hit
execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:13}] at @s run function mg:terra/prod_hit
scoreboard players reset @a[scores={mg.tvdd=1..}] mg.tvdd
scoreboard players remove @a[tag=mg.tvw,scores={mg.tvh=1..}] mg.tvh 15
scoreboard players set @a[tag=mg.tvw,scores={mg.tvh=..-1}] mg.tvh 0
execute as @a[tag=mg.tvoh,scores={mg.tvh=0}] run function mg:terra/cooled
scoreboard players remove @a[tag=mg.tvw,scores={mg.tvcd=1..}] mg.tvcd 1
scoreboard players remove @a[tag=mg.tvw,scores={mg.tvsc=1..}] mg.tvsc 1
scoreboard players remove @a[tag=mg.tvw,scores={mg.tval=1..}] mg.tval 1
execute as @a[tag=mg.tvw,scores={mg.tvhm=1..}] run function mg:terra/home_tick
execute as @a[tag=mg.tvw,scores={mg.tvms=1..}] run function mg:terra/mission_cmd
execute as @e[type=minecraft:interaction,tag=mg.tvbuy] if data entity @s interaction run function mg:terra/buy_int
execute as @e[type=minecraft:interaction,tag=mg.tvboard] if data entity @s interaction run function mg:terra/board_int
execute as @e[type=minecraft:item_display,tag=mg.tvpdi] at @s run tp @s ~ ~ ~ ~4 ~
scoreboard players operation $tvq3b mg.st = $tvt mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation $tvq3b mg.st %= #3 mg.st
execute as @e[tag=mg.tvd] at @s if entity @a[tag=mg.tvw,distance=..32] run function mg:terra/dsync
execute as @e[tag=mg.tvd] if score @s mg.tvph = $tvq3b mg.st at @s unless entity @a[tag=mg.tvw,distance=..32] if entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync
execute if score $tvq mg.st matches 0 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync
execute if score $tvq mg.st matches 10 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync
scoreboard players remove @e[tag=mg.tvd,scores={mg.tvst=1..}] mg.tvst 1
execute as @e[tag=mg.tvnetted,scores={mg.tvst=..0}] run function mg:terra/unnet
execute as @e[type=minecraft:marker,tag=mg.tvtrap] at @s if entity @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4] run function mg:terra/trap_fire
scoreboard players operation $tvq5 mg.st = $tvt mg.st
scoreboard players set #5 mg.st 5
scoreboard players operation $tvq5 mg.st %= #5 mg.st
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1},tag=!mg.tvcar] at @s if predicate mg:sneak run function mg:terra/crate_try
execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1,mg.tvmp=1..},tag=!mg.tvcar] unless predicate mg:sneak run scoreboard players set @s mg.tvmp 0
execute as @a[tag=mg.tvcar] at @s run function mg:terra/carry_tick
execute as @a[tag=mg.tvw,scores={mg.deaths=1..}] run function mg:terra/died
particle minecraft:reverse_portal -11.5 67 16.5 0.05 1.3 1.0 0.02 4
execute as @a[tag=mg.tvw] at @s if entity @e[type=minecraft:marker,tag=mg.tvexit,distance=..1.4] in minecraft:overworld run function mg:terra/leave
execute if score $tvq mg.st matches 0 run function mg:terra/second
execute if score $tvq mg.st matches 5 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one
execute if score $tvq mg.st matches 15 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one
function mg:terra/rpg/tick
