# Lunette (@s = duelliste, position exécutée) : clic droit = zoom (lenteur) + cache, de nouveau clic droit = retirée (mg.gads, gun/cl_right)
# mg.dlcr = accroupi (hauteur de tête pour le rayon : la lunette se pose debout aussi)
execute if predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run tag @s add mg.dlcr
execute unless predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run tag @s remove mg.dlcr
execute if entity @s[tag=mg.gads] run return run function mg:duel/scope_on
execute if entity @s[tag=mg.dlsc] run function mg:duel/unscope
