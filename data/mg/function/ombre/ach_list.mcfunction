# @s : liste des succès
tellraw @s {"text":"\n🏆 Succès et titres","color":"gold","bold":true}
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Premier sang","color":"gold","bold":true},{"text":" : Vaincre un premier monstre","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Premier sang","color":"gray"},{"text":" : Vaincre un premier monstre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chasseur","color":"gold","bold":true},{"text":" : Vaincre 100 monstres","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Chasseur","color":"gray"},{"text":" : Vaincre 100 monstres","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Fléau des ténèbres","color":"gold","bold":true},{"text":" : Vaincre 500 monstres","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Fléau des ténèbres","color":"gray"},{"text":" : Vaincre 500 monstres","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chasseur d'élites","color":"gold","bold":true},{"text":" : Vaincre 15 élites","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Chasseur d'élites","color":"gray"},{"text":" : Vaincre 15 élites","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Explorateur","color":"gold","bold":true},{"text":" : Découvrir 15 lieux","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Explorateur","color":"gray"},{"text":" : Découvrir 15 lieux","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Cartographe","color":"gold","bold":true},{"text":" : Découvrir tous les lieux","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Cartographe","color":"gray"},{"text":" : Découvrir tous les lieux","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Érudit","color":"gold","bold":true},{"text":" : Lire toutes les pages du grimoire","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Érudit","color":"gray"},{"text":" : Lire toutes les pages du grimoire","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Pilleur de trésors","color":"gold","bold":true},{"text":" : Ouvrir les 24 coffres cachés","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Pilleur de trésors","color":"gray"},{"text":" : Ouvrir les 24 coffres cachés","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Maître des donjons","color":"gold","bold":true},{"text":" : Terminer les 8 donjons","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Maître des donjons","color":"gray"},{"text":" : Terminer les 8 donjons","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Tueur de dragons","color":"gold","bold":true},{"text":" : Vaincre Ignarok","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Tueur de dragons","color":"gray"},{"text":" : Vaincre Ignarok","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Porteur de l'Aube","color":"gold","bold":true},{"text":" : Terminer la campagne","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Porteur de l'Aube","color":"gray"},{"text":" : Terminer la campagne","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Légende","color":"gold","bold":true},{"text":" : Atteindre le niveau 35","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Légende","color":"gray"},{"text":" : Atteindre le niveau 35","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Fortuné","color":"gold","bold":true},{"text":" : Posséder 10 000 💰","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Fortuné","color":"gray"},{"text":" : Posséder 10 000 💰","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Mercenaire","color":"gold","bold":true},{"text":" : Remplir 10 contrats","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Mercenaire","color":"gray"},{"text":" : Remplir 10 contrats","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Bon samaritain","color":"gold","bold":true},{"text":" : Rendre 8 quêtes secondaires","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Bon samaritain","color":"gray"},{"text":" : Rendre 8 quêtes secondaires","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Forgé dans l'acier","color":"gold","bold":true},{"text":" : Arme de palier 8","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Forgé dans l'acier","color":"gray"},{"text":" : Arme de palier 8","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p16 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Cavalier","color":"gold","bold":true},{"text":" : Acheter un destrier","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Cavalier","color":"gray"},{"text":" : Acheter un destrier","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olac
scoreboard players operation $b mg.st /= #p17 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Encyclopédiste","color":"gold","bold":true},{"text":" : Compléter le bestiaire","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Encyclopédiste","color":"gray"},{"text":" : Compléter le bestiaire","color":"dark_gray"}]
