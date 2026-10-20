"""Élytra : grille de voxels (Vox) et fusion en commandes fill/setblock (to_cmds). Module importé par sky_layout et sky_game.
"""

# =====================================================================================
# Voxels → commandes fill/setblock fusionnées
# =====================================================================================


class Vox:
    def __init__(self):
        self.v = {}

    def put(self, x, y, z, b):
        self.v[(x, y, z)] = b

    def bbox(self):
        xs = [p[0] for p in self.v]; ys = [p[1] for p in self.v]; zs = [p[2] for p in self.v]
        return min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)


def to_cmds(v):
    """Fusion : segments en x → rectangles en z → pavés en y."""
    layers = {}
    for (x, y, z), b in v.items():
        layers.setdefault((y, b), {}).setdefault(z, []).append(x)
    rects = {}
    for (y, b), rows in layers.items():
        runs = {}
        for z, xs in rows.items():
            xs.sort()
            s = p = xs[0]
            for x in xs[1:] + [None]:
                if x is not None and x == p + 1:
                    p = x
                    continue
                runs.setdefault((s, p), []).append(z)
                if x is not None:
                    s = p = x
        for (x0, x1), zs in runs.items():
            zs.sort()
            s = p = zs[0]
            for z in zs[1:] + [None]:
                if z is not None and z == p + 1:
                    p = z
                    continue
                rects.setdefault((x0, x1, s, p, b), []).append(y)
                if z is not None:
                    s = p = z
    out = []
    for (x0, x1, z0, z1, b), ys in rects.items():
        ys.sort()
        s = p = ys[0]
        for y in ys[1:] + [None]:
            if y is not None and y == p + 1 and (x1 - x0 + 1) * (z1 - z0 + 1) * (y - s + 1) <= 32768:
                p = y
                continue
            vol = (x1 - x0 + 1) * (z1 - z0 + 1) * (p - s + 1)
            if vol == 1:
                out.append((vol, s, f'setblock {x0} {s} {z0} minecraft:{b}'))
            else:
                out.append((vol, s, f'fill {x0} {s} {z0} {x1} {p} {z1} minecraft:{b}'))
            if y is not None:
                s = p = y
    # du bas vers le haut (les fleurs/herbes posées après leur support)
    out.sort(key=lambda t: t[1])
    return out
