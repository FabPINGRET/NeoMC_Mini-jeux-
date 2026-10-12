# $vm = minutes de jeu depuis la valeur de jeu $vg (→ $vh h $vm min)
execute store result score $vago mg.st run time query gametime
scoreboard players operation $vago mg.st -= $vg mg.st
scoreboard players set #1200 mg.st 1200
scoreboard players set #60 mg.st 60
scoreboard players operation $vago mg.st /= #1200 mg.st
scoreboard players operation $vh mg.st = $vago mg.st
scoreboard players operation $vh mg.st /= #60 mg.st
scoreboard players operation $vm mg.st = $vago mg.st
scoreboard players operation $vm mg.st %= #60 mg.st
