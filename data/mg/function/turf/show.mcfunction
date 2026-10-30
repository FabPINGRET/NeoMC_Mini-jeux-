# Turf Wars — gros affichage du score (objectif : 19 colonnes sur 31 = 60 %)
title @a[tag=mg.play] times 0 30 10
title @a[tag=mg.play] subtitle [{"text":"Objectif : 19 colonnes (60 %)","color":"gray"}]
title @a[tag=mg.play] title [{"score":{"name":"$nr","objective":"mg.st"},"color":"red","bold":true},{"text":"  -  ","color":"white"},{"score":{"name":"$nb","objective":"mg.st"},"color":"blue","bold":true}]
