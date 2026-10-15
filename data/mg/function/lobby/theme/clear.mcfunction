# Retire toutes les entités des thèmes : titre, animaux (et leur habillage), habillages orphelins
kill @e[type=minecraft:item_display,tag=mg.thrid]
execute as @e[tag=mg.thmob] run function mg:lobby/theme/gone
kill @e[tag=mg.thx]
# anciens mondes : le titre portait mg.thm (tag que Tron utilise aussi : jamais de kill générique dessus)
kill @e[type=minecraft:text_display,tag=mg.lby,tag=mg.thm,x=-80,y=30,z=-80,dx=160,dy=120,dz=160]
