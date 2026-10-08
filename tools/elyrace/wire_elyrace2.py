"""Branche les parcours multiples de la Course d'elytres : python wire_elyrace2.py <racine du depot>. A lancer APRES
gen_elyrace.py, une seule fois (apres wire_elyrace.py, deja applique sur main) : une 2e execution s'arrete sur la premiere
ancre introuvable, sans rien ecrire. Chaque ancre doit exister EXACTEMENT une fois (wirelib.Patcher : tout se fait en memoire,
rien n'est ecrit si une ancre manque) ; les fins de ligne de chaque fichier sont conservees.
Ids de lancement : 66 = parcours au hasard, menus.ID_BASE + NUM (81 = Canyon du Couchant, 82 = Pic Blanc) = ce parcours
(67..80 : TNT Tag, Bedwars, Elytra, Quakecraft sniper ; 100..196 : variantes).
core/request convertit 81..82 en $xc = id - 80 puis $game = 66, apres le bloc Quakecraft sniper et avant toute ligne qui teste 66 ;
core/go accepte 1..82 (seule la borne haute de la plage change, la clause « unless ... 100..196 » des variantes est conservee).
"""
import os
import sys

import dispatch as D
import menus as M
from wirelib import Patcher

VARIANTS = 'unless score @s mg.go matches 100..196'     # clause des variantes (feature/variantes) sur la ligne de validation de core/go
QUAKE_END = 'execute if score $game mg.st matches 79..80 run scoreboard players set $game mg.st 31'     # fin du bloc Quakecraft sniper


def go_range(p):
    """core/go : la borne haute de la plage acceptee passe de ID_BASE (derniere id prise : 80) a ID_BASE + nombre de parcours."""
    p.patch_fn('core/go', 'execute unless score @s mg.go matches 1..%d %s run return' % (M.ID_BASE, VARIANTS),
               'execute unless score @s mg.go matches 1..%d %s run return' % (M.ID_BASE + D.N_ROUTES, VARIANTS))


def request_wiring(p):
    """core/request : conversion des ids de parcours juste apres le bloc Quakecraft sniper (apres les remappages TNT Tag / Bedwars /
    Elytra / Quakecraft, qui ne les voient pas) et avant toute ligne qui teste le jeu 66 ; annonce du lancement deleguee a
    elyrace/announce (le parcours n'est pas encore tire en mode « au hasard »)."""
    path = p.fn_path('core/request')
    first, last = M.ID_BASE + 1, M.ID_BASE + D.N_ROUTES
    rng = '%d..%d' % (first, last)
    g = 'execute if score $game mg.st matches %s run scoreboard players ' % rng
    block = ("# Course d'élytres : 66 = parcours au hasard, %s = parcours 1..%d (%d Canyon du Couchant, %d Pic Blanc) → jeu 66 + parcours $xc (0 = au hasard)\n"
             'scoreboard players set $xc mg.st 0\n'
             + g + 'operation $xc mg.st = $game mg.st\n'
             + g + 'remove $xc mg.st %d\n'
             + g + 'set $game mg.st 66\n') % (rng, D.N_ROUTES, first, last, M.ID_BASE)
    p.between(path, QUAKE_END, 'scoreboard players set $pm mg.st 0', block)
    p.replace_line(path, 'execute if score $game mg.st matches 66 run tellraw',
                   'execute if score $game mg.st matches 66 run function mg:elyrace/announce')


def build_wiring(p):
    """core/setup_build (reconstruction du monde) et core/load : la construction passe par build_next (premier parcours sans drapeau).
    core/load remet le marqueur de construction $xbk a 0 (il n'est pas efface par un redemarrage) : build_next ne peut donc pas
    rester bloque. Si une construction tournait encore (schedule conserve), elle perd son etat ; build_next la relance 60 s apres
    le chargement depuis la tranche 1 (build_start remplace le schedule de build_wait, chaque tranche libere son forceload en
    s'achevant). Un schedule perdu (arret du serveur) donne le meme resultat."""
    p.patch_fn('core/setup_build', 'data remove storage mg:elyrace v1\nschedule function mg:elyrace/build 45s',
               'function mg:elyrace/forget\nschedule function mg:elyrace/build_next 45s')
    p.patch_fn('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:elyrace v1 run schedule function mg:elyrace/build 60s',
               'execute if score $setup mg.st matches 1 run scoreboard players set $xbk mg.st 0\n'
               'execute if score $setup mg.st matches 1 run schedule function mg:elyrace/build_next 60s')


def docs(p):
    """aide, README (texte et table des commandes), docs/GAMES.md."""
    p.replace_line(p.fn_path('aide'), 'tellraw @s [{"text":"• Course d\'élytres (admins) : "',
                   'tellraw @s [{"text":"• Course d\'élytres (admins) : ","color":"gray"},{"text":"/trigger mg.go set 66","color":"yellow"},'
                   '{"text":" (parcours au hasard), ","color":"gray"},{"text":"81","color":"yellow"},'
                   '{"text":" (Canyon du Couchant, 18 anneaux) ou ","color":"gray"},{"text":"82","color":"yellow"},'
                   '{"text":" (Pic Blanc, pas encore construit) ; reconstruire : /function mg:elyrace/build","color":"gray"}]')
    readme = p.path('README.md')
    p.patch(readme, "| **🪽 Course d'élytres : Canyon du Couchant** (id 66) |",
            "| **🪽 Course d'élytres : Canyon du Couchant** (id 81 ; id 66 = parcours au hasard, id 82 = Pic Blanc, pas encore construit) |")
    p.patch(readme, "avec la Course d'élytres, id 66 :", "avec la Course d'élytres, ids 66, 81 et 82 :")
    p.replace_line(readme, "| `/trigger mg.go set 66` | Course d'élytres : Canyon du Couchant |",
                   "| `/trigger mg.go set 66` | Course d'élytres : parcours au hasard parmi ceux qui sont construits | admins |\n"
                   "| `/trigger mg.go set 81` | Course d'élytres : Canyon du Couchant | admins |\n"
                   "| `/trigger mg.go set 82` | Course d'élytres : Pic Blanc (pas encore construit : partie annulée) | admins |")
    games = p.path('docs', 'GAMES.md')
    p.patch(games, '| 66 | `mg:elyrace/tick` |\n', '| 66 | `mg:elyrace/tick` (ids 81..82 → $xc) |\n')
    p.patch(games, 'Élytra 75..78 → 75 + `$elm` (remappage dans `core/request`).',
            'Élytra 75..78 → 75 + `$elm` ; Course d\'élytres 81..82 → 66 + `$xc` (remappage dans `core/request`).')


def wire_all(p):
    go_range(p)
    request_wiring(p)
    build_wiring(p)
    docs(p)


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    p = Patcher(os.path.abspath(sys.argv[1]))
    wire_all(p)
    print('%d fichiers modifies' % p.commit())


if __name__ == '__main__':
    main()
