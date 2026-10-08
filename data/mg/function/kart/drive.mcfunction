# Pilotage du kart de @s (chaque tick)
execute if entity @s[tag=mg.kout] run return 0
execute if score @s mg.kch matches 1.. run function mg:kart/choose
execute if score @s mg.krl matches 1.. run function mg:kart/roulette
execute if score $kph mg.st matches 0 run function mg:kart/engine
function mg:kart/kk
execute unless entity @e[tag=mg.kk] at @s run function mg:kart/kart_new
execute unless entity @e[tag=mg.kk] run function mg:kart/kk
execute if score @s mg.kv matches 1.. run function mg:kart/view_cmd
function mg:kart/seat
scoreboard players remove @s[scores={mg.kstk=1..}] mg.kstk 1
execute if entity @s[tag=mg.kstuck] run function mg:kart/stuck
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run function mg:kart/probe
execute if score $kg mg.st matches 0 if score @s mg.kvy matches ..0 as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s unless block ~ ~-1.2 ~ #mg:kart_pass run function mg:kart/step_down

scoreboard players set $kf mg.st 0
scoreboard players set $kb mg.st 0
scoreboard players set $kl mg.st 0
scoreboard players set $kr mg.st 0
scoreboard players set $kj mg.st 0
scoreboard players set $ks mg.st 0
execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs
execute if score $klob mg.st matches 0 if score $kbat mg.st matches 0 if score $kf mg.st matches 1 run scoreboard players add @s mg.kof 1
execute if score $klob mg.st matches 0 if score $kbat mg.st matches 0 if score $kb mg.st matches 1 if score $kf mg.st matches 0 run scoreboard players add @s mg.kof 1

# Objet : clic droit (vue assise) ou Ctrl (caméra de poursuite)
scoreboard players set $kuse mg.st 0
execute if score @s mg.qs matches 1.. run scoreboard players set $kuse mg.st 1
execute if score $ks mg.st matches 1 unless score @s mg.kspr matches 1 run scoreboard players set $kuse mg.st 1
scoreboard players operation @s mg.kspr = $ks mg.st
scoreboard players reset @s mg.qs
execute if score $kuse mg.st matches 1 run function mg:kart/use_item

# Chronos des objets
scoreboard players remove @s[scores={mg.kbo=1..}] mg.kbo 1
scoreboard players remove @s[scores={mg.kst=1..}] mg.kst 1
scoreboard players remove @s[scores={mg.kboo=1..}] mg.kboo 1
execute if score @s mg.kmg matches 1 run function mg:kart/mega_end
scoreboard players remove @s[scores={mg.kmg=1..}] mg.kmg 1
execute if score @s mg.kgd matches 1 run function mg:kart/golden_end
scoreboard players remove @s[scores={mg.kgd=1..}] mg.kgd 1
execute if score @s mg.kit matches 8..10 run function mg:kart/orbs
execute if score @s mg.kboo matches 1.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run particle minecraft:white_ash ~ ~0.8 ~ 0.6 0.5 0.6 0 6

# Bill Balle : pilote automatique
execute if score @s mg.kbill matches 1 run function mg:kart/bill_end
execute if score @s mg.kbill matches 1.. run scoreboard players remove @s mg.kbill 1
execute if score @s mg.kbill matches 1.. run function mg:kart/bill_move
execute if score @s mg.kbill matches 1.. unless entity @s[tag=mg.kfin] run return run function mg:kart/cp_check

execute if score $kwa mg.st matches 1 run return run function mg:kart/rescue
execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue
execute if score $kbat mg.st matches 0 if score $klob mg.st matches 0 at @e[type=minecraft:block_display,tag=mg.kk,limit=1] unless block ~ ~ ~ #mg:kart_pass unless block ~ ~1 ~ #mg:kart_pass run return run function mg:kart/rescue
execute if score @s mg.kof matches 200.. run return run function mg:kart/rescue

function mg:kart/speed
function mg:kart/steer
function mg:kart/heading
function mg:kart/vertical
execute if score $kbp mg.st matches 1 if score $kg mg.st matches 1 run function mg:kart/boost_pad
execute if score @s mg.kst matches 1.. run function mg:kart/star_touch
execute if score @s mg.kmg matches 1.. run function mg:kart/mega_touch

execute store result storage mg:kart m.d double 0.01 run scoreboard players get @s mg.ksp
scoreboard players operation $kc mg.st = @s mg.ksp
execute if score @s mg.ksp matches 0.. run scoreboard players add $kc mg.st 75
execute if score @s mg.ksp matches ..-1 run scoreboard players remove $kc mg.st 75
execute store result storage mg:kart m.c double 0.01 run scoreboard players get $kc mg.st
execute store result storage mg:kart m.t double 0.1 run scoreboard players get $kt mg.st
execute store result storage mg:kart m.h double 0.1 run scoreboard players get @s mg.khd
execute store result storage mg:kart m.v double 0.01 run scoreboard players get $kv mg.st
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/move with storage mg:kart m
function mg:kart/fx
execute unless entity @s[tag=mg.kfin] run function mg:kart/cp_check
