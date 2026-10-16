# @s : réinitialise ses points (200 ₵)
execute unless score @s mg.tvc matches 200.. run return run tellraw @s {"text":"Il faut 200 ₵ pour redistribuer tes points.","color":"red"}
scoreboard players remove @s mg.tvc 200
scoreboard players operation @s mg.trsp += @s mg.trs1
scoreboard players operation @s mg.trsp += @s mg.trs2
scoreboard players operation @s mg.trsp += @s mg.trs3
scoreboard players operation @s mg.trsp += @s mg.trs4
scoreboard players set @s mg.trs1 0
scoreboard players set @s mg.trs2 0
scoreboard players set @s mg.trs3 0
scoreboard players set @s mg.trs4 0
function mg:terra/rpg/st/apply
tellraw @s {"text":"♻ Points redistribuables (200 ₵).","color":"yellow"}
function mg:terra/rpg/sheet
