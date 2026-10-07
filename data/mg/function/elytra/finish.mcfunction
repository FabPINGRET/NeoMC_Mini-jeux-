# Arrivée (@s) : temps, record perso, record du serveur
scoreboard players operation $es mg.st = @s mg.et
scoreboard players operation $es mg.st /= #20 mg.st
scoreboard players operation $ecs mg.st = @s mg.et
scoreboard players operation $ecs mg.st %= #20 mg.st
scoreboard players operation $ecs mg.st *= #5 mg.st
title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]
execute if score $ecs mg.st matches ..9 run tellraw @s [{"text":"🪽 Parcours d'élytra bouclé en ","color":"aqua"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $ecs mg.st matches 10.. run tellraw @s [{"text":"🪽 Parcours d'élytra bouclé en ","color":"aqua"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1
execute unless score @s mg.erb matches 1.. run scoreboard players operation @s mg.erb = @s mg.et
execute if score @s mg.et < @s mg.erb run tellraw @s [{"text":"★ Nouveau record personnel !","color":"yellow","bold":true}]
execute if score @s mg.et < @s mg.erb run scoreboard players operation @s mg.erb = @s mg.et
execute unless score $erec mg.st matches 1.. run scoreboard players set $erec mg.st 999999
execute if score @s mg.et < $erec mg.st if score $ecs mg.st matches ..9 run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du parcours d'élytra : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]
execute if score @s mg.et < $erec mg.st if score $ecs mg.st matches 10.. run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du parcours d'élytra : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]
execute if score @s mg.et < $erec mg.st run scoreboard players operation $erec mg.st = @s mg.et
execute if score @s mg.et = $erec mg.st run function mg:hall/ely
function mg:elytra/stop
