# @s = joueur qui franchit l'arrivée du parcours 2 (Pic Blanc), temps #xrt (ticks, posé par finish) : record personnel, puis record du serveur
scoreboard players operation #xq mg.st = #xrt mg.st
function mg:elyrace/time
# #rp = 1 : meilleur temps personnel (ou premier temps)
scoreboard players set #rp mg.st 0
execute unless score @s mg.xr2 matches 1.. run scoreboard players set #rp mg.st 1
execute if score @s mg.xr2 matches 1.. if score #xrt mg.st < @s mg.xr2 run scoreboard players set #rp mg.st 1
execute if score #rp mg.st matches 0 run return 0
scoreboard players operation @s mg.xr2 = #xrt mg.st
execute if score $ecs mg.st matches ..9 run tellraw @s [{"text":"★ Nouveau record personnel : ","color":"yellow","bold":true},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $ecs mg.st matches 10.. run tellraw @s [{"text":"★ Nouveau record personnel : ","color":"yellow","bold":true},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
# #rs = 1 : nouveau record du serveur (un record du serveur est toujours un record personnel)
scoreboard players set #rs mg.st 0
execute unless score #srv mg.xr2 matches 1.. run scoreboard players set #rs mg.st 1
execute if score #srv mg.xr2 matches 1.. if score #xrt mg.st < #srv mg.xr2 run scoreboard players set #rs mg.st 1
execute if score #rs mg.st matches 0 run return 0
scoreboard players operation #srv mg.xr2 = #xrt mg.st
execute if score $ecs mg.st matches ..9 run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du serveur sur Pic Blanc : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $ecs mg.st matches 10.. run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du serveur sur Pic Blanc : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
function mg:hall/ely {key:"xr2",lbl:"🪽 Record Pic Blanc"}
