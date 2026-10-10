# Départ : chacun monte dans son bateau
scoreboard objectives setdisplay sidebar mg.atl
execute as @a[tag=mg.play] at @s run function mg:autotamp/boat
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
bossbar add mg:autotamp {"text":"🚗 Autos tamponneuses","color":"aqua"}
bossbar set mg:autotamp color blue
bossbar set mg:autotamp max 3600
bossbar set mg:autotamp players @a[tag=mg.play]
tellraw @a[tag=mg.play] [{"text":"🚗 AUTOS TAMPONNEUSES : ","color":"aqua","bold":true},{"text":"fonce dans les autres ! Chaque fois qu'on te tamponne (tu roulais moins vite), tu perds un coup ; à 0, éliminé. Dernier en piste = victoire. Accroupi = sortir (tu remontes aussitôt).","color":"gray"}]
