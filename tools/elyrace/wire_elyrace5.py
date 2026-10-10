"""Met a jour le README pour les anneaux fins, les ors et le bouton Rejouer (solo) de la Course d'elytres : python wire_elyrace5.py <racine du depot>. A lancer
APRES gen_elyrace.py et wire_elyrace.py (qui ecrit la ligne du README modifiee ici). Idempotent : chaque etape est sautee si son marqueur est
deja dans le README (quatre etapes : anneaux fins + ors en turbo, tant qu'aucun marqueur du turbo ni du bonus n'y est ; la phrase
"desinstaller pendant une course" ; les ors en bonus de temps ; « Rejouer » en fin de solo, phrase du solo et ligne du tableau des triggers). Chaque ancre doit exister EXACTEMENT une fois (wirelib.Patcher : tout se
fait en memoire, rien n'est ecrit si une ancre manque) ; les fins de ligne du fichier sont conservees.
Branchement : README, ligne de la Course d'elytres : anneaux a cadre fin (trou de 9 x 9), ors = bonus de temps de 2 s (retire du temps final,
une fois par course) a la place de la fusee, le meilleur temps gagne, nombre d'ors par parcours (Canyon 2, Pic Blanc 1 : voir GOLDS de course_*.py).
Le solo propose [Rejouer] (trigger mg.xs set 5) a l'arrivee, retour au lobby automatique au bout de 30 s. Aucun fichier du moteur (core/*) n'est touche. Python stdlib uniquement (compatible 3.8).
"""
import os
import sys

from wirelib import Patcher

MARKER = 'turbo de 3 s'
BONUS_MARKER = 'bonus de temps'
RETRY_MARKER = '[⟲ Rejouer]'
UNINSTALL_MARKER = "Désinstaller pendant une course"
UNINSTALL_OLD = 'au bout de 3 minutes le plus avancé gagne. **Contre-la-montre solo**'
UNINSTALL_NEW = ("au bout de 3 minutes le plus avancé gagne. **Désinstaller pendant une course** : la désinstallation remet la gravité normale "
                 "aux coureurs en ligne, pas aux participants déconnectés : ils garderaient la gravité de course (après la désinstallation, rien ne la leur rendra à la reconnexion). "
                 "**Contre-la-montre solo**")
RINGS_OLD = 'par leur trou de 9 × 9 (un anneau raté'
RINGS_NEW = "par leur trou de 9 × 9 (cadre fin de 11 × 11, un bloc d'épaisseur ; un anneau raté"
GOLD_OLD = "**3 anneaux d'or** en détour qui donnent chacun une fusée (aucune au départ)"
GOLD_NEW = ("**anneaux d'or** en détour (trou de 7 × 7 ; 2 sur le Canyon, 1 sur le Pic Blanc) qui donnent chacun un **turbo de 3 s** "
            "(la gravité de course passe de 0,104 à 0,13 : tu piques plus vite ; pas de fusée, la gravité de course est posée au départ "
            "et rendue à l'arrivée)")
BONUS_NEW = ("**anneaux d'or** en détour (trou de 7 × 7 ; 2 sur le Canyon, 1 sur le Pic Blanc) qui donnent chacun un **bonus de temps de 2 s** "
             "(retiré du temps final, une fois par course et gardé après une réapparition ; pas de fusée, la gravité de course est posée au départ "
             "et rendue à l'arrivée)")
FIRST_OLD = "Le premier arrivé gagne, les autres sont classés pendant 20 s"
FIRST_NEW = "Le meilleur temps gagne (bonus d'or compris) ; après le premier arrivé, les autres ont 20 s"
RETRY_OLD = "30 s d'attente entre deux solos (sauf admins) ;"
RETRY_NEW = ("30 s d'attente entre deux solos (sauf admins) ; à l'arrivée, **[⟲ Rejouer]** (`/trigger mg.xs set 5`) relance tout de suite le même parcours "
             "(autant de fois que tu veux), sinon retour automatique au lobby au bout de 30 s (**[⌂ Retour au lobby]** pour y aller plus vite) ;")
RETRY_ROW_OLD = "| `/trigger mg.xs set 2` / `set 3` | Contre-la-montre solo : abandonner / afficher ses meilleurs temps et les records du serveur | tous |\n"
RETRY_ROW_NEW = RETRY_ROW_OLD + "| `/trigger mg.xs set 5` | Contre-la-montre solo : rejouer le même parcours (bouton affiché à l'arrivée, 30 s avant le retour automatique au lobby) | tous |\n"
COUNTS = (("**22 anneaux**, 3 anneaux d'or,", "**22 anneaux**, 2 anneaux d'or,"),
          ("**20 anneaux**, 3 anneaux d'or,", "**20 anneaux**, 1 anneau d'or,"))


def wire_all(p):
    readme = p.path('README.md')
    text = p.text(readme)[0]
    if MARKER not in text and BONUS_MARKER not in text:
        p.patch(readme, RINGS_OLD, RINGS_NEW)
        p.patch(readme, GOLD_OLD, GOLD_NEW)
        for old, new in COUNTS:
            p.patch(readme, old, new)
    if UNINSTALL_MARKER not in text:
        p.patch(readme, UNINSTALL_OLD, UNINSTALL_NEW)
    if BONUS_MARKER not in text:
        p.patch(readme, GOLD_NEW, BONUS_NEW)
        p.patch(readme, FIRST_OLD, FIRST_NEW)
    if RETRY_MARKER not in text:
        p.patch(readme, RETRY_OLD, RETRY_NEW)
        p.patch(readme, RETRY_ROW_OLD, RETRY_ROW_NEW)


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    p = Patcher(os.path.abspath(sys.argv[1]))
    wire_all(p)
    print('%d fichiers modifies' % p.commit())


if __name__ == '__main__':
    main()
