# Insère t3w dans t3c (liste triée, 3 au plus) en retirant d'abord l'ancienne entrée du même joueur
execute if data storage mg:hall t3c[2] run data modify storage mg:hall t3q set from storage mg:hall t3c[2].u
execute if data storage mg:hall t3c[2] store success score #t3d mg.st run data modify storage mg:hall t3q set from storage mg:hall t3w.u
execute if data storage mg:hall t3c[2] if score #t3d mg.st matches 0 run data remove storage mg:hall t3c[2]
execute if data storage mg:hall t3c[1] run data modify storage mg:hall t3q set from storage mg:hall t3c[1].u
execute if data storage mg:hall t3c[1] store success score #t3d mg.st run data modify storage mg:hall t3q set from storage mg:hall t3w.u
execute if data storage mg:hall t3c[1] if score #t3d mg.st matches 0 run data remove storage mg:hall t3c[1]
execute if data storage mg:hall t3c[0] run data modify storage mg:hall t3q set from storage mg:hall t3c[0].u
execute if data storage mg:hall t3c[0] store success score #t3d mg.st run data modify storage mg:hall t3q set from storage mg:hall t3w.u
execute if data storage mg:hall t3c[0] if score #t3d mg.st matches 0 run data remove storage mg:hall t3c[0]
scoreboard players set #t3i mg.st -1
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[0] store result score #t3v mg.st run data get storage mg:hall t3c[0].s
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[0] if score #t3s mg.st > #t3v mg.st run scoreboard players set #t3i mg.st 0
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[1] store result score #t3v mg.st run data get storage mg:hall t3c[1].s
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[1] if score #t3s mg.st > #t3v mg.st run scoreboard players set #t3i mg.st 1
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[2] store result score #t3v mg.st run data get storage mg:hall t3c[2].s
execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[2] if score #t3s mg.st > #t3v mg.st run scoreboard players set #t3i mg.st 2
execute if score #t3i mg.st matches 0 run data modify storage mg:hall t3c insert 0 from storage mg:hall t3w
execute if score #t3i mg.st matches 1 run data modify storage mg:hall t3c insert 1 from storage mg:hall t3w
execute if score #t3i mg.st matches 2 run data modify storage mg:hall t3c insert 2 from storage mg:hall t3w
execute if score #t3i mg.st matches -1 unless data storage mg:hall t3c[2] run data modify storage mg:hall t3c append from storage mg:hall t3w
data remove storage mg:hall t3c[3]
