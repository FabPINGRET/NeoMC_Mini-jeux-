# Bandeau noel (appelé chaque seconde par lobby/theme/banner ; $thbl = ligne à afficher, 1..6)
bossbar set mg:thb color red
bossbar set mg:thb max 6
execute store result bossbar mg:thb value run scoreboard players get $thbl mg.st
execute if score $thbl mg.st matches 1 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"🎄 Le lutin du buffet offre 3 feux d'artifice (à ciel ouvert)","color":"white"}]
execute if score $thbl mg.st matches 2 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"🎩 3 chapeaux de Noël, galerie sous le Hall des scores","color":"white"}]
execute if score $thbl mg.st matches 3 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"🎁 Événement : la pluie de pièces devient chasse aux cadeaux","color":"white"}]
execute if score $thbl mg.st matches 4 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"🔴 Bonhommes de neige, rennes et Rudolph au spawn","color":"white"}]
execute if score $thbl mg.st matches 5 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"❄ De la neige sur les cartes de jeu en partie","color":"white"}]
execute if score $thbl mg.st matches 6 run bossbar set mg:thb name [{"text":"🎄 Noël · ","color":"red","bold":true},{"text":"⛸ Patinoire derrière le buffet : ça glisse !","color":"white"}]
