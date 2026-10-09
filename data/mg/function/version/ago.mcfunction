# $vm = minutes de jeu depuis la valeur de jeu $vg (→ $vh h $vm min)
execute store result score $vn mg.st run time query gametime
scoreboard players operation $vn mg.st -= $vg mg.st
scoreboard players set #1200 mg.st 1200
scoreboard players set #60 mg.st 60
scoreboard players operation $vn mg.st /= #1200 mg.st
scoreboard players operation $vh mg.st = $vn mg.st
scoreboard players operation $vh mg.st /= #60 mg.st
scoreboard players operation $vm mg.st = $vn mg.st
scoreboard players operation $vm mg.st %= #60 mg.st
