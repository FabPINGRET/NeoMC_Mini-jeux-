# @s entre au portail du terrain de foot (hub) : descend au terrain (foot/go), sauf si un admin l'a fermé ($ftoff)
execute if score $ftoff mg.st matches 1 run return run title @s actionbar {"text":"⚽ Terrain de foot fermé pour le moment","color":"red"}
function mg:foot/go
