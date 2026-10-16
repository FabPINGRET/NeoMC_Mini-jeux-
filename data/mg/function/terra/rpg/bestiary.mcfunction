# @s : liste du bestiaire dans le chat
tellraw @s {"text":"\n📖 Bestiaire du Dr Ossei","color":"aqua","bold":true}
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Slasher","color":"yellow","bold":true},{"text":" — Chasseur en meute, rapide et rusé. Il bondit sur sa proie.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Compsognathus","color":"yellow","bold":true},{"text":" — Minuscule mais jamais seul : les nuées submergent les imprudents.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Dilophosaure","color":"yellow","bold":true},{"text":" — Déploie sa collerette et crache un venin aveuglant à distance.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Gallimimus","color":"yellow","bold":true},{"text":" — Herbivore véloce qui file au moindre bruit. Protégé.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Pachycéphalosaure","color":"yellow","bold":true},{"text":" — Crâne en dôme : il charge tête baissée. Protégé.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Tricératops","color":"yellow","bold":true},{"text":" — Paisible tant qu'on le laisse tranquille. Ses cornes ne pardonnent pas.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Stégosaure","color":"yellow","bold":true},{"text":" — Les pointes de sa queue fauchent quiconque s'approche de trop près.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Ankylosaure","color":"yellow","bold":true},{"text":" — Un char d'assaut vivant, armé d'une massue au bout de la queue.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Brachiosaure","color":"yellow","bold":true},{"text":" — Le géant de la vallée. On peut le monter avec une selle.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Ptéranodon","color":"yellow","bold":true},{"text":" — Plonge du ciel sur les voyageurs isolés.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Carnotaure","color":"yellow","bold":true},{"text":" — Prédateur cornu qui charge et brise les palissades.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Spinosaure","color":"yellow","bold":true},{"text":" — La reine du marais. Plonge, ressurgit et appelle ses petits.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
scoreboard players operation $b mg.st = @s mg.trbs
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Roi Tyran","color":"yellow","bold":true},{"text":" — Le plus grand prédateur de Terra Nova. Son rugissement glace le sang.","color":"gray"}]
execute if score $b mg.st matches 0 run tellraw @s [{"text":" ✖ ","color":"dark_gray"},{"text":"??? (espèce inconnue)","color":"dark_gray"}]
