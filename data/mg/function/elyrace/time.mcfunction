# Temps #xq (ticks) -> $es (secondes) et $ecs (centiemes, par pas de 5), meme convention que mg:elytra/finish1 et mg:sky/finish ;
# $es et $ecs sont partages avec ces jeux : a recalculer juste avant chaque affichage (#k5 et #k20 : mg:elyrace/objectives)
scoreboard players operation $es mg.st = #xq mg.st
scoreboard players operation $es mg.st /= #k20 mg.st
scoreboard players operation $ecs mg.st = #xq mg.st
scoreboard players operation $ecs mg.st %= #k20 mg.st
scoreboard players operation $ecs mg.st *= #k5 mg.st
