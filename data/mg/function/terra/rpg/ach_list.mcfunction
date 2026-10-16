# @s : liste des succès
tellraw @s {"text":"\n🏆 Succès et titres","color":"gold","bold":true}
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Premier sang","color":"gold","bold":true},{"text":" — Abattre un premier monstre","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Premier sang","color":"gray"},{"text":" — Abattre un premier monstre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chasseur","color":"gold","bold":true},{"text":" — Abattre 50 monstres","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Chasseur","color":"gray"},{"text":" — Abattre 50 monstres","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Exterminateur","color":"gold","bold":true},{"text":" — Abattre 250 monstres","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Exterminateur","color":"gray"},{"text":" — Abattre 250 monstres","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chasseur d'élites","color":"gold","bold":true},{"text":" — Abattre 10 élites","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Chasseur d'élites","color":"gray"},{"text":" — Abattre 10 élites","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Reine déchue","color":"gold","bold":true},{"text":" — Vaincre le Spinosaure","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Reine déchue","color":"gray"},{"text":" — Vaincre le Spinosaure","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Briseur de fort","color":"gold","bold":true},{"text":" — Vaincre le lieutenant Varek","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Briseur de fort","color":"gray"},{"text":" — Vaincre le lieutenant Varek","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Régicide","color":"gold","bold":true},{"text":" — Vaincre le Roi Tyran","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Régicide","color":"gray"},{"text":" — Vaincre le Roi Tyran","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Naturaliste","color":"gold","bold":true},{"text":" — Compléter le bestiaire","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Naturaliste","color":"gray"},{"text":" — Compléter le bestiaire","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Maître des donjons","color":"gold","bold":true},{"text":" — Terminer les 4 donjons","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Maître des donjons","color":"gray"},{"text":" — Terminer les 4 donjons","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chasseur de trésors","color":"gold","bold":true},{"text":" — Trouver les 15 trésors cachés","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Chasseur de trésors","color":"gray"},{"text":" — Trouver les 15 trésors cachés","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Légende vivante","color":"gold","bold":true},{"text":" — Atteindre le niveau 20","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Légende vivante","color":"gray"},{"text":" — Atteindre le niveau 20","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trac
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Fortuné","color":"gold","bold":true},{"text":" — Posséder 5000 ₵","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"Fortuné","color":"gray"},{"text":" — Posséder 5000 ₵","color":"dark_gray"}]
