"""Parcours 2 de la Course d'elytres : Pic Blanc (haute montagne), ~1100 blocs de long.

Depart au sommet (gare du telepherique), descente le long de pylones, col entre deux sommets, glacier, crevasse de
glace, grotte de glace eclairee, village d'arrivee. Ce module decrit le PARCOURS (profil, anneaux, points de reprise,
anneaux d'or) et le RELIEF ; la grotte est dans cave_blanc.py, les decors (gare, pylones, cables, village) dans
props_blanc.py. Meme methode que le Canyon : le profil d'altitude est derive d'un vol de reference simule
(glide.Pilot), le relief est construit autour de cette trajectoire.
Python stdlib uniquement (compatible 3.8).
"""
import sys

import cave_blanc as CV
import course_common as CC
import frames as F
import glide as G
import terrain as T
import wind as WD

NUM = 2                                     # numero de parcours : dossier elyrace/c2/, drapeau de construction, bouton du menu
NAME = 'Pic Blanc'
ICON, COLOR, STARS = '🏔', 'aqua', 4                      # bouton du menu : icone (menu texte), couleur, difficulte (etoiles sur 4)
TIP = ('Parcours 2 (haute montagne, ~1100 blocs) : pylônes de téléphérique, col, glacier, crevasse de glace, grotte éclairée, '
       'village d\'arrivée.')
FLAG = 'c2v1'                                # drapeau de construction (stockage mg:elyrace) : pose par la derniere tranche
CZ = 29600                                   # axe du parcours (z)
X0, X1 = -16, 1136                           # emprise en x (72 chunks, 12 tranches)
Z0, Z1 = 29440, 29760                        # emprise en z (20 chunks)
SUMMIT = 281                                 # surface du sommet de depart (bloc) : les pieds sont a y 282
START_Y = SUMMIT + 1                         # altitude des pieds sur la plateforme de depart
EDGE_X = 32                                  # bord de la falaise
GATE_X = 27                                  # portillon de depart (x), devant les joueurs
ROWS = 4                                     # lignes de joueurs sur la plateforme de depart
TV, TH = 6, 2                                # epaisseur de la coque : verticale (blocs), horizontale (cellules)

# profil d'altitude voulu de la trajectoire (x, y) ; le vol de reference le suit a quelques blocs pres
YPTS = [(24, 282), (100, 258), (330, 208), (520, 172), (760, 128), (960, 96), (1110, 64)]

# anneaux obligatoires : (x, decalage lateral, zone). L'altitude vient du vol de reference.
RINGS = [
    (90, 0, 'pylon'), (135, 8, 'pylon'), (180, -8, 'pylon'), (225, 6, 'pylon'), (270, 0, 'pylon'),
    (325, 0, 'col'), (375, -6, 'col'), (425, 6, 'col'),
    (485, 0, 'glacier'),
    (545, -3, 'crevasse'), (595, 3, 'crevasse'), (645, -3, 'crevasse'), (695, 3, 'crevasse'),
    (765, 0, 'glacier'),
    (855, 0, 'cave'), (910, 0, 'cave'),
    (1010, 0, 'village'), (1050, 0, 'village'), (1082, 4, 'village'), (1112, 0, 'village'),
]
CPS = [4, 8, 13, 17]                         # un point de reprise apres ces anneaux (numeros d'anneau)
GOLDS = [(360, -10), (515, -9), (880, 9)]   # anneaux d'or : (x, decalage lateral) ; altitude = trajectoire
GOLD_DY = 2                                  # les anneaux d'or sont 2 blocs sous la trajectoire : sur une pente douce, le detour
                                             # (pilote a anticipation reduite) vole ~2,2 blocs plus bas que la ligne de reference
WINDS = [(205, 10), (450, -10), (790, 12)]   # anneaux de vent (detours bonus) : (x, decalage lateral) ; generes seulement si wind.WIND
R_UP = {n: 28 for n in CPS}                  # hauteur de reapparition au-dessus du centre de l'anneau de chaque point de reprise


def ydes(x):
    return T.lerp_pts(YPTS, x)


def lat(x):
    """Decalage lateral de la trajectoire (z - CZ) : polyligne passant par les anneaux."""
    pts = [(24, 0)] + [(r[0], r[1]) for r in RINGS]
    return T.smooth_pts(pts, x)


def reference_waypoints(step=12):
    """Points de passage du vol de reference : le profil voulu, un point tous les `step` blocs."""
    xs = list(range(60, 1110, step)) + [R[0] for R in RINGS]
    return [(x, ydes(x), CZ + lat(x) + 0.5) for x in sorted(set(xs))]


def start_state():
    """Etat du joueur qui saute du sommet : il a couru jusqu'au bord, chute 8 ticks avant d'ouvrir ses elytres."""
    return G.State(EDGE_X + 0.3, START_Y, CZ + 0.5, 0.28, 0.0, 0.0)


# ---------------------------------------------------------------- relief
ROCK = ['stone', 'andesite', 'calcite', 'tuff', 'diorite']
ICE = ['packed_ice', 'blue_ice', 'packed_ice', 'calcite']      # glace dans la crevasse, le glacier et la grotte (jamais `ice`)
ICE_X = (465, 1010)                          # intervalle en x construit en glace ; le reste en roche
Q = 3                                        # quantification des hauteurs : terrasses de 3 blocs
MAXY = 300                                   # sommets plafonnes (limite du monde : 319)
# tables par abscisse : demi-largeur de la vallee, profondeur du fond sous la trajectoire, hauteur du dessus au-dessus
# de la trajectoire, pente des parois (blocs de hauteur par bloc horizontal), amplitude du bruit
HALFW = [(0, 60), (300, 55), (335, 38), (430, 36), (465, 58), (500, 70), (518, 46), (538, 16), (720, 16), (745, 40),
         (790, 46), (826, 12), (975, 12), (1010, 40), (1040, 80), (1140, 95)]
DEPTH = [(0, 40), (300, 34), (430, 30), (500, 26), (538, 26), (720, 26), (745, 22), (790, 14), (826, 11), (975, 11),
         (1000, 16), (1040, 18), (1140, 18)]
TOP = [(0, -2), (80, -2), (180, 25), (300, 70), (335, 90), (430, 90), (465, 40), (500, 22), (538, 18), (720, 18),
       (745, 20), (780, 22), (790, 35), (975, 35), (1000, 30), (1030, 40), (1140, 60)]
SLOPE = [(0, 1.3), (300, 1.5), (430, 1.6), (465, 0.8), (500, 0.5), (518, 1.0), (538, 8), (720, 8), (745, 1.2),
         (790, 1.0), (826, 8), (975, 8), (1010, 1.5), (1040, 0.8), (1140, 0.8)]
NOISE = [(0, 1), (520, 1), (540, 0.2), (720, 0.2), (745, 1), (800, 1), (826, 0), (1000, 0), (1030, 1), (1140, 1)]


def halfw(x):
    return T.lerp_pts(HALFW, x)


def floor_y(path, x):
    return path.y(x) - T.lerp_pts(DEPTH, x)


def top_y(path, xc, zc):
    """Hauteur du dessus de la montagne (sans bruit) : quantifiee, plafonnee ; bosse au-dessus de la grotte."""
    h = path.y(xc) + T.lerp_pts(TOP, xc) + CV.hill(xc, zc - CZ - lat(xc))
    return Q * int(round(min(h, MAXY) / Q))


def surface(path, xc, zc):
    """Hauteur du sol de la cellule de centre (xc, zc)."""
    if xc < EDGE_X:                                          # sommet : plateau qui s'effile sur les cotes
        return max(SUMMIT - max(0, abs(zc - CZ) - 22) * 1.1, floor_y(path, EDGE_X))
    nz = T.lerp_pts(NOISE, xc)
    d = abs(zc - CZ - lat(xc)) + 7 * nz * T.fbm(xc, zc, 11, 3, 40.0) - halfw(xc)
    fl = floor_y(path, xc) + 2.5 * nz * (T.fbm(xc, zc, 5, 3, 30.0) + 1)
    top = path.y(xc) + T.lerp_pts(TOP, xc) + 4 * nz * (T.fbm(xc, zc, 23, 3, 70.0) + 1) + CV.hill(xc, zc - CZ - lat(xc))
    if d <= 0:
        return fl
    return min(top, fl + d * T.lerp_pts(SLOPE, xc) + 3 * nz * T.fbm(xc, zc, 31, 2, 20.0))


def relief(path):
    """Cree le World et y pose le relief : sommet, pente de pylones, col, glacier, crevasse, vallee de la grotte, village."""
    nx, nz = (X1 - X0) // T.S, (Z1 - Z0) // T.S
    w = T.World(X0, Z0, nx, nz)
    for i in range(nx):
        xc = w.cell_x(i) + 2
        for j in range(nz):
            h = min(surface(path, xc, w.cell_z(j) + 2), MAXY)
            w.ground(i, j, SUMMIT if h == SUMMIT else Q * int(round(h / Q)))       # le sommet reste exactement a SUMMIT
    return w


def snow_cells(w):
    """Cellules de surface plate (aucun voisin plus bas de plus de 6 blocs) : elles recoivent une couche de snow_block."""
    out = {}
    for i in range(w.nx):
        for j in range(w.nz):
            t = w.top(i, j)
            ok = all(abs(t - w.top(min(max(i + di, 0), w.nx - 1), min(max(j + dj, 0), w.nz - 1))) <= 6
                     for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if ok:
                out[(i, j)] = [[t - 1, t]]
    return out


def extra_checks(c):
    """Controles propres au Pic Blanc : blocs interdits (glace simple, neige poudreuse ou en couche, blocs a gravite, stalactites
    de dripstone qui tombent, blocs suspects), lumiere de la grotte."""
    bad = []
    banned = ('ice', 'powder_snow', 'snow', 'pointed_dripstone', 'sand', 'red_sand', 'gravel', 'concrete_powder', 'anvil')
    seen = set()
    for cmd in list(c.rects) + list(c.world.cmds):
        blk = cmd[-1].split('[')[0]
        if (blk in banned or blk.endswith('_concrete_powder') or blk.startswith('suspicious_')) and blk not in seen:
            seen.add(blk)
            bad.append('bloc interdit sur le Pic Blanc : %s' % blk)
    return bad + CV.light_problems(c.world)


def build():
    """Construit le parcours complet (relief, grotte, decors, anneaux). Retourne un Course."""
    import props_blanc as P
    c = CC.Course(sys.modules[__name__])
    c.rings, c.trace = CC.reference(c.spec)
    c.path = CC.Path(c.trace)
    c.strata = T.make_strata(11, ROCK)
    ice = T.make_strata(13, ICE)
    w = c.world = relief(c.path)
    CV.roof(w, c.path, c.spec)
    kept = w.shell(TV, TH)
    cut = lambda inside: {k: v for k, v in kept.items() if inside(w.cell_x(k[0]) + 2)}
    c.rects = w.rects(cut(lambda x: not ICE_X[0] <= x < ICE_X[1]), c.strata, 0) + w.rects(cut(lambda x: ICE_X[0] <= x < ICE_X[1]), ice, 0)
    c.rects += w.rects(snow_cells(w), [(0, 999, 'snow_block')], 0)
    for gx, off in GOLDS:
        c.golds.append((gx, int(round(c.path.y(gx))) - GOLD_DY, CZ + int(round(lat(gx))) + off))
    for wx, off in WD.active(c.spec):
        c.winds.append((wx, int(round(c.path.y(wx))) - GOLD_DY, CZ + int(round(lat(wx))) + off))
    CV.stalactites(w, c.path, c.spec, [r[0] for r in c.rings] + [g[0] for g in c.golds])
    P.props(c)
    for n, (x, cy, cz, zone) in enumerate(c.rings, 1):
        F.ring_frame(w, x, cy, cz, 'finish' if n == len(c.rings) else 'ring')
    c.cps = list(CPS)
    for gx, gy, gz in c.golds:
        F.gold_frame(w, gx, gy, gz)
    for wx, wy, wz in c.winds:
        F.wind_frame(w, wx, wy, wz)
    for n in CPS:
        x, cy, cz, zone = c.rings[n - 1]
        F.cp_gate(w, x, cy, cz)
        P.gate_feet(w, x, cy, cz)
    CV.place_lights(w, c.path, c.spec)                       # en dernier : apres tous les cadres (ils effaceraient les lumieres)
    for r in range(ROWS * 4):                              # places de depart : deux rangees de 8 (16 places)
        c.places.append((GATE_X - 2 - 4 * (r // 8), CZ - 10 + 3 * (r % 8)))
    return c
