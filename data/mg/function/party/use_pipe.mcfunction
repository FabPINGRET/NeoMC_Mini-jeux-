# Tuyau (@s) : échange de place avec un adversaire au hasard, puis le joueur lance son dé
execute unless score @s mg.mip matches 1.. run return run function mg:party/no_item
execute as @a[tag=mg.mpp,tag=mg.play,tag=!mg.mpcur,sort=random,limit=1] run tag @s add mg.mpsw
execute unless entity @a[tag=mg.mpsw] run return run tellraw @s [{"text":"Personne avec qui échanger !","color":"red"}]
scoreboard players remove @s mg.mip 1
scoreboard players operation $tmp mg.st = @s mg.mpi
scoreboard players operation @s mg.mpi = @a[tag=mg.mpsw,limit=1] mg.mpi
scoreboard players operation @a[tag=mg.mpsw] mg.mpi = $tmp mg.st
function mg:party/place
execute as @a[tag=mg.mpsw] run function mg:party/place
tellraw @a[tag=mg.mpp] [{"text":"🔀 TUYAU ! ","color":"yellow","bold":true},{"selector":"@s","color":"yellow"},{"text":" et ","color":"gray"},{"selector":"@a[tag=mg.mpsw]","color":"yellow"},{"text":" échangent leurs places.","color":"gray"}]
tag @a remove mg.mpsw
execute at @s run playsound minecraft:entity.enderman.teleport master @a[tag=mg.mpp] ~ ~ ~ 1 1
scoreboard players set $mpw mg.st 400
dialog show @s mg:party_roll
