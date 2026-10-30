"""tools/floaty : fl_terrain_cmd.rewrite_command (règles de réécriture d'UNE commande du terrain : un cas par règle, et le cas inverse).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'floaty'))
import fl_rewrite as R  # noqa: E402
import fl_sel  # noqa: E402
import fl_terrain as F  # noqa: E402
import fl_terrain_cmd as C  # noqa: E402

NOOP = R.NOOP


class Rules(unittest.TestCase):
    def setUp(self):
        self.ctx = C.Ctx()

    def rw(self, cmd):
        return C.rewrite_command(cmd, self.ctx)

    def test_gamerule_snake_and_camel_are_never_left(self):
        for cmd, why in (('gamerule doDaylightCycle false', 'risque_dur'), ('gamerule keepInventory true', 'risque_dur'),
                         ('gamerule advance_time false', 'retiree'), ('gamerule random_tick_speed 3', 'retiree'),
                         ('gamerule randomTickSpeed 3', 'risque_dur')):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (NOOP, 'noop', why))
        new, action, _ = self.rw('gamerule fall_damage false')                       # inverse : réécrit par L1, pas un NOOP
        self.assertEqual((new, action), ('execute as @a[tag=mg.flw] run attribute @s minecraft:fall_damage_multiplier base set 0', 'reecrit'))

    def test_time_set_is_noop_and_time_query_is_kept(self):
        self.assertEqual(self.rw('time set day'), (NOOP, 'noop', 'retiree'))
        new, action, _ = self.rw('time query daytime')                                      # inverse : lecture seule, gardée (pas un NOOP)
        self.assertEqual((action, 'time query daytime' in new), ('reecrit', True))

    def test_say_becomes_tellraw_and_say_with_selector_is_left(self):
        self.assertEqual(self.rw('say hello'), ('tellraw @a[tag=mg.flw] "hello"', 'reecrit', None))
        self.assertEqual(self.rw('say @a hi'), (None, 'laisse', 'non_analysable'))            # inverse : impossible de dire ce qui est du texte

    def test_schedule_keeps_the_trampoline_name_and_records_the_target(self):
        self.assertEqual(self.rw('schedule function boss:1/x 10t'), ('schedule function floaty:sched/boss/1/x 10t', 'reecrit', None))
        self.assertEqual(self.ctx.sched['schedule function boss:1/x 10t'], frozenset({'boss:1/x'}))
        self.assertEqual(self.rw('tellraw @a "x"')[1], 'reecrit')
        self.assertEqual(self.ctx.sched['tellraw @a "x"'], frozenset())                     # inverse : pas de cible hors d'un schedule

    def test_schedule_ids_with_dot_dot_or_empty_segments_are_refused(self):
        for cmd in ('schedule function a:../b 1t', 'schedule function a:b//c 1t', 'schedule function a:b/ 1t', 'schedule function a:/b 1t',
                    'schedule function a:./b 1t', 'schedule function ..:b 1t', 'schedule function a:b/.. 1t', 'schedule clear a:../b', 'schedule function a:b. 1t',
                    'schedule function a:b./c 1t', 'schedule clear a.:b'):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (None, 'laisse', 'non_analysable'))
                self.assertEqual(self.ctx.sched[cmd], frozenset())                          # aucun trampoline demandé
        self.assertEqual(self.rw('schedule function a.b:c.d/e-f_1 1t')[1:], ('reecrit', None))      # inverse : points, tirets, traits bas dans un segment
        for fn, ok in (('boss:1/x', True), ('a:..b', True), ('a:b..', False), ('a:b./c', False), ('a.:b', False), ('a:b.', False), ('a:b.c', True), ('a:..', False), ('a:', False), ('nocolon', False), (':x', False)):
            with self.subTest(fn):
                self.assertEqual(R.valid_function_id(fn), ok)

    def test_player_selectors_are_confined(self):
        for cmd, want in (('tellraw @a {"text":"x"}', 'tellraw @a[tag=mg.flw] {"text":"x"}'), ('tp @a 0 0 0', 'tp @a[tag=mg.flw] 0 0 0'),
                          ('playsound x master @a', 'playsound x master @a[tag=mg.flw]'),
                          ('spawnpoint @a 1 2 3', 'spawnpoint @a[tag=mg.flw] 1 2 3'),
                          ('advancement grant @a only a:b', 'advancement grant @a[tag=mg.flw] only a:b')):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (want, 'reecrit', None))
        self.assertEqual(self.rw('tellraw @a[tag=mg.flw] "x"')[1], 'inchange')              # inverse : déjà confiné, pas de second tag

    def test_entity_selector_gets_a_distance_and_the_slash_is_kept(self):
        self.assertEqual(self.rw('kill @e[type=zombie]'), ('kill @e[type=zombie,distance=0..]', 'reecrit', None))
        self.assertEqual(self.rw('/tellraw @a "x"'), ('/tellraw @a[tag=mg.flw] "x"', 'reecrit', None))
        self.assertEqual(self.rw('/time set day'), ('/' + NOOP, 'noop', 'retiree'))
        self.assertEqual(self.rw('/scoreboard players add x y 1'), (None, 'inchange', None))

    def test_author_lines_are_removed(self):
        self.assertEqual(self.rw('say hi LordDrewpicus'), (NOOP, 'noop', 'auteur'))
        self.assertEqual(self.rw('tellraw @a "bonjour"')[1], 'reecrit')                     # inverse : le texte courant n'est pas « auteur »

    def test_nested_commands_are_rewritten_and_reclassified(self):
        new, action, _ = self.rw('setblock 1 2 3 command_block{Command:"say hi"}')
        self.assertEqual((new, action), ('setblock 1 2 3 command_block{Command:"tellraw @a[tag=mg.flw] \\"hi\\""}', 'reecrit'))
        self.assertEqual(self.rw('setblock 1 2 3 command_block{Command:"gamerule keepInventory true"}'), (NOOP, 'noop', 'risque_dur'))
        self.assertEqual(self.rw('setblock 1 2 3 stone')[1], 'inchange')                    # inverse : sans Command:, rien à reclasser

    def test_unanalysable_is_left_and_with_a_hard_risk_becomes_noop(self):
        self.assertEqual(self.rw('tellraw @a "unclosed'), (None, 'laisse', 'non_analysable'))
        for cmd in ("execute if score l'ile a matches 1 run gamerule doFireTick false", 'stop', 'weather clear'):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (NOOP, 'noop', 'risque_dur'))
        self.assertEqual(self.rw("execute if score l'ile a matches 1 run say"), (None, 'laisse', 'non_analysable'))        # inverse : sans risque dur

    def test_advancement_everything_is_a_noop_for_any_selector(self):
        for cmd in ('advancement revoke @a everything', 'advancement grant @p everything', 'advancement revoke @s everything',
                    'advancement grant @s everything', 'advancement revoke LordTest everything', 'advancement grant @a[tag=x] everything',
                    'execute as @a run advancement revoke @s everything', 'advancement revoke @a[tag=x everything'):       # même crochet non fermé
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (NOOP, 'noop', 'eclate'))
        self.assertEqual(self.rw('/advancement grant @s everything'), ('/' + NOOP, 'noop', 'eclate'))
        self.assertEqual(self.rw('advancement revoke @a only a:b')[1:], ('reecrit', None))             # inverse : seulement `everything` est un NOOP
        self.assertEqual(self.rw('advancement grant @s from a:b')[1:], ('inchange', None))             # inverse : @s sans `everything` : intact

    def test_nested_advancement_everything_is_a_noop_too(self):
        for cmd in ('setblock 1 2 3 command_block{Command:"advancement grant @p everything"}',             # Command:"..." imbriquée
                    '/setblock 1 2 3 command_block{Command:"advancement revoke @s everything"}',
                    'data modify block ~ ~ ~ Command set value "advancement grant @p everything"',        # Command set value "..."
                    'summon command_block_minecart ~ ~ ~ {Command:"execute as @a run advancement grant @s everything"}',
                    'setblock 1 2 3 command_block{Command:"setblock 4 5 6 command_block{Command:\\"advancement grant @p everything\\"}"}'):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (('/' if cmd.startswith('/') else '') + NOOP, 'noop', 'eclate'))
        for cmd in ('setblock 1 2 3 command_block{Command:"tellraw @a \\"advancement grant x everything\\""}',      # inverse : texte d'un tellraw imbriqué
                    'data modify block ~ ~ ~ Command set value "tellraw @a \\"advancement grant x everything\\""',
                    'setblock 1 2 3 command_block{Command:"advancement grant @p only a:b"}', 'say advancement grant x everything'):
            with self.subTest(cmd):
                self.assertNotEqual(self.rw(cmd)[1:], ('noop', 'eclate'))
        self.assertEqual(self.rw('say advancement grant x everything')[1:], ('reecrit', None))         # inverse : un `say` n'est pas une commande advancement
        self.assertEqual(self.rw('setblock 1 2 3 command_block{Command:"say advancement grant x everything"}')[1:], ('reecrit', None))

    def test_author_rule_comes_before_everything(self):
        self.assertEqual(self.rw('advancement grant LordDrewpicus everything'), (NOOP, 'noop', 'auteur'))
        self.assertEqual(self.rw('/advancement revoke LordDrewpicus everything'), ('/' + NOOP, 'noop', 'auteur'))
        self.assertEqual(self.rw('advancement grant LordDrewpickle everything'), (NOOP, 'noop', 'eclate'))      # inverse : un autre pseudo est `eclate`
        self.assertEqual(self.rw('tellraw @a "LordDrewpicus"')[1], 'reecrit')                       # inverse : l'auteur dans une chaîne est du texte

    def test_everything_inside_a_string_is_not_an_advancement_everything(self):
        new, action, why = self.rw('tellraw @a "advancement grant x everything"')              # inverse du motif : dans une chaîne, réécrit normalement
        self.assertEqual((new, action, why), ('tellraw @a[tag=mg.flw] "advancement grant x everything"', 'reecrit', None))
        new, action, why = self.rw('say hello grant x everything')
        self.assertEqual((action, why), ('reecrit', None))
        self.assertTrue(new.startswith('tellraw @a[tag=mg.flw] '))

    def test_leading_whitespace_before_the_slash(self):
        self.assertEqual(self.rw(' /time set day'), ('/' + NOOP, 'noop', 'retiree'))
        self.assertEqual(self.rw('  /tellraw @a "x"'), ('/tellraw @a[tag=mg.flw] "x"', 'reecrit', None))
        self.assertEqual(self.rw('\t/scoreboard players add x y 1')[1], 'inchange')
        self.assertEqual(self.rw('time set day'), (NOOP, 'noop', 'retiree'))                       # inverse : sans espace ni barre, comme avant

    def test_other_dimension_is_a_hard_risk(self):
        for cmd in ('execute in minecraft:overworld run kill @e[type=item]', 'execute in minecraft:the_nether run setblock 1 2 3 stone',
                    'execute in minecraft:the_end run tp @a 0 0 0', 'tp @a 0 0 0 in minecraft:overworld'):      # sans dimension source connue
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (NOOP, 'noop', 'risque_dur'))
        self.assertEqual(self.rw('execute in mg:floaty run kill @e[type=item]')[1], 'reecrit')   # inverse : la dimension de Floaty reste permise

    def test_source_dimension_becomes_mg_floaty_and_other_dimensions_stay_noop(self):
        ctx = C.Ctx('minecraft:overworld')
        for cmd, want in (('execute in minecraft:overworld run kill @e[type=item]', 'execute in mg:floaty run kill @e[type=item,distance=0..]'),
                          ('/execute in minecraft:overworld run kill @e[type=item]', '/execute in mg:floaty run kill @e[type=item,distance=0..]'),
                          ('execute in overworld run kill @e[type=item]', 'execute in mg:floaty run kill @e[type=item,distance=0..]'),
                          ('execute in minecraft:overworld run tp @a 0 0 0', 'execute in mg:floaty run tp @a[tag=mg.flw] 0 0 0'),
                          ('execute in minecraft:overworld in minecraft:overworld run say hi',
                           'execute in mg:floaty in mg:floaty run tellraw @a[tag=mg.flw] "hi"'),
                          ('setblock 1 2 3 command_block{Command:"execute in minecraft:overworld run say hi"}',
                           'setblock 1 2 3 command_block{Command:"execute in mg:floaty run tellraw @a[tag=mg.flw] \\"hi\\""}')):
            with self.subTest(cmd):
                self.assertEqual(C.rewrite_command(cmd, ctx), (want, 'reecrit', None))
        for cmd in ('execute in minecraft:the_nether run kill @e[type=item]', 'execute in the_end run tp @a 0 0 0',
                    'execute in minecraft:overworld run execute in minecraft:the_nether run setblock 1 2 3 stone',
                    'execute in minecraft:overworld_caves run setblock 1 2 3 stone', 'execute in minecraft:overworld/x run setblock 1 2 3 stone'):
            with self.subTest(cmd):                                                                  # inverse : une AUTRE dimension reste un NOOP
                self.assertEqual(C.rewrite_command(cmd, ctx), (NOOP, 'noop', 'risque_dur'))
        text = 'tellraw @a "in minecraft:overworld"'                                                 # inverse : dans une chaîne, c'est du texte
        self.assertEqual(C.rewrite_command(text, ctx), ('tellraw @a[tag=mg.flw] "in minecraft:overworld"', 'reecrit', None))
        self.assertEqual(ctx.fx['execute in minecraft:overworld run tp @a 0 0 0']['dim'], 1)
        nether = C.Ctx('minecraft:the_nether')                                                      # la dimension source se configure
        self.assertEqual(C.rewrite_command('execute in the_nether run say hi', nether)[0], 'execute in mg:floaty run tellraw @a[tag=mg.flw] "hi"')
        self.assertEqual(C.rewrite_command('execute in minecraft:overworld run say hi', nether)[2], 'risque_dur')
        self.assertEqual(C.rewrite_command('execute in minecraft:overworld run kill @e[type=item]', C.Ctx()),
                         (NOOP, 'noop', 'risque_dur'))                                              # inverse : sans dimension source, rien n'est ramené

    def test_free_text_of_message_commands_is_neither_rewritten_nor_a_risk(self):
        ctx = C.Ctx('minecraft:overworld')
        for cmd in ('tell @s go back in overworld', 'msg @s go back in overworld', 'w @s back in overworld', 'me back in overworld',
                    'teammsg back in overworld', 'tm back in overworld', 'msg @s go in minecraft:the_nether', 'msg @s go run in overworld',
                    '/msg @s back in overworld', 'execute as @a run msg @s back in minecraft:the_end'):
            with self.subTest(cmd):                                  # pas de `in mg:floaty` dans le texte, et pas de risque dur (sinon NOOP)
                self.assertEqual(C.rewrite_command(cmd, ctx)[1:], ('reecrit' if 'execute' in cmd else 'inchange', None))
        self.assertEqual(C.rewrite_command('msg @p go back in overworld', ctx), ('msg @p[tag=mg.flw] go back in overworld', 'reecrit', None))
        self.assertEqual(C.rewrite_command('execute in overworld run msg @s back in overworld', ctx),     # inverse : l'`in` AVANT le msg est une dimension
                         ('execute in mg:floaty run msg @s back in overworld', 'reecrit', None))
        self.assertEqual(C.rewrite_command('execute in the_nether run msg @s hi', ctx), (NOOP, 'noop', 'risque_dur'))     # inverse : autre dimension
        self.assertEqual(F.classify('msg @s go back in overworld'), [])
        self.assertEqual(F.classify('execute in minecraft:the_nether run msg @s hi in the_end'), ['in_autre_dim'])
        self.assertEqual(F.classify("msg @s it's in overworld"), [])                     # chaîne non fermée : le repli sur le texte brut ne l'attrape pas non plus
        self.assertEqual(F.classify('tellraw @s {"text":"x"}'), [])                       # inverse : `tell` suivi d'une lettre n'est pas une commande de message

    def test_if_unless_dimension_follows_the_source_dimension_and_is_never_a_risk(self):
        ctx = C.Ctx('minecraft:overworld')
        for cmd, want in (('execute if dimension minecraft:overworld run say hi', 'execute if dimension mg:floaty run tellraw @a[tag=mg.flw] "hi"'),
                          ('execute unless dimension overworld run kill @e[type=item]', 'execute unless dimension mg:floaty run kill @e[type=item,distance=0..]'),
                          ('execute in overworld if dimension overworld run say hi',
                           'execute in mg:floaty if dimension mg:floaty run tellraw @a[tag=mg.flw] "hi"')):
            with self.subTest(cmd):
                self.assertEqual(C.rewrite_command(cmd, ctx), (want, 'reecrit', None))
        for cmd, want in (('execute if dimension minecraft:the_nether run say hi', 'execute if dimension minecraft:the_nether run tellraw @a[tag=mg.flw] "hi"'),
                          ('execute unless dimension my_dim run scoreboard players add x y 1', None)):
            with self.subTest(cmd):                                  # inverse : un TEST sur une autre dimension : intact, jamais un NOOP
                self.assertEqual(C.rewrite_command(cmd, ctx), (want, 'reecrit' if want else 'inchange', None))
        self.assertEqual(C.rewrite_command('execute if dimension overworld run scoreboard players add x y 1', C.Ctx())[1:], ('inchange', None))   # sans source
        self.assertEqual(F.classify('execute if dimension minecraft:the_nether run scoreboard players add x y 1'), [])
        self.assertEqual(ctx.fx['execute unless dimension overworld run kill @e[type=item]']['dim'], 1)

    def test_any_dimension_id_with_or_without_namespace_is_another_dimension(self):
        for cmd in ('execute in my_dim run setblock 1 2 3 stone', 'execute in the_nether run setblock 1 2 3 stone', 'execute in a.b-c:d/e run setblock 1 2 3 stone',
                    'execute in floaty run setblock 1 2 3 stone', 'execute in minecraft:my_dim run tp @a 0 0 0'):
            with self.subTest(cmd):
                self.assertEqual(self.rw(cmd), (NOOP, 'noop', 'risque_dur'))
        self.assertEqual(self.rw('execute in mg:floaty run setblock 1 2 3 stone')[1:], ('inchange', None))        # inverse : la dimension de Floaty
        self.assertEqual(F.classify('execute in my_dim run tp @s 0 0 0'), ['tp_autre_dim'])
        self.assertEqual(F.classify('execute in my_dim2 run scoreboard players add x y 1'), ['in_autre_dim'])     # chiffres et traits bas : un id de dimension
        self.assertEqual(F.classify('execute in my_dimX run scoreboard players add x y 1'), [])                    # majuscule : pas un id valide, aucun id partiel
        self.assertEqual(F.classify('execute in Overworld run scoreboard players add x y 1'), [])
        self.assertEqual(F.classify('scoreboard players set #in mg.st 1'), [])                                    # `#in` : un nom de joueur fictif, pas le mot `in`

    def test_compass_target_follows_the_source_dimension(self):
        give = 'give @s compass[lodestone_tracker={target:{dimension:"%s",pos:[1,2,3]}}] 1'
        old, new = give % 'minecraft:overworld', give % 'mg:floaty'
        self.assertEqual(C.rewrite_command(old, C.Ctx('minecraft:overworld')), (new, 'reecrit', None))
        self.assertEqual(C.rewrite_command(give % 'overworld', C.Ctx('minecraft:overworld')), (new, 'reecrit', None))
        self.assertEqual(C.rewrite_command(give % 'minecraft:the_nether', C.Ctx('minecraft:the_nether')), (new, 'reecrit', None))
        self.assertEqual(C.rewrite_command(old, C.Ctx('minecraft:the_nether'))[1:], ('inchange', None))        # inverse : l'overworld n'est pas la source
        self.assertEqual(C.rewrite_command(old, C.Ctx()), (new, 'reecrit', None))                                # sans source : comme L1 (overworld)
        self.assertEqual(R.rewrite_line(old, []), [new])                                                       # L1 (gen_floaty) : inchangé

    def test_setdisplay_is_removed_and_not_unsafe(self):
        self.assertEqual(self.rw('scoreboard objectives setdisplay sidebar x'), (NOOP, 'noop', 'setdisplay'))

    def test_sub_outside_leaves_strings_alone_and_text_start_finds_free_text(self):
        rx, repl = R.source_dim('minecraft:overworld').rx_in, r'\1 mg:floaty'
        for text in ('tellraw @a "a \\" in overworld"', "tellraw @a 'it''s in overworld'", 'tellraw @a "x in overworld'):
            with self.subTest(text):                                                  # guillemet échappé, '' collées, chaîne non fermée : intacts
                self.assertEqual(fl_sel.sub_outside(rx, repl, text), (text, 0))
        self.assertEqual(fl_sel.sub_outside(rx, repl, 'execute positioned 0 0 0 in minecraft:overworld run kill @e[type=item]'),
                         ('execute positioned 0 0 0 in mg:floaty run kill @e[type=item]', 1))
        self.assertEqual(C.rewrite_command('execute positioned 0 0 0 in minecraft:overworld run kill @e[type=item]', C.Ctx('minecraft:overworld'))[0],
                         'execute positioned 0 0 0 in mg:floaty run kill @e[type=item,distance=0..]')
        for text, want in (('msg @s a', 0), ('execute as @a run msg @s a', 18), ('$msg @s a', 1), ('/tell x', 1), ('execute run tellraw @a "x"', 26),
                           ('say hi', 6), ('execute as @a run tm x run tell y', 18), ('time set day', 12)):
            with self.subTest(text):
                self.assertEqual(fl_sel.text_start(text), want)

    def test_hard_list_matches_the_classifier_names(self):
        self.assertTrue(C.HARD <= set(F.RISK_NAMES))
        self.assertFalse({'selecteur_global', 'say', 'schedule'} & C.HARD)

    def test_cache_per_distinct_command(self):
        a = self.rw('say hello')
        self.assertIs(self.rw('say hello'), a)
        self.assertEqual(len(self.ctx.cache), 1)
        self.assertEqual(self.ctx.fx['say hello']['say'], 1)


if __name__ == '__main__':
    unittest.main()
