# Secret « Fou du volant » trouvé par @s : annonce à tout le monde
function mg:secrets/count
tellraw @a [{"text":"🕵 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a trouvé un secret du spawn : ","color":"gray"},{"text":"[Fou du volant]","color":"light_purple","bold":true},{"text":" (","color":"gray"},{"score":{"name":"$secn","objective":"mg.st"},"color":"gold"},{"text":"/18)","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.6 1.6
function mg:secrets/reward
