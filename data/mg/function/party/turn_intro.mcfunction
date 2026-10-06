# Annonce du tour (1,5 s) puis le joueur reçoit le dé
scoreboard players remove $mpw mg.st 1
execute if score $mpw mg.st matches 1.. run return 0
scoreboard players set $mph mg.st 1
scoreboard players set $mdn mg.st 1
scoreboard players set $mpw mg.st 400
execute as @a[tag=mg.mpcur] run function mg:party/give_dice
