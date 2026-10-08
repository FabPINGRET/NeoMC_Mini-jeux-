# Mode 3 : barrière ouverte, fusées, zone de 70 blocs
function mg:sky/pad3_open
give @a[tag=mg.play] minecraft:firework_rocket[minecraft:custom_data={mg_sky:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du ciel","color":"gold","italic":false}] 2
scoreboard players set $skz mg.st 700
data modify storage mg:sky z.r set value 70.0d
scoreboard players set $skpo mg.st 1
scoreboard objectives setdisplay sidebar mg.sks
tellraw @a[tag=mg.play] [{"text":"🌪 SURVIE EN VOL : ","color":"light_purple","bold":true},{"text":"reste en l'air ! Te poser, tomber sous l'arène ou rester 3 s hors de la zone (cercle rouge qui rétrécit) = éliminé. Une fusée toutes les 8 s, colonnes de vent = élan vers le haut. La plateforme s'effondre au bout de 10 s. Dernier en vol gagne.","color":"gray","bold":false}]
