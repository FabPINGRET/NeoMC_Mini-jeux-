# @s (interaction d'objet de quête) : le joueur qui a cliqué
scoreboard players operation $qid mg.st = @s mg.olnid
execute on target if entity @s[tag=mg.olw] run function mg:ombre/q/int_p
data remove entity @s interaction
data remove entity @s attack
