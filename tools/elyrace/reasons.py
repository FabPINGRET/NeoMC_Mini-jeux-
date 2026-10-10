"""Raison affichee au joueur quand la course le ramene au dernier point de reprise (mg:elyrace/why/<nom>) : un sous-titre (pas de message
dans le chat) puis la reapparition. Chaque cause de reprise (anneau rate, plus de coeur, sol, eau, vol plane perdu, sortie du parcours,
mort) appelle SA fonction why/<nom> ; seules elles appellent mg:elyrace/respawn (verifie par checks.logic_problems). Le sous-titre ne
s'affiche qu'avec un titre : un titre vide l'accompagne ; les durees (times) sont reposees a chaque fois, un autre jeu les ayant peut-etre raccourcies. Python stdlib uniquement (compatible 3.8).
"""
# (nom, texte, couleur) : le nom est celui de la fonction why/<nom>
REASONS = [
    ('miss', '✖ Anneau raté', 'red'),
    ('ko', '♡ Plus de cœur', 'red'),
    ('ground', '⬇ Au sol', 'gold'),
    ('water', "≈ Dans l'eau", 'aqua'),
    ('stall', '🪽 Vol plané perdu', 'yellow'),
    ('out', '⚠ Sorti du parcours', 'red'),
    ('dead', '☠ Mort', 'dark_red'),
]
HIT = ('💥 Choc ! -1 ♥', 'red')      # un mur touche, il reste des coeurs : pas de reprise, juste le sous-titre


def subtitle(text, color):
    """Lignes qui affichent `text` en sous-titre au joueur (@s) : durees (entree, maintien, sortie en ticks), sous-titre, titre vide."""
    return ['title @s times 5 50 15', 'title @s subtitle [{"text":"%s","color":"%s"}]' % (text, color), 'title @s title ""']


def call(name):
    """Commande de reprise d'une cause : l'unique facon d'appeler elyrace/respawn hors de why/*."""
    return 'function mg:elyrace/why/' + name


def functions():
    return {'why/' + n: ['# @s = joueur ramene au dernier point de reprise : %s (sous-titre, puis reapparition)' % t] + subtitle(t, c)
            + ['function mg:elyrace/respawn'] for n, t, c in REASONS}
