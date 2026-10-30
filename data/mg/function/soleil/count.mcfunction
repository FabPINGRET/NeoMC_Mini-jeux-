# Feu vert : « 1… 2… 3… » (titre + note de plus en plus aiguë) ; pas de barre de temps restant (trop facile)
scoreboard players operation $k mg.st = $sqg mg.st
scoreboard players operation $k mg.st -= $sqt mg.st
scoreboard players operation $k mg.st *= #3 mg.st
scoreboard players operation $k mg.st /= $sqg mg.st
execute if score $k mg.st matches 3.. run scoreboard players set $k mg.st 2
execute unless score $k mg.st = $sqk mg.st run function mg:soleil/count_step
