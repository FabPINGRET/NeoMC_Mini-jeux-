# 45 min écoulées sans joueur : la régénération attend le prochain mineur
scoreboard players set $fnt mg.st 0
scoreboard players set $fnpend mg.st 1
scoreboard players set $fnrp mg.st 0
execute store result score $fnpr mg.st run random value 900..2100
