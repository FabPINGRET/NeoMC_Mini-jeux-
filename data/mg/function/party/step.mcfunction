# Une case en avant (@s = joueur dont c'est le tour). Sur un embranchement : choix de la route d'abord
function mg:party/is_fork
execute if score $fk mg.st matches 1 if score $mpch mg.st matches 0 run return run function mg:party/fork_ask
execute if score $fk mg.st matches 1 run function mg:party/next_fork
execute if score $fk mg.st matches 0 run function mg:party/next
scoreboard players set $mpch mg.st 0
function mg:party/place
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run tp @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] ~ ~3 ~
scoreboard players remove $mpr mg.st 1
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] run playsound minecraft:block.note_block.bell master @a[tag=mg.mpp] ~ ~ ~ 0.8 1.4
title @a[tag=mg.mpp] actionbar [{"selector":"@s","color":"yellow"},{"text":" : encore ","color":"gray"},{"score":{"name":"$mpr","objective":"mg.st"},"color":"gold","bold":true},{"text":" case(s)","color":"gray"}]
execute if score @s mg.mpi = $mps mg.st run function mg:party/star_pass
function mg:party/case_type
execute if score $ct mg.st matches 6 if score @s mg.mpm matches 10.. run return run function mg:party/shop_open
execute if score $mpr mg.st matches ..0 run function mg:party/land
