# Course d'élytres : départ
function mg:elyrace/gate_off
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
tellraw @a[tag=mg.play] [{"text":"🪽 COURSE D'ÉLYTRES — CANYON DU COUCHANT : ","color":"aqua","bold":true},{"text":"saute de la falaise, ouvre tes élytres (espace en l'air) et franchis les 18 anneaux dans l'ordre, par le trou. Le premier arrivé gagne (3 minutes au plus).","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"♥ 3 cœurs : chaque choc contre un mur en retire un. Plus de cœur, anneau raté, sol, eau ou trop longtemps sans planer : retour en l'air au dernier point de reprise (colonnes lumineuses).","color":"gray"}]
tellraw @a[tag=mg.play] [{"text":"★ Trois anneaux d'or en détour : chacun donne une fusée (clic droit en vol pour accélérer).","color":"gold"}]
