# @s = admin (mg.xs 4) : arrête tous les contre-la-montre solo (sans toucher à core/abort : le solo n'est pas une partie)
execute unless entity @s[tag=mg.admin] run return run tellraw @s [{"text":"⚠ Réservé aux admins.","color":"red"}]
execute unless entity @a[tag=mg.xso] run return run tellraw @s [{"text":"Aucun contre-la-montre solo en cours.","color":"gray"}]
tellraw @a[tag=mg.xso] [{"selector":"@s","color":"yellow"},{"text":" a arrêté les contre-la-montre solo.","color":"red"}]
execute as @a[tag=mg.xso] run function mg:elyrace/solo/stop
