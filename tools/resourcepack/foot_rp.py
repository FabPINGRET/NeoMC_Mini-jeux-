# ------------------------------------------------------------------ terrain de foot : le bloc de test (corps de la balle) dessiné en ballon
# Exécuté par gen_rp.py (exec) : utilise png, wjson, box, PAL, A, OUT, os, math. Remplace le modèle vanilla du bloc de test
# (minecraft:block/test_block_start, jamais posable en survie) : la balle est un sulfur_cube dont le corps est un test_block (tools/lobby/foot_game.py).
# Ballon = 3 cubes imbriqués (un droit, deux tournés de 45° sur y et sur x, raccourcis sur leur axe pour éviter le z-fighting) : silhouette arrondie.
def _ball_rows():
    """16 lignes de 16 caractères : fond blanc, pentagones noirs (centre et coins), contours gris."""
    def pent(px, py, cx, cy, r=4.3):
        # pentagone régulier de rayon r, pointe en haut : le point est dedans s'il est du bon côté des 5 arêtes (apothème r cos 36°)
        return all((px - cx) * math.cos(math.radians(-54 + 72 * k)) + (py - cy) * math.sin(math.radians(-54 + 72 * k)) <= r * math.cos(math.radians(36))
                   for k in range(5))
    centres = [(7.5, 7.5), (-0.5, -0.5), (15.5, -0.5), (-0.5, 15.5), (15.5, 15.5)]
    rows = []
    for y in range(16):
        row = ''
        for x in range(16):
            if any(pent(x, y, cx, cy) for cx, cy in centres):
                row += 'k'
            elif any(pent(x, y, cx, cy, 5.5) for cx, cy in centres):
                row += 'l'                       # contour gris autour de chaque pentagone
            else:
                row += 'w'
        rows.append(row)
    return rows


png(os.path.join(A, 'textures', 'block', 'football.png'), _ball_rows(), PAL)
_ball = [box([2, 2, 2], [14, 14, 14], 'ball'), box([2, 2.5, 2], [14, 13.5, 14], 'ball'), box([2.5, 2, 2], [13.5, 14, 14], 'ball')]
_ball[1]['rotation'] = {'origin': [8, 8, 8], 'axis': 'y', 'angle': 45}
_ball[2]['rotation'] = {'origin': [8, 8, 8], 'axis': 'x', 'angle': 45}
wjson(os.path.join(OUT, 'assets', 'minecraft', 'models', 'block', 'test_block_start.json'), {
    "textures": {"ball": "mg:block/football", "particle": "mg:block/football"}, "elements": _ball})
