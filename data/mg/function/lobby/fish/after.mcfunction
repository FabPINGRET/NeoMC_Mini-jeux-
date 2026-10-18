# Chaque tick tant qu'un joueur porte mg.lfc ou qu'un marqueur mg.lfm reste (core/tick) : le tick suivant une prise, objets de la ligne et orbes d'XP tués
execute as @e[type=minecraft:marker,tag=mg.lfm] at @s run kill @e[type=minecraft:item,distance=..1.5]
execute as @a[tag=mg.lfc] at @s run kill @e[type=minecraft:experience_orb,distance=..2]
kill @e[type=minecraft:marker,tag=mg.lfm]
tag @a remove mg.lfc
