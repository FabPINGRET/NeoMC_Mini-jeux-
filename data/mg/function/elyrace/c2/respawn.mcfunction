# @s = joueur a replacer au dernier point de reprise : mur (3 coeurs), sol, eau, trop longtemps sans planer, anneau rate
scoreboard players set @s mg.xh 3
scoreboard players set @s mg.xg 40
scoreboard players set @s mg.xk 12
scoreboard players set @s mg.xl 0
scoreboard players set @s mg.xn 0
scoreboard players operation @s mg.xa = @s mg.xc
# gravite de base du parcours reposee (un attribut ne survit pas forcement a la mort) ; les ors pris (mg.xu) sont gardes
function mg:elyrace/c2/grav
# origine du balayage remise a zero : le saut jusqu'au point de reprise n'est pas un deplacement (le tick suivant ne franchit aucun anneau)
scoreboard players set @s mg.xq1 -1000000
# #tp = 1 si la teleportation a reussi : mg.deaths n'est remis a 0 qu'alors (un joueur mort sera replace au tick suivant)
scoreboard players set #tp mg.st 0
execute if score @s mg.xc matches 0 run function mg:elyrace/c2/place_tp
execute if score @s mg.xc matches 4 store success score #tp mg.st run tp @s 228.5 261 29604.5 270 0
execute if score @s mg.xc matches 8 store success score #tp mg.st run tp @s 428.5 222 29604.5 270 0
execute if score @s mg.xc matches 13 store success score #tp mg.st run tp @s 698.5 173 29601.5 270 0
execute if score @s mg.xc matches 17 store success score #tp mg.st run tp @s 1013.5 122 29600.5 270 0
execute if score #tp mg.st matches 1 run scoreboard players set @s mg.deaths 0
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:portal ~ ~1 ~ 0.4 0.8 0.4 0.3 40
function mg:elyrace/c2/hud
