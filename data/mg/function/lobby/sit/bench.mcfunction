# @s : un banc (spruce_stairs[half=bottom]) sous les pieds ou à côté, et libre ? Oui : s'y assoit (sit/seat), retourne 1 ; non : retourne 0
# un banc occupé est sauté (sit/bench_at retourne 0) : le candidat suivant, puis le sol
execute positioned ~ ~-1 ~ align xyz if function mg:lobby/sit/bench_at run return 1
execute positioned ~ ~ ~ align xyz if function mg:lobby/sit/bench_at run return 1
execute positioned ~1 ~ ~ align xyz if function mg:lobby/sit/bench_at run return 1
execute positioned ~-1 ~ ~ align xyz if function mg:lobby/sit/bench_at run return 1
execute positioned ~ ~ ~1 align xyz if function mg:lobby/sit/bench_at run return 1
execute positioned ~ ~ ~-1 align xyz if function mg:lobby/sit/bench_at run return 1
return 0
