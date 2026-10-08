# Course, chaque tick (@s = participant, positionné)
execute if entity @s[tag=mg.skf] run return 0
# Compteur « pas en vol plané » (négatif = délai de grâce)
scoreboard players add @s mg.skg 1
execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0
execute if entity @s[x=-8,y=235,z=27632,dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40
execute if entity @s[tag=mg.skstun] run scoreboard players set @s mg.skg -30
execute if score @s mg.skg matches 20.. run return run function mg:sky/rescue
execute unless entity @s[x=-205,y=88,z=27590,dx=410,dy=190,dz=820] run return run function mg:sky/rescue
function mg:sky/r_hud
execute if score @s mg.skr matches 0 run return run function mg:sky/rk/r0
execute if score @s mg.skr matches 1 run return run function mg:sky/rk/r1
execute if score @s mg.skr matches 2 run return run function mg:sky/rk/r2
execute if score @s mg.skr matches 3 run return run function mg:sky/rk/r3
execute if score @s mg.skr matches 4 run return run function mg:sky/rk/r4
execute if score @s mg.skr matches 5 run return run function mg:sky/rk/r5
execute if score @s mg.skr matches 6 run return run function mg:sky/rk/r6
execute if score @s mg.skr matches 7 run return run function mg:sky/rk/r7
execute if score @s mg.skr matches 8 run return run function mg:sky/rk/r8
execute if score @s mg.skr matches 9 run return run function mg:sky/rk/r9
execute if score @s mg.skr matches 10 run return run function mg:sky/rk/r10
execute if score @s mg.skr matches 11 run return run function mg:sky/rk/r11
execute if score @s mg.skr matches 12 run return run function mg:sky/rk/r12
execute if score @s mg.skr matches 13 run return run function mg:sky/rk/r13
execute if score @s mg.skr matches 14 run return run function mg:sky/rk/r14
execute if score @s mg.skr matches 15 run return run function mg:sky/rk/r15
execute if score @s mg.skr matches 16 run return run function mg:sky/rk/r16
execute if score @s mg.skr matches 17 run return run function mg:sky/rk/r17
execute if score @s mg.skr matches 18 run return run function mg:sky/rk/r18
execute if score @s mg.skr matches 19 run return run function mg:sky/rk/r19
