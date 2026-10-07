# @s atterrit dans l'eau : niveau suivant (ou victoire)
execute if score @s mg.cd matches 1.. run return 0
execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 60
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.3
scoreboard players add @s mg.dlv 1
execute if score @s mg.dlv matches 11.. run return run function mg:dropadv/finish
tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" passe au niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true}]
function mg:dropadv/spawn
function mg:dropadv/show_level
