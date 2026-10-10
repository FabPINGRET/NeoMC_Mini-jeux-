# Départ : premier ordre dans 2 s
scoreboard players set $msp mg.st 0
scoreboard players set $mst mg.st 40
scoreboard players set $msc mg.st 0
tellraw @a[tag=mg.play] [{"text":"👑 MASTER DIT : ","color":"gold","bold":true},{"text":"obéis aux ordres qui commencent par « Master dit » ; les autres sont des pièges, ne les fais pas ! Trop lent ou piégé = éliminé. Ça va de plus en plus vite…","color":"gray"}]
