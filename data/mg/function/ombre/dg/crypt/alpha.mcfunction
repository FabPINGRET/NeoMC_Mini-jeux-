# Cryptes de Valdor : l'alpha se réveille
scoreboard players set $od0 mg.st 7
function mg:ombre/m/a_crypte
tag @e[tag=mg.ollast] add mg.oldg0
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg0 max 320
bossbar set mg:oldg0 players @a[x=-131,y=49,z=-37,dx=27,dy=14,dz=89]
title @a[x=-131,y=49,z=-37,dx=27,dy=14,dz=89] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=-131,y=49,z=-37,dx=27,dy=14,dz=89] subtitle {"text":"Seigneur des cryptes","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=-131,y=49,z=-37,dx=27,dy=14,dz=89] -117.5 50 38.5 1 0.7
