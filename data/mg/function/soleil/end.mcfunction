# Fin : le premier arrivé gagne (seul : match nul)
execute unless score $state mg.st matches 2 run return 0
execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🔴 Fin de l'entraînement : ","color":"yellow"},{"score":{"name":"$sqn","objective":"mg.st"},"color":"yellow","bold":true},{"text":" arrivée(s).","color":"yellow"}]
execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw
execute if score $sqn mg.st matches 0 run tellraw @a {"text":"🔴 Personne n'a franchi la ligne…","color":"red"}
execute if score $sqn mg.st matches 0 run return run function mg:core/draw
execute as @a[tag=mg.sq1,limit=1] run function mg:core/win_player
execute if score $state mg.st matches 2 run function mg:core/draw
