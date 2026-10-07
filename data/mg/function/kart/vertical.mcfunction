# Tremplin, petit saut du dérapage, gravité
scoreboard players set $kv mg.st 0
execute if score $kju mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 48
execute if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 0
execute if score $kg mg.st matches 0 run scoreboard players remove @s mg.kvy 6
execute if score @s mg.kvy matches ..-90 run scoreboard players set @s mg.kvy -90
scoreboard players operation $kv mg.st = @s mg.kvy
