scoreboard players set $pvc mg.st 0
execute store result score $n mg.st if entity @a[tag=mg.pvpc]
execute if score $n mg.st matches ..1 run return 0
execute store result score $n mg.st if entity @e[type=minecraft:item,tag=mg.pvpcoin]
execute if score $n mg.st matches 4.. run return 0
execute store result score $cx mg.st run random value -9..35
execute store result score $cz mg.st run random value -7..31
execute store result storage mg:pvpc p.x int 1 run scoreboard players get $cx mg.st
execute store result storage mg:pvpc p.z int 1 run scoreboard players get $cz mg.st
function mg:pvpc/coin_at with storage mg:pvpc p
