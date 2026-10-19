# @s : bouton « S'asseoir » (mg.opt 76) : se lève si déjà assis, sinon banc sous les pieds ou adjacent, sinon par terre
execute if entity @s[tag=mg.sit] run return run function mg:lobby/sit/stand
execute unless function mg:lobby/sit/can run return 0
execute unless entity @s[nbt={OnGround:1b}] run return run title @s actionbar {"text":"🪑 Pose-toi d'abord au sol.","color":"gray"}
# core/opt tourne sans « at @s » : les coordonnées relatives de sit/bench se lisent à la position du joueur
execute at @s if function mg:lobby/sit/bench run return 1
execute at @s positioned ~ ~ ~ run return run function mg:lobby/sit/seat
