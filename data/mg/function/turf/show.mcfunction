# Turf Wars — gros affichage du score (objectif : 25 colonnes sur 31 = 80 %)
title @a[tag=mg.play] times 0 30 10
title @a[tag=mg.play] subtitle [{"text":"Objectif : 25 colonnes (80 %)","color":"gray"}]
title @a[tag=mg.play] title [{"score":{"name":"$nr","objective":"mg.st"},"color":"red","bold":true},{"text":"  -  ","color":"white"},{"score":{"name":"$nb","objective":"mg.st"},"color":"blue","bold":true}]
