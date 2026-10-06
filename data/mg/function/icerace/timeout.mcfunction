# Temps écoulé : le joueur le plus avancé gagne
tellraw @a[tag=mg.play] [{"text":"⛵ Temps écoulé : le plus avancé l'emporte !","color":"gold"}]
scoreboard players set $mx mg.st -1
execute as @a[tag=mg.play] run scoreboard players operation $mx mg.st > @s mg.rp
tag @a remove mg.rtp
execute as @a[tag=mg.play] if score @s mg.rp = $mx mg.st run tag @s add mg.rtp
execute as @a[tag=mg.rtp,limit=1] run function mg:core/win_player
tag @a remove mg.rtp
