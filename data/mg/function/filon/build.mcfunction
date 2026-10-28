# Île + entités + chunk de mine neuf
function mg:filon/island
function mg:filon/ents
function mg:filon/board
data modify storage mg:filon built set value 1
scoreboard players set $fnpend mg.st 1
tellraw @a[tag=mg.admin] {"text":"[Filon] Île construite.","color":"gray"}
