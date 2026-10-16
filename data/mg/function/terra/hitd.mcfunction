# @s (cible) : dégâts du tir ($(d)) et chiffre flottant
$damage @s $(d) minecraft:player_attack by @a[tag=mg.tvsh,limit=1]
$execute at @s run function mg:terra/rpg/dmgnum {d:$(d)}
