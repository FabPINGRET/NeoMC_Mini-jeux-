# Tombeaux d'Azhar : l'alpha se réveille
scoreboard players set $od4 mg.st 7
function mg:ombre/m/a_momie
tag @e[tag=mg.ollast] add mg.oldg4
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg4 max 1000
bossbar set mg:oldg4 players @a[x=93,y=47,z=35,dx=89,dy=14,dz=27]
title @a[x=93,y=47,z=35,dx=89,dy=14,dz=27] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=93,y=47,z=35,dx=89,dy=14,dz=27] subtitle {"text":"Momie royale","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=93,y=47,z=35,dx=89,dy=14,dz=27] 106.5 48 48.5 1 0.7
