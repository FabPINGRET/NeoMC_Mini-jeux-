# @s : redistribue ses points (300 💰, maître d'armes)
execute unless score @s mg.olg matches 300.. run return run tellraw @s {"text":"Il faut 300 💰.","color":"red"}
scoreboard players remove @s mg.olg 300
scoreboard players operation @s mg.olsp += @s mg.ols1
scoreboard players operation @s mg.olsp += @s mg.ols2
scoreboard players operation @s mg.olsp += @s mg.ols3
scoreboard players operation @s mg.olsp += @s mg.ols4
scoreboard players set @s mg.ols1 0
scoreboard players set @s mg.ols2 0
scoreboard players set @s mg.ols3 0
scoreboard players set @s mg.ols4 0
function mg:ombre/stats
tellraw @s {"text":"♻ Points redistribuables.","color":"yellow"}
