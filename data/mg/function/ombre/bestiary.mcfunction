# @s : bestiaire dans le chat
tellraw @s {"text":"\n📖 Bestiaire d'Ombrelune","color":"aqua","bold":true}
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Loup gris","color":"gray","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Brigand","color":"red","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Archer brigand","color":"red","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Goule","color":"dark_green","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Squelette","color":"white","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Araignée sylvestre","color":"dark_green","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Tisseuse","color":"dark_aqua","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Feu follet","color":"aqua","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Elfe noir","color":"dark_purple","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Loup-garou","color":"dark_gray","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Vagabond gelé","color":"aqua","bold":true},{"text":"  Pics de Givrecroc","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pics de Givrecroc","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Ours des glaces","color":"white","bold":true},{"text":"  Pics de Givrecroc","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pics de Givrecroc","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Loup des neiges","color":"white","bold":true},{"text":"  Pics de Givrecroc","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pics de Givrecroc","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Yéti","color":"white","bold":true},{"text":"  Pics de Givrecroc","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pics de Givrecroc","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Sorcière des marais","color":"dark_purple","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Noyé","color":"dark_aqua","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p16 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Embourbé","color":"dark_green","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p17 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Vase putride","color":"green","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p18 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Sangsue géante","color":"dark_red","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p19 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Momie","color":"gold","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p20 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Scorpion des sables","color":"gold","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p21 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Archer desséché","color":"yellow","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p22 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Djinn des vents","color":"aqua","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p23 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Pillard du désert","color":"gold","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p24 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Drake des braises","color":"gold","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p25 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Élémentaire de feu","color":"gold","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p26 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Cube de magma","color":"red","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p27 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Brute calcinée","color":"dark_red","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p28 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chevalier calciné","color":"dark_red","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs
scoreboard players operation $b mg.st /= #p29 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Nain renégat","color":"gray","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Arbalétrier nain","color":"gray","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Gardien runique","color":"blue","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Troggoïde","color":"dark_gray","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Rampant des profondeurs","color":"dark_gray","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chevalier noir","color":"dark_purple","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Nécromancien","color":"dark_purple","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Spectre","color":"dark_aqua","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Ombre errante","color":"dark_purple","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Cultiste de Malveth","color":"dark_purple","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Seigneur des cryptes","color":"dark_red","bold":true},{"text":"  Plaines de Valdor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Plaines de Valdor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Tisseuse alpha","color":"dark_red","bold":true},{"text":"  Forêt de Sylvanor","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Forêt de Sylvanor","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Wendigo des glaces","color":"dark_red","bold":true},{"text":"  Pics de Givrecroc","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pics de Givrecroc","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Gardien noyé","color":"dark_red","bold":true},{"text":"  Marais de Fangebrume","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Marais de Fangebrume","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Momie royale","color":"dark_red","bold":true},{"text":"  Sables d'Azhar","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Sables d'Azhar","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Forgeron calciné","color":"dark_red","bold":true},{"text":"  Pyrecendre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Pyrecendre","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Contremaître maudit","color":"dark_red","bold":true},{"text":"  Khazgarde","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Khazgarde","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.olbs2
scoreboard players operation $b mg.st /= #p16 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Gardien des âmes","color":"dark_red","bold":true},{"text":"  Terres d'Ombre","color":"dark_gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ??? ","color":"dark_gray"},{"text":" Terres d'Ombre","color":"dark_gray"}]
