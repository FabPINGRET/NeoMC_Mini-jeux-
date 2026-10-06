# Le dé (1 à 6, ou 2 / 3 dés avec un objet) roule au-dessus du joueur : vite, puis de plus en plus lentement, et s'arrête sur la dernière face
scoreboard players remove $mpw mg.st 1
scoreboard players operation $q mg.st = $mpw mg.st
scoreboard players operation $q mg.st %= #2 mg.st
scoreboard players operation $q4 mg.st = $mpw mg.st
scoreboard players operation $q4 mg.st %= #4 mg.st
execute if score $mpw mg.st matches 31.. run function mg:party/roll_face
execute if score $mpw mg.st matches 13..30 if score $q mg.st matches 0 run function mg:party/roll_face
execute if score $mpw mg.st matches 1..12 if score $q4 mg.st matches 0 run function mg:party/roll_face
execute if score $mpw mg.st matches 1.. run return 0

scoreboard players operation $mpr mg.st = $dv mg.st
title @a[tag=mg.mpp] times 5 40 10
title @a[tag=mg.mpp] title [{"score":{"name":"$dv","objective":"mg.st"},"color":"gold","bold":true}]
title @a[tag=mg.mpp] subtitle [{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":" avance","color":"gray"}]
execute if score $mdn mg.st matches 1 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":" fait ","color":"gray"},{"score":{"name":"$dv","objective":"mg.st"},"color":"gold","bold":true}]
execute if score $mdn mg.st matches 2 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":" fait ","color":"gray"},{"score":{"name":"$dv","objective":"mg.st"},"color":"gold","bold":true},{"text":" avec le dé double (","color":"gray"},{"score":{"name":"$d1","objective":"mg.st"},"color":"white"},{"text":" + ","color":"gray"},{"score":{"name":"$d2","objective":"mg.st"},"color":"white"},{"text":")","color":"gray"}]
execute if score $mdn mg.st matches 3 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":" fait ","color":"gray"},{"score":{"name":"$dv","objective":"mg.st"},"color":"gold","bold":true},{"text":" avec le dé triple (","color":"gray"},{"score":{"name":"$d1","objective":"mg.st"},"color":"white"},{"text":" + ","color":"gray"},{"score":{"name":"$d2","objective":"mg.st"},"color":"white"},{"text":" + ","color":"gray"},{"score":{"name":"$d3","objective":"mg.st"},"color":"white"},{"text":")","color":"gray"}]
execute as @a[tag=mg.mpp] at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1
execute as @a[tag=mg.mpp] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5
scoreboard players set $mph mg.st 3
scoreboard players set $mpw mg.st 40
