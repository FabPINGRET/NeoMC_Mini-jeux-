# The Dropper : Aventure — départ
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
execute as @a[tag=mg.play] run function mg:dropper/attr_on
tellraw @a[tag=mg.play] [{"text":"⬇ THE DROPPER : AVENTURE ! ","color":"aqua","bold":true},{"text":"13 niveaux à thème. Saute dans le puits et atterris dans l'EAU du fond : tout le reste te renvoie en haut du niveau. Le premier à finir les 13 niveaux gagne (13 minutes au plus).","color":"gray"}]
function mg:dropadv/show_level_all
