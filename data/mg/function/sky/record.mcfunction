# Nouveau record du serveur, course d'anneaux (@s ; $es / $ecs déjà calculés)
scoreboard players operation $skrec mg.st = $skt mg.st
execute if score $ecs mg.st matches ..9 run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record de la course Élytra : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]
execute if score $ecs mg.st matches 10.. run tellraw @a [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record de la course Élytra : ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]
function mg:hall/ely {key:"elyg",lbl:"🪽 Record Élytra : course"}
