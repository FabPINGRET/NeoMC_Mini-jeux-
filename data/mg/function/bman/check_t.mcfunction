execute store result score $yar mg.st if entity @a[tag=mg.play,team=mg_red]
execute store result score $yab mg.st if entity @a[tag=mg.play,team=mg_blue]
execute if score $yar mg.st matches 0 if score $yab mg.st matches 0 run return run function mg:core/draw
execute if score $yar mg.st matches 0 run return run function mg:core/win_blue
execute if score $yab mg.st matches 0 run return run function mg:core/win_red
