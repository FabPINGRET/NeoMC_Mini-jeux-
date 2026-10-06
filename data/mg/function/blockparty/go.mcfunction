# Block Party — début de partie
scoreboard players set $c20 mg.st 20
scoreboard players set $c5 mg.st 5
scoreboard players set $bmin mg.st 40
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
tellraw @a[tag=mg.play] [{"text":"▦ BLOCK PARTY ! ","color":"light_purple","bold":true},{"text":"Une couleur s'affiche dans ton inventaire : cours sur un bloc de cette couleur avant que tous les autres disparaissent ! Le temps diminue à chaque manche. Dernier debout = gagnant !","color":"gray"}]
function mg:blockparty/new_round
