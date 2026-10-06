# (OP) Construit la carte de la Mini Party (île à z 15000, en plusieurs ticks pour éviter un pic de lag)
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Construction du plateau de la Mini Party (quelques secondes)...","color":"gray"}]
function mg:party/build_1
