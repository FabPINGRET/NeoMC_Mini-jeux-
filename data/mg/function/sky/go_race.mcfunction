# Modes 1-2 : barrière ouverte, fusées (+ arc et charges de vent en mode 2)
function mg:sky/pad1_open
give @a[tag=mg.play] minecraft:firework_rocket[minecraft:custom_data={mg_sky:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du ciel","color":"gold","italic":false}] 3
execute if score $elm mg.st matches 2 run give @a[tag=mg.play] minecraft:bow[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:infinity":1},minecraft:custom_name={"text":"Arc du ciel","color":"red","italic":false}]
execute if score $elm mg.st matches 2 run give @a[tag=mg.play] minecraft:arrow[minecraft:custom_data={mg_sky:1b}]
execute if score $elm mg.st matches 2 run give @a[tag=mg.play] minecraft:wind_charge[minecraft:custom_data={mg_sky:1b},minecraft:custom_name={"text":"Charge de vent","color":"aqua","italic":false}] 3
scoreboard players set $skwt mg.st 0
scoreboard objectives setdisplay sidebar mg.skr
execute if score $elm mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🪽 COURSE D'ANNEAUX : ","color":"aqua","bold":true},{"text":"saute, ouvre tes élytres (Espace en l'air) et traverse les 20 anneaux DANS L'ORDRE — la traînée lumineuse montre le suivant. Anneaux dorés = +1 fusée. Le premier arrivé gagne (4 min max).","color":"gray","bold":false}]
execute if score $elm mg.st matches 2 run tellraw @a[tag=mg.play] [{"text":"🏹 COURSE + COMBAT : ","color":"red","bold":true},{"text":"même course de 20 anneaux, mais arc et charges de vent (rechargées toutes les 15 s) ! Un rival touché est sonné : ses élytres disparaissent 1,5 s. Personne ne meurt. Le premier arrivé gagne.","color":"gray","bold":false}]
