# Élytres libres, chaque tick (@s) : retirées en partie, en survie, sur un plot, en visite, en parkour
execute if entity @s[tag=mg.play] run return run function mg:elytra/free_stop
execute if entity @s[tag=mg.surv] run return run function mg:elytra/free_stop
execute if entity @s[tag=mg.inplot] run return run function mg:elytra/free_stop
execute if entity @s[tag=mg.visit] run return run function mg:elytra/free_stop
execute if entity @s[tag=mg.pkr] run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"Pas d'élytres pendant le parkour : rendues.","color":"red"}]
execute if entity @s[tag=mg.pkr] run return run function mg:elytra/free_stop
execute unless entity @s[gamemode=adventure] run return run function mg:elytra/free_stop
execute if score $lan mg.t matches 30 run function mg:elytra/free_refill
