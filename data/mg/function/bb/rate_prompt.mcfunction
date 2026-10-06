# À 12 s : fenêtre de notation pour ceux qui n'ont pas encore noté
execute as @a[tag=mg.play,scores={mg.br=0}] unless score @s mg.bi = $bbk mg.st run function mg:bb/rate_open
execute if score $bbs mg.st matches 1 as @a[tag=mg.play,scores={mg.br=0}] run function mg:bb/rate_open
