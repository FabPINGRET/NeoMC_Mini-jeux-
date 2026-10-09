"""Cadres communs a tous les parcours : anneaux obligatoires, anneaux d'or, portiques de reprise, colonnes rayees.
Tout ce qui est solide est enregistre dans le World pour que le pilote automatique le voie.
Python stdlib uniquement (compatible 3.8).
"""
RING_COLORS = {'ring': ('sea_lantern', 'light_blue_concrete'),         # (blocs des 4 coins, bande)
               'finish': ('sea_lantern', 'lime_concrete')}
# Tous les anneaux sont un plan d'un bloc d'epaisseur (x..x) : leur plan de franchissement est x + 0,5 (sweep.plane).


def ring_frame(w, x, cy, cz, kind='ring'):
    """Cadre carre de 11 x 11 (trou de 9 x 9, bande d'un bloc) dans le plan x, centre (cy, cz) : bande coloree, coins lumineux."""
    corner, band = RING_COLORS[kind]
    w.box(x, cy - 5, cz - 5, x, cy + 5, cz + 5, band)
    w.box(x, cy - 4, cz - 4, x, cy + 4, cz + 4, 'air')
    for dy in (-5, 5):
        for dz in (-5, 5):
            w.box(x, cy + dy, cz + dz, x, cy + dy, cz + dz, corner)


def gold_frame(w, x, cy, cz):
    """Anneau d'or : cadre d'or de 9 x 9 (1 bloc d'epaisseur et de profondeur), trou de 7 x 7."""
    for r, blk in ((4, 'gold_block'), (3, 'air')):
        w.box(x, cy - r, cz - r, x, cy + r, cz + r, blk)


def wind_frame(w, x, cy, cz):
    """Anneau de vent : cadre blanc de 9 x 9 (1 bloc d'epaisseur et de profondeur), trou de 7 x 7."""
    for r, blk in ((4, 'white_concrete'), (3, 'air')):
        w.box(x, cy - r, cz - r, x, cy + r, cz + r, blk)


def cp_gate(w, x, cy, cz):
    """Portique de point de reprise : deux colonnes lumineuses de part et d'autre de la trajectoire, linteau tres haut."""
    for dz in (-12, 11):
        w.box(x + 4, cy - 16, cz + dz, x + 5, cy + 34, cz + dz + 1, 'sea_lantern')
    w.box(x + 4, cy + 34, cz - 12, x + 5, cy + 35, cz + 12, 'lime_concrete')


def col(w, strata, x1, z1, x2, z2, y0, y1):
    """Colonne pleine rayee comme le relief (une boite par bande de materiau)."""
    for s0, s1, blk in strata:
        if s1 < y0:
            continue
        if s0 > y1:
            break
        w.box(x1, max(y0, s0), z1, x2, min(y1, s1), z2, blk)
