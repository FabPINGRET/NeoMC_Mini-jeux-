# Arrête la construction : libère les chargements forcés des tranches de tous les parcours puis rétablit ceux du jeu
schedule clear mg:elyrace/build
schedule clear mg:elyrace/build_next
schedule clear mg:elyrace/c1/build_wait
schedule clear mg:elyrace/c2/build_wait
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
scoreboard players set $xbk mg.st 0
function mg:core/forceloads
