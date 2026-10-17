# Dropper : Essais — départ
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:dropper/attr_on
tellraw @a[tag=mg.play] [{"text":"⬇ DROPPER : ESSAIS ! ","color":"aqua","bold":true},{"text":"Les 13 niveaux de l'Aventure, chacun à son rythme. Chaque saut compte pour un essai : atterris dans l'EAU du premier coup ! Le moins d'essais gagne (30 minutes au plus).","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"⏭ ","color":"gold","bold":true},{"text":"Objet « Passer ce niveau » (dernier emplacement) : clic droit 2 fois en 3 s pour aller au niveau suivant. Il ne compte pas comme réussi : sans niveau réussi, pas de victoire !","color":"gray"}]
function mg:dropadv/s_records
function mg:dropadv/show_level_all
