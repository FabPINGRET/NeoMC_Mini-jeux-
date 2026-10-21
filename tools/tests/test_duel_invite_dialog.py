"""Duel sniper : fenêtre d'invitation de l'invité (dialog inline) + ligne de chat de secours, réouverture (trigger 6), « Plus tard » (7),
et invariants du tag mg.dlui (fenêtre ouverte) sur data/mg/function/duel/*.mcfunction.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
DUEL = sorted((FUNC / 'duel').glob('*.mcfunction'))
SHOW = 'function mg:duel/inv_show'
INV_END = 'function mg:duel/inv_end'
UNTAG = 'tag @s remove mg.dlui'


def lines(rel):
    return (FUNC / (rel + '.mcfunction')).read_text(encoding='utf-8').splitlines()


def code(rel):
    return [l for l in lines(rel) if l and not l.startswith('#')]


def commands(node):
    """Toutes les commandes run_command d'une fenêtre (boutons et exit_action)."""
    found = []
    if isinstance(node, dict):
        if node.get('type') == 'minecraft:run_command':
            found.append(node['command'])
        for v in node.values():
            found += commands(v)
    elif isinstance(node, list):
        for v in node:
            found += commands(v)
    return found


def duel_code():
    """(nom de fonction, lignes de code) de chaque fonction du dossier duel."""
    return [(p.stem, [l for l in p.read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')]) for p in DUEL]


class Window(unittest.TestCase):
    def test_inv_dlg_is_valid_inline_dialog(self):
        body = code('duel/inv_dlg')
        self.assertEqual(len(body), 1)
        self.assertTrue(body[0].startswith('$dialog show @s {'))
        self.assertEqual(body[0].count('$(p)'), 1, 'le pseudo du défieur est l\'unique trou de macro')
        self.assertNotIn('@@', body[0])
        dlg = json.loads(body[0][len('$dialog show @s '):].replace('$(p)', 'X'))
        self.assertEqual(dlg['type'], 'minecraft:multi_action')
        self.assertIs(dlg['pause'], False)
        self.assertIs(dlg['can_close_with_escape'], True)
        self.assertEqual(sorted(commands(dlg)), ['trigger mg.duel set 2', 'trigger mg.duel set 3', 'trigger mg.duel set 7'])
        self.assertEqual(dlg['exit_action']['action']['command'], 'trigger mg.duel set 7')

    def test_inv_show_marks_window_then_opens_it(self):
        show = code('duel/inv_show')
        mark = [i for i, l in enumerate(show) if l == 'tag @s add mg.dlui']
        opens = [i for i, l in enumerate(show) if l.startswith('function mg:duel/inv_dlg with storage mg:duel inv')]
        self.assertEqual((len(mark), len(opens)), (1, 1))
        self.assertLess(mark[0], opens[0])
        self.assertTrue(any('Un joueur' in l for l in show), 'pseudo de repli')
        name = code('duel/inv_name')
        self.assertTrue(any('profile' in l and 'mg:duel inv.p' in l for l in name))
        self.assertTrue(any(l.startswith('kill @e[type=minecraft:item_display') for l in name), 'l\'item_display temporaire est tué')

    def test_challenge_sends_chat_line_and_opens_window(self):
        chk = code('duel/challenge_chk')
        line = [l for l in chk if l.startswith('tellraw @a[tag=mg.dltg,limit=1]')]
        self.assertEqual(len(line), 1)
        for n in (2, 3, 6):
            self.assertIn(f'trigger mg.duel set {n}', line[0])
        show = [i for i, l in enumerate(chk) if SHOW in l]
        self.assertEqual(len(show), 1)
        self.assertIn('tag=mg.dltg', chk[show[0]])
        self.assertIn('tag=!mg.rate', chk[show[0]], 'pas de fenêtre d\'office pendant la note de fin de partie')
        self.assertLess(chk.index('tag @s add mg.dlrq'), show[0])

    def test_pending_keeps_chat_line_and_reopens_window(self):
        pend = code('duel/pending')
        self.assertTrue(any(l.startswith('tellraw @s') and 'set 2' in l and 'set 3' in l for l in pend))
        self.assertEqual(pend[-1], SHOW)
        for rel in ('duel/list', 'duel/challenge_chk'):
            self.assertTrue(any(l.endswith('return run function mg:duel/pending') for l in code(rel)), rel)


class Invariants(unittest.TestCase):
    def test_every_invitation_end_clears_window_tag(self):
        """Toute fonction qui remet mg.dlto à zéro (hors setup : le duel démarre, inv_end est déjà passé) retire mg.dlui."""
        seen = []
        for name, fn in duel_code():
            if name == 'setup' or 'scoreboard players reset @s mg.dlto' not in fn:
                continue
            seen.append(name)
            self.assertTrue(UNTAG in fn or INV_END in fn, f'duel/{name} : invitation terminée sans retirer mg.dlui')
        self.assertTrue({'expire', 'refuse', 'cancel_t', 'inv_end', 'reconnect'} <= set(seen), seen)

    def test_dialog_clear_only_for_our_window(self):
        clears = [(name, l) for name, fn in duel_code() for l in fn if 'dialog clear' in l]
        for name, l in clears:
            ours = l.startswith('execute if entity @s[tag=mg.dlui] run dialog clear')
            self.assertTrue(ours or l == 'execute as @a[tag=mg.dlui] run dialog clear @s', f'duel/{name} : {l}')
        self.assertEqual(sorted(n for n, _ in clears), ['cancel_t', 'expire', 'refuse', 'remove'])

    def test_dialog_clear_followed_by_untag(self):
        for rel in ('duel/expire', 'duel/refuse', 'duel/cancel_t'):
            fn = code(rel)
            clear = [i for i, l in enumerate(fn) if 'dialog clear' in l]
            self.assertEqual(len(clear), 1, rel)
            self.assertEqual(fn[clear[0] + 1], UNTAG, rel)

    def test_failed_and_started_invitations_go_through_inv_end(self):
        for name in ('fail_gone', 'fail_busy', 'fail_map', 'start'):
            self.assertIn(INV_END, code(f'duel/{name}'), name)

    def test_reconnect_and_remove_clean_up(self):
        self.assertIn(UNTAG, code('duel/reconnect'))
        self.assertIn('tag @a remove mg.dlui', code('duel/remove'))
        self.assertIn('data remove storage mg:duel inv', code('duel/remove'))


class Tick(unittest.TestCase):
    def test_rating_window_drops_the_tag(self):
        """(a) la note de fin de partie (mg.rate) remplace notre fenêtre : mg.dlui est retiré, sans dialog clear."""
        tick = code('duel/tick')
        self.assertEqual(tick.count('tag @a[tag=mg.dlui,tag=mg.rate] remove mg.dlui'), 1)
        self.assertFalse([l for l in tick if 'dialog clear' in l])

    def test_busy_invitee_expires(self):
        """(b) un invité en attente devenu occupé voit l'invitation expirer ; busy ne tourne que pour les invités en attente."""
        run = [l for l in code('duel/tick') if l.endswith('run function mg:duel/inv_busy')]
        self.assertEqual(run, ['execute as @a[scores={mg.dlto=1..},tag=!mg.dl] run function mg:duel/inv_busy'])
        busy = code('duel/inv_busy')
        self.assertEqual(busy[0], 'function mg:duel/busy')
        untag = [i for i, l in enumerate(busy) if l.endswith(UNTAG)]
        expire = [i for i, l in enumerate(busy) if l.endswith('function mg:duel/expire')]
        self.assertEqual((len(untag), len(expire)), (1, 1))
        self.assertLess(untag[0], expire[0], 'mg.dlui retiré AVANT expire, sinon dialog clear fermerait la fenêtre qui a pris la place')
        for i in (untag[0], expire[0]):
            self.assertTrue(busy[i].startswith('execute if score $dlb mg.st matches 1 run '), busy[i])
        self.assertFalse([l for l in busy if 'dialog clear' in l])


class Commands(unittest.TestCase):
    def test_reopen_and_later(self):
        cmd = code('duel/cmd')
        reopen = [l for l in cmd if l.startswith('execute if score #dlv mg.st matches 6 if score @s mg.dlto matches 1.. run')]
        self.assertEqual(len(reopen), 1)
        self.assertTrue(reopen[0].endswith(SHOW))
        self.assertNotIn('mg.rate', reopen[0], '[Répondre] ouvre même pendant la note')
        self.assertTrue(any(l.startswith('execute if score #dlv mg.st matches 6 unless score @s mg.dlto matches 1.. run tellraw @s') for l in cmd))
        self.assertIn('execute if score #dlv mg.st matches 7 run ' + UNTAG, cmd)


if __name__ == '__main__':
    unittest.main()
