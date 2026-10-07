# Mes statistiques (@s = joueur) — via /trigger mg.opt set 25
execute unless score @s mg.wins = @s mg.wins run scoreboard players set @s mg.wins 0
execute unless score @s mg.stp = @s mg.stp run scoreboard players set @s mg.stp 0
execute unless score @s mg.stk = @s mg.stk run scoreboard players set @s mg.stk 0
tellraw @s [{"text":"— Mes statistiques —","color":"gold","bold":true}]
tellraw @s [{"text":"✦ Victoires : ","color":"gray"},{"score":{"name":"@s","objective":"mg.wins"},"color":"gold"},{"text":"   ▶ Parties jouées : ","color":"gray"},{"score":{"name":"@s","objective":"mg.stp"},"color":"white"},{"text":"   ⚔ Kills (toutes parties) : ","color":"gray"},{"score":{"name":"@s","objective":"mg.stk"},"color":"red"}]
