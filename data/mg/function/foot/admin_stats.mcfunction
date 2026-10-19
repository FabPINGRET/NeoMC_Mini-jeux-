# Admin (@s) : compteurs d'usage du terrain de foot (objectif mg.ftn) et score en cours (mg.ft)
execute unless score $but mg.ftn matches 0.. run scoreboard players set $but mg.ftn 0
execute unless score $eq mg.ftn matches 0.. run scoreboard players set $eq mg.ftn 0
execute unless score $ent mg.ftn matches 0.. run scoreboard players set $ent mg.ftn 0
execute if score $ftoff mg.st matches 1 run tellraw @s {"text":"⚽ Terrain de foot : désactivé","color":"red"}
execute unless score $ftoff mg.st matches 1 run tellraw @s {"text":"⚽ Terrain de foot : activé","color":"green"}
tellraw @s [{"text":"Usage : ","color":"gray"},{"text":"⚽ Buts ","color":"white"},{"score":{"name":"$but","objective":"mg.ftn"},"color":"yellow"},{"text":" · 🔴🔵 Choix d'équipe ","color":"white"},{"score":{"name":"$eq","objective":"mg.ftn"},"color":"yellow"},{"text":" · 🚪 Entrées ","color":"white"},{"score":{"name":"$ent","objective":"mg.ftn"},"color":"yellow"}]
tellraw @s [{"text":"Score en cours : ","color":"gray"},{"text":"Rouges ","color":"red"},{"score":{"name":"$ftr","objective":"mg.ft"},"color":"red"},{"text":" – ","color":"gray"},{"score":{"name":"$ftb","objective":"mg.ft"},"color":"blue"},{"text":" Bleus · buts libres ","color":"gray"},{"score":{"name":"$ftg","objective":"mg.ft"},"color":"yellow"}]
