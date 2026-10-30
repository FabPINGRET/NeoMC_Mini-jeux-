"""tools/floaty : correctifs de revue de L6a (faits en L6b), chacun avec son cas INVERSE : passager sans `Pos` (rider), `run_command` dans une
commande de panneau (seen), palettes ignorées à la racine seulement (_SKIP), déséchappement en une passe, faux positifs de sans_bloc documentés.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import sys
import unittest
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_signs as TS  # noqa: E402  (holder, faces, comp, chunk, EMPTY, MODERN)
import test_floaty_terrain as TT  # noqa: E402  (Base, mca, nbt, Str / Int / Comp / Lst)
import fl_signs  # noqa: E402
import fl_terrain as F  # noqa: E402

mca, nbt, Str, Int, Comp, Lst = TT.mca, TT.nbt, TT.Str, TT.Int, TT.Comp, TT.Lst
CB = ('command_block',)


def cart(**fields):
    return {'id': 'minecraft:command_block_minecart', 'Command': 'stop', **fields}


def outside(tree):
    return fl_signs.count_outside(tree, CB + ('stop',), F.HOLDERS)[1]            # compte « stop » : la Command d'un minecart


class Rider(unittest.TestCase):
    """Invariant : un passager sans `Pos` d'un porteur qui en a un est une entité (un minecart déjà analysé), pas du texte oublié."""

    def test_rider_without_pos_of_a_carrier_with_pos_is_not_counted(self):
        carrier = {'id': 'minecraft:zombie', 'Pos': [1.0, 2.0, 3.0], 'Passengers': [cart()]}
        self.assertEqual(outside({'Entities': [carrier]}), 0)
        deep = {'id': 'minecraft:zombie', 'Pos': [1.0, 2.0, 3.0], 'Passengers': [{'id': 'minecraft:pig', 'Passengers': [cart()]}]}
        self.assertEqual(outside({'Entities': [deep]}), 0)                              # le passager d'un passager l'est aussi

    def test_inverse_carrier_without_pos_or_other_list_key_still_counts(self):
        spawner_entity = {'id': 'minecraft:zombie', 'Passengers': [cart()]}              # SpawnData.entity : pas de Pos
        self.assertEqual(outside({'block_entities': [{'id': 'minecraft:mob_spawner', 'x': 1, 'y': 2, 'z': 3, 'SpawnData': {'entity': spawner_entity}}]}), 1)
        in_items = {'id': 'minecraft:zombie', 'Pos': [1.0, 2.0, 3.0], 'Items': [cart()]}   # `Items` n'est pas `Passengers` : un objet, pas un passager
        self.assertEqual(outside({'Entities': [in_items]}), 1)
        self.assertEqual(outside({'Entities': [cart(Pos=[1.0, 2.0, 3.0])]}), 0)           # le minecart lui-même (avec Pos) : holder


class Seen(TT.Base):
    """Invariant : les `run_command` que la commande d'un panneau contient elle-même sont des commandes vues, pas un panneau mal lu."""

    def scan(self, sign):
        path = self.dim / 'region' / 'r.2.0.mca'
        path.write_bytes(mca([(0, TS.chunk(TS.MODERN, [sign]), 2)]))
        stats = Counter()
        finds, pending = F.scan_file(path, stats)
        return finds, stats['panneau_illisible']

    def test_nested_run_commands_are_seen(self):
        one = 'tellraw @s {"text":"x","clickEvent":{"action":"run_command","value":"/trigger t"}}'
        two = 'tellraw @s [{"clickEvent":{"action":"run_command","value":"a"}},{"clickEvent":{"action":"run_command","value":"b"}}]'
        for cmd in (one, two):
            with self.subTest(cmd[:30]):
                finds, bad = self.scan(TS.holder('sign', (1, 2, 3), **TS.faces(front=[TS.comp(cmd=cmd), TS.EMPTY, TS.EMPTY, TS.EMPTY])))
                self.assertEqual(([f.command for f in finds], bad), ([cmd], 0))

    def test_inverse_a_stray_run_command_is_still_unreadable(self):
        one = 'tellraw @s {"clickEvent":{"action":"run_command","value":"/trigger t"}}'
        stray = TS.holder('sign', (1, 2, 3), **TS.faces(front=[TS.comp(cmd=one), TS.EMPTY, TS.EMPTY, TS.EMPTY]), Notes=Str('run_command'))
        self.assertEqual(self.scan(stray)[1], 1)                                       # 1 commande + 1 imbriquée vues, 3 présentes
        broken = TS.holder('sign', (1, 2, 3), **TS.faces(front=['{"clickEvent":{"action":"run_command"', '{}', '{}', '{}'], ctype=8))
        self.assertEqual(self.scan(broken)[1], 1)                                      # JSON invalide : aucune commande vue


class Skip(unittest.TestCase):
    """Invariant : palettes et ticks sont ignorés à la racine du chunk (ou de `Level`) ; plus bas, une clé du même nom est examinée."""

    PAL = {'palette': [{'Name': 'minecraft:command_block'}]}

    def test_root_and_level_are_skipped(self):
        self.assertEqual(fl_signs.count_outside({'sections': [self.PAL]}, CB, F.HOLDERS), [0])
        self.assertEqual(fl_signs.count_outside({'Level': {'Sections': [self.PAL], 'TileTicks': [{'i': 'minecraft:command_block'}]}}, CB, F.HOLDERS), [0])

    def test_inverse_same_names_deeper_are_examined(self):
        chest = {'id': 'minecraft:chest', 'x': 1, 'y': 2, 'z': 3, 'Items': [{'id': 'minecraft:stick', 'sections': 'command_block'}]}
        self.assertEqual(fl_signs.count_outside({'block_entities': [chest]}, CB, F.HOLDERS), [1])
        zombie = {'id': 'minecraft:zombie', 'Pos': [1.0, 2.0, 3.0], 'Level': {'sections': 'command_block'}, 'palette': 'command_block'}
        self.assertEqual(fl_signs.count_outside({'Entities': [zombie]}, CB, F.HOLDERS), [2])        # `Level` n'est spécial qu'à la racine
        self.assertEqual(fl_signs.count_outside({'Level': {'Level': {'sections': 'command_block'}}}, CB, F.HOLDERS), [1])

    def test_documented_false_positive_of_sans_bloc(self):
        display = {'id': 'minecraft:block_display', 'Pos': [1.0, 2.0, 3.0], 'block_state': {'Name': 'minecraft:command_block'}}
        self.assertEqual(fl_signs.count_outside({'Entities': [display]}, CB, F.HOLDERS), [1])        # avertissement de plus, jamais un trou
        self.assertIn('block_display', fl_signs.count_outside.__doc__)


class Unescape(unittest.TestCase):
    def test_single_pass(self):
        self.assertEqual(F._unescape(r'x\\ny\nz', '"'), r'x\ny z')                      # `\\n` reste un antislash puis « n » ; `\n` devient un espace

    def test_inverse_plain_escapes_and_unknown_ones(self):
        self.assertEqual(F._unescape(r'say \"hi\"', '"'), 'say "hi"')                    # échappement valide : fl_rewrite.unescape, pas le repli
        self.assertEqual(F._unescape(r'a\tb\qc', '"'), 'a bqc')                          # repli : \t -> espace, tout autre antislash est retiré


if __name__ == '__main__':
    unittest.main()
