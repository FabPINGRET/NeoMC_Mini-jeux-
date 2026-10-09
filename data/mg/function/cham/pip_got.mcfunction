# @s : la pipette a trouvé la matière $(m)
scoreboard players set $cmf mg.st 1
$scoreboard players set $cmm mg.st $(m)
scoreboard players operation $cmpp mg.st = @s mg.cmpt
function mg:cham/paint_do
particle minecraft:dust{color:[0.3,0.9,1.0],scale:1} ~ ~ ~ 0.15 0.15 0.15 0 8
execute at @s run playsound minecraft:item.bottle.fill player @s ~ ~ ~ 0.8 1.4
