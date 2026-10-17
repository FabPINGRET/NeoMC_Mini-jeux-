# Aventure : @s arrive au bout après au moins une passe : pas de victoire, spectateur, la partie continue
tag @s add mg.ddone
gamemode spectator @s
clear @s minecraft:warped_fungus_on_a_stick[custom_data~{mg_dskip:1b}]
tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" arrive au bout : ","color":"yellow"},{"score":{"name":"@s","objective":"mg.dok"},"color":"white","bold":true},{"text":"/13 réussis, ","color":"yellow"},{"score":{"name":"@s","objective":"mg.dsk"},"color":"white"},{"text":" passé(s) — pas de victoire à l'arrivée (classement final aux niveaux réussis)","color":"yellow"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
