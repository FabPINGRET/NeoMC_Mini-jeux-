# Temps écoulé : un arrivé en ligne gagne, sinon le plus avancé (anneaux validés, puis x maximal) ; rien parcouru : égalité
execute if entity @a[tag=mg.play,scores={mg.xf=1..}] run return run function mg:elyrace/end
tellraw @a[tag=mg.play] [{"text":"🪽 Temps écoulé : le plus avancé l'emporte !","color":"gold"}]
# clé de classement par joueur (dans mg.xx, libre à ce stade) : anneaux * 2000 + x maximal
scoreboard players set #k2000 mg.st 2000
execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx = @s mg.xa
execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx *= #k2000 mg.st
execute as @a[tag=mg.play] run scoreboard players operation @s mg.xx += @s mg.xp
scoreboard players set #mx mg.st -1
execute as @a[tag=mg.play] run scoreboard players operation #mx mg.st > @s mg.xx
execute if score #mx mg.st matches ..32 run return run function mg:core/draw
tag @a remove mg.xtp
execute as @a[tag=mg.play] if score @s mg.xx = #mx mg.st run tag @s add mg.xtp
execute as @a[tag=mg.xtp,limit=1] run function mg:core/win_player
tag @a remove mg.xtp
