# Réapparition (@s = joueur) : ailleurs dans l'arène, railgun rechargé, 2 s d'invincibilité
scoreboard players set @s mg.deaths 0
scoreboard players set @s mg.ks 0
scoreboard players set @s mg.cd 0
function mg:quake/spread_one
function mg:quake/kit
function mg:quake/fx
tag @s add mg.prot
scoreboard players set @s mg.qp 60
tag @s remove mg.qdd
gamemode adventure @s
