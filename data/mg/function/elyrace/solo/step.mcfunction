# @s = joueur en solo, vivant (@e[type=player]) : filet, décompte, course, arrivée
# filet : une partie l'a pris comme participant (ne devrait pas arriver, il est en pause) : le solo s'arrête
execute if entity @s[tag=mg.play] run return run function mg:elyrace/solo/stop
# lobby/wind_used (charge de vent) donne slow_falling : retiré, il fausserait la glisse
effect clear @s minecraft:slow_falling
execute if score @s mg.xph matches 1 run return run function mg:elyrace/solo/countdown
# phase 3 (arrivée) : 30 ticks pour lire le temps, puis retour au lobby ; aucune règle de course
execute if score @s mg.xph matches 3 if score @s mg.xst matches 30.. run return run function mg:elyrace/solo/stop
execute if score @s mg.xph matches 3 run return 0
# phase 2 : le tick du parcours (règles, anneaux, reprises), puis HUD et limite de temps
# (l'arrivée a pu passer le joueur en phase 3 pendant ce tick : plus de HUD ni de limite)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/player
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/player
execute unless score @s mg.xph matches 2 run return 0
scoreboard players operation #xm mg.st = @s mg.xst
scoreboard players operation #xm mg.st %= #k10 mg.st
execute if score #xm mg.st matches 0 run function mg:elyrace/hud
execute if score @s mg.xst matches 3000 run tellraw @s [{"text":"🪽 Plus que 30 secondes !","color":"gold"}]
execute if score @s mg.xst matches 3600.. run tellraw @s [{"text":"⏱ Temps écoulé (3 minutes) : contre-la-montre terminé sans arrivée.","color":"gray"}]
execute if score @s mg.xst matches 3600.. run function mg:elyrace/solo/stop
