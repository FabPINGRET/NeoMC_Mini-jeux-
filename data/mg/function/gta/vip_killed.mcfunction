# Avancement mg:gta_vip : @s a tué la cible d'un Contrat (la sienne ou non : mis_tick vérifie que c'est la sienne qui manque)
advancement revoke @s only mg:gta_vip
execute if score @s mg.gmt matches 2 run scoreboard players set @s mg.gmvk 1
