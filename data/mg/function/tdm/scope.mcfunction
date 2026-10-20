# Lunette (@s = joueur, position exécutée) : accroupi = zoom (lenteur) + cache ; se relever la retire
execute if predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run return run function mg:tdm/scope_on
execute if entity @s[tag=mg.tmsc] run function mg:tdm/unscope
