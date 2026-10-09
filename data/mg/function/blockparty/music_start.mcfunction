# Début de manche : la musique repart (plus vite au fil des manches)
scoreboard players set #32 mg.st 32
scoreboard players set $bmt mg.st 0
scoreboard players set $bmp mg.st 0
scoreboard players set $bms mg.st 3
execute if score $rd mg.st matches 7.. run scoreboard players set $bms mg.st 2
scoreboard players set $bsc mg.st 0
