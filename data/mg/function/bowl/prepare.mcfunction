# 🎳 Bowling — préparation : salle (asynchrone), pistes attribuées, joueurs en trop spectateurs
function mg:bowl/build_1
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 72
scoreboard players set $pz mg.st 35146
scoreboard players set $bt mg.st 0
scoreboard players set $bend mg.st 0
tag @a remove mg.bwl
tag @a remove mg.bnr
scoreboard players reset * mg.bln
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
scoreboard players set #km1 mg.st -1
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:3,c:"-3.5",b:-3500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:4,c:"3.5",b:3500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:2,c:"-10.5",b:-10500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:5,c:"10.5",b:10500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:1,c:"-17.5",b:-17500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:6,c:"17.5",b:17500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:0,c:"-24.5",b:-24500}
execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {l:7,c:"24.5",b:24500}
execute as @a[tag=mg.play,tag=!mg.bwl] run function mg:bowl/extra
