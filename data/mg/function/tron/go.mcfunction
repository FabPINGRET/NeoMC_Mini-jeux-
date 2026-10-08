# Départ : marqueurs de traînée, vitesse
scoreboard players set $trt mg.st 0
execute as @a[tag=mg.play] run function mg:tron/go_one
execute if score $trm mg.st matches 0 run effect give @a[tag=mg.play] minecraft:speed infinite 1 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
tellraw @a[tag=mg.play] [{"text":"⚡ TRON : ","color":"aqua","bold":true},{"text":"tu laisses un mur derrière toi. Touche un mur (même le tien) ou la bordure = éliminé. Interdit de s’arrêter plus de 2 s. Dernier en vie gagne !","color":"gray"}]
execute if score $trm mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🏍 Moto : tu ne peux pas descendre, fonce !","color":"gold"}
