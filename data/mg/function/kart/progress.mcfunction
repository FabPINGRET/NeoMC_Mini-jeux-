# Avancement : tours x 1000 + point de passage (arrivé : selon l'ordre d'arrivée) ; tableau en %
scoreboard players operation @s mg.kpg = @s mg.klp
scoreboard players operation @s mg.kpg *= #k1000 mg.st
scoreboard players operation @s mg.kpg += @s mg.kcp
execute if entity @s[tag=mg.kfin] run scoreboard players set @s mg.kpg 900000
execute if entity @s[tag=mg.kfin] run scoreboard players operation @s mg.kpg -= @s mg.kfp
execute if entity @s[tag=mg.kfin] run return 0
scoreboard players operation $kp mg.st = @s mg.klp
scoreboard players remove $kp mg.st 1
execute if score $kp mg.st matches ..-1 run scoreboard players set $kp mg.st 0
scoreboard players operation $kp mg.st *= $kK mg.st
scoreboard players operation $kp mg.st += @s mg.kcp
scoreboard players operation $kp mg.st *= #k100 mg.st
scoreboard players operation $kq mg.st = $kK mg.st
scoreboard players operation $kq mg.st *= $kLaps mg.st
scoreboard players operation $kp mg.st /= $kq mg.st
scoreboard players operation @s mg.kps = $kp mg.st
