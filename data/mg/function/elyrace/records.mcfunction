# @s = joueur : ses meilleurs temps et les records du serveur (mg.xs 3)
tellraw @s [{"text":"\n📊 Course d'élytres : records","color":"aqua","bold":true}]
function mg:elyrace/c1/records_show
function mg:elyrace/c2/records_show
tellraw @s [{"text":"Les temps de la course de groupe et du contre-la-montre solo comptent pour les mêmes records.","color":"dark_gray","italic":true}]
