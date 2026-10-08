# Fin du compte à rebours : un votant (marqué mg.vauto, accepté par core/go comme un admin) lance le jeu le plus voté. Généré.
scoreboard players set $vat mg.st -1
tag @r[tag=mg.init,tag=!mg.surv,scores={mg.vc=1..}] add mg.vauto
execute as @a[tag=mg.vauto,limit=1] run function mg:vote/launch
tag @a remove mg.vauto
