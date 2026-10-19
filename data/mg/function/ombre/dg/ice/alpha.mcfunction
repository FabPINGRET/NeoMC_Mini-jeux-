# Grotte de givre : l'alpha se réveille
scoreboard players set $od2 mg.st 7
function mg:ombre/m/a_wendigo
tag @e[tag=mg.ollast] add mg.oldg2
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg2 max 640
bossbar set mg:oldg2 players @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27]
title @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27] subtitle {"text":"Wendigo des glaces","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27] 44.5 66 -189.5 1 0.7
