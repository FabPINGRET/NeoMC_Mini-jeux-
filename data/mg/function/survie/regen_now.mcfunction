# Joueur déjà dans le monde de survie au moment de la régénération (@s) : même traitement
execute store result storage mg:survie id.id int 1 run scoreboard players get @s mg.svid
function mg:survie/regen_place with storage mg:survie id
