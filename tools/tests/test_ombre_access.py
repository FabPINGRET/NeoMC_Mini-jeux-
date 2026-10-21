"""Ombrelune : acces a pied au volcan de Pyrecendre et a Khazgarde (ol_access).
Lancer : python -m unittest discover -s tools/tests -v
"""
import collections
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCADE = ROOT / 'tools' / 'arcade'
if str(ARCADE) not in sys.path:
    sys.path.insert(0, str(ARCADE))
import ol_access as A   # noqa: E402
import ol_world as W    # noqa: E402

FILL = re.compile(r'fill (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+)')
MAX_FILL = 32768


def top(c):
    return max(W.H[c], W.COL[c][3] or 0)


def bfs(start, up=1):
    """Colonnes atteignables a pied : montee <= up par pas, descente libre."""
    seen = {start}
    q = collections.deque([start])
    while q:
        c = q.popleft()
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (c[0] + dx, c[1] + dz)
            if n in W.H and n not in seen and top(n) - top(c) <= up:
                seen.add(n)
                q.append(n)
    return seen


def volume(m):
    a = [int(g) for g in m.groups()]
    return (abs(a[3] - a[0]) + 1) * (abs(a[4] - a[1]) + 1) * (abs(a[5] - a[2]) + 1)


class Reachability(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reach = bfs((0, 0))

    def test_caldera_breach_reachable(self):
        x, y, z = A.breach_pt((180, 180), 117)
        self.assertIn((x, z), W.H)
        self.assertIn((x, z), self.reach)
        self.assertEqual(W.H[(x, z)], 116)   # sol de la breche au niveau de la caldeira (CALD_Y)

    def test_south_west_region_reachable(self):
        got = [c for c in self.reach if W.region_at(*c) == 'sw']
        self.assertGreater(len(got), 100)

    def test_parvis_reachable(self):
        self.assertIn((0, 135), self.reach)

    def test_start_is_in_map(self):
        self.assertIn((0, 0), W.H)


class Geometry(unittest.TestCase):
    def test_parvis_covers_dwarf_gate_paving(self):
        x0, zf = W.P['kgate']
        px0, pz0, px1, pz1 = A.PARVIS[:4]
        self.assertLessEqual(px0, x0 - 14)
        self.assertGreaterEqual(px1, x0 + 14)
        self.assertLessEqual(pz0, zf - 10)
        self.assertGreaterEqual(pz1, zf - 1)

    def test_parvis_level_is_gate_floor(self):
        self.assertEqual(A.PARVIS[4], 66)

    def test_hall_guard_covers_hall(self):
        x0, zf = W.P['kgate']
        gx0, gz0, gx1, gz1 = A.HALL_GUARD
        self.assertLessEqual(gx0, x0 - 17)
        self.assertGreaterEqual(gx1, x0 + 17)
        self.assertLessEqual(gz0, zf + 1)
        self.assertGreaterEqual(gz1, zf + 65)

    def test_no_carved_column_in_hall_guard(self):
        gx0, gz0, gx1, gz1 = A.HALL_GUARD
        W.terrain_cmds('s')   # le relief est deja calcule a l'import ; CARVED est complet
        bad = [c for c in A.CARVED if gx0 <= c[0] <= gx1 and gz0 <= c[1] <= gz1]
        self.assertEqual(bad, [])

    def test_gorges_leave_hall_untouched(self):
        for z in (140, 170, 206):
            self.assertEqual(A.gorges(0, z, 80), 80)
        self.assertEqual(A.gorges(0, 100, 80), 80)   # nord du parvis

    def test_gorges_only_lower(self):
        for c in list(W.H)[::37]:
            self.assertLessEqual(A.gorges(c[0], c[1], 90), 90)

    def test_carved_includes_parvis_and_breach(self):
        self.assertTrue(A.carved(0, 135))
        self.assertTrue(A.carved(*A.breach_pt((180, 180), 117)[::2]))
        self.assertFalse(A.carved(0, 0))

    def test_breach_axis_and_width(self):
        c = (180, 180)
        x, _, z = A.breach_pt(c, 117)
        self.assertTrue(A.in_breach(x, z, c))
        self.assertFalse(A.in_breach(c[0] - 10, c[1] - 10, c))   # derriere le centre
        self.assertFalse(A.in_breach(x + 5, z + 4, c))   # decalage perpendiculaire a l'axe, hors bande (> BREACH_HW)

    def test_ramp_routes_shape(self):
        routes = A.ramp_routes((180, 180))
        self.assertEqual(len(routes), 4)
        self.assertTrue(all(len(r) >= 2 for r in routes))


class FillVolumes(unittest.TestCase):
    def test_terrain_cmds_within_limit(self):
        worst = 0
        for k in W.REGIONS:
            for cmd in W.terrain_cmds(k):
                m = FILL.fullmatch(cmd[:cmd.index(' minecraft:')]) if cmd.startswith('fill') else None
                self.assertIsNotNone(m, cmd)
                worst = max(worst, volume(m))
        self.assertLessEqual(worst, MAX_FILL)

    def test_datapack_fills_within_limit(self):
        files = sorted((ROOT / 'data' / 'mg' / 'function' / 'ombre' / 'd').glob('*.mcfunction'))
        self.assertTrue(files)
        n = 0
        for f in files:
            for m in FILL.finditer(f.read_text(encoding='utf-8')):
                n += 1
                self.assertLessEqual(volume(m), MAX_FILL, f'{f.name}: {m.group(0)}')
        self.assertGreater(n, 0)


if __name__ == '__main__':
    unittest.main()
