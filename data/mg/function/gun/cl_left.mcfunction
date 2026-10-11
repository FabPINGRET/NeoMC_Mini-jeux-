# @s : clic gauche avec une arme → tir (boucles existantes) ; mitraillette : rafale de 8 ticks
scoreboard players set @s mg.qs 1
scoreboard players set @s mg.gqs 1
execute if items entity @s weapon.mainhand *[custom_data~{gun:2}] run scoreboard players set @s mg.gbu 8
