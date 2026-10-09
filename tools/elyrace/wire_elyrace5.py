"""Met a jour le README pour les anneaux fins et le turbo de la Course d'elytres : python wire_elyrace5.py <racine du depot>. A lancer
APRES gen_elyrace.py et wire_elyrace.py (qui ecrit la ligne du README modifiee ici). Idempotent : le marqueur (le texte du turbo) est
cherche dans le README, s'il y est le script ne fait rien. Chaque ancre doit exister EXACTEMENT une fois (wirelib.Patcher : tout se fait
en memoire, rien n'est ecrit si une ancre manque) ; les fins de ligne du fichier sont conservees.
Branchement : README, ligne de la Course d'elytres : anneaux a cadre fin (trou de 9 x 9), ors = turbo de 3 s (gravite de course 0,104,
0,13 pendant le turbo) a la place de la fusee, nombre d'ors par parcours (Canyon 2, Pic Blanc 1 : voir GOLDS de course_*.py).
Aucun fichier du moteur (core/*) n'est touche. Python stdlib uniquement (compatible 3.8).
"""
import os
import sys

from wirelib import Patcher

MARKER = 'turbo de 3 s'
RINGS_OLD = 'par leur trou de 9 × 9 (un anneau raté'
RINGS_NEW = "par leur trou de 9 × 9 (cadre fin de 11 × 11, un bloc d'épaisseur ; un anneau raté"
GOLD_OLD = "**3 anneaux d'or** en détour qui donnent chacun une fusée (aucune au départ)"
GOLD_NEW = ("**anneaux d'or** en détour (trou de 7 × 7 ; 2 sur le Canyon, 1 sur le Pic Blanc) qui donnent chacun un **turbo de 3 s** "
            "(la gravité de course passe de 0,104 à 0,13 : tu piques plus vite ; pas de fusée, la gravité de course est posée au départ "
            "et rendue à l'arrivée)")
COUNTS = (("**22 anneaux**, 3 anneaux d'or,", "**22 anneaux**, 2 anneaux d'or,"),
          ("**20 anneaux**, 3 anneaux d'or,", "**20 anneaux**, 1 anneau d'or,"))


def wire_all(p):
    readme = p.path('README.md')
    if MARKER in p.text(readme)[0]:
        return
    p.patch(readme, RINGS_OLD, RINGS_NEW)
    p.patch(readme, GOLD_OLD, GOLD_NEW)
    for old, new in COUNTS:
        p.patch(readme, old, new)


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    p = Patcher(os.path.abspath(sys.argv[1]))
    wire_all(p)
    print('%d fichiers modifies' % p.commit())


if __name__ == '__main__':
    main()
