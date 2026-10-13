# 🎄 Noël : animaux du thème, chaque seconde (joueur au spawn : chunks chargés, comptes justes)
execute unless entity @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,limit=1] run return 0
execute as @e[tag=mg.thmob] unless entity @s[x=-78,y=50,z=-78,dx=156,dy=70,dz=156] run function mg:lobby/theme/spot {f:"lobby/theme/back"}
execute store result score $thn mg.st if entity @e[type=minecraft:snow_golem,tag=mg.th_snowman]
execute if score $thn mg.st matches ..5 run function mg:lobby/theme/spot {f:"lobby/theme/noel/snowman"}
execute if score $thn mg.st matches 7.. as @e[type=minecraft:snow_golem,tag=mg.th_snowman,limit=1,sort=random] run function mg:lobby/theme/gone
execute store result score $thn mg.st if entity @e[type=minecraft:cow,tag=mg.th_reindeer]
execute if score $thn mg.st matches ..2 run function mg:lobby/theme/spot {f:"lobby/theme/noel/reindeer"}
execute if score $thn mg.st matches 4.. as @e[type=minecraft:cow,tag=mg.th_reindeer,limit=1,sort=random] run function mg:lobby/theme/gone
execute store result score $thn mg.st if entity @e[type=minecraft:cow,tag=mg.th_rudolph]
execute if score $thn mg.st matches ..0 run function mg:lobby/theme/spot {f:"lobby/theme/noel/rudolph"}
execute if score $thn mg.st matches 2.. as @e[type=minecraft:cow,tag=mg.th_rudolph,limit=1,sort=random] run function mg:lobby/theme/gone
