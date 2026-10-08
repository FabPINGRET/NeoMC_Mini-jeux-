# Arrête la construction : libère les chargements forcés des tranches de tous les parcours puis rétablit ceux du jeu
schedule clear mg:elyrace/build
schedule clear mg:elyrace/build_next
schedule clear mg:elyrace/c1/build_wait
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
scoreboard players set $xbk mg.st 0
function mg:core/forceloads
