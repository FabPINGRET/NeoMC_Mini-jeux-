# Macro {m} : matière des morceaux cochés (p.k1..k6)
$execute if data storage mg:cham p.k1 as @e[type=minecraft:block_display,tag=mg.cmk1] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
$execute if data storage mg:cham p.k2 as @e[type=minecraft:block_display,tag=mg.cmk2] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
$execute if data storage mg:cham p.k3 as @e[type=minecraft:block_display,tag=mg.cmk3] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
$execute if data storage mg:cham p.k4 as @e[type=minecraft:block_display,tag=mg.cmk4] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
$execute if data storage mg:cham p.k5 as @e[type=minecraft:block_display,tag=mg.cmk5] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
$execute if data storage mg:cham p.k6 as @e[type=minecraft:block_display,tag=mg.cmk6] if score @s mg.cmid = $cmid mg.st run data modify entity @s block_state set from storage mg:cham mats[$(m)]
