# Forge écarlate : l'alpha se réveille
scoreboard players set $od5 mg.st 7
function mg:ombre/m/a_forgeron
tag @e[tag=mg.ollast] add mg.oldg5
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg5 max 1024
bossbar set mg:oldg5 players @a[x=209,y=51,z=125,dx=27,dy=14,dz=89]
title @a[x=209,y=51,z=125,dx=27,dy=14,dz=89] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=209,y=51,z=125,dx=27,dy=14,dz=89] subtitle {"text":"Forgeron calciné","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=209,y=51,z=125,dx=27,dy=14,dz=89] 222.5 52 200.5 1 0.7
