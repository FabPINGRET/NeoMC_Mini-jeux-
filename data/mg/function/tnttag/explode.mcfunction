# BOUM : le porteur explose et est éliminé, puis nouvelle bombe (seulement s'il reste au moins 2 joueurs)
execute as @a[tag=mg.bomb,tag=mg.play] at @s run function mg:tnttag/boom
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $alive mg.st matches 2.. run function mg:tnttag/new_round
