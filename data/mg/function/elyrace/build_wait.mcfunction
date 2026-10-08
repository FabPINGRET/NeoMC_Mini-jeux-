# Attend le chargement de la tranche $xbk puis la construit
execute if score $xbk mg.st matches 1 if function mg:elyrace/loaded_1 run return run function mg:elyrace/build_1
execute if score $xbk mg.st matches 2 if function mg:elyrace/loaded_2 run return run function mg:elyrace/build_2
execute if score $xbk mg.st matches 3 if function mg:elyrace/loaded_3 run return run function mg:elyrace/build_3
execute if score $xbk mg.st matches 4 if function mg:elyrace/loaded_4 run return run function mg:elyrace/build_4
execute if score $xbk mg.st matches 5 if function mg:elyrace/loaded_5 run return run function mg:elyrace/build_5
execute if score $xbk mg.st matches 6 if function mg:elyrace/loaded_6 run return run function mg:elyrace/build_6
execute if score $xbk mg.st matches 7 if function mg:elyrace/loaded_7 run return run function mg:elyrace/build_7
execute if score $xbk mg.st matches 8 if function mg:elyrace/loaded_8 run return run function mg:elyrace/build_8
execute if score $xbk mg.st matches 9 if function mg:elyrace/loaded_9 run return run function mg:elyrace/build_9
execute if score $xbk mg.st matches 10 if function mg:elyrace/loaded_10 run return run function mg:elyrace/build_10
execute if score $xbk mg.st matches 11 if function mg:elyrace/loaded_11 run return run function mg:elyrace/build_11
scoreboard players add $xbw mg.st 1
# 2 minutes sans chargement : message, puis on libère les chargements forcés des tranches et on s'arrête
execute if score $xbw mg.st matches 120.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : zone pas chargée (tranche ","color":"red"},{"score":{"name":"$xbk","objective":"mg.st"},"color":"red"},{"text":"). Relance /function mg:elyrace/build.","color":"red"}]
execute if score $xbw mg.st matches 120.. run return run function mg:elyrace/build_abort
schedule function mg:elyrace/build_wait 20t
