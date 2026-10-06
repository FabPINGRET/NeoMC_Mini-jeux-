scoreboard players add $mpn mg.st 1
scoreboard players operation @s mg.mpo = $mpn mg.st
tellraw @a[tag=mg.mpp] [{"text":"    ","color":"gray"},{"score":{"name":"@s","objective":"mg.mpo"},"color":"yellow"},{"text":". ","color":"gray"},{"selector":"@s","color":"white"}]
