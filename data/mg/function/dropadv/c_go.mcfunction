# Dropper : Défi — départ de la première manche
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:dropper/attr_on
tellraw @a[tag=mg.play] [{"text":"⬇ DROPPER : DÉFI ! ","color":"aqua","bold":true},{"text":"Tout le monde dans le même puits, tiré au hasard parmi les niveaux de l'Aventure. Le premier dans l'EAU gagne la manche ; premier à 3 manches !","color":"gray"}]
function mg:dropadv/c_round
