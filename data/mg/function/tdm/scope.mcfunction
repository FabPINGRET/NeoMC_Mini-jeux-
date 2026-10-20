# Lunette (@s = joueur, position exécutée) : clic droit = zoom (lenteur) + cache, de nouveau clic droit = retirée (mg.gads, gun/cl_right)
# mg.tmcr = accroupi (hauteur de tête pour le rayon : la lunette se pose debout aussi)
execute if predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run tag @s add mg.tmcr
execute unless predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run tag @s remove mg.tmcr
execute if entity @s[tag=mg.gads] run return run function mg:tdm/scope_on
execute if entity @s[tag=mg.tmsc] run function mg:tdm/unscope
