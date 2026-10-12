# @s : joueur ; $hn = chapeau choisi
execute unless score $rp mg.st matches 1 run return run tellraw @s {"text":"Les chapeaux demandent le resource pack NeoMC.","color":"red"}
execute if score $hn mg.st matches 0 run return run function mg:hat/remove
execute if score $hn mg.st matches 13..20 unless score @s mg.wins matches 5.. run return run tellraw @s [{"text":"🔒 ","color":"red"},{"text":"Chapeau rare","color":"aqua"},{"text":" : 5 victoires requises (tu en as ","color":"gray"},{"score":{"name":"@s","objective":"mg.wins"},"color":"gold"},{"text":").","color":"gray"}]
execute if score $hn mg.st matches 21..24 unless score @s mg.wins matches 20.. run return run tellraw @s [{"text":"🔒 ","color":"red"},{"text":"Chapeau épique","color":"light_purple"},{"text":" : 20 victoires requises (tu en as ","color":"gray"},{"score":{"name":"@s","objective":"mg.wins"},"color":"gold"},{"text":").","color":"gray"}]
execute if score $hn mg.st matches 25..28 unless score @s mg.wins matches 50.. run return run tellraw @s [{"text":"🔒 ","color":"red"},{"text":"Chapeau légendaire","color":"gold"},{"text":" : 50 victoires requises (tu en as ","color":"gray"},{"score":{"name":"@s","objective":"mg.wins"},"color":"gold"},{"text":").","color":"gray"}]
execute if score $hn mg.st matches 29..32 unless score $theme mg.st matches 1 run return run tellraw @s [{"text":"🔒 ","color":"red"},{"text":"🎃 Chapeau de Halloween","color":"gold"},{"text":" : seulement pendant la saison.","color":"gray"}]
execute if score $hn mg.st matches 33..35 unless score $theme mg.st matches 2 run return run tellraw @s [{"text":"🔒 ","color":"red"},{"text":"🎄 Chapeau de Noël","color":"red"},{"text":" : seulement pendant la saison.","color":"gray"}]
execute if score $hn mg.st = @s mg.hat run return run tellraw @s {"text":"Tu portes déjà ce chapeau.","color":"gray"}
scoreboard players operation @s mg.hat = $hn mg.st
function mg:hat/strip
function mg:hat/wear_now
playsound minecraft:item.armor.equip_leather master @s ~ ~ ~ 1 1.2
particle minecraft:happy_villager ~ ~2.1 ~ 0.3 0.2 0.3 0 10
execute if score $hn mg.st matches 1 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Haut-de-forme","color":"white","bold":true}]
execute if score $hn mg.st matches 2 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chapeau de cowboy","color":"white","bold":true}]
execute if score $hn mg.st matches 3 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Bonnet à pompon","color":"white","bold":true}]
execute if score $hn mg.st matches 4 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Casquette","color":"white","bold":true}]
execute if score $hn mg.st matches 5 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Béret","color":"white","bold":true}]
execute if score $hn mg.st matches 6 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chapeau de paille","color":"white","bold":true}]
execute if score $hn mg.st matches 7 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Grenouille","color":"white","bold":true}]
execute if score $hn mg.st matches 8 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Canard","color":"white","bold":true}]
execute if score $hn mg.st matches 9 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Gâteau d'anniversaire","color":"white","bold":true}]
execute if score $hn mg.st matches 10 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Casque pastèque","color":"white","bold":true}]
execute if score $hn mg.st matches 11 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Cône de chantier","color":"white","bold":true}]
execute if score $hn mg.st matches 12 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Poulet sur la tête","color":"white","bold":true}]
execute if score $hn mg.st matches 13 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Toque de diplômé","color":"aqua","bold":true}]
execute if score $hn mg.st matches 14 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chat endormi","color":"aqua","bold":true}]
execute if score $hn mg.st matches 15 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Axolotl","color":"aqua","bold":true}]
execute if score $hn mg.st matches 16 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Abeille","color":"aqua","bold":true}]
execute if score $hn mg.st matches 17 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Burger","color":"aqua","bold":true}]
execute if score $hn mg.st matches 18 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Sushi","color":"aqua","bold":true}]
execute if score $hn mg.st matches 19 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chapeau TNT","color":"aqua","bold":true}]
execute if score $hn mg.st matches 20 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Casquette à hélice","color":"aqua","bold":true}]
execute if score $hn mg.st matches 21 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chapeau de sorcier","color":"light_purple","bold":true}]
execute if score $hn mg.st matches 22 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Casque viking","color":"light_purple","bold":true}]
execute if score $hn mg.st matches 23 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Heaume de chevalier","color":"light_purple","bold":true}]
execute if score $hn mg.st matches 24 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Bocal à poisson","color":"light_purple","bold":true}]
execute if score $hn mg.st matches 25 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Couronne flottante","color":"gold","bold":true}]
execute if score $hn mg.st matches 26 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Crâne de dragon","color":"gold","bold":true}]
execute if score $hn mg.st matches 27 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Laurier de champion","color":"gold","bold":true}]
execute if score $hn mg.st matches 28 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Couronne de flammes","color":"gold","bold":true}]
execute if score $hn mg.st matches 29 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chapeau de sorcière","color":"gold","bold":true}]
execute if score $hn mg.st matches 30 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Citrouille-lanterne","color":"gold","bold":true}]
execute if score $hn mg.st matches 31 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Drap de fantôme","color":"gold","bold":true}]
execute if score $hn mg.st matches 32 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Chauve-souris","color":"gold","bold":true}]
execute if score $hn mg.st matches 33 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Bonnet de Noël","color":"red","bold":true}]
execute if score $hn mg.st matches 34 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Bois de renne","color":"red","bold":true}]
execute if score $hn mg.st matches 35 run tellraw @s [{"text":"🎩 Tu portes maintenant : ","color":"gray"},{"text":"Tête de bonhomme de neige","color":"red","bold":true}]
