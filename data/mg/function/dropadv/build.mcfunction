# (OP) Construit les 10 niveaux du Dropper Aventure
function mg:dropadv/fl_add
scoreboard players set $daw mg.st 0
schedule function mg:dropadv/build_wait 20t
