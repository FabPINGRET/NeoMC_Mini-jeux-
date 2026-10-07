# (OP) Construit le Royaume Koopa : zone chargée, puis construction dès que tous ses chunks sont prêts
function mg:kart/t2/fl_add
scoreboard players set $kbw2 mg.st 0
schedule function mg:kart/t2/build_wait 20t
