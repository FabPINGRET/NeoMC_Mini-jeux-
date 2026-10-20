# Bombardier, la ville : gratte-ciel, villa, lieux, commerces, toits (skyline) : exécuté par gen_bomber.py (exec), à sa place dans l'ordre d'origine.
# Utilise : LOTX, LOTZ, PARK, YT, fill, in_park, put, random.

# ---------------------------------------------------------------- bâtiments
STYLES = {
    'glass':  dict(wall=['light_blue_stained_glass', 'cyan_stained_glass', 'gray_stained_glass', 'blue_stained_glass'],
                   frame=['white_concrete', 'light_gray_concrete', 'gray_concrete', 'iron_block'], step=4),
    'brick':  dict(wall=['bricks', 'red_terracotta', 'brown_terracotta', 'terracotta', 'granite'],
                   frame=['black_stained_glass', 'gray_stained_glass'], step=2),
    'deco':   dict(wall=['white_terracotta', 'light_gray_terracotta', 'polished_diorite', 'calcite', 'smooth_sandstone'],
                   frame=['gray_stained_glass', 'black_stained_glass', 'light_gray_stained_glass'], step=3),
    'dark':   dict(wall=['black_concrete', 'gray_concrete', 'polished_deepslate'],
                   frame=['light_blue_stained_glass', 'cyan_stained_glass', 'orange_stained_glass'], step=2),
}
ROOFTOP = []                                       # (x1, z1, x2, z2, top, style) pour les décors de toit


def tower(x1, z1, x2, z2, yb, h, style, wall=None, frame=None, slab=None, roof=True):
    """Bâtiment creux : 4 façades, intérieur vidé, fenêtres en colonnes, planchers tous les 4 blocs."""
    s = STYLES[style]
    wall = wall or random.choice(s['wall'])
    frame = frame or random.choice(s['frame'])
    yt = yb + h - 1
    if style == 'glass':
        glass, solid = wall, frame
    else:
        glass, solid = frame, wall
    fill(x1, yb, z1, x2, yt, z1, solid); fill(x1, yb, z2, x2, yt, z2, solid)
    fill(x1, yb, z1, x1, yt, z2, solid); fill(x2, yb, z1, x2, yt, z2, solid)
    if x2 - x1 >= 2 and z2 - z1 >= 2:
        fill(x1 + 1, yb, z1 + 1, x2 - 1, yt, z2 - 1, 'air')
    # fenêtres (colonnes) : verre continu pour les tours vitrées (montants tous les 4), alternance sinon
    st = s['step']
    w0, w1 = yb + 1, yt - 1
    if w1 > w0:
        for x in range(x1 + 1, x2):
            on = ((x - x1) % st != 0) if style == 'glass' else ((x - x1) % st == 1 or (st == 3 and (x - x1) % 3 == 2))
            if on:
                fill(x, w0, z1, x, w1, z1, glass); fill(x, w0, z2, x, w1, z2, glass)
        for z in range(z1 + 1, z2):
            on = ((z - z1) % st != 0) if style == 'glass' else ((z - z1) % st == 1 or (st == 3 and (z - z1) % 3 == 2))
            if on:
                fill(x1, w0, z, x1, w1, z, glass); fill(x2, w0, z, x2, w1, z, glass)
    # planchers (bandeaux en façade)
    sl = slab or solid
    for y in range(yb + 4, yt, 4):
        fill(x1, y, z1, x2, y, z2, sl)
    fill(x1, yb, z1, x2, yb, z2, sl)
    fill(x1, yt, z1, x2, yt, z2, solid if style != 'glass' else frame)
    if style != 'glass':                          # rez-de-chaussée : vitrines
        for x in range(x1 + 2, x2 - 1, 3):
            fill(x, yb + 1, z1, x + 1, yb + 2, z1, 'glass'); fill(x, yb + 1, z2, x + 1, yb + 2, z2, 'glass')
    if roof:
        ROOFTOP.append((x1, z1, x2, z2, yt, style))
    return yt


def setbacks(x1, z1, x2, z2, yb, h, style, tiers=3):
    """Tour à gradins (art déco) : chaque étage en retrait de 2 blocs."""
    wall = random.choice(STYLES[style]['wall']); frame = random.choice(STYLES[style]['frame'])
    y = yb
    parts = [0.55, 0.3, 0.15][:tiers]
    for i, f in enumerate(parts):
        hh = max(4, int(h * f) // 4 * 4 + 1)
        last = i == len(parts) - 1 or (x2 - x1) < 8 or (z2 - z1) < 8
        top = tower(x1, z1, x2, z2, y, hh, style, wall, frame, roof=last)
        if last:
            return top
        y = top
        x1, z1, x2, z2 = x1 + 2, z1 + 2, x2 - 2, z2 - 2
    return y


def height_for(cx, cz):
    if cx >= 56 or cx <= -80:
        return random.randint(10, 26), 'brick'
    if cz >= 21:                                   # Upper : brownstones et immeubles moyens
        return random.choice([(random.randint(10, 22), 'brick'), (random.randint(18, 34), 'deco')])
    if cz <= -57:                                  # Downtown : grandes tours de verre
        return random.choice([(random.randint(40, 84), 'glass'), (random.randint(30, 60), 'dark'), (random.randint(20, 40), 'deco')])
    return random.choice([(random.randint(28, 72), 'glass'), (random.randint(24, 56), 'deco'),
                          (random.randint(14, 30), 'brick'), (random.randint(26, 52), 'dark')])


LANDMARK_LOTS = {}


def split(a, b, minw):
    n = b - a + 1
    if n < 2 * minw + 1 or random.random() < 0.3:
        return [(a, b)]
    k = random.randint(minw, n - minw - 1)
    return [(a, a + k - 1)] + split(a + k + 1, b, minw)


def empire(x1, z1, x2, z2):
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    W, F = 'smooth_sandstone', 'gray_stained_glass'
    t = tower(x1, z1, x2, z2, 65, 13, 'deco', W, F, roof=False)
    t = tower(cx - 7, cz - 5, cx + 7, cz + 5, t, 49, 'deco', W, F, roof=False)
    t = tower(cx - 5, cz - 4, cx + 5, cz + 4, t, 17, 'deco', W, F, roof=False)
    t = tower(cx - 3, cz - 3, cx + 3, cz + 3, t, 9, 'deco', W, F, roof=False)
    fill(cx - 3, t, cz - 3, cx + 3, t, cz + 3, 'gold_block')
    t = tower(cx - 2, cz - 2, cx + 2, cz + 2, t + 1, 6, 'deco', W, 'light_blue_stained_glass', roof=False)
    fill(cx - 1, t + 1, cz - 1, cx + 1, t + 4, cz + 1, 'gold_block')
    fill(cx, t + 5, cz, cx, t + 14, cz, 'lightning_rod')


def chrysler(x1, z1, x2, z2):
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    W, F = 'white_terracotta', 'black_stained_glass'
    t = tower(x1, z1, x2, z2, 65, 17, 'deco', W, F, roof=False)
    t = tower(cx - 5, cz - 5, cx + 5, cz + 5, t, 45, 'deco', W, F, roof=False)
    for i, r in enumerate([4, 3, 2, 1]):           # couronne en écailles d'acier
        fill(cx - r, t + 1, cz - r, cx + r, t + 4, cz + r, 'iron_block')
        for d in range(-r + 1, r, 2):
            fill(cx + d, t + 2, cz - r, cx + d, t + 3, cz - r, 'black_stained_glass')
            fill(cx + d, t + 2, cz + r, cx + d, t + 3, cz + r, 'black_stained_glass')
            fill(cx - r, t + 2, cz + d, cx - r, t + 3, cz + d, 'black_stained_glass')
            fill(cx + r, t + 2, cz + d, cx + r, t + 3, cz + d, 'black_stained_glass')
        t += 4
    fill(cx, t + 1, cz, cx, t + 2, cz, 'gold_block')
    fill(cx, t + 3, cz, cx, t + 13, cz, 'lightning_rod')


def needle(x1, z1, x2, z2):
    t = tower(x1, z1, x2, z2, 65, 85, 'glass', 'cyan_stained_glass', 'light_gray_concrete', roof=False)
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    t = tower(cx - 2, cz - 2, cx + 2, cz + 2, t, 5, 'glass', 'light_blue_stained_glass', 'iron_block', roof=False)
    fill(cx, t + 1, cz, cx, t + 9, cz, 'lightning_rod')


SHOP_CAND = []                                   # bâtiments dont la façade nord donne sur une rue : commerces de Neo GTA
VILLA = (26, 47, 46, 61)                         # villa partagée de Neo GTA (îlot en face du parc, côté est)


def villa(x1, z1, x2, z2):
    """Villa : garage à 5 places (façade nord sur la rue), maison sur deux niveaux, toit avec piscine et hélistation."""
    fill(x1, 64, z1, x2, 64, z2, 'moss_block')                                   # pelouse
    # garage (z1 .. z1 + 5) : béton gris, grande porte ouverte sur la rue, sol lisse
    gz2 = z1 + 5
    fill(x1, 65, z1, x2, 65, gz2, 'smooth_quartz')
    fill(x1, 66, z1, x2, 69, z1, 'light_gray_concrete'); fill(x1, 66, gz2, x2, 69, gz2, 'light_gray_concrete')
    fill(x1, 66, z1, x1, 69, gz2, 'light_gray_concrete'); fill(x2, 66, z1, x2, 69, gz2, 'light_gray_concrete')
    fill(x1 + 1, 66, z1 + 1, x2 - 1, 68, gz2 - 1, 'air')
    fill(x1, 69, z1, x2, 69, gz2, 'gray_concrete')
    fill(x1 + 2, 66, z1, x2 - 2, 68, z1, 'air')                                  # porte du garage
    fill(x1 + 1, 69, z1, x2 - 1, 69, z1, 'black_concrete')
    for x in range(x1 + 3, x2 - 1, 3):
        put(x, 66, gz2 - 1, 'yellow_carpet')                                      # places de parking
        put(x, 68, gz2 - 1, 'sea_lantern')
    # maison (gz2 + 1 .. z2) : deux niveaux blancs et vitrés, toit-terrasse
    hz1 = gz2 + 1
    fill(x1, 65, hz1, x2, 65, z2, 'polished_diorite')
    for (ya, yb) in ((66, 69), (70, 74)):
        fill(x1, ya, hz1, x2, yb, hz1, 'white_concrete'); fill(x1, ya, z2, x2, yb, z2, 'white_concrete')
        fill(x1, ya, hz1, x1, yb, z2, 'white_concrete'); fill(x2, ya, hz1, x2, yb, z2, 'white_concrete')
        fill(x1 + 1, ya, hz1 + 1, x2 - 1, yb, z2 - 1, 'air')
        fill(x1 + 1, ya + 1, z2, x2 - 1, yb - 1, z2, 'light_blue_stained_glass')   # baies vitrées côté sud
        fill(x1, ya + 1, hz1 + 1, x1, yb - 1, z2 - 1, 'light_blue_stained_glass')
        fill(x2, ya + 1, hz1 + 1, x2, yb - 1, z2 - 1, 'light_blue_stained_glass')
    fill(x1, 69, hz1, x2, 69, z2, 'smooth_quartz')                               # plancher de l'étage
    fill(x1 + 1, 69, hz1 + 1, x1 + 2, 69, hz1 + 2, 'air')                        # trémie de l'escalier
    for k in range(4):
        put(x1 + 1, 65 + k, hz1 + 4 - k, 'quartz_stairs[facing=north]')
    fill(x1, 75, hz1, x2, 75, z2, 'smooth_quartz')                               # toit
    fill(x1, 76, hz1, x2, 76, hz1, 'white_concrete'); fill(x1, 76, z2, x2, 76, z2, 'white_concrete')
    fill(x1, 76, hz1, x1, 76, z2, 'white_concrete'); fill(x2, 76, hz1, x2, 76, z2, 'white_concrete')
    fill(x1 + 1, 75, hz1 + 1, x1 + 8, 75, z2 - 1, 'light_blue_stained_glass')    # piscine (toit)
    fill(x1 + 1, 74, hz1 + 1, x1 + 8, 74, z2 - 1, 'light_blue_concrete')
    fill(x1 + 11, 76, hz1 + 1, x2 - 1, 76, z2 - 1, 'gray_carpet')                # hélistation
    hx, hzc = (x1 + 11 + x2 - 1) // 2, (hz1 + z2) // 2
    fill(hx - 1, 76, hzc - 1, hx - 1, 76, hzc + 1, 'yellow_carpet'); fill(hx + 1, 76, hzc - 1, hx + 1, 76, hzc + 1, 'yellow_carpet')
    put(hx, 76, hzc, 'yellow_carpet')
    # rez-de-chaussée : salon (canapé, télé), râtelier d'armes au fond, porte côté avenue
    fill(x1, 66, hz1 + 3, x1, 68, hz1 + 4, 'air')
    fill(x1 + 4, 66, hz1 + 2, x1 + 8, 66, hz1 + 2, 'white_wool')
    fill(x1 + 4, 67, hz1 + 1, x1 + 8, 67, hz1 + 1, 'white_wool')
    fill(x1 + 5, 66, hz1 + 5, x1 + 7, 67, hz1 + 5, 'black_concrete'); put(x1 + 6, 67, hz1 + 5, 'sea_lantern')
    fill(x1 + 1, 66, z2 - 1, x2 - 1, 66, z2 - 1, 'red_carpet')
    for x in range(x1 + 2, x2 - 1, 3):
        fill(x, 67, z2 - 1, x, 68, z2 - 1, 'iron_bars')
    for x in range(x1 + 3, x2 - 1, 5):
        put(x, 68, hz1 + 3, 'sea_lantern'); put(x, 74, hz1 + 3, 'sea_lantern')
    # étage : chambre (lit en laine, tapis)
    fill(x2 - 6, 70, hz1 + 2, x2 - 4, 70, hz1 + 4, 'red_wool'); fill(x2 - 6, 70, hz1 + 2, x2 - 4, 70, hz1 + 2, 'white_wool')
    fill(x1 + 6, 70, hz1 + 2, x1 + 12, 70, hz1 + 5, 'light_gray_carpet')
    # ascenseur vers le toit (ses plaques sont posées par Neo GTA) : gaine vitrée
    fill(x2 - 1, 66, hz1 + 1, x2 - 1, 68, hz1 + 1, 'glass')


PLACES = {}                                      # lieux de Neo GTA bâtis dans la ville (exportés dans neo_city.json)


def shell(x1, z1, x2, z2, h, wall, floor, glass, roof=None):
    """Bâtiment sur h niveaux de 4 blocs, porte de 3 blocs au milieu de la façade nord (z1, côté rue), bandeaux de fenêtres."""
    yt = 65 + 4 * h
    fill(x1, 65, z1, x2, 65, z2, floor)
    fill(x1, 66, z1, x2, yt, z1, wall); fill(x1, 66, z2, x2, yt, z2, wall)
    fill(x1, 66, z1, x1, yt, z2, wall); fill(x2, 66, z1, x2, yt, z2, wall)
    fill(x1 + 1, 66, z1 + 1, x2 - 1, yt - 1, z2 - 1, 'air')
    for k in range(1, h):
        fill(x1, 65 + 4 * k, z1, x2, 65 + 4 * k, z2, floor)
    fill(x1, yt, z1, x2, yt, z2, roof or wall)
    for k in range(h):
        y = 67 + 4 * k
        fill(x1 + 1, y, z1, x2 - 1, y + 1, z1, glass); fill(x1 + 1, y, z2, x2 - 1, y + 1, z2, glass)
        fill(x1, y, z1 + 1, x1, y + 1, z2 - 1, glass); fill(x2, y, z1 + 1, x2, y + 1, z2 - 1, glass)
    mx = (x1 + x2) // 2
    fill(mx - 1, 66, z1, mx + 1, 68, z1, 'air')
    return mx, yt


def hospital(x1, z1, x2, z2):
    mx, yt = shell(x1, z1, x2, z2, 3, 'white_concrete', 'smooth_quartz', 'light_blue_stained_glass')
    fill(mx - 3, 69, z1 - 1, mx + 3, 69, z1 - 1, 'white_concrete')               # auvent
    fill(mx - 1, 70, z1, mx + 1, 74, z1, 'red_concrete'); fill(mx - 2, 71, z1, mx + 2, 73, z1, 'red_concrete')
    fill(mx, 70, z1, mx, 74, z1, 'red_concrete'); fill(mx - 2, 72, z1, mx + 2, 72, z1, 'red_concrete')
    fill(x1 + 2, 66, z1 + 3, x1 + 6, 66, z1 + 3, 'smooth_quartz'); fill(x1 + 2, 67, z1 + 3, x1 + 6, 67, z1 + 3, 'smooth_quartz_slab')   # accueil
    for x in range(x1 + 2, x2 - 1, 3):                                            # chambres : lits
        fill(x, 66, z2 - 3, x, 66, z2 - 2, 'white_wool'); put(x, 66, z2 - 1, 'red_wool')
        fill(x, 70, z2 - 3, x, 70, z2 - 2, 'white_wool'); put(x, 70, z2 - 1, 'red_wool')
    for x in range(x1 + 3, x2 - 1, 4):
        put(x, 68, (z1 + z2) // 2, 'sea_lantern'); put(x, 72, (z1 + z2) // 2, 'sea_lantern')
    put(x2 - 2, 66, z1 + 2, 'potted_fern'); put(x1 + 8, 66, z1 + 3, 'brewing_stand')
    fill(mx - 2, yt, z1 + 3, mx + 2, yt, z1 + 9, 'red_concrete'); fill(mx - 1, yt, z1 + 4, mx + 1, yt, z1 + 8, 'white_concrete')
    fill(mx - 1, yt, z1 + 5, mx - 1, yt, z1 + 7, 'red_concrete'); fill(mx + 1, yt, z1 + 5, mx + 1, yt, z1 + 7, 'red_concrete'); put(mx, yt, z1 + 6, 'red_concrete')
    PLACES['hospital'] = [mx, z1 + 2]


def police(x1, z1, x2, z2):
    mx, yt = shell(x1, z1, x2, z2, 2, 'light_gray_concrete', 'polished_andesite', 'gray_stained_glass', 'blue_concrete')
    fill(x1, 66, z1, x2, 66, z1, 'blue_concrete'); fill(mx - 1, 66, z1, mx + 1, 68, z1, 'air')
    fill(x1, 69, z1, x2, 69, z1, 'blue_concrete')
    put(mx - 2, 70, z1, 'redstone_lamp[lit=true]'); put(mx + 2, 70, z1, 'sea_lantern')
    fill(x1 + 2, 66, z1 + 3, x1 + 8, 66, z1 + 3, 'dark_oak_planks'); fill(x1 + 2, 67, z1 + 3, x1 + 8, 67, z1 + 3, 'polished_blackstone_slab')   # bureaux
    fill(x2 - 8, 66, z1 + 3, x2 - 2, 66, z1 + 3, 'dark_oak_planks'); fill(x2 - 8, 67, z1 + 3, x2 - 2, 67, z1 + 3, 'polished_blackstone_slab')
    for x in range(x1 + 2, x2 - 3, 4):                                            # cellules
        fill(x, 66, z2 - 4, x + 2, 68, z2 - 4, 'iron_bars'); fill(x + 3, 66, z2 - 4, x + 3, 68, z2 - 1, 'iron_block')
        put(x + 1, 66, z2 - 2, 'white_wool')
    fill(x1 + 1, 66, z1 + 6, x1 + 1, 68, z1 + 10, 'iron_bars')                    # râtelier
    for x in range(x1 + 3, x2 - 1, 4):
        put(x, 68, (z1 + z2) // 2, 'sea_lantern')
    PLACES['police'] = [mx, z1 + 2]


def casino(x1, z1, x2, z2):
    mx, yt = shell(x1, z1, x2, z2, 2, 'black_concrete', 'red_wool', 'yellow_stained_glass', 'black_concrete')
    fill(x1, 65, z1, x2, 65, z2, 'black_concrete'); fill(x1 + 1, 65, z1 + 1, x2 - 1, 65, z2 - 1, 'red_wool')
    fill(x1, 70, z1, x2, 72, z1, 'gold_block')                                   # marquise dorée
    for x in range(x1, x2 + 1, 2):
        put(x, 73, z1, 'glowstone'); put(x, 69, z1, 'sea_lantern')
    fill(mx - 1, 66, z1, mx + 1, 68, z1, 'air')
    slots = []
    for x in range(x1 + 2, x2 - 1, 3):                                            # machines à sous contre le mur sud
        fill(x, 66, z2 - 1, x, 67, z2 - 1, 'gold_block'); put(x, 68, z2 - 1, 'red_stained_glass')
        slots.append([x, z2 - 2])
    rx, rz = mx, (z1 + z2) // 2 + 1                                               # roulette
    fill(rx - 2, 66, rz - 1, rx + 2, 66, rz + 1, 'dark_oak_planks'); fill(rx - 1, 67, rz - 1, rx + 1, 67, rz + 1, 'green_carpet')
    put(rx, 67, rz, 'red_carpet')
    fill(x1 + 1, 66, z1 + 2, x1 + 1, 67, z1 + 6, 'dark_oak_planks')               # bar
    for z in range(z1 + 2, z1 + 7, 2):
        put(x1 + 1, 68, z, 'brewing_stand')
    for x in range(x1 + 3, x2 - 1, 4):
        put(x, 69, (z1 + z2) // 2, 'iron_chain'); put(x, 68, (z1 + z2) // 2, 'lantern[hanging=true]')
    PLACES['casino'] = {'slots': slots[:6], 'roulette': [rx, rz - 2], 'door': [mx, z1]}


def club(x1, z1, x2, z2):
    mx, yt = shell(x1, z1, x2, z2, 2, 'black_concrete', 'black_concrete', 'purple_stained_glass', 'black_concrete')
    fill(x1 + 1, 69, z1 + 1, x2 - 1, 69, z2 - 1, 'air')                            # double hauteur
    fill(x1, 70, z1, x2, 71, z1, 'magenta_concrete')
    for x in range(x1, x2 + 1, 2):
        put(x, 72, z1, 'sea_lantern')
    fx1, fz1, fx2, fz2 = mx - 4, z1 + 4, mx + 4, z1 + 10                          # piste de danse
    fill(fx1, 65, fz1, fx2, 65, fz2, 'white_concrete')
    fill(mx - 2, 66, z2 - 2, mx + 2, 66, z2 - 1, 'black_concrete'); put(mx - 1, 67, z2 - 2, 'note_block'); put(mx + 1, 67, z2 - 2, 'jukebox')   # DJ
    for (x, z) in [(x1 + 1, z2 - 1), (x2 - 1, z2 - 1), (x1 + 1, z1 + 3), (x2 - 1, z1 + 3)]:
        fill(x, 66, z, x, 68, z, 'black_concrete'); put(x, 67, z, 'note_block')    # enceintes
    fill(x2 - 1, 66, z1 + 5, x2 - 1, 67, z1 + 9, 'dark_oak_planks')               # bar
    fill(x1 + 1, 66, z1 + 5, x1 + 1, 66, z1 + 9, 'purple_wool')                   # banquettes VIP
    for x in range(x1 + 3, x2 - 1, 3):
        put(x, 72, (z1 + z2) // 2, 'sea_lantern')
    PLACES['club'] = {'floor': [fx1, fz1, fx2, fz2], 'box': [x1, z1, x2, z2], 'dj': [mx, z2 - 2]}


LANDMARKS = {(-40, -51): empire, (-8, -51): chrysler, (24, -75): needle,
             (-72, -27): hospital, (24, -27): police, (24, -3): casino, (-72, 21): club}
TIMES = (-12, -6)                                  # carrefour à écrans
BILLBOARD = ['red_concrete', 'yellow_concrete', 'lime_concrete', 'magenta_concrete', 'cyan_concrete', 'orange_concrete', 'blue_concrete']

for (lx1, lx2) in LOTX:
    for (lz1, lz2) in LOTZ:
        if in_park(lx1, lz1):
            continue
        bx1, bx2, bz1, bz2 = lx1 + 2, lx2 - 2, lz1 + 2, lz2 - 2
        if bx2 - bx1 < 3 or bz2 - bz1 < 3:
            continue
        if (lx1, lz1) in LANDMARKS:
            fill(bx1, 65, bz1, bx2, YT - 1, bz2, 'air')        # îlot vidé (anciens immeubles plus hauts)
            LANDMARKS[(lx1, lz1)](bx1, bz1, bx2, bz2)
            continue
        for (ax, bx) in split(bx1, bx2, 6):
            for (az, bz) in split(bz1, bz2, 6):
                h, style = height_for((ax + bx) // 2, (az + bz) // 2)
                if style == 'deco' and h > 30 and bx - ax >= 10 and bz - az >= 10:
                    top = setbacks(ax, az, bx, bz, 65, h, 'deco')
                else:
                    top = tower(ax, az, bx, bz, 65, h, style)
                if az == bz1 and bx - ax >= 8 and bz - az >= 7 and h >= 9 and not (PARK[0] - 8 <= ax <= PARK[2] + 8 and PARK[1] - 8 <= az <= PARK[3]):
                    SHOP_CAND.append((ax, az, bx, bz))
                # carrefour à écrans : panneaux colorés sur les façades qui donnent sur le carrefour
                near = abs((ax + bx) / 2 - TIMES[0]) < 30 and abs((az + bz) / 2 - TIMES[1]) < 24
                if near:
                    fx = bx if (ax + bx) / 2 < TIMES[0] else ax
                    fz = bz if (az + bz) / 2 < TIMES[1] else az
                    for k in range(2):
                        c = random.choice(BILLBOARD)
                        y0 = 68 + k * 8
                        if y0 + 6 < top:
                            fill(fx, y0, az + 1, fx, y0 + 5, bz - 1, c)
                            fill(fx, y0 - 1, az + 1, fx, y0 - 1, bz - 1, 'sea_lantern')
                            fill(ax + 1, y0, fz, bx - 1, y0 + 5, fz, random.choice(BILLBOARD))
                            fill(ax + 1, y0 + 6, fz, bx - 1, y0 + 6, fz, 'glowstone')

# commerces (Neo GTA) : porte, auvent, comptoir et caisse au rez-de-chaussée de 6 immeubles bien répartis
SHOP_NAMES = [('🛒 Supérette', 'lime'), ('💎 Bijouterie', 'cyan'), ('⛽ Station', 'orange'), ('🍔 Burger', 'red'), ('💊 Pharmacie', 'white'), ('📱 Téléphones', 'blue')]
_rs = random.Random(42)
SHOPS = []
for c in sorted(SHOP_CAND, key=lambda b: (b[0] + 3 * b[1])):
    if len(SHOPS) < len(SHOP_NAMES) and all(abs(c[0] - o[0]) + abs(c[1] - o[1]) > 45 for o in SHOPS) and _rs.random() < 0.7:
        SHOPS.append(c)
for c in sorted(SHOP_CAND, key=lambda b: (b[0] + 3 * b[1])):          # complément si l'écart de 45 blocs ne suffit pas
    if len(SHOPS) < len(SHOP_NAMES) and c not in SHOPS and all(abs(c[0] - o[0]) + abs(c[1] - o[1]) > 16 for o in SHOPS):
        SHOPS.append(c)
for k, ((sx, sz, ex, ez), (nm, col)) in enumerate(zip(SHOPS, SHOP_NAMES)):
    mx = (sx + ex) // 2
    ix1, ix2, iz2 = sx + 1, ex - 1, ez - 1                                       # intérieur ; caisse en sz + 3 (côté clients), comptoir en sz + 4
    fill(mx - 1, 66, sz, mx + 1, 68, sz, 'air')                                  # porte
    fill(ix1, 66, sz + 1, ix2, 68, iz2, 'air')
    fill(ix1, 65, sz + 1, ix2, 65, iz2, ['smooth_quartz', 'polished_andesite', 'smooth_stone_slab', 'black_concrete', 'white_concrete', 'polished_deepslate'][k])
    fill(mx - 2, 69, sz - 1, mx + 2, 69, sz - 1, f'{col}_wool')                  # auvent
    fill(ix1, 66, sz + 4, ix2, 66, sz + 4, 'dark_oak_planks'); fill(ix1, 67, sz + 4, ix2, 67, sz + 4, 'smooth_quartz_slab')
    fill(mx, 66, sz + 4, mx, 67, sz + 4, 'air')                                  # passage derrière le comptoir (le caissier)
    put(mx + 1, 67, sz + 4, 'lodestone')                                         # caisse enregistreuse
    for x in range(ix1 + 1, ix2, 3):
        put(x, 68, sz + 2, 'sea_lantern')
    back = sz + 5
    if k == 0:      # supérette : rayons de produits, frigos, fruits et légumes
        fill(ix1, 66, back + 1, ix2, 67, iz2, 'barrel')
        fill(ix1, 66, sz + 1, ix1, 67, sz + 3, 'white_concrete'); fill(ix1, 68, sz + 1, ix1, 68, sz + 3, 'glass')
        fill(ix2, 66, sz + 1, ix2, 66, sz + 3, 'hay_block'); put(ix2, 67, sz + 1, 'melon'); put(ix2, 67, sz + 2, 'carved_pumpkin'); put(ix2, 67, sz + 3, 'melon')
        put(mx - 1, 68, sz + 4, 'cake')
    elif k == 1:    # bijouterie : vitrines (verre sur socles noirs), or et pierres précieuses
        for x in (ix1, ix2):
            fill(x, 66, sz + 1, x, 66, sz + 3, 'black_concrete'); fill(x, 67, sz + 1, x, 67, sz + 3, 'glass')
        put(ix1, 66, sz + 2, 'gold_block'); put(ix2, 66, sz + 2, 'diamond_block'); put(ix2, 66, sz + 1, 'emerald_block'); put(ix1, 66, sz + 3, 'amethyst_block')
        fill(ix1, 66, back + 1, ix2, 68, iz2, 'black_concrete'); fill(ix1 + 1, 67, iz2, ix2 - 1, 67, iz2, 'gold_block')
    elif k == 2:    # station-service : pompes sur le trottoir, rayons de bidons
        for x in (mx - 4, mx + 4):
            if sx <= x <= ex:
                fill(x, 65, sz - 2, x, 66, sz - 2, 'red_concrete'); put(x, 67, sz - 2, 'iron_block'); put(x, 68, sz - 2, 'redstone_lamp[lit=true]')
        fill(ix1, 66, sz + 1, ix1, 67, sz + 3, 'barrel'); fill(ix2, 66, sz + 1, ix2, 66, sz + 3, 'cauldron')
        fill(ix1, 66, back + 1, ix2, 67, iz2, 'barrel')
    elif k == 3:    # burger : cuisine derrière le comptoir, tables et tabourets
        fill(ix1, 66, back + 1, ix2, 66, iz2, 'smoker'); fill(ix1, 67, back + 1, ix2, 67, iz2, 'furnace')
        for x in (ix1 + 1, ix2 - 1):
            put(x, 66, sz + 2, 'oak_fence'); put(x, 67, sz + 2, 'smooth_quartz_slab')
            put(x, 66, sz + 1, 'oak_stairs[facing=south]'); put(x, 66, sz + 3, 'oak_stairs[facing=north]')
        fill(mx - 2, 68, sz + 4, mx - 2, 68, sz + 4, 'red_concrete')
    elif k == 4:    # pharmacie : tout blanc, étagères, croix verte en façade
        fill(ix1, 66, sz + 1, ix1, 68, sz + 3, 'white_concrete'); fill(ix2, 66, sz + 1, ix2, 68, sz + 3, 'white_concrete')
        fill(ix1, 67, sz + 1, ix1, 67, sz + 3, 'flower_pot'); fill(ix1, 66, back + 1, ix2, 68, iz2, 'white_concrete')
        put(mx - 1, 68, sz + 4, 'brewing_stand')
        fill(mx, 70, sz, mx, 72, sz, 'lime_concrete'); fill(mx - 1, 71, sz, mx + 1, 71, sz, 'lime_concrete')
    else:           # téléphones : tables d'exposition noires et lumineuses
        for x in (ix1, ix2):
            fill(x, 66, sz + 1, x, 66, sz + 3, 'black_concrete'); fill(x, 67, sz + 1, x, 67, sz + 3, 'black_carpet')
        fill(ix1, 66, back + 1, ix2, 68, iz2, 'gray_concrete'); fill(ix1 + 1, 67, iz2, ix2 - 1, 67, iz2, 'sea_lantern')

# toits : châteaux d'eau, climatiseurs, antennes
for (x1, z1, x2, z2, yt, style) in ROOFTOP:
    w_, d_ = x2 - x1, z2 - z1
    if style in ('brick', 'deco') and w_ >= 6 and d_ >= 6 and random.random() < 0.75:
        tx, tz = random.randint(x1 + 1, x2 - 4), random.randint(z1 + 1, z2 - 4)
        for (lx, lz) in [(tx, tz), (tx + 2, tz), (tx, tz + 2), (tx + 2, tz + 2)]:
            fill(lx, yt + 1, lz, lx, yt + 2, lz, 'stripped_spruce_log')
        fill(tx, yt + 3, tz, tx + 2, yt + 5, tz + 2, 'spruce_planks')
        fill(tx + 1, yt + 3, tz, tx + 1, yt + 5, tz, 'stripped_spruce_wood')
        put(tx + 1, yt + 6, tz + 1, 'spruce_slab')
        fill(tx, yt + 6, tz, tx + 2, yt + 6, tz, 'spruce_slab'); fill(tx, yt + 6, tz + 2, tx + 2, yt + 6, tz + 2, 'spruce_slab')
    elif style in ('glass', 'dark'):
        cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
        if w_ >= 6 and d_ >= 6:
            fill(cx - 2, yt + 1, cz - 2, cx + 1, yt + 3, cz + 1, 'light_gray_concrete')
        put(cx, yt + 4 if w_ >= 6 and d_ >= 6 else yt + 1, cz, 'lightning_rod')
        if yt > 110:
            fill(cx, yt + 5, cz, cx, yt + 8, cz, 'lightning_rod')
    if w_ >= 4 and d_ >= 4 and random.random() < 0.6:
        ax, az = random.randint(x1 + 1, x2 - 2), random.randint(z1 + 1, z2 - 1)
        fill(ax, yt + 1, az, ax + 1, yt + 1, az, 'iron_block')
