# Annonce du lancement (appelée par mg:core/request, avant prepare : en mode « au hasard » le parcours n'est pas encore tiré)
# un lancement de groupe n'est jamais un solo : le drapeau $xs est remis à 0 (le solo ne passe pas par request)
scoreboard players set $xs mg.st 0
execute if score $xc mg.st matches 0 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},{"text":"🪽 COURSE D'ÉLYTRES","color":"aqua","bold":true},{"text":" : un parcours au hasard parmi ceux qui sont construits (le premier arrivé gagne) !","color":"gray"}]
execute if score $xc mg.st matches 1 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},{"text":"🪽 COURSE D'ÉLYTRES","color":"aqua","bold":true},{"text":" : Canyon du Couchant (22 anneaux, le premier arrivé gagne) !","color":"gray"}]
execute if score $xc mg.st matches 2 run tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance la ","color":"gray"},{"text":"🪽 COURSE D'ÉLYTRES","color":"aqua","bold":true},{"text":" : Pic Blanc (20 anneaux, le premier arrivé gagne) !","color":"gray"}]
