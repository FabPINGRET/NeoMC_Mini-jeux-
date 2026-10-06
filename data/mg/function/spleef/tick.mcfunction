# Spleef — tick de jeu

# Rétrécissement progressif de l'arène (avertissement 3 s avant)
scoreboard players remove $sk mg.st 1
execute if score $sk mg.st matches 60 if score $ss mg.st matches ..9 run title @a[tag=mg.play] actionbar [{"text":"⚠ Les bords de l'arène vont disparaître !","color":"gold"}]
execute if score $sk mg.st matches ..0 if score $ss mg.st matches ..9 run function mg:spleef/shrink
execute if score $sk mg.st matches ..0 if score $ss mg.st matches 10.. run scoreboard players set $sk mg.st 9999

# Chute sous le dernier étage → éliminé
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play] if score @s mg.t <= $yd mg.st run function mg:core/eliminate

# Mort accidentelle → éliminé
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate

# Victoire
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
