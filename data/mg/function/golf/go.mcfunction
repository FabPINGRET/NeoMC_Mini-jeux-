# ⛳ Départ
execute as @a[tag=mg.play] run function mg:golf/kit
scoreboard players reset @a[tag=mg.play] mg.qs
scoreboard objectives setdisplay sidebar mg.gfd
tellraw @a[tag=mg.play] [{"text":"⛳ GOLF : ","color":"green","bold":true},{"text":"6 trous (par 23), tout le monde joue en même temps. Vise avec le regard, ","color":"gray"},{"text":"clic droit","color":"yellow"},{"text":" quand la jauge est au bon niveau. ","color":"gray"},{"text":"Bois/Fer","color":"gold"},{"text":" = vol en cloche, ","color":"gray"},{"text":"Putter","color":"green"},{"text":" = roule (green). Eau / vide = +1 coup. 8 coups max par trou. Le plus petit total gagne !","color":"gray"}]
