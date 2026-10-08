# Fin : le plus de points gagne (égalité ou 0 point = pas de vainqueur)
tp @a[tag=mg.play] 0.5 64 19420.5
gamemode adventure @a[tag=mg.play]
scoreboard players set $tmax mg.st 0
scoreboard players operation $tmax mg.st > @a[tag=mg.play] mg.tpt
execute if score $tmax mg.st matches 0 run tellraw @a[tag=!mg.surv] {"text":"📞 Aucun mot n'a survécu jusqu'au bout : pas de vainqueur !","color":"gold"}
execute if score $tmax mg.st matches 0 run return run function mg:core/draw
scoreboard players set $twn mg.st 0
execute as @a[tag=mg.play] if score @s mg.tpt = $tmax mg.st run scoreboard players add $twn mg.st 1
execute if score $twn mg.st matches 2.. run tellraw @a[tag=!mg.surv] {"text":"📞 Égalité en tête : pas de vainqueur unique !","color":"gold"}
execute if score $twn mg.st matches 2.. run return run function mg:core/draw
execute as @a[tag=mg.play] if score @s mg.tpt = $tmax mg.st run function mg:core/win_player
