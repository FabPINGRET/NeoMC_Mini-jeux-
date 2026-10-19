# Session (dans la dimension) : équipes, règles, barres des boss
function mg:ombre/clear
function mg:ombre/rules
function mg:ombre/consts
team add mg_olel
team modify mg_olel color gold
team add mg_ol
team modify mg_ol friendlyFire false
team modify mg_ol color light_purple
team join mg_ol @a[tag=mg.olw]
function mg:ombre/boss/setup
scoreboard players set $olsu mg.st 1
