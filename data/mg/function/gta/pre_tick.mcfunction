# Avant la survie (core/tick) : un joueur du GTA sorti de la dimension sans passer par la sortie perd ses tags
execute as @a[tag=mg.gtw] at @s unless dimension mg:gta run function mg:gta/strayed
