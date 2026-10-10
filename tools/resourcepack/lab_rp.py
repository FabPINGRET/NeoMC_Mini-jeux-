# ------------------------------------------------------------------ Labyrinthe aveugle : écran noir du marcheur
# Exécuté par gen_rp.py (exec) : utilise png_rgba, wjson, A, math, os.
# Police mg:lab, glyphe  : 256 × 128 noir, petit trou flou au centre (on devine un bloc devant soi).
# Envoyé en titre (échelle 4) : hauteur 160 → 640 × 1280 px d'interface, de quoi couvrir l'écran ; ascent = hauteur / 2 - 3.


def lab_blind_img():
    w, h = 256, 128
    cx, cy = (w - 1) / 2, (h - 1) / 2
    img = []
    for y in range(h):
        row = []
        for x in range(w):
            d = math.hypot(x - cx, y - cy)
            a = 255 if d >= 9 else int(255 * max(0.0, (d - 4) / 5))
            row.append((0, 0, 0, a))
        img.append(row)
    return img


png_rgba(os.path.join(A, 'textures', 'font', 'lab_blind.png'), lab_blind_img())
wjson(os.path.join(A, 'font', 'lab.json'), {"providers": [
    {"type": "bitmap", "file": "mg:font/lab_blind.png", "ascent": 77, "height": 160, "chars": [""]}]})
