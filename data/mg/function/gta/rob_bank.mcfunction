# @s braque la banque : 15 s dans la salle des coffres, alarme, 4 étoiles d'un coup
scoreboard players add @s mg.grob 5
function mg:gta/rob_bar_bank
execute if score @s mg.grob matches 5 run tellraw @a[tag=mg.gtw] [{"text":"🚨 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" braque la banque de Neo City !","color":"red","bold":true}]
execute if score @s mg.grob matches 5 if score @s mg.gwl matches ..3 run scoreboard players set @s mg.gwl 4
execute if score @s mg.grob matches 5 run scoreboard players set @s mg.gwt 300
execute if score @s mg.grob matches 5 run team leave @s
scoreboard players operation $gbk mg.st = @s mg.grob
scoreboard players set #20 mg.st 20
scoreboard players operation $gbk mg.st %= #20 mg.st
execute if score $gbk mg.st matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 0.8
execute if score $gbk mg.st matches 15 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 1.1
execute if score @s mg.grob matches 300.. run function mg:gta/rob_bank_ok
