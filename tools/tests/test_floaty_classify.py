"""tools/floaty : fl_terrain.classify (risques d'une commande de bloc de commande) et fl_terrain.string_selectors, sur des commandes écrites ici.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_terrain as F  # noqa: E402

G = ['selecteur_global']


class Classify(unittest.TestCase):
    CASES = [
        ('setworldspawn 1 2 3', ['setworldspawn']),
        ('/gamerule doDaylightCycle false', ['gamerule']),
        ('execute as @p run time set day', ['time', 'selecteur_global']),
        ('time add 100', ['time']), ('weather clear', ['weather']), ('difficulty peaceful', ['difficulty']),
        ('execute in minecraft:overworld run tp @s 0 64 0', ['tp_autre_dim']),
        ('execute in the_nether run teleport @s 0 64 0', ['tp_autre_dim']),
        ('execute in minecraft:the_end run setblock 0 0 0 stone', ['in_autre_dim']),
        ('execute in mg:floaty run tp @s 0 64 0', []),
        ('function minecraft:load', ['fonction_vanilla']), ('function #minecraft:tick', ['fonction_vanilla']),
        ('function floaty:boss/start', []),
        ('scoreboard objectives setdisplay sidebar Kills', ['setdisplay']),
        ('schedule function floaty:x 1s', ['schedule']), ('say hello', ['say']),
        ('tellraw @a {"text":"x"}', G), ('kill @e', G), ('give @r stone', G),
        ('tellraw @a[tag=mg.flw] {"text":"x"}', []), ('tellraw @s {"text":"the weather in the end"}', []),
        ('tp @s ~ ~1 ~', []), ('', []),
        # sélecteurs globaux (règle de fl_sel) : joueur = tag=mg.flw ; entité = position ; @s jamais
        ('kill @e[type=item]', G), ('tag @a[tag=x] add y', G),
        ('effect give @a[] speed', G), ('gamemode adventure @a[gamemode=survival]', G),
        ('kill @e[limit=1]', G), ('kill @n', G), ('kill @n[tag=npc]', G),
        ('kill @e[tag=mg.flw]', G), ('kill @a[tag=mg.flw,x=1]', []),
        ('kill @e[distance=..5]', []), ('tag @a[tag=mg.flw] add y', []),
        ('kill @n[distance=..3]', []), ('kill @s[tag=x]', []),
        ('tellraw @s {"selector":"@a"}', G), ('tellraw @s {"text":"@a"}', []),
        ('setblock ~ ~ ~ command_block{Command:"kill @e"}', G),       # commande imbriquée
        ('setblock ~ ~ ~ command_block{Command:"kill @s"}', []),
        ("say it's @a", ['say', 'selecteur_global']), ("say it's me", ['say']),           # chaîne non fermée : repli prudent
        # commandes d'administration / globales (ancrées : début de commande ou derrière run)
        ('advancement revoke @s only mg:x', ['advancement']), ('tick rate 5', ['tick']), ('tick freeze', ['tick']),
        ('worldborder set 100', ['worldborder']), ('datapack disable "file/x"', ['datapack']), ('reload', ['reload']),
        ('defaultgamemode adventure', ['defaultgamemode']), ('stop', ['stop']), ('/stop', ['stop']), ('execute as @s run stop', ['stop']),
        ('op Steve', ['admin_joueurs']), ('deop Steve', ['admin_joueurs']), ('ban Steve x', ['admin_joueurs']),
        ('kick Steve bye', ['admin_joueurs']), ('whitelist off', ['admin_joueurs']),
        ('scoreboard objectives remove kills', ['scoreboard_purge']), ('scoreboard players reset * kills', ['scoreboard_purge']),
        ('function mg:x', ['fonction_neomc']), ('function #mg:tick', ['fonction_neomc']),
        ('execute as @a[tag=mg.flw] run function mg:x', ['fonction_neomc']),
        ('scoreboard players reset @s kills', []), ('scoreboard objectives add x dummy', []), ('stopsound @s', []),
        ('scoreboard players operation @s a = @s b', []), ('tellraw @s {"text":"stop reload op tick"}', []),
        ('function floaty:x', []), ('advancement grant @s only mg:x', []),
    ]

    def check(self, cases):
        for cmd, want in cases:
            with self.subTest(cmd):
                self.assertEqual(F.classify(cmd), want)

    def test_cases(self):
        self.check(self.CASES)

    def test_nested_command_strings_are_classified(self):
        self.check([
            ('setblock ~ ~ ~ command_block{Command:"gamerule doDaylightCycle true",auto:1b}', ['gamerule']),
            ('summon command_block_minecart ~ ~ ~ {Command:"stop"}', ['stop']),
            ('data merge block ~ ~ ~ {Command:"op X"}', ['admin_joueurs']),
            ("data merge block ~ ~ ~ {Command:'time set day'}", ['time']),                       # chaîne entre apostrophes
            ('setblock ~ ~ ~ command_block{Command:"kill @e[type=item]",auto:1b}', G),
            (r'setblock ~ ~ ~ command_block{Command:"tellraw @s {\"selector\":\"@e\"}"}', G),        # échappée : @e dans un selector JSON
            (r'setblock ~ ~ ~ command_block{Command:"tellraw @s {\"text\":\"run stop\"}"}', []),     # texte, pas un stop
            (r'setblock ~ ~ ~ {Command:"setblock ~ ~ ~ {Command:\"weather clear\"}"}', ['weather']),    # deux niveaux
            ('setblock ~ ~ ~ command_block{Command:"time set day"} run op X', ['time', 'admin_joueurs']),
        ])

    def test_union_is_sorted_and_deduplicated(self):
        got = F.classify('setblock ~ ~ ~ {Command:"time set day"} run time set night')
        self.assertEqual(got, ['time'])
        got = F.classify('execute as @a run setblock ~ ~ ~ {Command:"stop"}')
        self.assertEqual(got, ['stop', 'selecteur_global'])               # du plus grave au moins grave

    def test_tellraw_text_is_not_a_command(self):
        self.check([
            ('tellraw @a[tag=mg.flw] {"text":"run stop"}', []),
            ('tellraw @a[tag=mg.flw] {"text":"run op Steve and run reload"}', []),
            ('tellraw @a[tag=mg.flw] {"text":"x","clickEvent":{"action":"run_command","value":"/stop"}}', []),
            ('tellraw @a[tag=!mg.flw] {"text":"x"}', G),                  # tag négatif : pas le tag requis
        ])

    def test_selector_rule_follows_fl_sel(self):
        self.check([
            ('kill @a[limit=1,tag=mg.flw,sort=random]', []),
            ('execute as @e[type=zombie] at @s run tp @s ~ ~1 ~', G),
            ('/kill @e', G),
            ('kill @e[type=x', G),                                        # crochet non fermé : repli prudent
            ('kill @r[type=zombie,tag=mg.flw]', G),                       # @r d'un autre type = entité : le tag ne borne rien
            ('kill @r[type=zombie,distance=..3]', []),
            ('kill @p[type=player,tag=mg.flw]', []),
        ])

    def test_player_selectors_need_the_tag_even_with_a_position(self):
        # fl_sel (L1) marque tout joueur d'un tag=mg.flw : une position seule ne borne pas @a (classement prudent, documenté)
        self.check([
            ('tp @a[x=0,y=0,z=0,dx=5] ~ ~ ~', G), ('tag @a[distance=..5] add y', G), ('tag @a[tag=x,distance=0..] add y', G),
            ('tp @a[tag=mg.flw,x=0,y=0,z=0,dx=5] ~ ~ ~', []),
        ])

    def test_function_without_namespace_is_vanilla(self):
        self.check([('function load', ['fonction_vanilla']), ('function #tick', ['fonction_vanilla']),
                    ('execute as @s run function load', ['fonction_vanilla']), ('function #floaty:tick', []),
                    ('function load_all', ['fonction_vanilla'])])

    def test_new_categories(self):
        self.check([
            ('save-off', ['sauvegarde']), ('save-on', ['sauvegarde']), ('save-all flush', ['sauvegarde']),
            ('execute as @s run save-all', ['sauvegarde']),
            ('setidletimeout 0', ['admin_serveur']), ('debug start', ['admin_serveur']), ('jfr start', ['admin_serveur']),
            ('perf start', ['admin_serveur']), ('perfect', []), ('debugger', []),
            ('pardon Steve', ['admin_joueurs']), ('pardon-ip 1.2.3.4', ['admin_joueurs']), ('ban-ip 1.2.3.4', ['admin_joueurs']),
        ])

    def test_trampoline_schedule_is_not_a_risk(self):
        self.check([
            ('schedule function floaty:sched/a/b 1s', []), ('schedule clear floaty:sched/a/b', []),
            ('schedule function floaty:boss/x 1s', ['schedule']), ('schedule function mg:sched/x 1s', ['schedule']),
        ])

    def test_apostrophe_outside_quotes_does_not_hide_the_rest_of_the_line(self):
        self.check([
            ("execute if score l'ile obj matches 1 run stop", ['stop']),
            ("execute if score l'ile obj matches 1 in minecraft:overworld run setblock 0 0 0 stone", ['in_autre_dim']),
            ("execute if score l'ile obj matches 1 run kill @e", G),
            ("execute if score l'ile obj matches 1 run say ok", ['say']),
            ("execute if score l'ile obj matches 1 run tellraw @s {\"text\":\"run stop\"}", ['stop']),      # repli prudent : le texte brut est examiné aussi
            ("execute if score l'ile obj matches 1 run tellraw @s {\"text\":\"ok\"}", []),
            ("setblock ~ ~ ~ {Command:\"execute if score l'ile o matches 1 run stop\"}", ['stop']),      # même repli dans un niveau imbriqué
            ("setblock ~ ~ ~ {Command:\"say it's @a\"}", ['say', 'selecteur_global']),
        ])

    def test_function_conditions_are_risks(self):
        self.check([
            ('execute if function minecraft:x run say hi', ['fonction_vanilla', 'say']),
            ('execute unless function load run say hi', ['fonction_vanilla', 'say']),
            ('execute unless function mg:x run say hi', ['fonction_neomc', 'say']),
            ('execute if function floaty:x run say hi', ['say']),
            ('execute if entity @s[tag=function] run say hi', ['say']),
        ])

    def test_command_set_value_is_a_nested_level(self):
        self.check([
            ('data modify block ~ ~ ~ Command set value "stop"', ['stop']),
            ("data modify block ~ ~ ~ Command set value 'op X'", ['admin_joueurs']),
            ('data modify block ~ ~ ~ Command set value "kill @e"', G),
            ('data modify block ~ ~ ~ Command set value "say hi"', ['say']),
            ('data modify block ~ ~ ~ CustomName set value "stop"', []),
        ])
        self.assertEqual(F.string_selectors('data modify block ~ ~ ~ Command set value "kill @e"'), 0)        # examiné : plus « non examiné »
        self.assertEqual(F.string_selectors('data modify block ~ ~ ~ CustomName set value "@e"'), 1)

    def test_lenient_unescape_fallback(self):
        self.check([
            (r'setblock ~ ~ ~ {Command:"stop\n"}', ['stop']),                                  # \n : séquence inconnue de fl_rewrite.unescape
            ('setblock ~ ~ ~ {Command:"op X' + chr(92) + 'u0021"}', ['admin_joueurs']),                # \u : idem (antislash construit : chr(92))
            (r'setblock ~ ~ ~ {Command:"say a\nkill @e"}', ['say', 'selecteur_global']),
        ])

    def test_risk_names_are_unique_and_ordered(self):
        self.assertEqual(len(set(F.RISK_NAMES)), len(F.RISK_NAMES))
        self.assertLess(F.RISK_NAMES.index('stop'), F.RISK_NAMES.index('sauvegarde'))
        self.assertLess(F.RISK_NAMES.index('admin_serveur'), F.RISK_NAMES.index('admin_joueurs'))


class StringSelectors(unittest.TestCase):
    def test_counts_selectors_left_in_strings(self):
        for cmd, want in [('tellraw @s {"text":"@a"}', 1), ('tellraw @s {"selector":"@a"}', 0), ('say hi', 0), ('', 0),
                          ('tellraw @s [{"text":"@a"},{"text":"@e"}]', 2),
                          (r'setblock ~ ~ ~ {Command:"tellraw @s {\"text\":\"@e\"}"}', 1),             # dans une commande imbriquée
                          (r'setblock ~ ~ ~ {Command:"tellraw @s {\"selector\":\"@e\"}"}', 0),
                          ('tellraw @s {"text":"mail@a.b"}', 0)]:
            with self.subTest(cmd):
                self.assertEqual(F.string_selectors(cmd), want)


if __name__ == '__main__':
    unittest.main()
