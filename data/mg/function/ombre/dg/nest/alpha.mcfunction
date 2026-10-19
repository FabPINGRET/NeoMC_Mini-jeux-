# Nid des tisseuses : l'alpha se réveille
scoreboard players set $od1 mg.st 7
function mg:ombre/m/a_tisseuse
tag @e[tag=mg.ollast] add mg.oldg1
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg1 max 480
bossbar set mg:oldg1 players @a[x=-225,y=53,z=-211,dx=27,dy=14,dz=89]
title @a[x=-225,y=53,z=-211,dx=27,dy=14,dz=89] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=-225,y=53,z=-211,dx=27,dy=14,dz=89] subtitle {"text":"Tisseuse alpha","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=-225,y=53,z=-211,dx=27,dy=14,dz=89] -211.5 54 -197.5 1 0.7
