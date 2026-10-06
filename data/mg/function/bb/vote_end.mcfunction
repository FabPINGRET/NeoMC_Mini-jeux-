# Fin du créneau : on enregistre la moyenne chez le constructeur, puis on passe à la suivante
execute as @a[tag=mg.play] if score @s mg.bi = $bbk mg.st run function mg:bb/bank
function mg:bb/vote_next
