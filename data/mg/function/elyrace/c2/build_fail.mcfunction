# Abandon de la construction du parcours 2 : libère les chargements forcés de ses tranches seulement, puis rétablit ceux du jeu
forceload remove -16 29440 79 29759
forceload remove 80 29440 175 29759
forceload remove 176 29440 271 29759
forceload remove 272 29440 367 29759
forceload remove 368 29440 463 29759
forceload remove 464 29440 559 29759
forceload remove 560 29440 655 29759
forceload remove 656 29440 751 29759
forceload remove 752 29440 847 29759
forceload remove 848 29440 943 29759
forceload remove 944 29440 1039 29759
forceload remove 1040 29440 1135 29759
# $xbk revient à 0 : build_next peut de nouveau construire (le drapeau du parcours n'est pas posé)
scoreboard players set $xbk mg.st 0
function mg:core/forceloads
# la tranche 1 recouvre la zone de départ : si une partie se joue sur ce parcours, son fl_add est rétabli
execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run execute if score $xc mg.st matches 2 run function mg:elyrace/c2/fl_add
# nouvel essai dans 5 minutes (build_next : premier parcours sans drapeau ; reporté tant qu'une partie se joue)
schedule function mg:elyrace/build_next 300s
