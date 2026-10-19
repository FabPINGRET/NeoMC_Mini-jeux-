# Bandeau du thème en place (chaque seconde, lobby/theme/tick) : une ligne toutes les 8 s, puis rien jusqu'à la fin du cycle de 180 s ($thbt = seconde du cycle)
execute if score $thbt mg.st matches 179.. run scoreboard players set $thbt mg.st -1
# $thbt absent (thème posé ou redémarrage) : le cycle repart à 0, la première ligne dure ses 8 s pleines
execute unless score $thbt mg.st matches 0.. run scoreboard players set $thbt mg.st -1
scoreboard players add $thbt mg.st 1
# l'événement du lobby a sa bossbar mg:ev (get visible : succès = existence ; mg:ev n'est jamais masquée, elle n'existe que pendant l'annonce et l'événement) : le bandeau s'efface
execute store success score $thbe mg.st run bossbar get mg:ev visible
execute if score $thbe mg.st matches 1 run return run function mg:lobby/theme/banner_hide
scoreboard players set #thb8 mg.st 8
scoreboard players operation $thbl mg.st = $thbt mg.st
scoreboard players operation $thbl mg.st /= #thb8 mg.st
scoreboard players add $thbl mg.st 1
# passé la dernière ligne : barre retirée jusqu'à la prochaine période
execute if score $theme mg.st matches 1 if score $thbl mg.st matches 6.. run return run function mg:lobby/theme/banner_hide
execute if score $theme mg.st matches 2 if score $thbl mg.st matches 7.. run return run function mg:lobby/theme/banner_hide
# mg:thb absente (la bossbar n'a jamais été masquée : le succès de get visible vaut son existence)
execute store success score $thbe mg.st run bossbar get mg:thb visible
execute if score $thbe mg.st matches 0 run bossbar add mg:thb ""
execute if score $theme mg.st matches 1 run function mg:lobby/theme/halloween/banner
execute if score $theme mg.st matches 2 run function mg:lobby/theme/noel/banner
execute in minecraft:overworld run bossbar set mg:thb players @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,gamemode=!spectator]
