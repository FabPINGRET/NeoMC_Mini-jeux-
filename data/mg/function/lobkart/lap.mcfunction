# Ligne d'arrivée franchie par un pilote du spawn (@s) : tour chronométré, record perso et record du circuit
scoreboard players add @s mg.klp 1
execute if score @s mg.klp matches 1 run scoreboard players set @s mg.klt 0
execute if score @s mg.klp matches 1 run return run title @s actionbar [{"text":"🏁 C'est parti, le chrono tourne !","color":"green","bold":true}]
scoreboard players operation $s mg.st = @s mg.klt
scoreboard players operation $s mg.st /= #k20 mg.st
scoreboard players operation $d mg.st = @s mg.klt
scoreboard players operation $d mg.st %= #k20 mg.st
scoreboard players operation $d mg.st /= #k2 mg.st
tellraw @s [{"text":"🏁 Tour en ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s","color":"gold"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
execute if score @s mg.klb matches 1.. if score @s mg.klt < @s mg.klb run tellraw @s [{"text":"★ Nouveau record perso !","color":"aqua","bold":true}]
execute unless score @s mg.klb matches 1.. run scoreboard players operation @s mg.klb = @s mg.klt
execute if score @s mg.klt < @s mg.klb run scoreboard players operation @s mg.klb = @s mg.klt
execute unless score $klrec mg.st matches 1.. run function mg:lobkart/record
execute if score $klrec mg.st matches 1.. if score @s mg.klt < $klrec mg.st run function mg:lobkart/record
scoreboard players set @s mg.klt 0
