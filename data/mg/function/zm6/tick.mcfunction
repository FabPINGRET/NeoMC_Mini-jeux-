# 🧟 Zombies — tick
execute as @a[tag=mg.play,tag=!mg.zdead,scores={mg.deaths=1..}] run function mg:zm6/die
execute as @a[tag=mg.play,scores={mg.zkl=1..}] run function mg:zm6/kill_points
execute as @a[tag=mg.zqrw] run function mg:zm6/qr_tick
execute positioned 8 80 39795 run function mg:zx/tick
execute as @e[type=minecraft:interaction,tag=mg.zbuy,x=-48,y=-64,z=39764,dx=112,dy=384,dz=62] if data entity @s interaction run function mg:zm6/buy
execute if score $zph mg.st matches 0 run function mg:zm6/break_tick
execute if score $zph mg.st matches 1 run function mg:zm6/round_tick
scoreboard players add $zt mg.st 1
scoreboard players operation $zq mg.st = $zt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $zq mg.st %= #20 mg.st
execute if score $zq mg.st matches 0 run function mg:zm6/second
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play,tag=!mg.zdead] unless entity @a[tag=mg.zqrw] run function mg:zm6/defeat
