# Décor du spawn (entités mg.lby) : modèles du resource pack si $rp = 1, sinon vanilla (généré)
kill @e[tag=mg.lby]
kill @e[type=minecraft:text_display,tag=mg.deco]
function mg:lobby/deco_common
execute if score $rp mg.st matches 1 run function mg:lobby/deco_rp
execute unless score $rp mg.st matches 1 run function mg:lobby/deco_vn
