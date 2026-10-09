# ⛏ Mini UHC Run — tick
scoreboard players add $uht mg.st 1
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..50}] run function mg:core/eliminate
execute as @e[type=minecraft:item,x=-43,y=50,z=34357,dx=86,dy=70,dz=86] run function mg:uhc2/smelt
execute if score $uht mg.st matches 1800 run tellraw @a[tag=mg.play] {"text":"⛏ PvP dans 1 minute !","color":"gold"}
execute if score $uht mg.st matches 2800 run tellraw @a[tag=mg.play] {"text":"⛏ PvP dans 10 secondes !","color":"red"}
execute if score $uht mg.st matches 3000 run function mg:uhc2/pvp
scoreboard players operation $uhq mg.st = $uht mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $uhq mg.st %= #20 mg.st
execute if score $uhq mg.st matches 0 run function mg:uhc2/second
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $n0 mg.st matches ..1 if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] if score $uht mg.st matches 6000.. run return run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
