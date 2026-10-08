# Fin de l'élan (@s)
effect clear @s minecraft:levitation
execute if entity @s[tag=mg.play] run title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow","bold":true}]
execute if entity @s[tag=mg.play] run title @s title [{"text":" "}]
