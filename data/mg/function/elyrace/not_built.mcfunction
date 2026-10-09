# Parcours pas (entièrement) construit : on n'envoie personne dedans, partie annulée
execute if score $xc mg.st matches 0 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : ","color":"red"},{"text":"aucun parcours n'est construit : construction en cours, ou lance /function mg:elyrace/c1/build","color":"red"}]
execute if score $xc mg.st matches 1 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : ","color":"red"},{"text":"le parcours 1 (Canyon du Couchant) n'est pas (entièrement) construit : construction en cours, ou lance /function mg:elyrace/c1/build","color":"red"}]
execute if score $xc mg.st matches 2 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d'élytres : ","color":"red"},{"text":"le parcours 2 (Pic Blanc) n'est pas (entièrement) construit : construction en cours, ou lance /function mg:elyrace/c2/build","color":"red"}]
tellraw @a[tag=mg.play] [{"text":"🪽 Le parcours n'est pas encore construit : partie annulée.","color":"red"}]
# partie annulée ; $xc remis à 0 d'abord : cleanup (fl_remove) ne doit rien libérer, la zone d'un parcours en construction reste chargée
# (elyrace/draw : en solo, fin du contre-la-montre ; sinon core/draw)
scoreboard players set $xc mg.st 0
function mg:elyrace/draw
