scoreboard players set vyrn_machine bool 0
execute if items entity @p[gamemode=!spectator,tag=mg.flw] weapon.* minecraft:shield run scoreboard players set vyrn_machine bool 1
execute if score vyrn_machine bool matches 1 run tag @p[gamemode=!spectator,tag=mg.flw] add vyrn
execute if score vyrn_machine bool matches 1 run advancement grant @p[tag=!spectator,tag=mg.flw] only sidequest_2:npc_vyrn
execute as @a[tag=mg.flw] run function game:100_check
execute if score vyrn_machine bool matches 1 run tellraw @p[gamemode=!spectator,tag=mg.flw] [{"text":"Your shield has been empowered with","color":"gray","italic":true},{"text":" Vyrn's Enfeeblement","color":"green"},{"text":"! This effect will remain even if you change your ","color":"gray"},{"text":"shield pattern","color":"aqua"},{"text":"...","color":"gray"}]
execute if score vyrn_machine bool matches 1 run playsound minecraft:item.totem.use master @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute if score vyrn_machine bool matches 1 at @p[gamemode=!spectator,tag=mg.flw] run particle minecraft:scrape ~ ~1 ~ 0.5 0.7 0.5 0.5 200
