# Pilotage du kart de @s (chaque tick)
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 run function mg:kart/remount
execute on vehicle at @s run function mg:kart/probe
execute if score $kwa mg.st matches 1 run return run function mg:kart/rescue
execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue

# Touches (plus de commandes une fois la course finie)
scoreboard players set $kf mg.st 0
scoreboard players set $kb mg.st 0
scoreboard players set $kl mg.st 0
scoreboard players set $kr mg.st 0
scoreboard players set $kj mg.st 0
execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs

scoreboard players remove @s[scores={mg.kbo=1..}] mg.kbo 1
scoreboard players remove @s[scores={mg.kst=1..}] mg.kst 1
function mg:kart/speed
function mg:kart/steer
function mg:kart/vertical
execute if score $kbp mg.st matches 1 if score $kg mg.st matches 1 run function mg:kart/boost_pad
execute if score @s mg.kst matches 1.. run function mg:kart/star_touch

# Déplacement
execute store result storage mg:kart m.d double 0.01 run scoreboard players get @s mg.ksp
scoreboard players operation $kc mg.st = @s mg.ksp
execute if score @s mg.ksp matches 0.. run scoreboard players add $kc mg.st 75
execute if score @s mg.ksp matches ..-1 run scoreboard players remove $kc mg.st 75
execute store result storage mg:kart m.c double 0.01 run scoreboard players get $kc mg.st
execute store result storage mg:kart m.t int 1 run scoreboard players get $kt mg.st
execute store result storage mg:kart m.v double 0.01 run scoreboard players get $kv mg.st
execute on vehicle run function mg:kart/move with storage mg:kart m
function mg:kart/fx
