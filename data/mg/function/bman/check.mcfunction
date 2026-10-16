# Fin de partie ?
execute unless score $n0 mg.st matches 2.. run return 0
execute if score $ym mg.st matches 1 run return run function mg:bman/check_t
execute store result score $ya mg.st if entity @a[tag=mg.play]
execute if score $ya mg.st matches 1 as @a[tag=mg.play] run return run function mg:core/win_player
execute if score $ya mg.st matches 0 run function mg:core/draw
