# (Re)construit l'île (zone chargée le temps de la construction) : au chargement si besoin, ou par un admin
scoreboard players set $fnb mg.st 1
execute in minecraft:overworld run forceload add -30 45970 46 46046
schedule function mg:filon/build_wait 40t
