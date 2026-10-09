# Récompense de mg:cham_hit : @s (chasseur) a frappé un joueur
advancement revoke @s only mg:cham_hit
execute unless entity @s[tag=mg.cms] run return 0
tag @s add mg.cmhunt
execute as @a[tag=mg.cmh,tag=!mg.cmout] if data entity @s {HurtTime:10s} run function mg:cham/found
tag @s remove mg.cmhunt
