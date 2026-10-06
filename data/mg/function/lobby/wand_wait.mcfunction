# @s = joueur : baguette en recharge
scoreboard players operation $apc mg.st = @s mg.wd
scoreboard players add $apc mg.st 19
scoreboard players set $apk mg.st 20
scoreboard players operation $apc mg.st /= $apk mg.st
title @s actionbar [{"text":"✦ Baguette en recharge : ","color":"gold"},{"score":{"name":"$apc","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gold"}]
