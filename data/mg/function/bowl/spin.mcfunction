# effet : la boule revient vers le centre (si lancée au centre : à l'opposé de sa direction)
execute if score #lx mg.st matches 1.. run return run scoreboard players set #sp mg.st -1
execute if score #lx mg.st matches ..-1 run return run scoreboard players set #sp mg.st 1
execute if score #vx mg.st matches ..-1 run return run scoreboard players set #sp mg.st 1
scoreboard players set #sp mg.st -1
