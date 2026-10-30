"""tools/floaty : panneaux (`sign`, `hanging_sign`) à `run_command` lus par fl_terrain / fl_signs (format NBT ou JSON, quelle que soit la
DataVersion du chunk), panneau mal lu (« panneau_illisible »), run_command hors panneau (livre, coffre : « rc_hors_panneau », jamais
« sans_bloc ») et command_block hors bloc (objet de coffre, spawner, falling_block : « sans_bloc »), sur de faux .mca (aides de test_floaty_terrain).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_terrain as TT  # noqa: E402  (Base, mca, nbt, be, Str / Int / Byte / Comp / Lst)
import fl_terrain as F  # noqa: E402

be, nbt, mca = TT.be, TT.nbt, TT.mca
Str, Int, Byte, Comp, Lst = TT.Str, TT.Int, TT.Byte, TT.Comp, TT.Lst
MODERN, JSON_FORMAT, OLD = 4903, 4324, 2500          # 4325 = 1.21.5 : composants NBT ; avant : chaînes JSON ; 2500 = 1.16 (Text1-4)


def comp(text='', cmd=None, extra=None):
    """Composant NBT (1.21.5+) : texte, click_event run_command, sous-composants `extra`."""
    d = {'text': Str(text)}
    if cmd is not None:
        d['click_event'] = Comp({'action': Str('run_command'), 'command': Str(cmd)})
    if extra:
        d['extra'] = Lst(10, extra)
    return d


def json_msg(cmd, extra=None):
    """Message JSON (avant 1.21.5) : texte vide + clickEvent run_command, sous-composants `extra` (liste de dict Python)."""
    d = {'text': '', 'clickEvent': {'action': 'run_command', 'value': cmd}}
    if extra:
        d['extra'] = extra
    return json.dumps(d)


def holder(kind, pos, **fields):
    return {'id': Str('minecraft:' + kind), 'x': Int(pos[0]), 'y': Int(pos[1]), 'z': Int(pos[2]), **fields}


def faces(front=None, back=None, ctype=10):
    """front_text / back_text : listes de 4 messages (compounds, ou chaînes JSON avec ctype=8) ; None = face absente."""
    out = {}
    for name, msgs in (('front_text', front), ('back_text', back)):
        if msgs is not None:
            out[name] = Comp({'messages': Lst(ctype, msgs), 'has_glowing_text': Byte(0)})
    return out


def chunk(dv, entities):
    return nbt({'DataVersion': Int(dv), 'block_entities': Lst(10, entities)})


EMPTY = comp()
BOOK = holder('chest', (1, 2, 3), Items=Lst(10, [{'id': Str('minecraft:written_book'), 'count': Int(1), 'components': Comp({
    'minecraft:written_book_content': Comp({'pages': Lst(10, [{'raw': Str(json_msg('/stop'))}])})})}]))


class Signs(TT.Base):
    def scan(self, raw):
        path = self.dim / 'region' / 'r.2.0.mca'
        path.write_bytes(mca([(0, raw, 2)]))
        stats = Counter()
        finds, pending = F.scan_file(path, stats)
        return sorted((f.kind, f.command) for f in finds), stats, pending, finds

    def test_nbt_components_front_back_and_nested_extra(self):
        sign = holder('sign', (5, 70, 9), **faces(
            front=[EMPTY, comp('a', cmd='gamerule doDaylightCycle false'), comp(extra=[comp('x', extra=[comp('y', cmd='stop')])]), EMPTY],
            back=[comp(cmd='tp @a 0 0 0'), EMPTY, EMPTY, EMPTY]))
        hanging = holder('hanging_sign', (6, 70, 9), **faces(front=[EMPTY, EMPTY, EMPTY, comp(cmd='op X')], back=[EMPTY] * 4))
        got, stats, pending, finds = self.scan(chunk(MODERN, [sign, hanging]))
        self.assertEqual(got, [('hanging_sign[front,3]', 'op X'), ('sign[back,0]', 'tp @a 0 0 0'),
                               ('sign[front,1]', 'gamerule doDaylightCycle false'), ('sign[front,2]', 'stop')])
        self.assertEqual({(f.pos, f.auto) for f in finds}, {((5, 70, 9), False), ((6, 70, 9), False)})
        self.assertEqual((stats['sans_bloc'], stats['rc_hors_panneau'], stats['illisible']), (0, 0, 0))
        self.assertEqual(pending, {'sans_bloc': [], 'rc_hors_panneau': [], 'panneau_illisible': []})

    def test_json_strings_before_1_21_5(self):
        sign = holder('sign', (1, 2, 3), **faces(front=[
            json_msg('/op X'), json.dumps({'text': '', 'extra': [{'text': 'x', 'extra': [{'clickEvent': {'action': 'run_command', 'value': 'weather clear'}}]}]}),
            '"abc"', 'pas du json'], back=[json.dumps({'text': 'x', 'clickEvent': {'action': 'open_url', 'value': 'http://x'}})] + ['""'] * 3, ctype=8))
        got, stats, pending, _ = self.scan(chunk(JSON_FORMAT, [sign]))
        self.assertEqual(got, [('sign[front,0]', '/op X'), ('sign[front,1]', 'weather clear')])      # texte nu, JSON invalide, open_url : ignorés
        self.assertEqual((stats['illisible'], stats['sans_bloc'], pending['rc_hors_panneau']), (0, 0, []))

    def test_text1_to_text4_before_1_20(self):
        sign = holder('sign', (1, 2, 3), Text1=Str('""'), Text2=Str(json_msg('/time set day')), Text3=Str('""'), Text4=Str(json_msg('say hi')))
        got, _, _, _ = self.scan(chunk(OLD, [sign]))
        self.assertEqual(got, [('sign[text,1]', '/time set day'), ('sign[text,3]', 'say hi')])

    def test_format_does_not_depend_on_the_chunk_data_version(self):
        nbt_sign = holder('sign', (1, 2, 3), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        json_sign = holder('sign', (1, 2, 3), **faces(front=[json_msg('stop'), '""', '""', '""'], ctype=8))
        for dv in (4325, 4324, 0):
            for name, be_ in (('nbt', nbt_sign), ('json', json_sign)):
                with self.subTest(dv=dv, format=name):
                    got, stats, pending, _ = self.scan(chunk(dv, [be_]))
                    self.assertEqual(got, [('sign[front,0]', 'stop')])
                    self.assertEqual((pending['rc_hors_panneau'], pending['panneau_illisible']), ([], []))    # un panneau est un holder

    def test_data_version_absent(self):
        sign = holder('sign', (1, 2, 3), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        got, _, _, _ = self.scan(nbt({'block_entities': Lst(10, [sign])}))
        self.assertEqual(got, [('sign[front,0]', 'stop')])

    def test_unreadable_sign_is_flagged_with_its_chunk(self):
        bad_json = holder('sign', (1, 2, 3), **faces(front=['{"text":"x","clickEvent":{"action":"run_command","value":"stop"', '""', '""', '""'], ctype=8))
        wrong_type = holder('sign', (4, 2, 3), Text1=Int(7), Text2=Str('{"text":"x","extra":[1,{"clickEvent":{"action":"open_url","value":"u"}}]}'))
        good = holder('sign', (5, 2, 3), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        for name, be_ in (('json invalide', bad_json), ('texte non JSON', holder('sign', (1, 2, 3), Text3=Str('run_command')))):
            with self.subTest(name):
                got, stats, pending, _ = self.scan(chunk(MODERN, [be_]))
                self.assertEqual((got, stats['panneau_illisible'], pending['panneau_illisible']), ([], 1, [('region/r.2.0.mca', 64, 0)]))
                self.assertEqual((stats['rc_hors_panneau'], stats['sans_bloc'], stats['illisible']), (0, 0, 0))
        got, stats, _, _ = self.scan(chunk(MODERN, [wrong_type, good]))           # aucun run_command dans le panneau bizarre : pas signalé
        self.assertEqual((got, stats['panneau_illisible']), ([('sign[front,0]', 'stop')], 0))

    def test_readable_sign_next_to_an_unreadable_one_keeps_its_command(self):
        good = holder('sign', (1, 2, 3), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        bad = holder('sign', (4, 2, 3), Text1=Str('{"clickEvent":{"action":"run_command","value":"op X"}'))
        got, stats, _, _ = self.scan(chunk(MODERN, [good, bad]))
        self.assertEqual((got, stats['panneau_illisible']), ([('sign[front,0]', 'stop')], 1))

    def test_filtered_messages_in_json_strings(self):
        sign = holder('sign', (1, 2, 3), front_text=Comp({
            'messages': Lst(8, [json_msg('stop'), '""', '""', '""']),
            'filtered_messages': Lst(8, [json_msg('stop'), json_msg('op X'), '""', '""'])}))
        got, stats, _, _ = self.scan(chunk(JSON_FORMAT, [sign]))
        self.assertEqual(got, [('sign[front,0]', 'stop'), ('sign[front,1,filtered]', 'op X')])
        self.assertEqual(stats['panneau_illisible'], 0)                          # le doublon filtered est compté dans `vus`

    def test_sign_stored_as_a_chest_object_is_outside_a_holder(self):
        item = {'id': Str('minecraft:oak_sign'), 'count': Int(1), 'tag': Comp({'BlockEntityTag': Comp({
            'id': Str('minecraft:sign'), 'front_text': Comp({'messages': Lst(10, [comp(cmd='stop'), EMPTY, EMPTY, EMPTY])})})})}
        got, stats, pending, _ = self.scan(chunk(MODERN, [holder('chest', (1, 2, 3), Items=Lst(10, [item]))]))
        self.assertEqual((got, stats['rc_hors_panneau'], len(pending['rc_hors_panneau'])), ([], 1, 1))

    def test_entities_file_minecart_with_run_command_is_not_flagged(self):
        cart = {'id': Str('minecraft:command_block_minecart'), 'Pos': Lst(6, [1.5, 64.0, -2.5]),
                'Command': Str('tellraw @a[tag=mg.flw] {"text":"x","clickEvent":{"action":"run_command","value":"/stop"}}')}
        got, stats, pending, finds = self.scan(nbt({'Entities': Lst(10, [cart])}))
        self.assertEqual((len(got), finds[0].pos), (1, (1, 64, -3)))
        self.assertEqual((stats['rc_hors_panneau'], stats['sans_bloc'], pending['sans_bloc']), (0, 0, []))

    def test_minecart_passenger_is_a_find(self):
        cart = {'id': Str('minecraft:command_block_minecart'), 'Command': Str('time set day')}
        rider = {'id': Str('minecraft:zombie'), 'Pos': Lst(6, [8.0, 64.0, 9.0]), 'Passengers': Lst(10, [cart])}
        got, stats, pending, finds = self.scan(nbt({'Entities': Lst(10, [rider])}))
        self.assertEqual((got, finds[0].pos, stats['sans_bloc']), ([('command_block_minecart', 'time set day')], (8, 64, 9), 0))

    def test_command_block_outside_a_holder_is_sans_bloc_even_next_to_a_real_block(self):
        real = be('command_block', 1, 2, 3, 'say ok')
        spawner = holder('mob_spawner', (4, 2, 3), SpawnData=Comp({'entity': Comp({'id': Str('minecraft:command_block_minecart'), 'Command': Str('stop')})}))
        falling = {'id': Str('minecraft:falling_block'), 'Pos': Lst(6, [1.0, 2.0, 3.0]), 'BlockState': Comp({'Name': Str('minecraft:command_block')}),
                   'TileEntityData': Comp({'Command': Str('stop'), 'id': Str('minecraft:command_block')})}
        chest = holder('chest', (5, 2, 3), Items=Lst(10, [{'id': Str('minecraft:command_block'), 'count': Int(1)}]))
        cases = (('spawner', spawner), ('falling_block', falling), ('coffre', chest))
        for name, other in cases:
            with self.subTest(name):
                got, stats, pending, _ = self.scan(chunk(MODERN, [real, other]))
                self.assertEqual((len(got), stats['sans_bloc'], pending['sans_bloc']), (1, 1, [('region/r.2.0.mca', 64, 0)]))

    def test_palettes_and_ticks_next_to_a_real_block_are_not_sans_bloc(self):
        real = be('command_block', 1, 2, 3, 'say ok')
        raw = nbt({'DataVersion': Int(MODERN), 'block_entities': Lst(10, [real]),
                   'sections': Lst(10, [{'block_states': Comp({'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])})}]),
                   'block_ticks': Lst(10, [{'i': Str('minecraft:command_block'), 'x': Int(1), 'y': Int(2), 'z': Int(3)}])})
        got, stats, pending, _ = self.scan(raw)
        self.assertEqual((len(got), stats['sans_bloc'], pending['sans_bloc']), (1, 0, []))

    def test_filtered_messages_only_add_a_different_command(self):
        same = comp(cmd='stop')
        sign = holder('sign', (1, 2, 3), front_text=Comp({
            'messages': Lst(10, [same, EMPTY, EMPTY, EMPTY]),
            'filtered_messages': Lst(10, [comp(cmd='stop'), comp(cmd='op X'), EMPTY, EMPTY])}))
        got, _, _, _ = self.scan(chunk(MODERN, [sign]))
        self.assertEqual(got, [('sign[front,0]', 'stop'), ('sign[front,1,filtered]', 'op X')])

    def test_book_run_command_is_neither_sans_bloc_nor_a_find(self):
        got, stats, pending, _ = self.scan(chunk(MODERN, [BOOK]))
        self.assertEqual(got, [])
        self.assertEqual((stats['sans_bloc'], pending['sans_bloc']), (0, []))
        self.assertEqual((stats['rc_hors_panneau'], pending['rc_hors_panneau']), (1, [('region/r.2.0.mca', 64, 0)]))
        self.assertEqual(F.UNREAD.count('rc_hors_panneau') + F.UNREAD.count('sans_bloc'), 0)

    def test_book_next_to_a_sign_still_flags_the_chunk(self):
        sign = holder('sign', (5, 70, 9), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        got, stats, _, _ = self.scan(chunk(MODERN, [sign, BOOK]))
        self.assertEqual((got, stats['rc_hors_panneau']), ([('sign[front,0]', 'stop')], 1))

    def test_command_block_with_click_event_is_not_outside_a_holder(self):
        click = be('command_block', 1, 2, 3, 'tellraw @a[tag=mg.flw] {"text":"x","clickEvent":{"action":"run_command","value":"/stop"}}')
        got, stats, pending, _ = self.scan(TT.chunk_blocks([click]))
        self.assertEqual(len(got), 1)
        self.assertEqual((stats['rc_hors_panneau'], pending['rc_hors_panneau']), (0, []))

    def test_command_block_palette_without_block_stays_sans_bloc_even_with_a_sign(self):
        sign = holder('sign', (5, 70, 9), **faces(front=[comp(cmd='stop'), EMPTY, EMPTY, EMPTY]))
        raw = nbt({'DataVersion': Int(MODERN), 'block_entities': Lst(10, [sign]),
                   'sections': Lst(10, [{'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])}])})
        got, stats, pending, _ = self.scan(raw)
        self.assertEqual((len(got), stats['sans_bloc'], len(pending['sans_bloc'])), (1, 1, 1))

    def test_signs_are_classified_and_reported(self):
        sign = holder('sign', (5, 70, 9), **faces(front=[EMPTY, comp(cmd='gamerule doDaylightCycle false'), EMPTY, EMPTY]))
        hanging = holder('hanging_sign', (6, 70, 9), **faces(back=[comp(cmd='tellraw @a {"text":"x"}'), EMPTY, EMPTY, EMPTY]))
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(mca([(0, chunk(MODERN, [sign, hanging]), 2)]))
        text = self.build()['report'].read_text(encoding='utf-8')
        self.assertIn('5 70 9\tsign[front,1]\t-\tgamerule\tgamerule doDaylightCycle false', text)
        self.assertIn('6 70 9\thanging_sign[back,0]\t-\tselecteur_global\ttellraw @a {"text":"x"}', text)
        self.assertIn('3 commandes du terrain (blocs, minecarts, panneaux) : 1 command_block_minecart, 1 hanging_sign, 1 sign', text)   # par type, pas par face / ligne


if __name__ == '__main__':
    unittest.main()
