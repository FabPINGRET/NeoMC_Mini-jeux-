# Départ
scoreboard players set $sqt mg.st 0
scoreboard players set $sqc mg.st 0
bossbar add mg:soleil {"text":"🔴 1, 2, 3 Soleil","color":"red"}
bossbar set mg:soleil color red
bossbar set mg:soleil max 1800
bossbar set mg:soleil players @a[tag=mg.play]
function mg:soleil/green
tellraw @a[tag=mg.play] [{"text":"🔴 1, 2, 3… SOLEIL ! ","color":"red","bold":true},{"text":"Avance quand la poupée a le dos tourné. Quand elle se retourne (« SOLEIL ! »), ne bouge plus : le moindre mouvement, même un saut, et tu es éliminé. Franchis la ligne rouge avant la fin (1 min 30) !","color":"gray"}]
