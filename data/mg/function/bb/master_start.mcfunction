scoreboard players set $bbp mg.st 0
scoreboard players set $bbt mg.st 0
function mg:bb/suggest
execute as @a[tag=mg.bm] run function mg:bb/master_give
title @a[tag=mg.play] title [{"text":"✎ Maître du mot","color":"gold","bold":true}]
title @a[tag=mg.play] subtitle [{"selector":"@a[tag=mg.bm]","color":"yellow"},{"text":" choisit le thème…","color":"gray"}]
tellraw @a[tag=mg.play,tag=!mg.bm] [{"selector":"@a[tag=mg.bm]","color":"yellow","bold":true},{"text":" est le MAÎTRE DU MOT : il a 60 secondes pour donner le thème à construire (sinon ce sera un mot aléatoire).","color":"gray"}]
