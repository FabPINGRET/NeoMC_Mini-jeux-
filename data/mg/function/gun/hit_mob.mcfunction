# Mob : on retire la vie directement (pas d'invulnérabilité), coup fatal crédité au tireur
execute store result score $gh mg.st run data get entity @s Health 10
scoreboard players operation $gh mg.st -= $gdm mg.st
execute if score $gh mg.st matches 1.. store result entity @s Health float 0.1 run scoreboard players get $gh mg.st
execute if score $gh mg.st matches 1.. at @s run playsound minecraft:entity.zombie.hurt hostile @a ~ ~ ~ 0.5 1
execute if score $gh mg.st matches ..0 run damage @s 1000 minecraft:player_attack by @a[tag=mg.gsh,limit=1]
