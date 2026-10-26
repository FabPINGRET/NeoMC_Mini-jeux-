"""Lampadaires du spawn : aucun effacement d'air posé ailleurs (Hall, */spawn_clean, portails) ne doit couper un lampadaire.
Un fill d'air qui emporte la base (y 64) laissait le poteau et la lanterne en l'air ; gen_lobby.lamp() n'en pose plus sous un
effacement connu (theme_world.clears). Lire les build_N du spawn tels qu'ils sont dans data/mg/function.
Lancer depuis la racine du depot : python -m unittest discover -s tools/tests -v   (la racine est derivee de ce fichier).
"""
import functools
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
F = ROOT / 'data' / 'mg' / 'function'
sys.path.insert(0, str(ROOT / 'tools' / 'lobby'))
import theme_world as TW   # noqa: E402

BASES = {'minecraft:chiseled_polished_blackstone', 'minecraft:chiseled_stone_bricks', 'minecraft:polished_andesite'}
LANTERN = 'minecraft:lantern'
# tags de filtre `replace #tag` sans rapport avec un lampadaire (base, mur, lanterne) : ne comptent pas comme touche
SAFE_TAGS = {'#minecraft:leaves', '#minecraft:logs', '#minecraft:replaceable', '#minecraft:flowers'}
# lampadaires que gen_lobby saute (un clear d'air posterieur les couperait) : aucun ne doit exister dans les build_N
SKIPPED = {(-4, 17), (-56, 32), (-4, -17), (4, -17), (17, -4)}
EXPECTED_LAMPS = 40   # nombre de lampadaires dans lobby/build_N
# clears conditionnels qui touchent une colonne de lampadaire, connus et inoffensifs : (fichier relatif, ligne) -> raison.
# Vide : foot/build.mcfunction:87-90 (execute if block ... polished_blackstone_wall run fill ... air en (-2,-18), (-2,-15),
# (1,-18), (1,-15)) ne coupent aucune colonne de lampadaire.
CONDITIONAL_OK = {}


@functools.lru_cache(maxsize=None)
def lamps():
    """(x, z, {y: bloc}) de chaque lampadaire du lobby : base y 64, poteau de *_wall, lanterne au sommet."""
    saved = (dict(TW.W), list(TW.DYN))   # theme_world est un module global : on restaure son etat apres la relecture
    try:
        return _read_lamps()
    finally:
        TW.W.clear()
        TW.W.update(saved[0])
        TW.DYN[:] = saved[1]


def _read_lamps():
    TW.W.clear()
    TW.DYN.clear()
    for p in sorted((F / 'lobby').glob('build_*.mcfunction'), key=lambda q: TW.num(str(q))):
        for l in p.read_text(encoding='utf-8').splitlines():
            TW.apply(l, False)
    out = []
    for (x, y, z), b in sorted(TW.W.items()):
        if y != 64 or TW.bid(b) not in BASES:
            continue
        col, top = {64: TW.bid(b)}, 65
        while TW.bid(TW.W.get((x, top, z))).endswith('_wall'):
            col[top] = TW.bid(TW.W[(x, top, z)])
            top += 1
        if top > 65 and TW.bid(TW.W.get((x, top, z))) == LANTERN:
            col[top] = LANTERN
            out.append((x, z, col))
    return tuple((x, z, tuple(col.items())) for x, z, col in out)


def hits(x, z, col, box):
    """Cases (y) du lampadaire que la boîte efface : toute la colonne si le clear est sans filtre, sinon les cases du bloc filtré."""
    x1, x2, y1, y2, z1, z2, filt = box
    if not (x1 <= x <= x2 and z1 <= z <= z2):
        return []
    # un filtre #tag n'est jamais compare a un bloc : il compte comme touche, sauf tags sans rapport avec un lampadaire
    tag = filt is not None and filt.startswith('#') and filt not in SAFE_TAGS
    return [y for y, b in col if y1 <= y <= y2 and (filt is None or tag or TW.bid(filt) == b)]


def conditional_clears():
    """Effacements d'air derriere un `execute ... run fill|setblock ... air` (invisibles pour TW.clears) : (rel, n, boite).
    Memes exclusions que TW.clears (build_N du lobby, desinstaller, autre dimension) + lobby/theme/ (decors saisonniers)."""
    out = []
    for p in sorted(F.rglob('*.mcfunction')):
        rel = p.relative_to(F).as_posix()
        if re.fullmatch(r'lobby/build_\d+\.mcfunction', rel) or rel == 'desinstaller.mcfunction' or '/theme/' in '/' + rel:
            continue
        lines = p.read_text(encoding='utf-8').splitlines()
        if TW.other_dimension(lines):
            continue
        for n, l in enumerate(lines, 1):
            m = re.match(r'^\s*execute\s.*?\brun\s+((?:fill|setblock)\s.+)$', l)
            box = TW.clear_box(m[1]) if m else None
            if box:
                out.append((rel, n, box))
    return out


class LobbyLamps(unittest.TestCase):
    def test_lamps_found(self):
        self.assertGreaterEqual(len(lamps()), 30, 'lampadaires du lobby introuvables : build_N absents ?')

    def test_lamp_count_and_skipped_positions_pinned(self):
        # tout nouveau lampadaire saute (ou ajoute) change ce nombre : a mettre a jour en connaissance de cause
        self.assertEqual(len(lamps()), EXPECTED_LAMPS)
        present = {(x, z) for x, z, _ in lamps()}
        self.assertEqual(sorted(present & SKIPPED), [], 'lampadaire pose a une position qu\'un clear coupe')

    def test_no_conditional_clear_hits_a_lamp(self):
        found = []
        for rel, n, box in conditional_clears():
            if (rel, n) in CONDITIONAL_OK:
                continue
            for x, z, col in lamps():
                ys = hits(x, z, col, box)
                if ys:
                    found.append(f'lampadaire ({x},{z}) y{min(ys)}-{max(ys)} <- {rel}:{n} (clear conditionnel)')
        self.assertEqual(found, [], 'effacements conditionnels qui coupent un lampadaire :\n' + '\n'.join(found))

    def test_no_clear_hits_a_lamp(self):
        found = []
        for rel, n, box in TW.clears(str(F)):
            for x, z, col in lamps():
                ys = hits(x, z, col, box)
                if ys:
                    found.append(f'lampadaire ({x},{z}) y{min(ys)}-{max(ys)} <- {rel}:{n}')
        self.assertEqual(found, [], 'effacements qui coupent un lampadaire :\n' + '\n'.join(found))


class ClearBox(unittest.TestCase):
    def test_clear_box_unfiltered_fill(self):
        self.assertEqual(TW.clear_box('fill -5 65 15 -4 64 36 minecraft:air'), (-5, -4, 64, 65, 15, 36, None))
        self.assertEqual(TW.clear_box('fill 1 64 1 2 64 2 air strict'), (1, 2, 64, 64, 1, 2, None))

    def test_clear_box_replace_filter(self):
        b = TW.clear_box('fill -60 64 15 -6 71 36 minecraft:air replace #minecraft:leaves')
        self.assertEqual(b, (-60, -6, 64, 71, 15, 36, '#minecraft:leaves'))
        self.assertEqual(TW.clear_box('fill 0 64 0 1 64 1 air replace lantern')[6], 'minecraft:lantern')

    def test_clear_box_tag_filter_returned_as_is(self):
        self.assertEqual(TW.clear_box('fill 0 64 0 1 64 1 air replace #minecraft:walls')[6], '#minecraft:walls')

    def test_hits_tag_filter_counts_unless_safe(self):
        col = ((64, 'minecraft:polished_andesite'), (65, 'minecraft:stone_brick_wall'), (66, 'minecraft:lantern'))
        box = lambda f: (0, 0, 64, 66, 0, 0, f)
        self.assertEqual(hits(0, 0, col, box('#minecraft:walls')), [64, 65, 66])
        self.assertEqual(hits(0, 0, col, box('#minecraft:leaves')), [])
        self.assertEqual(hits(0, 0, col, box('minecraft:lantern')), [66])
        self.assertEqual(hits(0, 0, col, box(None)), [64, 65, 66])
        self.assertEqual(hits(1, 0, col, box(None)), [])

    def test_clear_box_not_an_air_clear(self):
        self.assertIsNone(TW.clear_box('fill -60 64 15 -6 64 36 minecraft:snow replace minecraft:air'))
        self.assertIsNone(TW.clear_box('fill 0 64 0 1 64 1 minecraft:air keep'))
        self.assertIsNone(TW.clear_box('execute if entity @a run fill 0 64 0 1 64 1 air'))

    def test_clear_box_setblock_and_clip(self):
        self.assertEqual(TW.clear_box('setblock 4 64 -17 minecraft:air'), (4, 4, 64, 64, -17, -17, None))
        self.assertEqual(TW.clear_box('setblock 4 64 -17 minecraft:air destroy')[6], None)
        self.assertEqual(TW.clear_box('fill 70 64 0 200 64 1 air')[:2], (70, 80))
        self.assertIsNone(TW.clear_box('fill 100 64 0 200 64 1 air'))


if __name__ == '__main__':
    unittest.main()
