# Chaque seconde : temps restant, monstres (coop)
scoreboard players operation $cvs mg.st = $cvt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $cvs mg.st /= #20 mg.st
scoreboard players set $cvl mg.st 180
execute if score $cvm mg.st matches 1 run scoreboard players set $cvl mg.st 360
scoreboard players operation $cvl mg.st -= $cvs mg.st
execute if score $cvm mg.st matches 0 run bossbar set mg:convoy name [{"text":"🚚 Convoi — manche ","color":"gold"},{"score":{"name":"$cvr","objective":"mg.st"}},{"text":" — "},{"score":{"name":"$cvl","objective":"mg.st"},"color":"yellow"},{"text":" s"}]
execute if score $cvm mg.st matches 1 run bossbar set mg:convoy name [{"text":"🚚 Convoi — ","color":"gold"},{"score":{"name":"$cvh","objective":"mg.st"},"color":"red"},{"text":" ❤ — "},{"score":{"name":"$cvl","objective":"mg.st"},"color":"yellow"},{"text":" s"}]
execute if score $cvm mg.st matches 1 run function mg:convoy/coop_second
