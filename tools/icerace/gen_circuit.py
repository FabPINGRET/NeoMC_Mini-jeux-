"""Génère le circuit de la course de bateaux sur glace (icerace) : tracé doux, murs, grille, points de passage.

    python3 tools/icerace/gen_circuit.py      # depuis la racine du dépôt

Écrit data/mg/function/icerace/{build,cp_check,rescue,place_one,gate_on,gate_off}.mcfunction,
met à jour le perchoir et le spawnpoint de prepare.mcfunction, et dessine tools/icerace/apercu.png.

Tracé : la ligne médiane est définie par son PROFIL DE COURBURE (enchaînement de lignes droites et de
virages à rampes sin², donc courbure continue), intégré puis fermé numériquement (2 inconnues : longueur
de fin de ligne droite et rayon du dernier virage). Le rayon mini est donc maîtrisé par construction ;
il est recalculé sur la courbe échantillonnée et le script refuse d'écrire quoi que ce soit s'il est < 14.
Sens de course : anti-horaire vu du ciel (nord en haut) : ligne droite des stands vers l'est (sud du circuit),
grand virage à gauche en deux temps, S doux sur le contre-bord, épingle large à l'ouest.
Rasterisation : cellule = piste si son centre est à <= HW de la ligne médiane ; murs = cellules hors piste
voisines (8-voisinage) d'une cellule de piste → aucun trou possible ; contrôles topologiques avant écriture.
"""
import math, os, re, sys
import numpy as np
from scipy import ndimage
from scipy.optimize import least_squares
from scipy.spatial import cKDTree

ROOT = os.getcwd()
FN = os.path.join(ROOT, 'data', 'mg', 'function', 'icerace')
TOOLS = os.path.join(ROOT, 'tools', 'icerace')
if not os.path.isdir(FN):
    sys.exit('À lancer depuis la racine du dépôt (data/mg/function/icerace introuvable)')

CX, CZ = 0, 13200                 # centre de la zone
X0, X1, Z0, Z1 = -75, 75, 13145, 13255   # zone (forceloadée), bornes incluses
Y = 80                            # sol de la piste (joueurs en y 81)
HW = 5.0                          # demi-largeur de piste (largeur 10 en ligne droite, 9 à 11 en courbe)
RCP = HW + 1.5                    # rayon de détection des points de passage
R_LIMIT = 14.0                    # rayon de courbure mini exigé pour la ligne médiane
R_SNOW = 26.0                     # rayon en dessous duquel l'extérieur du virage est en neige
SNOW_OFF = 1.0                    # neige au-delà d'1 bloc de la ligne médiane, côté extérieur
DS = 0.05                         # pas d'échantillonnage de la ligne médiane
RAMP = 10.0                       # longueur des rampes de courbure (entrée/sortie de virage)

# ------------------------------------------------------------------ tracé (profil de courbure)
# Repère mathématique (x est, z nord), angles en degrés, gauche > 0. Les inconnues LX, R3 ferment la boucle.
L0 = 14.0                         # début de la ligne droite des stands (après la ligne de départ)
A1, R1 = 105, 16.0                # virage 1 : gauche 105°
A2, R2 = 75, 16.0                 # virage 2 : gauche 75° (enchaîné : grand virage en deux temps)
BS, RS = 30, 15.0                 # S doux : gauche 30° puis droite 30°


def turn(angle, R):
    """Virage : rampe sin² de RAMP blocs, plateau à 1/R, rampe. Renvoie (courbures, pas)."""
    angle = math.radians(angle)
    L = max(0.0, abs(angle) * R - RAMP) + 2 * RAMP
    n = max(8, int(math.ceil(L / DS)))
    ds = L / n
    s = (np.arange(n) + 0.5) * ds
    w = np.ones(n)
    up, dn = s < RAMP, s > L - RAMP
    w[up] = np.sin(math.pi / 2 * s[up] / RAMP) ** 2
    w[dn] = np.sin(math.pi / 2 * (L - s[dn]) / RAMP) ** 2
    return w * angle / (w.sum() * ds), ds


def straight(L):
    L = max(L, 0.0)
    n = max(1, int(math.ceil(L / DS)))
    return np.zeros(n), L / n


def pieces(LX, R3):
    return [straight(L0), turn(A1, R1), turn(A2, R2), turn(BS, RS), turn(-BS, RS),
            turn(360 - A1 - A2, R3), straight(LX)]


def closure(P):
    th = x = z = 0.0
    for k, ds in P:
        t = th + (np.cumsum(k) - k / 2) * ds
        x += np.cos(t).sum() * ds
        z += np.sin(t).sum() * ds
        th += k.sum() * ds
    return x, z


sol = least_squares(lambda v: closure(pieces(*v)), (20.0, 16.0), bounds=([0.0, 10.0], [200.0, 60.0]))
LX, R3 = sol.x
P = pieces(LX, R3)
pts, KM, SEG = [], [], []
th = x = z = 0.0
for k, ds in P:
    for kk in k:
        pts.append((x, z)); KM.append(kk); SEG.append(ds)
        t = th + kk * ds / 2
        x += math.cos(t) * ds; z += math.sin(t) * ds; th += kk * ds
GAP = math.hypot(x, z)                    # défaut de fermeture
pts = np.array(pts); KM = np.array(KM); seg = np.array(SEG)
# Repère Minecraft : z vers le sud → on retourne z (la courbure change de signe)
ZC = int(round(CZ + (pts[:, 1].max() - pts[:, 1].min()) / 2))   # z de la ligne droite (entier)
XOFF = int(round(CX - (pts[:, 0].max() + pts[:, 0].min()) / 2))
pos = np.stack([pts[:, 0] + XOFF, ZC - pts[:, 1]], 1)
KS = -KM                                   # courbure signée en repère Minecraft
NS = len(pos)
S = np.concatenate([[0], np.cumsum(seg)[:-1]])
LENGTH = float(seg.sum())
TAN = np.roll(pos, -1, 0) - np.roll(pos, 1, 0)
TAN /= np.linalg.norm(TAN, axis=1)[:, None]
RMIN = 1 / np.abs(KS).max()
# contrôle indépendant : courbure par cercle circonscrit sur des triplets espacés de 1 bloc
h = int(round(1 / DS))
a_, b_, c_ = np.roll(pos, h, 0), pos, np.roll(pos, -h, 0)
cr = np.abs((b_[:, 0] - a_[:, 0]) * (c_[:, 1] - a_[:, 1]) - (b_[:, 1] - a_[:, 1]) * (c_[:, 0] - a_[:, 0]))
RMIN_GEO = float(np.min(np.linalg.norm(b_ - a_, axis=1) * np.linalg.norm(c_ - b_, axis=1)
                        * np.linalg.norm(c_ - a_, axis=1) / np.maximum(2 * cr, 1e-12)))


def at_s(s):
    """Indice d'échantillon le plus proche de l'abscisse s (modulo la longueur)."""
    s %= LENGTH
    return int(np.argmin(np.abs(((S - s + LENGTH / 2) % LENGTH) - LENGTH / 2)))


def yaw(i):
    return round(math.degrees(math.atan2(-TAN[i, 0], TAN[i, 1])), 1)


# ------------------------------------------------------------------ ligne droite, grille, ligne d'arrivée
straight_i = np.where((np.abs(KS) < 1e-12) & (np.abs(pos[:, 1] - ZC) < 1e-6))[0]
SX0, SX1 = pos[straight_i, 0].min(), pos[straight_i, 0].max()
GATE = int(math.floor(SX0)) + 26          # colonne du portillon (grille de 8 rangs derrière)
LINE = GATE + 2                           # ligne d'arrivée : colonnes LINE et LINE+1
GRID = [(GATE - 2.5 - 3 * r, ZC + dz) for r in range(8) for dz in (-3, 0, 3)]
GYAW = -90.0                              # vers l'est
i_fin = int(np.argmin(np.hypot(pos[:, 0] - (LINE + 5), pos[:, 1] - ZC)))
S_FIN = S[i_fin]
CP = [at_s(S_FIN + LENGTH * k / 10) for k in range(1, 11)]   # CP[9] = juste après la ligne d'arrivée

# ------------------------------------------------------------------ rasterisation
xs = np.arange(X0, X1 + 1)
zs = np.arange(Z0, Z1 + 1)
GX, GZ = np.meshgrid(xs + 0.5, zs + 0.5, indexing='ij')     # centres des cellules
dist, near = cKDTree(pos).query(np.stack([GX.ravel(), GZ.ravel()], 1))
dist = dist.reshape(GX.shape)
near = near.reshape(GX.shape)
off = (TAN[near, 0] * (GZ - pos[near, 1]) - TAN[near, 1] * (GX - pos[near, 0]))   # décalage latéral signé
track = dist <= HW
wall = ndimage.binary_dilation(track, np.ones((3, 3), bool)) & ~track
empty = ~track & ~wall
lab, nlab = ndimage.label(empty)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
infield = np.isin(lab, [k for k in range(1, nlab + 1) if k not in border])

# Courbure lissée (max sur ±6 blocs) pour des zones de neige continues
win = int(6 / DS)
kmax = ndimage.maximum_filter1d(np.abs(KS), 2 * win + 1, mode='wrap')
ksign = np.sign(ndimage.uniform_filter1d(KS, 2 * win + 1, mode='wrap'))
outside = off * ksign[near] < 0
snow = track & outside & (np.abs(off) >= SNOW_OFF) & (kmax[near] > 1 / R_SNOW)
snow &= ~((GZ > ZC - 8) & (GZ < ZC + 8) & (GX > SX0 - 2) & (GX < SX1 + 2))   # jamais sur la ligne droite

# ------------------------------------------------------------------ contrôles (AVANT toute écriture)
errs = []
if GAP > 0.05:
    errs.append(f'boucle non fermée (écart {GAP:.2f})')
if min(RMIN, RMIN_GEO) < R_LIMIT:
    errs.append(f'rayon mini {min(RMIN, RMIN_GEO):.1f} < {R_LIMIT}')
if not 180 <= LENGTH <= 220:
    errs.append(f'longueur {LENGTH:.0f} hors de 180..220')
if GRID[-1][0] - 1 < SX0 or LINE + 4 > SX1:
    errs.append('grille / ligne d\'arrivée hors de la ligne droite')
if wall[0].any() or wall[-1].any() or wall[:, 0].any() or wall[:, -1].any():
    errs.append('mur sur le bord de la zone')
if ndimage.label(track)[1] != 1:
    errs.append('piste non connexe')
if nlab != 2 or len(border) != 1:
    errs.append(f'topologie : {nlab} zones vides (attendu 2 : extérieur + intérieur de la boucle)')
widths = []
for i in range(0, NS, int(2 / DS)):        # largeur réelle (cellules de piste sur la normale)
    nx, nz = -TAN[i, 1], TAN[i, 0]
    cnt = 0
    for t in np.arange(-7, 7.01, 0.25):
        cx, cz = int(math.floor(pos[i, 0] + t * nx)) - X0, int(math.floor(pos[i, 1] + t * nz)) - Z0
        cnt += track[cx, cz]
    widths.append(cnt * 0.25)
WMIN, WMAX = min(widths), max(widths)
# pas de rapprochement entre deux portions éloignées de la piste
sub, ssub = pos[::20], S[::20]
dd = np.hypot(sub[:, None, 0] - sub[None, :, 0], sub[:, None, 1] - sub[None, :, 1])
ds_ = np.abs(ssub[:, None] - ssub[None, :])
ds_ = np.minimum(ds_, LENGTH - ds_)
gap = dd[ds_ > 3 * HW + 6].min()
if gap < 2 * HW + 3:
    errs.append(f'deux portions de piste trop proches ({gap:.1f})')
for k, i in enumerate(CP):
    cx, cz = int(math.floor(pos[i, 0])), int(math.floor(pos[i, 1]))
    if not track[cx - X0, cz - Z0]:
        errs.append(f'point {k + 1} hors piste')
if (S[CP[0]] - S_FIN) % LENGTH < 15:
    errs.append('point 1 trop près de la grille')

print(f'Longueur ligne médiane : {LENGTH:.1f} blocs (fermeture : LX={LX:.2f}, R3={R3:.2f}, écart {GAP:.3f})')
print(f'Rayon de courbure mini : {RMIN:.2f} (contrôle géométrique {RMIN_GEO:.2f}, exigé >= {R_LIMIT})')
print(f'Largeur : {2 * HW:.0f} nominale, mesurée {WMIN:.2f} .. {WMAX:.2f}')
if errs:
    print('ERREURS — rien n\'est écrit :', *errs, sep='\n  ')
    sys.exit(1)


# ------------------------------------------------------------------ écriture
def rects(mask):
    """Découpe un masque 2D en rectangles (runs en x par ligne z, fusionnés sur z)."""
    runs = {}
    for zi in range(mask.shape[1]):
        col = mask[:, zi]
        xi = 0
        while xi < len(col):
            if col[xi]:
                xe = xi
                while xe + 1 < len(col) and col[xe + 1]:
                    xe += 1
                runs.setdefault((xi, xe), []).append(zi)
                xi = xe + 1
            else:
                xi += 1
    out = []
    for (xa, xb), zl in runs.items():
        za = prev = zl[0]
        for z in zl[1:] + [None]:
            if z is not None and z == prev + 1:
                prev = z
                continue
            out.append((xa + X0, za + Z0, xb + X0, prev + Z0))
            if z is not None:
                za = prev = z
    return sorted(out, key=lambda r: (r[1], r[0]))


def fills(mask, y0, y1, block):
    out = []
    for xa, za, xb, zb in rects(mask):
        assert (xb - xa + 1) * (zb - za + 1) * (y1 - y0 + 1) <= 32768
        out.append(f'fill {xa} {y0} {za} {xb} {y1} {zb} minecraft:{block}')
    return out


def write(name, lines):
    with open(os.path.join(FN, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def f1(v):
    return f'{v:.1f}'


DISP = 'Tags:["mg.ird","mg.fx"]'    # décor en entités : retiré par build et par le retour au lobby (mg.fx)
B = ['# Course de bateaux sur glace — circuit généré par tools/icerace/gen_circuit.py (centre 0 ~ 13200)',
     f'# Ligne médiane {LENGTH:.0f} blocs, largeur {2 * HW:.0f}, rayon mini {RMIN:.1f}. Ne pas éditer à la main.',
     '# Effacement complet de la zone (une couche par fill : 151 x 111 = 16761 blocs)']
for y in range(79, 91):
    B.append(f'fill {X0} {y} {Z0} {X1} {y} {Z1} minecraft:air')
B.append('kill @e[tag=mg.ird]')
B.append('# Piste : glace compacte, neige à l\'extérieur des virages (freine)')
B += fills(track & ~snow, Y, Y, 'packed_ice')
B += fills(snow, Y, Y, 'snow_block')
B.append('# Intérieur de la boucle : neige')
B += fills(infield, Y, Y, 'snow_block')
B.append('# Murs (sol + 2 blocs) + barrières jusqu\'en y 85')
B += fills(wall, Y, Y + 2, 'light_blue_concrete')
B += fills(wall, Y + 3, Y + 5, 'barrier')

# Lanternes : dans le haut du mur (y 82), tous les ~9 blocs de chaque côté
lant = []
wi = np.argwhere(wall)
w_s = S[near[wall]]
w_side = np.sign(off[wall])
w_d = dist[wall]
for side in (-1, 1):
    for s0 in np.arange(4.5, LENGTH, 9):
        ok = (w_side == side) & (w_d < HW + 1.6)
        dS = np.abs(((w_s - s0 + LENGTH / 2) % LENGTH) - LENGTH / 2)
        cand = np.where(ok & (dS < 2))[0]
        if len(cand):
            k = cand[np.argmin(dS[cand])]
            x, z = wi[k][0] + X0, wi[k][1] + Z0
            if not (LINE - 1 <= x <= LINE + 2 and abs(z - ZC) < 8):
                lant.append((x, z))
B.append('# Lanternes dans les murs')
B += [f'setblock {x} {Y + 2} {z} minecraft:sea_lantern' for x, z in lant]

# Ligne de départ/arrivée : damier en block_display (sans effet sur la glisse)
zt = [z for z in range(Z0, Z1 + 1) if track[LINE - X0, z - Z0] and abs(z - ZC) < 8]
ZA, ZB = min(zt), max(zt)
B.append('# Ligne de départ/arrivée en damier (affichage seulement, la glace reste dessous)')
for x in (LINE, LINE + 1):
    for z in range(ZA, ZB + 1):
        blk = 'black_concrete' if (x + z) % 2 else 'white_concrete'
        B.append(f'summon minecraft:block_display {x} {Y + 1}.005 {z} {{{DISP},block_state:{{Name:"minecraft:{blk}"}},'
                 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,0.01f,1f]}}')
B.append('# Arche de départ : piliers, poutre en damier, fanions, panneau')
for z in (ZA - 1, ZB + 1):
    B.append(f'fill {LINE} {Y} {z} {LINE + 1} {Y + 6} {z} minecraft:white_concrete')
    B.append(f'setblock {LINE} {Y + 3} {z} minecraft:sea_lantern')
    B.append(f'setblock {LINE + 1} {Y + 3} {z} minecraft:sea_lantern')
for x in (LINE, LINE + 1):
    for y in (Y + 7, Y + 8):
        for z in range(ZA - 1, ZB + 2):
            blk = 'black_concrete' if (x + y + z) % 2 else 'white_concrete'
            B.append(f'setblock {x} {y} {z} minecraft:{blk}')
for z in range(ZA, ZB + 1):
    col = ('red', 'white', 'light_blue')[(z - ZA) % 3]
    B.append(f'setblock {LINE - 1} {Y + 7} {z} minecraft:{col}_wall_banner[facing=west]')
    B.append(f'setblock {LINE + 2} {Y + 7} {z} minecraft:{col}_wall_banner[facing=east]')
B.append(f'summon minecraft:text_display {LINE + 1} {Y + 10}.2 {ZC} {{{DISP},billboard:"center",'
         'text:[{"text":"⛵ COURSE SUR GLACE","color":"aqua","bold":true}],background:1073741824,'
         'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}')

# Sapins enneigés dans la boucle (loin des murs)
dist_in = ndimage.distance_transform_edt(infield)
trees = []
order = sorted(np.argwhere(dist_in >= 4).tolist(), key=lambda c: -dist_in[c[0], c[1]])
for cx, cz in order:
    if all(math.hypot(cx - a, cz - b) >= 9 for a, b in trees):
        trees.append((cx, cz))
    if len(trees) >= 7:
        break
B.append('# Sapins enneigés')
for cx, cz in trees:
    x, z = cx + X0, cz + Z0
    ht = 7 if (x + z) % 2 else 6
    vox = {}
    layers = [(Y + 3, 2), (Y + 4, 1), (Y + 5, 2), (Y + 6, 1)] + ([(Y + 7, 1)] if ht == 7 else [])
    for y, r in layers:
        for dx in range(-r, r + 1):
            for dz in range(-r, r + 1):
                if abs(dx) + abs(dz) <= r + (r > 1) and not (r == 2 and abs(dx) == 2 and abs(dz) == 2):
                    vox[(x + dx, y, z + dz)] = 'spruce_leaves[persistent=true]'
    top = Y + ht
    vox[(x, top, z)] = 'spruce_leaves[persistent=true]'
    colmax = {}
    for (vx, vy, vz) in vox:
        colmax[(vx, vz)] = max(colmax.get((vx, vz), 0), vy)
    B.append(f'fill {x} {Y + 1} {z} {x} {top - 1} {z} minecraft:spruce_log')
    for (vx, vy, vz), blk in sorted(vox.items(), key=lambda kv: kv[0][1]):
        if (vx, vz) != (x, z) or vy == top:
            B.append(f'setblock {vx} {vy} {vz} minecraft:{blk}')
    for (vx, vz), vy in colmax.items():
        B.append(f'setblock {vx} {vy + 1} {vz} minecraft:snow')

# Fanions sur mâts dans la boucle, le long de la ligne droite
B.append('# Fanions')
flags = []
for x in range(int(SX0) + 4, int(SX1) - 2, 8):
    for z in range(ZC - 7, ZC - 14, -1):
        if infield[x - X0, z - Z0] and dist[x - X0, z - Z0] >= HW + 2:
            if all(math.hypot(x - (a + X0), z - (b + Z0)) >= 4 for a, b in trees):
                flags.append((x, z))
            break
for n, (x, z) in enumerate(flags):
    col = ('red', 'light_blue', 'white')[n % 3]
    B.append(f'fill {x} {Y + 1} {z} {x} {Y + 3} {z} minecraft:spruce_fence')
    B.append(f'setblock {x} {Y + 4} {z} minecraft:{col}_banner[rotation=0]')
B.append('# Portillon fermé')
B.append('function mg:icerace/gate_on')
write('build', B)

# Portillon : toute la largeur de la colonne GATE
zg = [z for z in range(Z0, Z1 + 1) if track[GATE - X0, z - Z0] and abs(z - ZC) < 8]
write('gate_on', ['# Portillon de départ (verre rouge) — généré par tools/icerace/gen_circuit.py',
                  f'fill {GATE} {Y + 1} {min(zg)} {GATE} {Y + 3} {max(zg)} minecraft:red_stained_glass'])
write('gate_off', ['# GO : ouvre le portillon — généré par tools/icerace/gen_circuit.py',
                   f'fill {GATE} {Y + 1} {min(zg)} {GATE} {Y + 3} {max(zg)} minecraft:air'])

C = ['# Détection des points de passage (appelé chaque tick, @s = chaque joueur via execute as)',
     '# Généré par tools/icerace/gen_circuit.py']
for k, i in enumerate(CP):
    C.append(f'execute if score @s mg.cp matches {k} positioned {f1(pos[i, 0])} 81 {f1(pos[i, 1])} '
             f'if entity @s[distance=..{RCP}] run function mg:icerace/cp_hit')
write('cp_check', C)

g2 = GRID[4]
R = ['# Secours : joueur tombé hors piste → dernier point de passage (@s = joueur)',
     '# Généré par tools/icerace/gen_circuit.py',
     f'execute if score @s mg.cp matches 0 run tp @s {f1(g2[0])} 81 {f1(g2[1])} {GYAW} 0']
for k, i in enumerate(CP):
    R.append(f'execute if score @s mg.cp matches {k + 1} run tp @s {f1(pos[i, 0])} 81 {f1(pos[i, 1])} {yaw(i)} 0')
write('rescue', R)

PL = ['# Course de glace — place le joueur (@s) sur la grille et le met dans un bateau',
      '# Généré par tools/icerace/gen_circuit.py',
      'scoreboard players add $ri mg.st 1',
      'scoreboard players operation @s mg.ri = $ri mg.st']
for n, (x, z) in enumerate(GRID, 1):
    m = f'{n}..' if n == 24 else str(n)
    PL.append(f'execute if score $ri mg.st matches {m} run tp @s {f1(x)} 81 {f1(z)} {GYAW} 0')
PL += [f'execute at @s run summon minecraft:birch_boat ~ ~ ~ {{Invulnerable:1b,Rotation:[{GYAW}f,0.0f],Tags:["mg.ib","mg.mine"]}}',
       'scoreboard players operation @e[tag=mg.mine,limit=1] mg.ri = @s mg.ri',
       'ride @s mount @e[tag=mg.mine,limit=1]',
       'tag @e[tag=mg.ib] remove mg.mine']
write('place_one', PL)

# prepare : perchoir au-dessus du centre de la boucle, spawnpoint sur la grille
ic = np.argwhere(infield).mean(0)
PX, PZ = int(round(ic[0] + X0)), int(round(ic[1] + Z0))
pp = os.path.join(FN, 'prepare.mcfunction')
src = open(pp, encoding='utf-8').read()
src = re.sub(r'scoreboard players set \$px mg\.st -?\d+', f'scoreboard players set $px mg.st {PX}', src)
src = re.sub(r'scoreboard players set \$py mg\.st -?\d+', 'scoreboard players set $py mg.st 100', src)
src = re.sub(r'scoreboard players set \$pz mg\.st -?\d+', f'scoreboard players set $pz mg.st {PZ}', src)
src = re.sub(r'spawnpoint @s -?\d+ \d+ -?\d+', f'spawnpoint @s {GATE - 3} 81 {ZC}', src)
open(pp, 'w', encoding='utf-8').write(src)

# ------------------------------------------------------------------ aperçu
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
img = np.ones(track.shape + (3,))
img[infield] = (0.93, 0.95, 0.97)
img[track] = (0.62, 0.78, 0.95)
img[snow] = (0.98, 0.98, 1.0)
img[wall] = (0.15, 0.45, 0.75)
fig, ax = plt.subplots(figsize=(12, 9.5))
ax.imshow(img.transpose(1, 0, 2), origin='upper', extent=(X0, X1 + 1, Z1 + 1, Z0), interpolation='nearest')
ax.plot(np.append(pos[:, 0], pos[0, 0]), np.append(pos[:, 1], pos[0, 1]), color='#c03', lw=0.8, ls='--')
for x, z in lant:
    ax.add_patch(plt.Rectangle((x, z), 1, 1, color='#fc0'))
for x, z in GRID:
    ax.plot(x, z, 's', color='#7a4', ms=5)
ax.plot([GATE + 0.5, GATE + 0.5], [min(zg), max(zg) + 1], color='red', lw=3)
for x in (LINE, LINE + 1):
    for z in range(ZA, ZB + 1):
        ax.add_patch(plt.Rectangle((x, z), 1, 1, color='k' if (x + z) % 2 else '#ddd'))
for cx, cz in trees:
    ax.add_patch(plt.Circle((cx + X0 + 0.5, cz + Z0 + 0.5), 2.5, color='#285'))
for x, z in flags:
    ax.plot(x + 0.5, z + 0.5, '^', color='#a33')
for k, i in enumerate(CP):
    ax.add_patch(plt.Circle((pos[i, 0], pos[i, 1]), RCP, fill=False, color='#e60', lw=1))
    ax.text(pos[i, 0], pos[i, 1], str(k + 1), ha='center', va='center', fontsize=11, weight='bold', color='#e60')
ax.annotate('', xy=(LINE + 12, ZC), xytext=(LINE + 4, ZC), arrowprops=dict(arrowstyle='->', lw=2))
ax.plot(PX, PZ, 'x', color='purple', ms=10)
ax.set_xlim(X0, X1 + 1); ax.set_ylim(Z1 + 1, Z0)
ax.set_aspect('equal'); ax.grid(alpha=0.25)
ax.set_title(f'Course sur glace — {LENGTH:.0f} blocs, largeur {2 * HW:.0f}, rayon mini {RMIN:.1f} (nord en haut)')
fig.tight_layout()
fig.savefig(os.path.join(TOOLS, 'apercu.png'), dpi=90)

# ------------------------------------------------------------------ résumé
print(f'Piste {track.sum()} cellules, neige {snow.sum()}, murs {wall.sum()}')
print(f'Ligne droite x {SX0:.1f} .. {SX1:.1f} (z {ZC}), portillon x {GATE}, ligne x {LINE}-{LINE + 1}, z {ZA}..{ZB}')
print(f'Écart mini entre portions éloignées : {gap:.1f}')
for k, i in enumerate(CP):
    print(f'  point {k + 1:2d} : {pos[i, 0]:6.1f} {pos[i, 1]:8.1f}  yaw {yaw(i):6.1f}  s={(S[i] - S_FIN) % LENGTH:5.1f} après la ligne')
print(f'Perchoir {PX} 100 {PZ} ; sapins {len(trees)} ; fanions {len(flags)} ; lanternes {len(lant)} ; commandes build {len(B)}')
print('Contrôles OK')
