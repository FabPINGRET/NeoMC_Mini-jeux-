# Attend le chargement de la tranche $xbk puis la construit (parcours 1)
# $xbk à 0 = aucune construction en cours (arrêtée par build_abort, build_fail ou core/load) : un schedule resté en attente s'éteint ici
execute if score $xbk mg.st matches 0 run return 0
# une partie démarre pendant la construction (course, solo ou autre jeu) : on ne construit pas (les remplissages sont lourds) et $xbw
# n'avance pas (pas de faux build_fail). Choix assumé : la tranche en cours reste chargée de force pendant la pause (la relâcher puis
# la recharger ferait ré-attendre le chargement) ; la pause dure autant que la partie, jusqu'à ce que $state revienne à 0
# et que les solos soient finis (un solo ne passe pas par $state : garde propre, SOLO_BUSY)
execute unless score $state mg.st matches 0 run return run schedule function mg:elyrace/c1/build_wait 20t
execute if entity @a[tag=mg.xso] run return run schedule function mg:elyrace/c1/build_wait 20t
execute if score $xbk mg.st matches 1 if function mg:elyrace/c1/loaded_1 run return run function mg:elyrace/c1/clear_1
execute if score $xbk mg.st matches 2 if function mg:elyrace/c1/loaded_2 run return run function mg:elyrace/c1/clear_2
execute if score $xbk mg.st matches 3 if function mg:elyrace/c1/loaded_3 run return run function mg:elyrace/c1/clear_3
execute if score $xbk mg.st matches 4 if function mg:elyrace/c1/loaded_4 run return run function mg:elyrace/c1/clear_4
execute if score $xbk mg.st matches 5 if function mg:elyrace/c1/loaded_5 run return run function mg:elyrace/c1/clear_5
execute if score $xbk mg.st matches 6 if function mg:elyrace/c1/loaded_6 run return run function mg:elyrace/c1/clear_6
execute if score $xbk mg.st matches 7 if function mg:elyrace/c1/loaded_7 run return run function mg:elyrace/c1/clear_7
execute if score $xbk mg.st matches 8 if function mg:elyrace/c1/loaded_8 run return run function mg:elyrace/c1/clear_8
execute if score $xbk mg.st matches 9 if function mg:elyrace/c1/loaded_9 run return run function mg:elyrace/c1/clear_9
execute if score $xbk mg.st matches 10 if function mg:elyrace/c1/loaded_10 run return run function mg:elyrace/c1/clear_10
execute if score $xbk mg.st matches 11 if function mg:elyrace/c1/loaded_11 run return run function mg:elyrace/c1/clear_11
scoreboard players add $xbw mg.st 1
# 2 minutes sans chargement : message, puis on libère les chargements forcés des tranches et on s'arrête
execute if score $xbw mg.st matches 120.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : zone pas chargée (parcours 1, tranche ","color":"red"},{"score":{"name":"$xbk","objective":"mg.st"},"color":"red"},{"text":"). Relance /function mg:elyrace/c1/build.","color":"red"}]
execute if score $xbw mg.st matches 120.. run return run function mg:elyrace/c1/build_fail
schedule function mg:elyrace/c1/build_wait 20t
