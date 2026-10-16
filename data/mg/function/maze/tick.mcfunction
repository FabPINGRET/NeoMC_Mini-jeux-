# 🌀 Labyrinthe — tick
scoreboard players add $jtm mg.st 1
execute as @a[tag=mg.play,gamemode=adventure,x=50,y=64,z=41096,dx=6,dy=6,dz=7] run return run function mg:maze/arrive
execute as @e[type=minecraft:marker,tag=mg.jbm] at @s run function mg:maze/bonus_tick
execute as @e[type=minecraft:marker,tag=mg.jtr] at @s as @a[tag=mg.play,gamemode=adventure,distance=..0.9] run function mg:maze/trap
execute as @e[type=minecraft:marker,tag=mg.jtp] at @s as @a[tag=mg.play,gamemode=adventure,distance=..0.8,scores={mg.jc=0}] run function mg:maze/tele
scoreboard players remove @a[scores={mg.jc=1..}] mg.jc 1
execute as @a[tag=mg.play,scores={mg.je=1..}] run function mg:maze/eagle_tick
scoreboard players operation $jq mg.st = $jtm mg.st
scoreboard players set #160 mg.st 160
scoreboard players operation $jq mg.st %= #160 mg.st
execute if score $jq mg.st matches 0 run function mg:maze/gates
scoreboard players set #20 mg.st 20
scoreboard players operation $jq mg.st = $jtm mg.st
scoreboard players operation $jq mg.st %= #20 mg.st
execute if score $jq mg.st matches 0 run function mg:maze/second
execute if score $state mg.st matches 2 if score $jtm mg.st matches 6000.. run function mg:maze/time_up
