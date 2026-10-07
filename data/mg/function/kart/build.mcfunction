# (OP) Construit le Circuit Champignon : zone chargée, puis construction dès que tous ses chunks sont prêts
function mg:kart/fl_add
scoreboard players set $kbw mg.st 0
schedule function mg:kart/build_wait 20t
