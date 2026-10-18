# Appelé chaque tick (core/tick) tant qu'un joueur porte mg.lsm ; « at @s » : le ~ de rotate lit sa rotation
execute as @a[tag=mg.lsm] at @s run function mg:lobby/sit/move_step
