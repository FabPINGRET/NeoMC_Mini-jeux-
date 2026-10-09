# Fenêtre texte « version du datapack » (@s = admin)
tellraw @s [{"text":"\n","color":"gold"},{"text":"ℹ VERSION DU DATAPACK","color":"gold","bold":true}]
execute unless data storage mg:version files run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"En place : ","color":"white","bold":true},{"text":"inconnue (pack non déployé par datapack-sync, ou datapack-sync pas encore mis à jour)","color":"gray"}]
execute if data storage mg:version files run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"En place : ","color":"white","bold":true},{"nbt":"files.commit","storage":"mg:version","color":"yellow","bold":true},{"text":" du ","color":"gray"},{"nbt":"files.date","storage":"mg:version","color":"yellow"},{"text":"\n   ","color":"gray"},{"nbt":"files.subject","storage":"mg:version","color":"gray","italic":true}]
execute store result score $vg mg.st run data get storage mg:version gt
function mg:version/ago
tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"Chargée","color":"white"},{"text":" (il y a ","color":"gray"},{"score":{"name":"$vh","objective":"mg.st"},"color":"gray"},{"text":" h ","color":"gray"},{"score":{"name":"$vm","objective":"mg.st"},"color":"gray"},{"text":" min de serveur allumé)","color":"gray"}]
execute unless data storage mg:version recv run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"Reçue de GitHub : ","color":"white","bold":true},{"text":"rien (datapack-sync ne l'a jamais signalée)","color":"gray"}]
execute if data storage mg:version recv run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"Reçue de GitHub : ","color":"white","bold":true},{"nbt":"recv.commit","storage":"mg:version","color":"yellow","bold":true},{"text":" du ","color":"gray"},{"nbt":"recv.date","storage":"mg:version","color":"yellow"},{"text":", déposée le ","color":"gray"},{"nbt":"recv.at","storage":"mg:version","color":"yellow"}]
execute if data storage mg:version seen run execute store result score $vg mg.st run data get storage mg:version seen.gt
execute if data storage mg:version seen run function mg:version/ago
execute if data storage mg:version seen run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"Dernière vérif GitHub : ","color":"white"},{"nbt":"seen.at","storage":"mg:version","color":"yellow"},{"text":" (il y a ","color":"gray"},{"score":{"name":"$vh","objective":"mg.st"},"color":"gray"},{"text":" h ","color":"gray"},{"score":{"name":"$vm","objective":"mg.st"},"color":"gray"},{"text":" min de serveur allumé)","color":"gray"}]
scoreboard players set $vd mg.st 0
data modify storage mg:version tmp set from storage mg:version recv.commit
execute if data storage mg:version recv unless data storage mg:version files run scoreboard players set $vd mg.st 1
execute if data storage mg:version recv if data storage mg:version files store success score $vd mg.st run data modify storage mg:version tmp set from storage mg:version files.commit
data remove storage mg:version tmp
execute if score $vd mg.st matches 1 run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"⚠ La version reçue n'est pas celle en place. ","color":"red","bold":true},{"text":"[Appliquer : /reload]","color":"green","bold":true,"click_event":{"action":"run_command","command":"/minecraft:reload"},"hover_event":{"action":"show_text","value":"OP : /minecraft:reload (entre deux parties)"}},{"text":"\n   Si ça reste rouge après le reload : le chargement a échoué → logs du serveur (scripts/logs.ps1 mc).","color":"gray"}]
execute if score $vd mg.st matches 0 if data storage mg:version files run tellraw @s [{"text":"[Version] ","color":"gold"},{"text":"✔ À jour : la dernière version reçue est en place.","color":"green","bold":true}]
tellraw @s {"text":"   Vérif GitHub figée depuis longtemps (> 5 min) = datapack-sync arrêté ou planté (scripts/etat.ps1).","color":"dark_gray"}
