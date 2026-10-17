# @s = joueur, position = centre du banc (posés par bench_hit) : s'y assoit, ou se lève s'il y est déjà
execute store result score #lbn mg.st run time query gametime
scoreboard players operation #lbd mg.st = @s mg.lsb
scoreboard players add #lbd mg.st 10
execute if score @s mg.lsb matches 1.. if score #lbn mg.st < #lbd mg.st run return 0
scoreboard players operation @s mg.lsb = #lbn mg.st
# assis sur ce banc : on se lève (le siège est à SEAT_DY au-dessus du pied du banc)
execute if entity @s[tag=mg.sit] positioned ~ ~0.5 ~ on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat,distance=..0.3] run return run execute on passengers run function mg:lobby/sit/stand
# banc pris par un autre : message, et un joueur déjà assis garde sa place
execute align xyz positioned ~0.5 ~0.5 ~0.5 if entity @e[type=minecraft:item_display,tag=mg.seat,distance=..0.3] run return run title @s actionbar {"text":"🪑 Place déjà prise.","color":"gray"}
# assis ailleurs (autre banc, sol) : on se lève d'abord
execute if entity @s[tag=mg.sit] run function mg:lobby/sit/stand
execute unless function mg:lobby/sit/can run return 0
execute align xyz if function mg:lobby/sit/bench_at run scoreboard players add $bnc mg.lsn 1
