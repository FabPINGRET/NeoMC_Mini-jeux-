# Fin d'une manche (attaque/défense) : score = distance ×10 (+ temps restant si arrivé)
scoreboard players operation $cvx mg.st = $cvp mg.st
scoreboard players set #10 mg.st 10
scoreboard players operation $cvx mg.st *= #10 mg.st
scoreboard players set $cvy mg.st 3600
scoreboard players operation $cvy mg.st -= $cvt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $cvy mg.st /= #20 mg.st
execute if score $cvp mg.st matches 120.. run scoreboard players operation $cvx mg.st += $cvy mg.st
execute if score $cvr mg.st matches 1 run scoreboard players operation $cvs1 mg.st = $cvx mg.st
execute if score $cvr mg.st matches 2 run scoreboard players operation $cvs2 mg.st = $cvx mg.st
tellraw @a[tag=mg.play] [{"text":"🚚 Fin de la manche : ","color":"gold"},{"score":{"name":"$cvx","objective":"mg.st"},"color":"yellow","bold":true},{"text":" points (","color":"gray"},{"score":{"name":"$cvp","objective":"mg.st"},"color":"gray"},{"text":" blocs)","color":"gray"}]
execute if score $cvr mg.st matches 2 run return run function mg:convoy/final
scoreboard players set $cvr mg.st 2
scoreboard players set $cvo mg.st 1
function mg:convoy/reset_cart
execute as @a[tag=mg.play] run function mg:convoy/respawn
function mg:convoy/round_msg
