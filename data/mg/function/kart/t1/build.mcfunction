# (OP) Construit le Circuit Champignon : zone chargée, puis construction dès que tous ses chunks sont prêts
function mg:kart/t1/fl_add
scoreboard players set $kbw mg.st 0
schedule function mg:kart/t1/build_wait 20t
