# Puits des âmes : l'alpha se réveille
scoreboard players set $od7 mg.st 7
function mg:ombre/m/a_ames
tag @e[tag=mg.ollast] add mg.oldg7
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg7 max 1024
bossbar set mg:oldg7 players @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89]
title @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89] subtitle {"text":"Gardien des âmes","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89] -209.5 46 206.5 1 0.7
