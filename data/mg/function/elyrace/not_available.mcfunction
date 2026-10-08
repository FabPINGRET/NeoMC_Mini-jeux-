# Parcours dont le module n'existe pas encore (emplacement réservé) : partie annulée
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : le parcours ","color":"red"},{"score":{"name":"$xc","objective":"mg.st"},"color":"red"},{"text":" n'est pas encore disponible.","color":"red"}]
tellraw @a[tag=mg.play] [{"text":"🪽 Ce parcours n'est pas encore disponible : partie annulée.","color":"red"}]
# partie annulée ; $xc remis à 0 d'abord : cleanup (fl_remove) ne doit rien libérer, la zone d'un parcours en construction reste chargée
scoreboard players set $xc mg.st 0
function mg:core/draw
