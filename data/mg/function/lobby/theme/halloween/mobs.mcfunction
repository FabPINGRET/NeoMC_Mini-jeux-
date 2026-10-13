# 🎃 Halloween : animaux du thème, chaque seconde (joueur au spawn : chunks chargés, comptes justes)
execute unless entity @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,limit=1] run return 0
execute as @e[tag=mg.thmob] unless entity @s[x=-78,y=50,z=-78,dx=156,dy=70,dz=156] run function mg:lobby/theme/spot {f:"lobby/theme/back"}
execute store result score $thn mg.st if entity @e[type=minecraft:bat,tag=mg.th_bat]
execute if score $thn mg.st matches ..7 run function mg:lobby/theme/spot {f:"lobby/theme/halloween/bat"}
execute if score $thn mg.st matches 9.. as @e[type=minecraft:bat,tag=mg.th_bat,limit=1,sort=random] run function mg:lobby/theme/gone
execute store result score $thn mg.st if entity @e[type=minecraft:allay,tag=mg.th_ghost]
execute if score $thn mg.st matches ..5 run function mg:lobby/theme/spot {f:"lobby/theme/halloween/ghost"}
execute if score $thn mg.st matches 7.. as @e[type=minecraft:allay,tag=mg.th_ghost,limit=1,sort=random] run function mg:lobby/theme/gone
# habillage : chaque animal à habiller a son item_display monté, les orphelins disparaissent
execute if score $rp mg.st matches 1 run tag @e[tag=mg.thdress] add mg.thnd
execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle run tag @s remove mg.thnd
execute as @e[tag=mg.thnd,tag=mg.th_ghost] at @s run function mg:lobby/theme/halloween/dress_ghost
tag @e[tag=mg.thnd] remove mg.thnd
tag @e[type=minecraft:item_display,tag=mg.thrid] add mg.thor
execute as @e[tag=mg.thmob] on passengers run tag @s remove mg.thor
kill @e[tag=mg.thor]
# un objet donné à un allay retombe par terre (on ne le perd pas, l'allay ne le duplique pas)
execute as @e[type=minecraft:allay,tag=mg.thmob] if items entity @s weapon.mainhand * at @s run function mg:lobby/theme/allay_drop
