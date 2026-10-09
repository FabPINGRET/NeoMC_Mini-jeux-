# 🏰 The Towers — tick
scoreboard players add $twt mg.st 1
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:tower/respawn
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..68}] run function mg:tower/respawn
fill -38 77 20799 -36 81 20801 minecraft:air
fill 36 77 20799 38 81 20801 minecraft:air
execute as @a[tag=mg.play,team=mg_blue,x=-38,y=76,z=20799,dx=2,dy=3,dz=2] run function mg:tower/score_blue
execute as @a[tag=mg.play,team=mg_red,x=36,y=76,z=20799,dx=2,dy=3,dz=2] run function mg:tower/score_red
scoreboard players operation $twq mg.st = $twt mg.st
scoreboard players set #300 mg.st 300
scoreboard players operation $twq mg.st %= #300 mg.st
execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 20800.5 {Item:{id:"minecraft:arrow",count:4}}
execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 20800.5 {Item:{id:"minecraft:golden_apple",count:1}}
execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 20800.5 {Item:{id:"minecraft:white_terracotta",count:16}}
execute if score $twt mg.st matches 10800 run tellraw @a[tag=mg.play] {"text":"🏰 Plus qu'une minute !","color":"gold"}
execute if score $state mg.st matches 2 if score $twt mg.st matches 12000.. run function mg:tower/timeout
execute store result score $twr mg.st if entity @a[tag=mg.play,team=mg_red]
execute store result score $twb mg.st if entity @a[tag=mg.play,team=mg_blue]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $twr mg.st matches 0 if score $twb mg.st matches 1.. run return run function mg:core/win_blue
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $twb mg.st matches 0 if score $twr mg.st matches 1.. run return run function mg:core/win_red
execute if score $state mg.st matches 2 if score $twb mg.st matches 0 if score $twr mg.st matches 0 run function mg:core/draw
