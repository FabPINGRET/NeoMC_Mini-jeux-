scoreboard players set $mph mg.st 5
scoreboard players set $mpw mg.st 120
title @a[tag=mg.mpp] times 0 30 5
tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"text":"Fin du tour ","color":"gray"},{"score":{"name":"$mpround","objective":"mg.st"},"color":"white"},{"text":" : place au mini-jeu ! ","color":"gray"},{"text":"(vainqueur +10 pièces, les autres +3)","color":"dark_gray"}]
title @a[tag=mg.mpp] subtitle [{"text":"Mini-jeu...","color":"gray"}]
