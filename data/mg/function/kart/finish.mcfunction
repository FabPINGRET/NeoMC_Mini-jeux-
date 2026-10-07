tag @s add mg.kfin
scoreboard players add $kfo mg.st 1
scoreboard players operation @s mg.kfp = $kfo mg.st
scoreboard players set @s mg.kps 100
execute if score $kfo mg.st matches 1 run scoreboard players operation $kend mg.st = $ktime mg.st
execute if score $kfo mg.st matches 1 run scoreboard players add $kend mg.st 600
scoreboard players operation $ksec mg.st = $ktime mg.st
scoreboard players operation $ksec mg.st /= #k20 mg.st
title @s title [{"score":{"name":"@s","objective":"mg.kfp"},"color":"gold","bold":true},{"text":"ᵉ","color":"gold"}]
title @s subtitle [{"text":"🏁 Arrivée en ","color":"yellow"},{"score":{"name":"$ksec","objective":"mg.st"},"color":"white"},{"text":" s","color":"yellow"}]
tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" franchit la ligne en position ","color":"gray"},{"score":{"name":"@s","objective":"mg.kfp"},"color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"$ksec","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]
execute if score $kfo mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"⏱ 30 secondes pour finir la course !","color":"gold"}]
execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.play] ~ ~ ~ 1 1
