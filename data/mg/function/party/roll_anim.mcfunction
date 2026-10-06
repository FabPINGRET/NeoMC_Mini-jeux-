# Le dé (1 à 10) roule 1,5 s au-dessus du joueur puis s'arrête sur le résultat
scoreboard players remove $mpw mg.st 1
execute store result score $dv mg.st run random value 1..10
function mg:party/dice_show
execute if score $mpw mg.st matches 1.. as @a[tag=mg.mpp] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.4 2
execute if score $mpw mg.st matches 1.. run return 0

scoreboard players operation $mpr mg.st = $dv mg.st
title @a[tag=mg.mpp] title [{"score":{"name":"$dv","objective":"mg.st"},"color":"gold","bold":true}]
title @a[tag=mg.mpp] subtitle [{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":" avance !","color":"gray"}]
execute as @a[tag=mg.mpp] at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1
scoreboard players set $mph mg.st 3
scoreboard players set $mpw mg.st 15
