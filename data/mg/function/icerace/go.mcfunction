# Course de bateaux sur glace — départ (3 tours)
function mg:icerace/gate_off
scoreboard players set $rc1 mg.st 10
scoreboard players set $rc2 mg.st 100
scoreboard players set $rc3 mg.st 30
scoreboard players set $rt mg.st 0
scoreboard players set @a[tag=mg.play] mg.cp 0
scoreboard players set @a[tag=mg.play] mg.lp 0
scoreboard players set @a[tag=mg.play] mg.rp 0
scoreboard objectives setdisplay sidebar mg.rp
tellraw @a[tag=mg.play] [{"text":"⛵ COURSE SUR GLACE : ","color":"aqua","bold":true},{"text":"3 tours, 10 points de passage par tour (ils se valident dans l'ordre). Z/S pour avancer, Q/D pour tourner. Le premier qui termine gagne !","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"Tu sors du bateau ? Il te reprend tout de suite. Tombé hors piste ? Retour au dernier point de passage.","color":"gray"}]
