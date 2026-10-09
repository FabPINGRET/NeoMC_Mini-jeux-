# Départ : marqueurs de traînée, vitesse
scoreboard players set $trt mg.st 0
execute as @a[tag=mg.play] run function mg:tron/go_one
execute if score $trm mg.st matches 0 run effect give @a[tag=mg.play] minecraft:speed infinite 1 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:glowing infinite 0 true
effect give @e[tag=mg.trh] minecraft:glowing infinite 0 true
scoreboard players set @a[tag=mg.play] mg.trj 200
scoreboard players reset @a[tag=mg.play] mg.qs
execute if score $trm mg.st matches 1 run item replace entity @a[tag=mg.play] hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={tron_jump:1b},custom_name=[{"text":"⤴ Saut","color":"gold","bold":true,"italic":false}],lore=[[{"text":"Clic droit puis Espace : saute par-dessus un mur","color":"gray","italic":false}],[{"text":"Recharge : 20 s","color":"gray","italic":false}]],unbreakable={}]
tellraw @a[tag=mg.play] [{"text":"⚡ TRON : ","color":"aqua","bold":true},{"text":"tu laisses un mur derrière toi. Touche un mur (même le tien) ou la bordure = éliminé. Interdit de s’arrêter plus de 2 s. Dernier en vie gagne !","color":"gray"}]
execute if score $trm mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🏍 Moto : tu ne peux pas descendre. ⤴ Saut (clic droit, puis Espace) pour passer au-dessus d'un mur, une fois toutes les 20 s.","color":"gold"}
