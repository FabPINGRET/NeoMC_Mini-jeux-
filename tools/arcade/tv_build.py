"""🏗 Terra Nova : boîte à outils de construction en voxels (structures détaillées des régions).

Une structure est un dictionnaire de voxels (x, y, z) -> bloc, construit avec des primitives (pavés, murs, toits à pignon,
fenêtres, escaliers, mobilier…), puis converti en commandes « fill » (rectangles fusionnés couche par couche).
`render(vox, path)` en fait une image isométrique (contrôle visuel sans client Minecraft).
"""
import math
import random

AIR = 'air'


class Vox:
    def __init__(self, seed=1):
        self.v = {}
        self.r = random.Random(seed)

    # ---------------------------------------------------------------- primitives
    def set(self, x, y, z, b):
        self.v[(x, y, z)] = b

    def get(self, x, y, z):
        return self.v.get((x, y, z))

    def fill(self, x1, y1, z1, x2, y2, z2, b, hollow=False, outline=False, only=None, keep=False):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        z1, z2 = sorted((z1, z2))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    # une couche seule en outline : seulement le contour (sinon tout est « bord »)
                    edge = x in (x1, x2) or z in (z1, z2) or (y in (y1, y2) and not (outline and y1 == y2))
                    if (hollow or outline) and not edge:
                        if hollow:
                            self.v[(x, y, z)] = AIR
                        continue
                    if only is not None and self.v.get((x, y, z)) not in only:
                        continue
                    if keep and (x, y, z) in self.v and self.v[(x, y, z)] != AIR:
                        continue
                    self.v[(x, y, z)] = b(x, y, z) if callable(b) else b

    def clear(self, x1, y1, z1, x2, y2, z2):
        self.fill(x1, y1, z1, x2, y2, z2, AIR)

    def walls(self, x1, z1, x2, z2, y1, y2, b):
        """Quatre murs (sans sol ni plafond)."""
        self.fill(x1, y1, z1, x2, y2, z1, b)
        self.fill(x1, y1, z2, x2, y2, z2, b)
        self.fill(x1, y1, z1, x1, y2, z2, b)
        self.fill(x2, y1, z1, x2, y2, z2, b)

    def pillars(self, x1, z1, x2, z2, y1, y2, b):
        for x, z in ((x1, z1), (x1, z2), (x2, z1), (x2, z2)):
            self.fill(x, y1, z, x, y2, z, b)

    def frame_walls(self, x1, z1, x2, z2, y1, y2, wall, post, beam=None, step=4):
        """Murs à colombages : poteaux aux angles et tous les `step` blocs, poutre en haut."""
        self.walls(x1, z1, x2, z2, y1, y2, wall)
        for x in list(range(x1, x2 + 1, step)) + [x2]:
            self.fill(x, y1, z1, x, y2, z1, post)
            self.fill(x, y1, z2, x, y2, z2, post)
        for z in list(range(z1, z2 + 1, step)) + [z2]:
            self.fill(x1, y1, z, x1, y2, z, post)
            self.fill(x2, y1, z, x2, y2, z, post)
        if beam:
            ax = beam
            self.fill(x1, y2, z1, x2, y2, z1, f'{ax}[axis=x]')
            self.fill(x1, y2, z2, x2, y2, z2, f'{ax}[axis=x]')
            self.fill(x1, y2, z1, x1, y2, z2, f'{ax}[axis=z]')
            self.fill(x2, y2, z1, x2, y2, z2, f'{ax}[axis=z]')

    def windows(self, x1, z1, x2, z2, y, h, glass, every=3, skip=()):
        for x in range(x1 + 2, x2 - 1, every):
            for z in (z1, z2):
                if (x, z) not in skip:
                    self.fill(x, y, z, x, y + h - 1, z, glass)
        for z in range(z1 + 2, z2 - 1, every):
            for x in (x1, x2):
                if (x, z) not in skip:
                    self.fill(x, y, z, x, y + h - 1, z, glass)

    def door(self, x, y, z, facing, mat='spruce', width=1):
        """Porte (2 de haut) ; facing = côté vers lequel on sort (north/south/east/west)."""
        hinge = 'left'
        for i in range(width):
            dx, dz = ((i, 0) if facing in ('north', 'south') else (0, i))
            self.set(x + dx, y, z + dz, f'{mat}_door[facing={facing},half=lower,hinge={hinge},open=false]')
            self.set(x + dx, y + 1, z + dz, f'{mat}_door[facing={facing},half=upper,hinge={hinge},open=false]')
            hinge = 'right'

    def opening(self, x1, y1, z1, x2, y2, z2):
        self.fill(x1, y1, z1, x2, y2, z2, AIR)

    def gable_roof(self, x1, z1, x2, z2, y, axis, stairs, slab, block, overhang=1, peak_block=None):
        """Toit à deux pans. axis = 'x' : faîtage parallèle à x (pentes vers nord et sud)."""
        x1 -= overhang
        x2 += overhang
        z1 -= overhang
        z2 += overhang
        if axis == 'x':
            depth = (z2 - z1 + 1)
            n = depth // 2
            for i in range(n):
                yy = y + i
                self.fill(x1, yy, z1 + i, x2, yy, z1 + i, f'{stairs}[facing=south,half=bottom]')
                self.fill(x1, yy, z2 - i, x2, yy, z2 - i, f'{stairs}[facing=north,half=bottom]')
                if i > 0:                                      # pignons
                    for xx in (x1 + overhang, x2 - overhang):
                        self.fill(xx, yy, z1 + i + 1, xx, yy, z2 - i - 1, block)
            if depth % 2:
                self.fill(x1, y + n, z1 + n, x2, y + n, z1 + n, slab)
            if peak_block:
                self.fill(x1, y + n - (0 if depth % 2 else 1), (z1 + z2) // 2, x2, y + n - (0 if depth % 2 else 1), (z1 + z2) // 2, peak_block, only=(AIR, None))
        else:
            depth = (x2 - x1 + 1)
            n = depth // 2
            for i in range(n):
                yy = y + i
                self.fill(x1 + i, yy, z1, x1 + i, yy, z2, f'{stairs}[facing=east,half=bottom]')
                self.fill(x2 - i, yy, z1, x2 - i, yy, z2, f'{stairs}[facing=west,half=bottom]')
                if i > 0:
                    for zz in (z1 + overhang, z2 - overhang):
                        self.fill(x1 + i + 1, yy, zz, x2 - i - 1, yy, zz, block)
            if depth % 2:
                self.fill(x1 + n, y + n, z1, x1 + n, y + n, z2, slab)

    def flat_roof(self, x1, z1, x2, z2, y, slab, rim=None):
        self.fill(x1, y, z1, x2, y, z2, slab)
        if rim:
            self.walls(x1, z1, x2, z2, y + 1, y + 1, rim)

    def stair_run(self, x, y, z, dx, dz, n, stairs, facing, support=None):
        """Escalier droit montant de n marches dans la direction (dx, dz)."""
        for i in range(n):
            self.set(x + dx * i, y + i, z + dz * i, f'{stairs}[facing={facing},half=bottom]')
            if support:
                self.fill(x + dx * i, y - 1, z + dz * i, x + dx * i, y + i - 1, z + dz * i, support, keep=True)

    def spiral(self, cx, cz, r, y1, y2, step_block, center=None, per_turn=12):
        """Escalier en colimaçon autour d'un axe (cx, cz)."""
        for i, y in enumerate(range(y1, y2 + 1)):
            a = 2 * math.pi * i / per_turn
            x, z = round(cx + r * math.cos(a)), round(cz + r * math.sin(a))
            self.fill(x, y, z, x, y, z, step_block)
            self.fill(x, y + 1, z, x, y + 3, z, AIR, only=None)
            x2, z2 = round(cx + (r - 1) * math.cos(a)), round(cz + (r - 1) * math.sin(a))
            if (x2, z2) != (cx, cz):
                self.fill(x2, y, z2, x2, y, z2, step_block)
        if center:
            self.fill(cx, y1, cz, cx, y2 + 3, cz, center)

    def ruin(self, x1, y1, z1, x2, y2, z2, chance=0.15, mossy=None, top_bias=True):
        """Abîme une structure : trous (plus nombreux en haut), blocs moussus."""
        mossy = mossy or {}
        for (x, y, z), b in list(self.v.items()):
            if not (x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2) or b == AIR:
                continue
            t = (y - y1) / max(1, (y2 - y1))
            if self.r.random() < chance * (0.3 + 1.4 * t if top_bias else 1):
                self.v[(x, y, z)] = AIR
            elif b.split('[')[0] in mossy and self.r.random() < 0.35:
                self.v[(x, y, z)] = mossy[b.split('[')[0]] + (b[b.index('['):] if '[' in b else '')

    def scatter(self, x1, y, z1, x2, z2, blocks, n, on=None):
        for _ in range(n):
            x, z = self.r.randint(x1, x2), self.r.randint(z1, z2)
            if self.v.get((x, y, z), AIR) == AIR and (on is None or self.v.get((x, y - 1, z)) not in (AIR, None)):
                self.v[(x, y, z)] = self.r.choice(blocks)

    # ---------------------------------------------------------------- mobilier
    def bed(self, x, y, z, facing='north', color='red'):
        dx, dz = {'north': (0, -1), 'south': (0, 1), 'east': (1, 0), 'west': (-1, 0)}[facing]
        self.set(x, y, z, f'{color}_bed[facing={facing},part=foot]')
        self.set(x + dx, y, z + dz, f'{color}_bed[facing={facing},part=head]')

    def table(self, x, y, z, top='spruce_pressure_plate', leg='spruce_fence'):
        self.set(x, y, z, leg)
        self.set(x, y + 1, z, top)

    def chair(self, x, y, z, facing, mat='spruce'):
        self.set(x, y, z, f'{mat}_stairs[facing={facing},half=bottom]')

    def shelf(self, x1, y, z1, x2, z2, items=('barrel[facing=up]', 'chiseled_bookshelf[facing=south]', 'bookshelf', 'decorated_pot')):
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                self.set(x, y, z, self.r.choice(items))

    def lamp(self, x, y, z, hanging=True, kind='lantern'):
        if hanging:
            self.set(x, y + 1, z, 'iron_chain')
            self.set(x, y, z, f'{kind}[hanging=true]')
        else:
            self.set(x, y, z, f'{kind}[hanging=false]')

    # ---------------------------------------------------------------- sortie
    def cmds(self, late=()):
        """Commandes fill : par couche, rectangles de même bloc fusionnés (glouton).
        late : noms de blocs (sans minecraft: ni état) émis dans une passe finale, après toute la structure. Reconstruction en place : une
        échelle (ou autre bloc à support) posée avant son dos saute si l'ancien dos est non porteur (vitre...) et ne revient pas."""
        late = frozenset(late)
        out = []
        layers, late_layers = {}, {}
        for (x, y, z), b in self.v.items():
            (late_layers if b.split('[')[0] in late else layers).setdefault(y, {})[(x, z)] = b
        for pool in (layers, late_layers):
            for y in sorted(pool):
                L = dict(pool[y])
                for (x, z) in sorted(L):
                    if (x, z) not in L:
                        continue
                    b = L[(x, z)]
                    x2 = x
                    while (x2 + 1, z) in L and L[(x2 + 1, z)] == b:
                        x2 += 1
                    z2 = z
                    while all((xx, z2 + 1) in L and L[(xx, z2 + 1)] == b for xx in range(x, x2 + 1)):
                        z2 += 1
                    for xx in range(x, x2 + 1):
                        for zz in range(z, z2 + 1):
                            del L[(xx, zz)]
                    if (x, z) == (x2, z2):
                        out.append(f'setblock {x} {y} {z} minecraft:{b}')
                    else:
                        out.append(f'fill {x} {y} {z} {x2} {y} {z2} minecraft:{b}')
        return out


# ---------------------------------------------------------------- rendu isométrique (contrôle visuel)
COLORS = {
    'spruce': (110, 80, 50), 'oak': (160, 130, 80), 'birch': (210, 200, 160), 'dark_oak': (70, 50, 30), 'mangrove': (120, 50, 45),
    'acacia': (170, 90, 50), 'jungle': (150, 110, 70), 'stone': (125, 125, 125), 'cobblestone': (110, 110, 110), 'mossy': (90, 115, 80),
    'andesite': (135, 135, 135), 'deepslate': (70, 70, 75), 'tuff': (105, 105, 95), 'basalt': (75, 75, 80), 'blackstone': (45, 40, 45),
    'obsidian': (25, 15, 40), 'crying': (80, 20, 120), 'white': (230, 230, 230), 'light_gray': (160, 160, 160), 'gray': (90, 90, 90),
    'black': (30, 30, 30), 'red': (170, 40, 35), 'orange': (220, 120, 40), 'yellow': (230, 200, 60), 'lime': (120, 200, 50),
    'green': (70, 120, 40), 'cyan': (40, 130, 140), 'light_blue': (90, 160, 220), 'blue': (50, 70, 170), 'brown': (110, 75, 45),
    'terracotta': (155, 90, 65), 'glass': (190, 230, 240), 'copper': (190, 110, 80), 'iron': (200, 200, 205), 'gold': (240, 200, 60),
    'lantern': (255, 210, 120), 'lava': (255, 110, 10), 'water': (50, 90, 200), 'magma': (180, 70, 20), 'bone': (225, 220, 200),
    'hay': (210, 180, 60), 'leaves': (60, 120, 40), 'log': (100, 75, 50), 'mud': (90, 75, 60), 'sand': (215, 200, 150),
    'brick': (150, 70, 60), 'quartz': (235, 230, 225), 'prismarine': (90, 160, 140), 'sea_lantern': (200, 240, 230), 'barrel': (130, 95, 55),
    'wool': (220, 220, 220), 'concrete': (200, 200, 200), 'sulfur': (220, 210, 80), 'packed_mud': (140, 105, 80), 'rail': (140, 120, 100),
    'chain': (60, 60, 70), 'bars': (110, 110, 115), 'polished': (60, 55, 60),
}


def color_of(b):
    n = b.split('[')[0]
    for key in sorted(COLORS, key=len, reverse=True):
        if key in n:
            return COLORS[key]
    return (200, 0, 200)


def render(vox, path, scale=6, cut_y=None, title=''):
    from PIL import Image, ImageDraw
    pts = [(x, y, z, b) for (x, y, z), b in vox.v.items() if b != AIR and (cut_y is None or y <= cut_y)]
    if not pts:
        return
    xs = [p[0] for p in pts]
    zs = [p[2] for p in pts]
    ys = [p[1] for p in pts]

    def proj(x, y, z):
        return ((x - z) * 0.866 * scale, ((x + z) * 0.5 - y) * scale)
    cs = [proj(x, y, z) for x, y, z, _ in pts]
    ox, oy = -min(c[0] for c in cs) + scale * 2, -min(c[1] for c in cs) + scale * 3
    W = int(max(c[0] for c in cs) + ox + scale * 2)
    H = int(max(c[1] for c in cs) + oy + scale * 2)
    img = Image.new('RGB', (W, H + 14), (235, 240, 245))
    d = ImageDraw.Draw(img)
    pts.sort(key=lambda p: (p[0] + p[2], p[1]))
    for x, y, z, b in pts:
        col = color_of(b)
        top = [proj(x, y + 1, z), proj(x + 1, y + 1, z), proj(x + 1, y + 1, z + 1), proj(x, y + 1, z + 1)]
        right = [proj(x + 1, y, z), proj(x + 1, y + 1, z), proj(x + 1, y + 1, z + 1), proj(x + 1, y, z + 1)]
        front = [proj(x, y, z + 1), proj(x + 1, y, z + 1), proj(x + 1, y + 1, z + 1), proj(x, y + 1, z + 1)]
        for poly, k in ((top, 1.0), (right, 0.7), (front, 0.85)):
            d.polygon([(px + ox, py + oy) for px, py in poly], fill=tuple(int(c * k) for c in col))
    d.text((4, H), title, fill=(0, 0, 0))
    img.save(path)
