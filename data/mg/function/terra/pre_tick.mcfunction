# Avant la survie (core/tick) : un joueur de Terra Nova sorti de la dimension sans passer par la sortie perd ses tags
execute as @a[tag=mg.tvw] at @s unless dimension mg:terranova run function mg:terra/strayed
