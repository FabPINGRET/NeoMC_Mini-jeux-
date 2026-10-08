# @s = joueur a replacer au dernier point de reprise : mur (3 coeurs), sol, eau, trop longtemps sans planer, anneau rate
scoreboard players set @s mg.xh 3
scoreboard players set @s mg.xg 40
scoreboard players set @s mg.xk 12
scoreboard players set @s mg.xl 0
scoreboard players set @s mg.xn 0
scoreboard players operation @s mg.xa = @s mg.xc
# #tp = 1 si la teleportation a reussi : mg.deaths n'est remis a 0 qu'alors (un joueur mort sera replace au tick suivant)
scoreboard players set #tp mg.st 0
execute if score @s mg.xc matches 0 run function mg:elyrace/place_tp
execute if score @s mg.xc matches 4 store success score #tp mg.st run tp @s 283.5 225 27011.5 270 0
execute if score @s mg.xc matches 8 store success score #tp mg.st run tp @s 508.5 192 27000.5 270 0
execute if score @s mg.xc matches 12 store success score #tp mg.st run tp @s 718.5 159 26988.5 270 0
execute if score @s mg.xc matches 15 store success score #tp mg.st run tp @s 871.5 135 27000.5 270 0
execute if score #tp mg.st matches 1 run scoreboard players set @s mg.deaths 0
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:portal ~ ~1 ~ 0.4 0.8 0.4 0.3 40
function mg:elyrace/hud
