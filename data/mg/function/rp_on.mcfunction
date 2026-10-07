# Active les modèles du resource pack NeoMC (kart 3D, objets Mario Kart, boîtes ?) : à utiliser quand tous les joueurs ont le pack
scoreboard players set $rp mg.st 1
tellraw @s [{"text":"✔ ","color":"green"},{"text":"Modèles du resource pack activés (spawn tout de suite, kart à la prochaine course).","color":"gray"}]
function mg:lobby/deco
function mg:lobby/armory_build
