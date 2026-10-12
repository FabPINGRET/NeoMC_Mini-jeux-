# Départ : rôles annoncés en secret ; le couteau arrive dans 10 s
scoreboard players set $mmt mg.st 0
scoreboard players set $mmc mg.st 0
scoreboard players set @a mg.deaths 0
scoreboard players set @a mg.mmk 0
scoreboard players set @a[tag=mg.play] mg.mma 0
scoreboard players set @a[tag=mg.play] mg.mmo 0
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.mmd] run function mg:mm/det_kit
execute if score $mmm mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🏚 Manoir","color":"aqua","bold":true}]
execute if score $mmm mg.st matches 2 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"⚓ Entrepôt du port","color":"aqua","bold":true}]
execute if score $mmm mg.st matches 3 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🛒 Supermarché","color":"aqua","bold":true}]
execute if score $mmm mg.st matches 4 run tellraw @a[tag=mg.play] [{"text":"🗺 Carte : ","color":"gray"},{"text":"🌿 Serre","color":"aqua","bold":true}]
title @a[tag=mg.mmm] title {"text":"🔪 TUEUR","color":"red","bold":true}
title @a[tag=mg.mmm] subtitle {"text":"Élimine tout le monde sans te faire prendre","color":"gray"}
title @a[tag=mg.mmd] title {"text":"🏹 DÉTECTIVE","color":"aqua","bold":true}
title @a[tag=mg.mmd] subtitle {"text":"Trouve le tueur et abats-le","color":"gray"}
title @a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd] title {"text":"😇 INNOCENT","color":"green","bold":true}
title @a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd] subtitle {"text":"Survis ; 10 pièces d'or = un arc","color":"gray"}
tellraw @a[tag=mg.mmm] [{"text":"🔪 Tu es le TUEUR. ","color":"red","bold":true},{"text":"Ton couteau arrive dans 10 s : un coup suffit. Personne ne connaît ton rôle, reste discret. Attention au détective et à son arc. Dans les 45 dernières secondes, les innocents brillent.","color":"gray"}]
tellraw @a[tag=mg.mmd] [{"text":"🏹 Tu es le DÉTECTIVE. ","color":"aqua","bold":true},{"text":"Une flèche toutes les 5 s, tir chargé = mortel. Si tu tues un innocent, tu es éliminé ! Si tu meurs, ton arc tombe : un innocent pourra le ramasser.","color":"gray"}]
tellraw @a[tag=mg.play,tag=!mg.mmm,tag=!mg.mmd] [{"text":"😇 Tu es INNOCENT. ","color":"green","bold":true},{"text":"Survis jusqu'à la fin. Ramasse 10 pièces d'or pour un arc, ou récupère celui du détective s'il tombe. Tuer un innocent = éliminé.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🔪 Mode entraînement (seul) : tu es détective, entraîne-toi au tir et ramasse l'or. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}]
