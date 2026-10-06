# Donne ses PV de boss à @s (macro : hp, name = JSON du nom) + barre de vie de boss
$attribute @s minecraft:max_health base set $(hp)
$data modify entity @s Health set value $(hp)f
$scoreboard players set $bmax mg.st $(hp)
tag @s remove mg.bossn
tag @s add mg.boss
bossbar add mg:boss {"text":"BOSS","color":"dark_red"}
$bossbar set mg:boss name $(name)
$bossbar set mg:boss max $(hp)
bossbar set mg:boss color red
bossbar set mg:boss style notched_10
bossbar set mg:boss visible true
