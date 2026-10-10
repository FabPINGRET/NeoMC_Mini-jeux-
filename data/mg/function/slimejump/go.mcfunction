# Départ
scoreboard players set $sjt mg.st 0
fill -2 81 37801 2 81 37801 minecraft:air
bossbar add mg:slimejump {"text":"🟩 Slime Jump","color":"green"}
bossbar set mg:slimejump color green
bossbar set mg:slimejump max 4800
bossbar set mg:slimejump players @a[tag=mg.play]
tellraw @a[tag=mg.play] [{"text":"🟩 SLIME JUMP : ","color":"green","bold":true},{"text":"saute de slime en slime jusqu'à l'arrivée (diamant) ! Rebondis plusieurs fois pour monter aux corniches. 4 points de passage en émeraude : une chute ramène au dernier. Le premier arrivé gagne.","color":"gray"}]
