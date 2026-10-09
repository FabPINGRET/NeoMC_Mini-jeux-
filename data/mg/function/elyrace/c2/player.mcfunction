# @s = joueur en course (pas encore arrivé) : turbo, position, délais, règles
# turbo d'un anneau d'or : décompte (gold_hit pose mg.xu), la gravité de base du parcours revient au dernier tick
execute if score @s mg.xu matches 1 run function mg:elyrace/c2/grav
scoreboard players remove @s[scores={mg.xu=1..}] mg.xu 1
execute store result score @s mg.xx run data get entity @s Pos[0]
scoreboard players operation @s mg.xp > @s mg.xx
scoreboard players remove @s[scores={mg.xg=1..}] mg.xg 1
scoreboard players remove @s[scores={mg.xk=1..}] mg.xk 1
execute if predicate mg:gliding run scoreboard players set @s mg.xl 1
execute if predicate mg:gliding run scoreboard players set @s mg.xn 0
execute unless predicate mg:gliding if score @s mg.xl matches 1 run scoreboard players add @s mg.xn 1
function mg:elyrace/speed
# Mort (filet) ou sorti de la zone construite (monde vide) : retour au dernier point de reprise
execute if score @s mg.deaths matches 1.. run return run function mg:elyrace/c2/respawn
execute unless entity @s[x=-16,y=0,z=29440,dx=1152,dy=330,dz=320] run return run function mg:elyrace/c2/respawn
# Encore sur la plateforme de départ : aucune règle
execute if score @s mg.xx matches ..32 run return 0
execute if score @s mg.xg matches 0 if score @s mg.xn matches 11.. run return run function mg:elyrace/c2/respawn
execute if score @s mg.xg matches 0 at @s if block ~ ~ ~ minecraft:water run return run function mg:elyrace/c2/respawn
execute if score @s mg.xg matches 0 at @s if data entity @s {OnGround:1b} run return run function mg:elyrace/c2/respawn
function mg:elyrace/c2/rings
