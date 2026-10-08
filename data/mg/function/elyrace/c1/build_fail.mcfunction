# Abandon de la construction du parcours 1 : libère les chargements forcés de ses tranches seulement, puis rétablit ceux du jeu
forceload remove -16 26848 79 27151
forceload remove 80 26848 175 27151
forceload remove 176 26848 271 27151
forceload remove 272 26848 367 27151
forceload remove 368 26848 463 27151
forceload remove 464 26848 559 27151
forceload remove 560 26848 655 27151
forceload remove 656 26848 751 27151
forceload remove 752 26848 847 27151
forceload remove 848 26848 943 27151
forceload remove 944 26848 1039 27151
# $xbk revient à 0 : build_next peut de nouveau construire (le drapeau du parcours n'est pas posé)
scoreboard players set $xbk mg.st 0
function mg:core/forceloads
# la tranche 1 recouvre la zone de départ : si une partie se joue sur ce parcours, son fl_add est rétabli
execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run execute if score $xc mg.st matches 1 run function mg:elyrace/c1/fl_add
# nouvel essai dans 5 minutes (build_next : premier parcours sans drapeau ; reporté tant qu'une partie se joue)
schedule function mg:elyrace/build_next 300s
