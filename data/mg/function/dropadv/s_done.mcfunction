# @s a fini tous les niveaux : total d'essais, records, puis spectateur en attendant les autres
scoreboard players set @s mg.dlv 13
tag @s add mg.ddone
gamemode spectator @s
execute if score @s mg.dsk matches 0 run tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" termine les 13 niveaux en ","color":"yellow"},{"score":{"name":"@s","objective":"mg.dtt"},"color":"white","bold":true},{"text":" essais !","color":"yellow"}]
execute if score @s mg.dsk matches 1.. run tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"gold","bold":true},{"text":" arrive au bout : ","color":"yellow"},{"score":{"name":"@s","objective":"mg.dok"},"color":"white","bold":true},{"text":"/13 réussis (","color":"yellow"},{"score":{"name":"@s","objective":"mg.dsk"},"color":"white"},{"text":" passé(s)), ","color":"yellow"},{"score":{"name":"@s","objective":"mg.dtt"},"color":"white","bold":true},{"text":" essais","color":"yellow"}]
execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
clear @s minecraft:warped_fungus_on_a_stick[custom_data~{mg_dskip:1b}]
execute if score @s mg.dsk matches 1.. run return run tellraw @s [{"text":"★ Niveau(x) passé(s) : pas de record cette fois.","color":"gray"}]
scoreboard players set $dsn mg.st 0
execute unless score @s mg.dsb matches 1.. run scoreboard players set $dsn mg.st 1
execute if score @s mg.dsb matches 1.. if score @s mg.dtt < @s mg.dsb run scoreboard players set $dsn mg.st 1
execute if score $dsn mg.st matches 1 run scoreboard players operation @s mg.dsb = @s mg.dtt
execute if score $dsn mg.st matches 1 run tellraw @s [{"text":"★ Nouveau record personnel : ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white"},{"text":" essais !","color":"aqua"}]
execute if score $dsn mg.st matches 0 run tellraw @s [{"text":"★ Ton record reste à ","color":"gray"},{"score":{"name":"@s","objective":"mg.dsb"},"color":"white"},{"text":" essais.","color":"gray"}]
scoreboard players set $dsn mg.st 0
execute unless score #srv mg.dsb matches 1.. run scoreboard players set $dsn mg.st 1
execute if score #srv mg.dsb matches 1.. if score @s mg.dtt < #srv mg.dsb run scoreboard players set $dsn mg.st 1
execute if score $dsn mg.st matches 1 run function mg:dropadv/s_srv
