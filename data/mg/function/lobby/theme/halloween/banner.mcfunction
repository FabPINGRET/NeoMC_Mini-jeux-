# Bandeau halloween (appelé chaque seconde par lobby/theme/banner ; $thbl = ligne à afficher, 1..5)
bossbar set mg:thb color purple
bossbar set mg:thb max 5
execute store result bossbar mg:thb value run scoreboard players get $thbl mg.st
execute if score $thbl mg.st matches 1 run bossbar set mg:thb name [{"text":"🎃 Halloween · ","color":"dark_purple","bold":true},{"text":"🎃 Ragoût mystère de la sorcière : 12 effets, dont le lapin !","color":"white"}]
execute if score $thbl mg.st matches 2 run bossbar set mg:thb name [{"text":"🎃 Halloween · ","color":"dark_purple","bold":true},{"text":"🎩 4 chapeaux d'Halloween, galerie sous le Hall des scores","color":"white"}]
execute if score $thbl mg.st matches 3 run bossbar set mg:thb name [{"text":"🎃 Halloween · ","color":"dark_purple","bold":true},{"text":"🍬 Événement : la pluie de pièces devient chasse aux bonbons","color":"white"}]
execute if score $thbl mg.st matches 4 run bossbar set mg:thb name [{"text":"🎃 Halloween · ","color":"dark_purple","bold":true},{"text":"👻 Fantômes, chauves-souris et eau rouge au spawn","color":"white"}]
execute if score $thbl mg.st matches 5 run bossbar set mg:thb name [{"text":"🎃 Halloween · ","color":"dark_purple","bold":true},{"text":"🎃 Les cartes de jeu se parent d'Halloween en partie","color":"white"}]
