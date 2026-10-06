# Mob Arena — @s a lancé une snowball : boule de feu si Pyromane
scoreboard players reset @s mg.us
execute unless score $mt mg.st matches 3 if score @s mg.cl matches 6 run function mg:mobarena/class/fireball
