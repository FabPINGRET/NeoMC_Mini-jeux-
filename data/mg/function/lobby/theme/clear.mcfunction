# Retire toutes les entités des thèmes (titre, animaux, habillages)
kill @e[type=minecraft:item_display,tag=mg.thrid]
execute as @e[tag=mg.thmob] run function mg:lobby/theme/gone
kill @e[tag=mg.thm]
