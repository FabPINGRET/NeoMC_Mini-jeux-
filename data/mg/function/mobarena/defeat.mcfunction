# Mob Arena — défaite collective
kill @e[tag=mg.mob]
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 60
title @a title [{"text":"DÉFAITE...","color":"dark_red","bold":true}]
title @a subtitle [{"text":"L'arène a eu raison de vous","color":"gray"}]
tellraw @a [{"text":"☠ Tombés à la vague ","color":"gray"},{"score":{"name":"$wv","objective":"mg.st"},"color":"red","bold":true},{"text":" — retentez votre chance !","color":"gray"}]
execute as @a at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8
