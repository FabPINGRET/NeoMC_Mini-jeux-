# Lunette (@s = duelliste, position exécutée) : accroupi = zoom (lenteur) + cache ; se relever la retire
execute if predicate {condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}} run return run function mg:duel/scope_on
execute if entity @s[tag=mg.dlsc] run function mg:duel/unscope
