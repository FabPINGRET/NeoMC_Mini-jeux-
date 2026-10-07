# Désactive les modèles du resource pack (visuels vanilla)
scoreboard players set $rp mg.st 0
tellraw @s [{"text":"✔ ","color":"green"},{"text":"Modèles du resource pack désactivés (spawn tout de suite, kart à la prochaine course).","color":"gray"}]
function mg:lobby/deco
function mg:lobby/armory_build
