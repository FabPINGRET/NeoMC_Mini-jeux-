# Chaque seconde (lobby/theme/tick) : recharge des cadeaux, objets retirés aux joueurs occupés ailleurs, effets du ragoût
scoreboard players remove @a[scores={mg.thc=1..}] mg.thc 1
clear @a[tag=mg.play] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.ely] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.xso] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.lk] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.inplot] *[minecraft:custom_data~{mg_thg:1b}]
clear @a[tag=mg.visit] *[minecraft:custom_data~{mg_thg:1b}]
# Ragoût mystère : anciens ragoûts (effets vanilla) retirés ; compte à rebours (mg.ths)
clear @a minecraft:suspicious_stew[minecraft:custom_data={mg_thg:1b}]
scoreboard players remove @a[scores={mg.ths=1..}] mg.ths 1
# à 0, le mini-moi ne reprend pas sa taille sous un plafond bas : reporté d'une seconde
execute as @a[tag=mg.thmini,scores={mg.ths=0}] at @s unless block ~ ~1 ~ #minecraft:replaceable run scoreboard players set @s mg.ths 1
execute as @a[scores={mg.ths=0}] at @s run playsound minecraft:block.amethyst_block.chime neutral @a[distance=..16] ~ ~ ~ 1 0.8
execute as @a[scores={mg.ths=0}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.play,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.ely,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.xso,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.lk,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.inplot,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.visit,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
execute as @a[tag=mg.pkr,scores={mg.ths=1..}] run function mg:lobby/theme/stew_clear
# lapins : tous marqués orphelins, ceux des joueurs lapin sont gardés (stew_rabbit_keep), les autres tués
tag @e[type=minecraft:rabbit,tag=mg.thbun] add mg.thbo
execute as @a[tag=mg.thbun] run function mg:lobby/theme/stew_rabbit_keep
kill @e[type=minecraft:rabbit,tag=mg.thbo]
