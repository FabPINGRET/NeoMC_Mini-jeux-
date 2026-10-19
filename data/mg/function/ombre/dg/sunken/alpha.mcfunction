# Temple englouti : l'alpha se réveille
scoreboard players set $od3 mg.st 7
function mg:ombre/m/a_noye
tag @e[tag=mg.ollast] add mg.oldg3
tag @e[tag=mg.ollast] add mg.oldg
tag @e[tag=mg.ollast] add mg.oldga
execute as @e[tag=mg.ollast] run data merge entity @s {CustomNameVisible:1b,Glowing:1b}
bossbar set mg:oldg3 max 820
bossbar set mg:oldg3 players @a[x=132,y=47,z=-213,dx=89,dy=14,dz=27]
title @a[x=132,y=47,z=-213,dx=89,dy=14,dz=27] title {"text":"ALPHA","color":"dark_red","bold":true}
title @a[x=132,y=47,z=-213,dx=89,dy=14,dz=27] subtitle {"text":"Gardien noyé","color":"gray"}
playsound minecraft:entity.ravager.roar hostile @a[x=132,y=47,z=-213,dx=89,dy=14,dz=27] 207.5 48 -199.5 1 0.7
