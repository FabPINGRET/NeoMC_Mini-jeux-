"""tools/floaty : réécriture des lignes de la carte Scourge (fl_rewrite + fl_sel), sur des lignes en clair — la vraie carte n'est pas
nécessaire (la CI ne l'a pas). Le générateur et le lecteur NBT sont testés dans test_floaty_gen.py.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_rewrite as R  # noqa: E402

ROOTS = ['main_quest:root', 'sidequest:root', 'sidequest_2:root']


def rw(line, st=None):
    return R.rewrite_line(line, ROOTS, st)


class SelectorCase(unittest.TestCase):
    def one(self, line, want, st=None):
        self.assertEqual(rw(line, st), [want])

    def test_players_bare_and_args(self):
        self.one('tag @a add x', 'tag @a[tag=mg.flw] add x')
        self.one('tag @p add x', 'tag @p[tag=mg.flw] add x')
        self.one('tag @r add x', 'tag @r[tag=mg.flw] add x')
        self.one('scoreboard players set @a[scores={a=1..}] v 0', 'scoreboard players set @a[scores={a=1..},tag=mg.flw] v 0')
        self.one('tag @a[] add x', 'tag @a[tag=mg.flw] add x')

    def test_already_tagged_untouched(self):
        self.one('tag @a[tag=mg.flw] add x', 'tag @a[tag=mg.flw] add x')

    def test_nested_nbt_and_scores(self):
        self.one('execute as @a[distance=..10,nbt={SelectedItem:{id:"minecraft:blaze_rod"}},tag=!a] run tag @s add y',
                 'execute as @a[distance=..10,nbt={SelectedItem:{id:"minecraft:blaze_rod"}},tag=!a,tag=mg.flw] run tag @s add y')
        self.one('tag @a[nbt={Inventory:[{Slot:-106b,id:"minecraft:x"}]}]',
                 'tag @a[nbt={Inventory:[{Slot:-106b,id:"minecraft:x"}]},tag=mg.flw]')
        # virgule et crochet fermant dans une chaîne NBT : ne coupent pas le sélecteur
        self.one('tag @a[nbt={a:"x,]"}]', 'tag @a[nbt={a:"x,]"},tag=mg.flw]')

    def test_entities_get_distance(self):
        self.one('kill @e[type=item]', 'kill @e[type=item,distance=0..]')
        self.one('tp @e[type=minecraft:phantom] ~ -500 ~', 'tp @e[type=minecraft:phantom,distance=0..] ~ -500 ~')
        self.one('kill @e', 'kill @e[distance=0..]')
        self.one('execute as @n[tag=npc] run tag @s add y', 'execute as @n[tag=npc,distance=0..] run tag @s add y')
        self.one('tag @r[type=zombie] add y', 'tag @r[type=zombie,distance=0..] add y')
        # x= dans scores n'est pas positionnel
        self.one('kill @e[scores={x=1}]', 'kill @e[scores={x=1},distance=0..]')

    def test_positional_untouched(self):
        for l in ('kill @e[distance=..5]', 'kill @e[x=1,y=2,z=3,dx=4]', 'kill @e[y=319,dy=5000]', 'kill @e[tag=a,dz=1]'):
            self.one(l, l)

    def test_self_untouched(self):
        self.one('execute as @e[type=item] run kill @s', 'execute as @e[type=item,distance=0..] run kill @s')
        self.one('tag @s add x', 'tag @s add x')
        self.one('execute if entity @s[x=-1000,dx=-20000] run tag @s add y', 'execute if entity @s[x=-1000,dx=-20000] run tag @s add y')

    def test_commands_with_players(self):
        self.one('xp set @a 0 levels', 'xp set @a[tag=mg.flw] 0 levels')
        self.one('execute as @a[gamemode=survival] run gamemode adventure @s',
                 'execute as @a[gamemode=survival,tag=mg.flw] run gamemode adventure @s')
        self.one('clear @a minecraft:arrow', 'clear @a[tag=mg.flw] minecraft:arrow')
        self.one('spawnpoint @a -10441 84 429 0 0', 'spawnpoint @a[tag=mg.flw] -10441 84 429 0 0')

    def test_strings(self):
        st = R.Stats()
        # "selector" JSON : réécrit ; texte libre entre guillemets : intact
        self.one('tellraw @a [{"selector":"@p"},{"text":"mail @a"}]',
                 'tellraw @a[tag=mg.flw] [{"selector":"@p[tag=mg.flw]"},{"text":"mail @a"}]', st)
        self.assertEqual((st.sel_json, st.str_skipped), (1, 1))
        self.one('tellraw @s {"selector":"@s"}', 'tellraw @s {"selector":"@s"}')
        self.one('tag x@a add y', 'tag x@a add y')

    def test_selector_json_and_types(self):
        self.one('tellraw @s {"selector":"@e[type=item]"}', 'tellraw @s {"selector":"@e[type=item,distance=0..]"}')
        self.one('tag @p[type=player] add x', 'tag @p[type=player,tag=mg.flw] add x')
        self.one('tag @r[type=minecraft:player] add x', 'tag @r[type=minecraft:player,tag=mg.flw] add x')
        self.one('tag @p[type=zombie,distance=..5] add x', 'tag @p[type=zombie,distance=..5] add x')
        self.one('kill @n', 'kill @n[distance=0..]')
        self.one('tag @a[tag=x,] add y', 'tag @a[tag=x,tag=mg.flw] add y')      # virgule finale : pas de ",,"

    def test_macro_lines(self):
        self.assertEqual(rw('$gamerule advance_time false'), [])
        self.assertEqual(rw('$time query day'), ['$execute in mg:floaty run time query day'])
        self.assertEqual(rw('$execute as @a run schedule function boss:x 5s'), ['$execute as @a[tag=mg.flw] run schedule function floaty:sched/boss/x 5s'])
        self.assertEqual(rw('$schedule function boss:x 5s'), ['$schedule function floaty:sched/boss/x 5s'])
        self.assertEqual(rw('$advancement revoke @s everything'), [f'$advancement revoke @s from {r}' for r in ROOTS])
        self.assertEqual(rw('$tag @a add $(x)'), ['$tag @a[tag=mg.flw] add $(x)'])

    def test_unsafe_flagged(self):
        st = R.Stats()
        rw('tag it\'s @a add x', st)
        rw('tag @a[tag=x add y', st)
        self.assertEqual([w for w, _ in st.unsafe], ['chaîne non fermée', 'crochet de sélecteur déséquilibré'])

    def test_comments_and_blank_untouched(self):
        self.assertEqual(rw('#XP SET @a 0'), ['#XP SET @a 0'])
        self.assertEqual(rw(''), [''])


class CommandCase(unittest.TestCase):
    def test_author_dropped(self):
        st = R.Stats()
        self.assertEqual(rw('execute as LordDrewpicus at @s run tp @e[tag=carrying] ~ ~-2 ~', st), [])
        self.assertEqual(rw('#execute as LordDrewpicus at @s run fill ~ ~ ~ ~ ~ ~ air', st), [])
        self.assertEqual(rw('give LordDrewpicus barrel[lock={components:{"minecraft:custom_name":\'"X"\'}}] 1', st), [])
        self.assertEqual((st.dropped, st.lines), (3, 3))

    def test_fall_damage(self):
        self.assertEqual(rw('gamerule fall_damage false'), ['attribute @a[tag=mg.flw] minecraft:fall_damage_multiplier base set 0'])
        self.assertEqual(rw('gamerule fall_damage true'), ['attribute @a[tag=mg.flw] minecraft:fall_damage_multiplier base set 1'])
        self.assertEqual(rw('execute as @a run gamerule fall_damage false'),
                         ['execute as @a[tag=mg.flw] run attribute @a[tag=mg.flw] minecraft:fall_damage_multiplier base set 0'])

    def test_global_gamerules_and_time_neutralized(self):
        """gamerule global + horloge partagee avec l'overworld (prouve sur un serveur 26.2) : retires, jamais rejoues."""
        st = R.Stats()
        for l in ('gamerule advance_time false', 'gamerule advance_time true', 'gamerule random_tick_speed 0', 'time set noon', 'time add 100',
                  'execute as @p if entity @s[tag=a] run time set night', 'execute if score a b matches 1 run gamerule advance_time false'):
            self.assertEqual(rw(l, st), [], l)
        self.assertEqual(st.neutral, 7)
        self.assertEqual(st.gamerules, {'gamerule advance_time false': 2, 'gamerule advance_time true': 1, 'gamerule random_tick_speed 0': 1})

    def test_time_query_kept_in_dimension(self):
        st = R.Stats()
        self.assertEqual(rw('execute store result score T Value run time query day', st),
                         ['execute in mg:floaty store result score T Value run time query day'])
        self.assertEqual((st.times, st.neutral), (1, 0))

    def test_other_gamerule_in_dimension(self):
        st = R.Stats()
        self.assertEqual(rw('gamerule do_mob_spawning false', st), ['execute in mg:floaty run gamerule do_mob_spawning false'])
        self.assertEqual((st.neutral, st.gamerules), (0, {'gamerule do_mob_spawning false': 1}))

    def test_neutralized_in_command_block(self):
        """Command:"/time set night" d'un setblock : remplace par la commande sans effet (jamais laisse tel quel)."""
        out = rw('setblock ~ ~ ~ command_block{Command:"/time set night"}')
        self.assertEqual(len(out), 1)
        self.assertIn(R.NOOP, out[0])
        self.assertNotIn('time set', out[0])

    def test_schedule_trampoline(self):
        st = R.Stats()
        self.assertEqual(rw('schedule function boss:1/cutscene/2 6s', st), ['schedule function floaty:sched/boss/1/cutscene/2 6s'])
        self.assertEqual(rw('schedule function tool:worldgate 10t replace', st), ['schedule function floaty:sched/tool/worldgate 10t replace'])
        self.assertEqual(rw('execute unless block ^ ^ ^ air run schedule function boss:1/x 3s', st),
                         ['execute unless block ^ ^ ^ air run schedule function floaty:sched/boss/1/x 3s'])
        self.assertEqual(rw('schedule clear boss:1/x', st), ['schedule clear floaty:sched/boss/1/x'])
        self.assertEqual(st.sched, {'boss:1/cutscene/2', 'tool:worldgate', 'boss:1/x'})
        self.assertEqual(R.sched_name('boss:1/cutscene/2'), 'floaty:sched/boss/1/cutscene/2')
        self.assertEqual(R.trampoline('boss:1/x', (1274, 209, 181))[1],
                         'execute in mg:floaty positioned 1274 209 181 run function boss:1/x')
        rw('schedule function #a:b 1s', st)
        self.assertEqual([w for w, _ in st.unsafe], ['schedule inattendu'])

    def test_setdisplay_dropped(self):
        st = R.Stats()
        for slot in ('sidebar', 'list', 'below_name', 'sidebar.team.red'):
            self.assertEqual(rw(f'scoreboard objectives setdisplay {slot} Value', st), [])
        self.assertEqual(rw('execute if score a b matches 1 run scoreboard objectives setdisplay sidebar', st), [])
        self.assertEqual(rw('scoreboard objectives add Value dummy', st), ['scoreboard objectives add Value dummy'])
        self.assertEqual((st.setdisplay, len(st.unsafe)), (5, 5))

    def test_say_is_not_server_wide(self):
        st = R.Stats()
        self.assertEqual(rw('say Remember to "destroy" it!', st), ['tellraw @a[tag=mg.flw] "Remember to \\"destroy\\" it!"'])
        self.assertEqual(rw('execute if score a b matches 1 run say é\\ok', st),
                         ['execute if score a b matches 1 run tellraw @a[tag=mg.flw] "é\\\\ok"'])
        self.assertEqual((st.says, st.unsafe), (2, []))
        rw('say hi @s', st)
        self.assertEqual(len(st.unsafe), 1)

    def test_command_blocks(self):
        st = R.Stats()
        # guillemets doubles : \" et \\ déséchappés, réécrits, ré-échappés ; le / de tête est gardé
        self.assertEqual(
            rw('setblock ~ ~ ~ chest{Command:"/tellraw @a [{\\"text\\":\\"x\\"}]",auto:1b}', st),
            ['setblock ~ ~ ~ chest{Command:"/tellraw @a[tag=mg.flw] [{\\"text\\":\\"x\\"}]",auto:1b}'])
        # guillemets simples : le JSON garde ses " tels quels
        self.assertEqual(
            rw('setblock ~ ~ ~ chest{Command:\'execute as @a[distance=..10] run tellraw @s {"text":"x"}\',auto:1b}', st),
            ['setblock ~ ~ ~ chest{Command:\'execute as @a[distance=..10,tag=mg.flw] run tellraw @s {"text":"x"}\',auto:1b}'])
        self.assertEqual(rw('setblock ~ ~ ~ chest{Command:"playsound a block @a ~ ~ ~ 1 1"}', st),
                         ['setblock ~ ~ ~ chest{Command:"playsound a block @a[tag=mg.flw] ~ ~ ~ 1 1"}'])
        # commande sans effet : intacte ; échappement inconnu : intact + avertissement
        self.assertEqual(rw('setblock ~ ~ ~ chest{Command:"setblock ~ ~ ~ air"}'), ['setblock ~ ~ ~ chest{Command:"setblock ~ ~ ~ air"}'])
        self.assertEqual(rw('setblock ~ ~ ~ chest{Command:"say \\n @a"}', st), ['setblock ~ ~ ~ chest{Command:"say \\n @a"}'])
        self.assertEqual((st.blocks, [w for w, _ in st.unsafe]), (3, ['Command : échappement inconnu']))

    def test_compass_dimension(self):
        st = R.Stats()
        self.assertEqual(rw('item replace entity @s weapon.mainhand with compass[lodestone_tracker={target:{dimension:"minecraft:overworld",pos:[I;1,2,3]}}] 1', st),
                         ['item replace entity @s weapon.mainhand with compass[lodestone_tracker={target:{dimension:"mg:floaty",pos:[I;1,2,3]}}] 1'])
        self.assertEqual(st.dims, 1)

    def test_revoke_everything(self):
        want = [f'advancement revoke @a[tag=mg.flw] from {r}' for r in ROOTS]
        self.assertEqual(rw('advancement revoke @a everything'), want)
        self.assertEqual(rw('execute as @s run advancement revoke @s everything'),
                         [f'execute as @s run advancement revoke @s from {r}' for r in ROOTS])
        st = R.Stats()
        self.assertEqual(rw('advancement grant @a everything', st), ['advancement grant @a[tag=mg.flw] everything'])
        self.assertEqual(len(st.unsafe), 1)
        # un revoke ciblé n'est pas éclaté
        self.assertEqual(rw('advancement revoke @a only main_quest:quest_1'), ['advancement revoke @a[tag=mg.flw] only main_quest:quest_1'])


if __name__ == '__main__':
    unittest.main()
