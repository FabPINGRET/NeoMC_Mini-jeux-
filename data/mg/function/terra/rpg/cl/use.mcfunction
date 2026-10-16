# @s : clic droit sur l'objet de capacité
execute if score @s mg.trcd matches 1.. run return run function mg:terra/rpg/cl/wait
scoreboard players set $rk mg.st 1
execute if score @s mg.trlv matches 5.. run scoreboard players set $rk mg.st 2
execute if score @s mg.trlv matches 10.. run scoreboard players set $rk mg.st 3
execute if score @s mg.trlv matches 15.. run scoreboard players set $rk mg.st 4
execute if score @s mg.trcl matches 1 run scoreboard players set @s mg.trcd 300
execute if score @s mg.trcl matches 1 if score $rk mg.st matches 4 run scoreboard players set @s mg.trcd 200
execute if score @s mg.trcl matches 1 run function mg:terra/rpg/cl/act_soldat
execute if score @s mg.trcl matches 2 run scoreboard players set @s mg.trcd 300
execute if score @s mg.trcl matches 2 if score $rk mg.st matches 4 run scoreboard players set @s mg.trcd 200
execute if score @s mg.trcl matches 2 run function mg:terra/rpg/cl/act_eclaireur
execute if score @s mg.trcl matches 3 run scoreboard players set @s mg.trcd 400
execute if score @s mg.trcl matches 3 if score $rk mg.st matches 4 run scoreboard players set @s mg.trcd 280
execute if score @s mg.trcl matches 3 run function mg:terra/rpg/cl/act_scientifique
execute if score @s mg.trcl matches 4 run scoreboard players set @s mg.trcd 500
execute if score @s mg.trcl matches 4 if score $rk mg.st matches 4 run scoreboard players set @s mg.trcd 360
execute if score @s mg.trcl matches 4 run function mg:terra/rpg/cl/act_ingenieur
