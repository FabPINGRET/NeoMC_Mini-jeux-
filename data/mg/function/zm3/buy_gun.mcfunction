# Macro $(n) : arme achetée (déjà possédée → chargeur rempli)
$scoreboard players set $zgn mg.st $(n)
execute as @a[tag=mg.zbuyer] run function mg:zm3/give_gun
