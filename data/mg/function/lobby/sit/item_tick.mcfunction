# Appelé chaque tick (core/tick) tant qu'un joueur porte mg.lsg : mg.lsw fait attendre un tick avant de rendre l'objet
execute as @a[tag=mg.lsg,tag=!mg.lsw] run function mg:lobby/sit/item_back
tag @a[tag=mg.lsw] remove mg.lsw
