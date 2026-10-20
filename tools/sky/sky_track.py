"""Élytra : géométrie du parcours (anneaux, plateformes, zone de jeu) et espace de noms des fonctions (NS).
Module importé par sky_shapes, sky_layout, sky_game et sky_modes.
"""
NS = 'mg:sky'


# =====================================================================================
# Géométrie : parcours (modes 1-2)
# =====================================================================================
PAD1 = (0, 235, 27640)      # plateforme de départ (dessus du plancher à y 235)
PAD3 = (0, 195, 29000)      # plateforme de décollage de l'arène (mode 3)
PADR = 6                    # rayon des plateformes
# (x, y, z, taille du cadre, type)  type : n normal, b boost (fusée), f arrivée
RINGS = [
    (0, 226, 27700, 9, 'n'),
    (35, 219, 27745, 7, 'n'),
    (85, 213, 27775, 7, 'n'),
    (135, 205, 27815, 9, 'b'),
    (150, 198, 27880, 7, 'n'),
    (110, 193, 27930, 7, 'n'),
    (55, 188, 27955, 9, 'n'),
    (-5, 182, 27975, 7, 'n'),
    (-70, 176, 27990, 9, 'b'),
    (-130, 169, 28030, 7, 'n'),
    (-155, 163, 28090, 7, 'n'),
    (-120, 157, 28140, 9, 'n'),
    (-60, 151, 28160, 7, 'n'),
    (0, 145, 28175, 9, 'b'),
    (60, 139, 28190, 7, 'n'),
    (120, 132, 28220, 7, 'n'),
    (150, 126, 28280, 9, 'n'),
    (115, 120, 28335, 9, 'b'),
    (55, 114, 28360, 7, 'n'),
    (-10, 108, 28350, 9, 'f'),
]
N = len(RINGS)
ZONE = (-205, 88, 27590, 410, 190, 820)          # sortie de zone (x, y, z, dx, dy, dz)
PERCH1 = (0, 250, 27700)
PERCH3 = (0, 222, 28940)
ARENA = (0, 29000)
FLOOR3 = 96                                       # mode 3 : sous ce y = éliminé
RING_COLS = ['pearlescent_froglight', 'verdant_froglight', 'sea_lantern']

PATH = [(PAD1[0], PAD1[1] + 1, PAD1[2])] + [(x, y, z) for x, y, z, _, _ in RINGS]


def axis_of(i):
    """Axe de traversée de l'anneau i (0-based) : 'x' (cadre dans le plan YZ) ou 'z'."""
    a = PATH[i]
    b = PATH[i + 2] if i + 2 < len(PATH) else PATH[i + 1]
    dx, dz = b[0] - a[0], b[2] - a[2]
    return 'x' if abs(dx) >= abs(dz) else 'z'


AXES = [axis_of(i) for i in range(N)]
