# Mines profondes : l'alpha se réveille
scoreboard players set $od6 mg.st 7
function mg:ombre/m/a_contremaitre
tag @e[tag=mg.ollast] add mg.oldg6
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg6 max 1024
bossbar set mg:oldg6 players @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89]
title @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89] subtitle {"text":"Contremaître maudit","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89] -47.5 48 218.5 1 0.7
