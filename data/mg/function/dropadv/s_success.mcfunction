# @s atterrit dans l'eau : niveau réussi (en mg.dtr essais), niveau suivant ou arrivée
execute unless score $state mg.st matches 2 run return 0
execute if score @s mg.cd matches 1.. run return 0
execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 60
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.3
execute if score @s mg.dtr matches 1 run tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" réussit le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" du premier coup !","color":"green"}]
execute if score @s mg.dtr matches 2.. run tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" réussit le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" en ","color":"gray"},{"score":{"name":"@s","objective":"mg.dtr"},"color":"white"},{"text":" essais","color":"gray"}]
scoreboard players add @s mg.dok 1
scoreboard players set @s mg.dkc 0
scoreboard players add @s mg.dlv 1
execute if score @s mg.dlv matches 14.. run return run function mg:dropadv/s_done
scoreboard players add @s mg.dtt 1
scoreboard players set @s mg.dtr 1
function mg:dropadv/spawn
function mg:dropadv/show_level
