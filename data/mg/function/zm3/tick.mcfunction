# 🧟 Zombies — tick
execute as @a[tag=mg.play,tag=!mg.zdead,scores={mg.deaths=1..}] run function mg:zm3/die
execute as @a[tag=mg.play,scores={mg.zk=1..}] run function mg:zm3/kill_points
execute as @e[type=minecraft:interaction,tag=mg.zbuy] if data entity @s interaction run function mg:zm3/buy
execute if score $zph mg.st matches 0 run function mg:zm3/break_tick
execute if score $zph mg.st matches 1 run function mg:zm3/round_tick
scoreboard players add $zt mg.st 1
scoreboard players operation $zq mg.st = $zt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $zq mg.st %= #20 mg.st
execute if score $zq mg.st matches 0 run function mg:zm3/second
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play,tag=!mg.zdead] run function mg:zm3/defeat
