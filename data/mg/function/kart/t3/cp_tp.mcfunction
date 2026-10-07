# Forteresse Bob-omb : retour en jeu (@s = kart) sur un point de départ au hasard
execute store result score $kr2 mg.st run random value 1..16
execute if score $kr2 mg.st matches 1 run return run tp @s 51.0 65 22010.1 101.2 0
execute if score $kr2 mg.st matches 2 run return run tp @s 43.2 65 22028.9 123.8 0
execute if score $kr2 mg.st matches 3 run return run tp @s 28.9 65 22043.2 146.2 0
execute if score $kr2 mg.st matches 4 run return run tp @s 10.1 65 22051.0 168.8 0
execute if score $kr2 mg.st matches 5 run return run tp @s -10.1 65 22051.0 -168.8 0
execute if score $kr2 mg.st matches 6 run return run tp @s -28.9 65 22043.2 -146.2 0
execute if score $kr2 mg.st matches 7 run return run tp @s -43.2 65 22028.9 -123.8 0
execute if score $kr2 mg.st matches 8 run return run tp @s -51.0 65 22010.1 -101.2 0
execute if score $kr2 mg.st matches 9 run return run tp @s -51.0 65 21989.9 -78.8 0
execute if score $kr2 mg.st matches 10 run return run tp @s -43.2 65 21971.1 -56.2 0
execute if score $kr2 mg.st matches 11 run return run tp @s -28.9 65 21956.8 -33.8 0
execute if score $kr2 mg.st matches 12 run return run tp @s -10.1 65 21949.0 -11.3 0
execute if score $kr2 mg.st matches 13 run return run tp @s 10.1 65 21949.0 11.3 0
execute if score $kr2 mg.st matches 14 run return run tp @s 28.9 65 21956.8 33.7 0
execute if score $kr2 mg.st matches 15 run return run tp @s 43.2 65 21971.1 56.2 0
execute if score $kr2 mg.st matches 16 run return run tp @s 51.0 65 21989.9 78.7 0
