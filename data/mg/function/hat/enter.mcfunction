# @s : descend dans la galerie
tp @s -24.5 45 24.5 180 0
playsound minecraft:block.beacon.activate master @s ~ ~ ~ 0.6 1.6
tellraw @s [{"text":"🎩 Galerie des chapeaux","color":"gold","bold":true},{"text":" : clique sur un piédestal pour porter son chapeau, partout et pendant les parties. ✦ Victoires : ","color":"gray"},{"score":{"name":"@s","objective":"mg.wins"},"color":"gold"}]
