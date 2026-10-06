# Arrivée (@s = coureur) : temps, records, retour au lobby
function mg:parkour/bar
scoreboard players operation $t mg.st = @s mg.ppt
scoreboard players operation $s mg.st = $t mg.st
scoreboard players operation $s mg.st /= $pk20 mg.st
scoreboard players operation $d mg.st = $t mg.st
scoreboard players operation $d mg.st %= $pk20 mg.st
scoreboard players operation $d mg.st /= $pk2 mg.st
tellraw @a [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a terminé le PARKOUR en ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"green","bold":true},{"text":".","color":"green"},{"score":{"name":"$d","objective":"mg.st"},"color":"green"},{"text":" s ","color":"green"},{"text":"(","color":"gray"},{"score":{"name":"@s","objective":"mg.ppf"},"color":"red"},{"text":" chutes)","color":"gray"}]
# Record personnel
execute unless score @s mg.ppb matches 1.. run tellraw @s [{"text":"✔ Premier temps enregistré.","color":"aqua"}]
execute if score @s mg.ppb matches 1.. if score @s mg.ppt < @s mg.ppb run tellraw @s [{"text":"✔ Nouveau record personnel !","color":"aqua","bold":true}]
execute unless score @s mg.ppb matches 1.. run scoreboard players operation @s mg.ppb = @s mg.ppt
execute if score @s mg.ppt < @s mg.ppb run scoreboard players operation @s mg.ppb = @s mg.ppt
# Record du lobby
execute unless score $pkrec mg.st matches 1.. run function mg:parkour/record
execute if score $pkrec mg.st matches 1.. if score @s mg.ppt < $pkrec mg.st run function mg:parkour/record
# Fin de course
tag @s remove mg.pkr
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
execute at @s run particle minecraft:firework ~ ~1 ~ 0.6 0.8 0.6 0.1 60
tp @s 0.5 64 0.5 facing 0.5 64 8.5
