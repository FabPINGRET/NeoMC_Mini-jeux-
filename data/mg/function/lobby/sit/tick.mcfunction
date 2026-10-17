# Appelé chaque tick (core/tick) tant qu'un joueur porte mg.sit
# refus (partie, survie, plot, coupé par un admin...) : on se lève
execute as @a[tag=mg.sit] unless function mg:lobby/sit/ok run function mg:lobby/sit/stand
# balayage : tout siège et tout assis sont candidats (mg.seato) ; chacun perd la marque s'il est lié à l'autre
tag @e[type=minecraft:item_display,tag=mg.seat] add mg.seato
tag @a[tag=mg.sit] add mg.seato
execute as @a[tag=mg.sit] on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat] run tag @s remove mg.seato
execute as @e[type=minecraft:item_display,tag=mg.seat] on passengers if entity @s[tag=mg.sit] run tag @s remove mg.seato
# restent : les assis sans siège (Maj vanilla, reconnexion, mort) et les sièges sans assis
execute as @a[tag=mg.seato] run function mg:lobby/sit/stand
kill @e[type=minecraft:item_display,tag=mg.seato]
tag @a remove mg.seato
