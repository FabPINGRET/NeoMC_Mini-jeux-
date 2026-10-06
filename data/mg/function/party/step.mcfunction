# Une case en avant (@s = joueur dont c'est le tour)
scoreboard players add @s mg.mpi 1
execute if score @s mg.mpi matches 32.. run scoreboard players set @s mg.mpi 0
function mg:party/place
scoreboard players remove $mpr mg.st 1
execute at @s run playsound minecraft:block.note_block.bell master @a[tag=mg.mpp] ~ ~ ~ 0.8 1.4
title @a[tag=mg.mpp] actionbar [{"selector":"@s","color":"yellow"},{"text":" : encore ","color":"gray"},{"score":{"name":"$mpr","objective":"mg.st"},"color":"gold","bold":true},{"text":" case(s)","color":"gray"}]
execute if score @s mg.mpi = $mps mg.st run function mg:party/star_pass
execute if score $mpr mg.st matches ..0 run function mg:party/land
