# Fin de la Mini Party : classement (étoiles puis pièces) et victoire
scoreboard players set $mph mg.st 9
execute as @a[tag=mg.mpp] run scoreboard players operation @s mg.mpz = @s mg.mpk
execute as @a[tag=mg.mpp] run scoreboard players operation @s mg.mpz *= #1000 mg.st
execute as @a[tag=mg.mpp] run scoreboard players operation @s mg.mpz += @s mg.mpm
scoreboard players set $best mg.st -1
execute as @a[tag=mg.mpp] if score @s mg.mpz > $best mg.st run scoreboard players operation $best mg.st = @s mg.mpz
tellraw @a [{"text":"\n★ RÉSULTATS DE LA MINI PARTY ★","color":"gold","bold":true}]
execute as @a[tag=mg.mpp] run tellraw @a [{"text":"  ","color":"gray"},{"selector":"@s","color":"white"},{"text":" : ★ ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpk"},"color":"yellow"},{"text":"   ● ","color":"gold"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold"}]
execute unless entity @a[tag=mg.mpp] run return run function mg:core/draw
execute as @a[tag=mg.mpp] if score @s mg.mpz = $best mg.st run function mg:core/win_player
