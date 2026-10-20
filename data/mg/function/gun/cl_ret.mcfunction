# Viseur au centre de l'écran pour ceux qui visent au lobby (Neo GTA a le sien : gta/aim)
scoreboard players set $gcret mg.st 0
# sauf le duel et le TDM : leur lunette (duel/scope, tdm/scope) pose son propre cache
title @a[tag=mg.gads,tag=!mg.gtw,tag=!mg.dl,tag=!mg.play] times 0 5 2
execute if score $rp mg.st matches 1 run title @a[tag=mg.gads,tag=!mg.gtw,tag=!mg.dl,tag=!mg.play] title {"text":"","font":"mg:gta","color":"white","shadow_color":0}
execute unless score $rp mg.st matches 1 run title @a[tag=mg.gads,tag=!mg.gtw,tag=!mg.dl,tag=!mg.play] title {"text":"+","color":"white"}
