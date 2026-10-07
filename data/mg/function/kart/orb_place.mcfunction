scoreboard players operation $ka2 mg.st = @s mg.kdd
scoreboard players operation $ka2 mg.st *= #k120 mg.st
scoreboard players operation $ka2 mg.st += $kob mg.st
execute store result storage mg:kart o.a int 1 run scoreboard players get $ka2 mg.st
scoreboard players operation $kb2 mg.st = @s mg.kdd
scoreboard players operation $kb2 mg.st *= #k65 mg.st
scoreboard players add $kb2 mg.st 120
execute store result storage mg:kart o.b double 0.01 run scoreboard players get $kb2 mg.st
execute if entity @s[tag=mg.korbs] run function mg:kart/orb_spin with storage mg:kart o
execute if entity @s[tag=mg.korbb] run function mg:kart/orb_trail with storage mg:kart o
