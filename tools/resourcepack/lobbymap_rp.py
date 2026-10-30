# ------------------------------------------------------------------ spawn : grande carte du lobby (fond de l'armurerie), vue de dessus, nord en haut
# Exécuté par gen_rp.py (exec, après lobby_rp.py) : utilise sys, os, math, wjson, item_def, png_rgba, new_img, render_text, blit, ACCENT, A, R.
# La carte est rendue depuis les fonctions de construction du spawn (data/mg/function, via tools/lobby/theme_world.py) : gen_lobby, gen_hall,
# gen_pvpcave, gen_foot, gen_gta, gen_terranova et gen_ombrelune passent donc AVANT gen_rp (cf. README, « Ordre des générateurs »).
# Fenêtre x, z de -78 à 77 à 4 px par bloc (624 x 624 = 16 x 39 : mipmaps intacts), nord (z négatif) en haut, est (x positif) à droite.
LM_X0 = LM_Z0 = -78
LM_S = 4
LM_SIZE = 624
LM_C = LM_SIZE // 2                           # centre du disque (px) : correspond au point (0, 0) du monde
# blocs jamais « le plus haut » d'une colonne ; s'y ajoutent les plantes de theme_world (fleurs, herbe, fougères : sinon le sol est moucheté)
LM_IGNORE = {'minecraft:light', 'minecraft:barrier', 'minecraft:structure_void', 'minecraft:vine', 'minecraft:glow_lichen', 'minecraft:lily_pad'}
LM_VOID = (24, 32, 56)
LM_DYES = {'white': (249, 255, 254), 'orange': (249, 128, 29), 'magenta': (199, 78, 189), 'light_blue': (58, 179, 218),
           'yellow': (254, 216, 61), 'lime': (128, 199, 31), 'pink': (243, 139, 170), 'gray': (71, 79, 82), 'light_gray': (157, 157, 151),
           'cyan': (22, 156, 156), 'purple': (137, 50, 184), 'blue': (60, 68, 170), 'brown': (131, 84, 50), 'green': (94, 124, 22),
           'red': (176, 46, 38), 'black': (29, 29, 33)}
LM_WOOD = ('oak', 'spruce', 'birch', 'jungle', 'acacia', 'mangrove', 'cherry', 'bamboo', 'planks', '_log', '_wood')
# (sous-chaînes du nom du bloc, couleur) : la première règle qui correspond l'emporte (les teintes et les herbes sont traitées à part)
LM_RULES = [(('water',), (64, 118, 210)), (('glass',), (170, 210, 230)), (('dark_oak',), (80, 55, 35)), (LM_WOOD, (140, 105, 65)),
            (('dirt', 'path', 'mud', 'podzol', 'farmland'), (170, 140, 95)), (('sand',), (220, 205, 150)),
            (('deepslate', 'blackstone'), (70, 70, 80)), (('gold',), (240, 200, 60)), (('lantern',), (250, 240, 190)),
            (('quartz', 'calcite', 'diorite'), (230, 228, 220)), (('stone', 'cobble', 'andesite'), (150, 150, 150)),
            (('red_mushroom_block', 'red_banner'), (196, 46, 46)), (('brown_mushroom_block',), (150, 112, 80)), (('mushroom_stem',), (222, 216, 200)),
            (('crying_obsidian',), (70, 32, 110)), (('obsidian',), (26, 18, 44)), (('purpur',), (168, 120, 170)), (('amethyst',), (150, 100, 220)),
            (('end_rod',), (240, 240, 228)), (('target',), (228, 228, 222)), (('hay_block',), (214, 182, 62)), (('flowering_azalea',), (110, 160, 80)),
            (('emerald_block',), (60, 196, 110)), (('iron_block',), (214, 214, 214)), (('coal_block',), (34, 34, 38)), (('copper',), (196, 120, 80))]

def lm_color(b):
    n = b.split(':')[-1]
    if n == 'cherry_leaves': return (236, 170, 200)
    if n.endswith('_leaves'): return (56, 118, 48)
    if 'grass' in n or 'fern' in n or n in ('moss_block', 'moss_carpet'): return (96, 156, 70)
    if any(k in n for k in ('concrete', 'wool', 'terracotta', 'carpet')):
        return next((c for d, c in LM_DYES.items() if n.startswith(d + '_')), (152, 94, 67))
    for keys, c in LM_RULES:
        if any(k in n for k in keys): return c
    return (180, 170, 160)

def lm_tops():
    """(x, z) -> (y, id du bloc) du bloc le plus haut de chaque colonne de la fenêtre, d'après le modèle du spawn (theme_world)."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lobby'))
    import theme_world as TW
    F_ = os.path.join(R, 'data', 'mg', 'function')
    TW.load(F_)
    # load() range ces constructions parmi les zones modifiées ailleurs (DYN) : on les rejoue pour que leurs blocs figurent dans W
    for rel in ('hall/build', 'hub/build', 'pvpc/build', 'foot/build', 'elytra/build'):
        p = os.path.join(F_, *rel.split('/')) + '.mcfunction'
        assert os.path.isfile(p), ('fonction de construction absente (relancer son générateur)', p)
        for l in open(p, encoding='utf-8'):
            m = TW.CMD.match(l.strip())
            # elytra/build : les anneaux (y 150-176) masqueraient le lobby vu de dessus, on ne garde que les socles (y < 100)
            if rel == 'elytra/build' and m and max(int(m[3]), int(m[6] or m[3])) >= 100: continue
            TW.apply(l, False)
    tops = {}
    for (x, y, z), b in TW.W.items():
        k = TW.bid(b)
        if k in LM_IGNORE or k in TW.PLANTS or not (LM_X0 <= x < LM_X0 + LM_SIZE // LM_S and LM_Z0 <= z < LM_Z0 + LM_SIZE // LM_S): continue
        if (x, z) not in tops or y > tops[(x, z)][0]: tops[(x, z)] = (y, k)
    return tops

def lm_shaded(tops):
    """(x, z) -> couleur ombrée façon carte vanilla : plus haut que la colonne nord = plus clair, plus bas = plus sombre, puis la hauteur."""
    out = {}
    for (x, z), (y, k) in tops.items():
        ny = tops.get((x, z - 1), (y,))[0]
        f = (1.12 if y > ny else 0.82 if y < ny else 1.0) * (0.85 + 0.3 * max(0.0, min(1.0, (y - 63) / 25)))
        out[(x, z)] = tuple(min(255, int(c * f)) for c in lm_color(k))
    return out

def lm_px(x, z): return int((x - LM_X0) * LM_S), int((z - LM_Z0) * LM_S)

def lm_ring(img, cx, cy, r, col):
    """Disque plein de rayon r (px) centré sur (cx, cy)."""
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if math.hypot(x + 0.5 - cx, y + 0.5 - cy) <= r: img[y][x] = col + (255,)

def lm_render():
    tops = lm_tops()
    cols = lm_shaded(tops)
    img = new_img(LM_SIZE, LM_SIZE)
    for py in range(LM_SIZE):
        for px in range(LM_SIZE):
            d = math.hypot(px + 0.5 - LM_C, py + 0.5 - LM_C)
            if d < 302: img[py][px] = cols.get((LM_X0 + px // LM_S, LM_Z0 + py // LM_S), LM_VOID) + (255,)
            elif d < 304: img[py][px] = (214, 170, 60, 255)                # liseré or
            elif d < LM_C: img[py][px] = (62, 40, 22, 255)                 # bordure en chêne noir
    # contours de 2 px : Armurerie (or), Stand de tir (rouge), Hall des scores (cyan)
    for (x1, x2, z1, z2), col in (((-57, -35, -11, 11), (240, 200, 60)), ((-57, -37, -34, -16), (230, 60, 50)), ((-60, -12, 19, 31), (60, 220, 230))):
        (ax, ay), (bx, by) = lm_px(x1, z1), lm_px(x2 + 1, z2 + 1)
        for py in range(ay, by):
            for px in range(ax, bx):
                if (px < ax + 2 or px >= bx - 2 or py < ay + 2 or py >= by - 2) and math.hypot(px + 0.5 - LM_C, py + 0.5 - LM_C) < 302:
                    img[py][px] = col + (255,)
    marks = []                                                              # (nom, x0, y0, x1, y1) : tout ce qui est posé sur la carte
    for name, (x, z), r, col, edge in (('vous', (-55, 0), 7, (226, 40, 40), (255, 255, 255)), ('centre', (0, 0), 5, (255, 200, 50), (70, 45, 10))):
        cx, cy = lm_px(x, z)
        lm_ring(img, cx, cy, r, edge)
        lm_ring(img, cx, cy, r - 1, col)
        marks.append((name, cx - r, cy - r, cx + r + 1, cy + r + 1))
    for txt, (x, z) in (('ARMURERIE', (-46, -5)), ('VOUS ÊTES ICI', (-46, 6)), ('STAND DE TIR', (-47, -25)), ('HALL DES SCORES', (-36, 25)),
                        ('PLOTS', (0, -54)), ('KART', (0, 58)), ('PARKOUR', (58, 0)), ('TERRA NOVA', (-9, -19)), ('NEO GTA', (9, -12)),
                        ('OMBRELUNE', (-9, -29)), ('FOOT', (-6, -39)), ('ÉLYTRES', (24, -4)), ('PVP', (13, 17)), ('ÉTANG', (32, -36))):
        t = render_text(txt, 2, (255, 255, 255), (225, 225, 235), (20, 20, 24), ol=1, shadow=(0, 0, 0, 120), sh=1)
        cx, cy = lm_px(x, z)
        top = 0 if any(c in ACCENT for c in txt) else 4        # sans accent, les 2 rangées d'accent (4 px) sont vides : on centre la hauteur utile
        ox, oy = cx - len(t[0]) // 2, cy - top - (len(t) - top) // 2
        blit(img, t, ox, oy)
        marks.append((txt, ox, oy, ox + len(t[0]), oy + len(t)))
    n = render_text('N', 3, (255, 255, 255), (225, 225, 235), (20, 20, 24), ol=1, shadow=(0, 0, 0, 120), sh=1)   # nord, en haut
    nx = LM_C - len(n[0]) // 2
    marks.append(('N', nx, 14, nx + len(n[0]), 14 + len(n)))
    for i, a in enumerate(marks):
        assert all(math.hypot(x - LM_C, y - LM_C) <= 300 for x in (a[1], a[3]) for y in (a[2], a[4])), ('hors du disque', a)
        for b in marks[:i]:
            assert a[3] <= b[1] or b[3] <= a[1] or a[4] <= b[2] or b[4] <= a[2], ('repères superposés', a, b)
    blit(img, n, nx, 14)
    return img

lm = lm_render()
png_rgba(os.path.join(A, 'textures', 'item', 'lobby_map.png'), lm)
# disque plat dans le plan z = 8 (16 unités = 1 bloc) ; les deux faces ont la même texture : le texte se lit à l'endroit des deux côtés,
# quel que soit le sens dans lequel item_display retourne le modèle (le culling cache la face côté mur)
wjson(os.path.join(A, 'models', 'item', 'lobby_map.json'), {
    "textures": {"m": "mg:item/lobby_map", "particle": "mg:item/lobby_map"},
    "elements": [{"from": [0, 0, 8], "to": [16, 16, 8], "shade": False,
                  "faces": {"north": {"uv": [0, 0, 16, 16], "texture": "#m"}, "south": {"uv": [0, 0, 16, 16], "texture": "#m"}}}]})
item_def('lobby_map', 'mg:item/lobby_map')
print('spawn : carte du lobby', len(lm[0]), 'x', len(lm))
