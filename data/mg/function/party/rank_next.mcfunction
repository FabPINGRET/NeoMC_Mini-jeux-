# Classement : le meilleur restant (étoiles puis pièces) est affiché, puis on recommence
execute unless entity @a[tag=mg.mpp,tag=!mg.mprk] run return 0
scoreboard players set $rs mg.st -1
execute as @a[tag=mg.mpp,tag=!mg.mprk] if score @s mg.mpk > $rs mg.st run scoreboard players operation $rs mg.st = @s mg.mpk
scoreboard players set $rcn mg.st -1
execute as @a[tag=mg.mpp,tag=!mg.mprk] if score @s mg.mpk = $rs mg.st if score @s mg.mpm > $rcn mg.st run scoreboard players operation $rcn mg.st = @s mg.mpm
execute as @a[tag=mg.mpp,tag=!mg.mprk] if score @s mg.mpk = $rs mg.st if score @s mg.mpm = $rcn mg.st run tag @s add mg.mpcand
scoreboard players add $rk mg.st 1
execute as @a[tag=mg.mpcand,limit=1] run function mg:party/rank_line
tag @a remove mg.mpcand
function mg:party/rank_next
