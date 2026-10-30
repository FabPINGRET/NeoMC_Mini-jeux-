"""tools/floaty : une commande à CIBLE UNIQUE (`attribute`, `damage`, `ride`, `data modify entity`...) ne reçoit jamais un sélecteur
multi-cibles. fl_sel.fix_selector confine @a à `tag=mg.flw` et @e à `distance=0..`, mais ne pose pas de limite : `attribute @a[tag=mg.flw] ...`
échoue en jeu dès que deux joueurs sont dans la dimension (« Only one entity is allowed »). Le garde-fou lit les fonctions RÉELLES
(les espaces de noms de tools/floaty/owned.txt, plus floaty) et refuse, derrière une commande à cible unique, un sélecteur hors chaîne
qui est @a / @e sans `limit=1`, ou @p / @r avec un `limit` supérieur à 1. La commande est lue dans le préfixe du sélecteur : du dernier
` run ` (ou du début de ligne) jusqu'au sélecteur, le motif étant ancré en fin de préfixe.
Corrigé à la source par `execute as @a[tag=mg.flw] run attribute @s ...` (fl_rewrite, gamerule fall_damage).
Cas à UNE entité contrôlés : `tp <cibles> <x> @e[...]` (destination), `tp @e[...]` seul (c'est la destination, pas l'entité déplacée),
`tp|teleport <cibles> <loc> facing entity @e[...]` et `rotate <cible> facing entity @e[...]`. `execute ... facing entity @e[...]` est
accepté (le sélecteur d'un `execute facing` n'est pas contrôlé ici), de même que `tp @e[...] <loc>` (plusieurs entités déplacées : permis).
Limites connues (non vues par le garde-fou) :
- `function <id> with entity <sélecteur>` : la source de macro exige UNE entité, non contrôlée ;
- `spectate <cible> <joueur>` : seul le premier argument est contrôlé (le joueur qui spectate ne l'est pas) ;
- `loot ... kill <sélecteur>` : la source du butin exige UNE entité, non contrôlée ;
- un nom d'objectif, d'équipe ou de joueur fictif égal à une commande (`scoreboard players add attribute @a 1`) : faux positif possible ;
- chaînes `Command:"..."` imbriquées (blocs de commande posés par setblock) : fl_sel.scan les saute, leur contenu n'est pas lu.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_sel  # noqa: E402

OWNED = ROOT / 'tools' / 'floaty' / 'owned.txt'
DATA = ROOT / 'data'
AT_SELECTOR = re.compile(r'@[aepr]')                    # préfiltre des lignes de la partie réelle
LEAD = re.compile(r'\s*[/$]?\s*')                       # espaces, `/` ou `$` de macro en tête de ligne
# fin du préfixe d'un sélecteur : la commande attend UNE cible (le préfixe est rstrip : le motif est ancré en fin)
SINGLE = re.compile(r'(?<![\w:.-])(?:attribute|damage|spectate|rotate|ride|ride \S+ mount|damage .* (?:by|from)'
                    r'|(?:data (?:get|merge|modify|remove)|store (?:result|success)|(?:if|unless) data) entity'
                    r'|from entity|(?:tp|teleport) \S+|(?:tp|teleport) .* facing entity|rotate \S+ facing entity)$')
ALONE = re.compile(r'(?<![\w:.-])(?:tp|teleport)$')        # `tp @e[...]` sans rien après : le sélecteur est la destination


def multi(letter, inner):
    """True si le sélecteur @letter[inner] peut viser plus d'une entité : @a / @e sans limit=1, @p / @r avec limit > 1, limit illisible."""
    parts = fl_sel.split_args(inner or '')
    if parts is None:
        return True                                              # chaîne non fermée : rien de prouvé
    limits = [p.split('=', 1)[1].strip() for p in parts if p.split('=', 1)[0].strip() == 'limit' and '=' in p]
    try:
        n = int(limits[-1]) if limits else None
    except ValueError:
        return True                                              # `limit=$(n)` et autres : non prouvé
    if letter in 'ae':
        return n != 1
    return letter in 'pr' and n is not None and n > 1


def refused(line):
    """Sélecteurs de la ligne qui visent plusieurs entités derrière une commande à cible unique -> liste de textes."""
    s = line.rstrip('\r\n')
    spans, runs, _ = fl_sel.scan(s)
    lead = LEAD.match(s).end()
    out = []
    for a, b, letter, inner, js in spans:
        if js or letter not in 'aepr' or not multi(letter, inner):
            continue
        start = max([lead] + [r for r in runs if r <= a])
        before = s[start:a].rstrip()
        if SINGLE.search(before) or (ALONE.search(before) and not s[b:].strip()):
            out.append(s[a:b])
    return out


class Unit(unittest.TestCase):
    def test_refuses_a_multi_target_selector_behind_a_single_target_command(self):
        for line in ('attribute @a[tag=x] minecraft:max_health base set 2',
                     'execute as @p run damage @e[type=zombie] 1',
                     'ride @s mount @e[type=boat]',
                     'data modify entity @e[tag=x] CustomName set value "a"',
                     'tp @s @e[tag=x]',
                     'tp @s ~ ~ ~ facing entity @e[tag=x]',
                     'execute as @a[tag=x] run tp @s ~ ~1 ~ facing entity @e[tag=y]',
                     'teleport @a[tag=x,limit=1] ~ ~ ~ facing entity @a[tag=y]',
                     'rotate @s facing entity @e[tag=x]',
                     'tp @e[tag=x]',
                     'execute as @s run teleport @a[tag=x]',
                     'execute as @s run attribute @a[tag=mg.flw] minecraft:scale base set 1',
                     'execute store result entity @e[tag=x] Health int 1 run say hi',
                     'damage @s 3 minecraft:generic by @e[tag=boss]',
                     'attribute @p[limit=2] minecraft:max_health base set 2'):
            with self.subTest(line):
                self.assertTrue(refused(line), line)

    def test_accepts_a_single_target_or_a_command_that_takes_many(self):
        for line in ('attribute @a[tag=mg.flw,limit=1] minecraft:max_health base set 2',
                     'attribute @p minecraft:max_health base set 2',
                     'attribute @s minecraft:max_health base set 2',
                     'execute as @a[tag=mg.flw] run attribute @s minecraft:fall_damage_multiplier base set 0',
                     'kill @e[type=item]',
                     'tp @a[tag=x] ~ ~1 ~',
                     'tp @e[tag=x] @s',
                     'tp @e[tag=x] @p',
                     'tp @s ~ ~ ~ facing entity @s',
                     'rotate @s facing entity @p',
                     'tp @s @e[tag=x,limit=1]',
                     'execute facing entity @e[tag=x] feet run say hi',
                     'tellraw @a "attribute @a x"',
                     'attribute @r[limit=1] minecraft:max_health base set 2',
                     'execute as @e[type=zombie] run data modify entity @s CustomName set value "a"',
                     'execute as @a run say attribute'):
            with self.subTest(line):
                self.assertEqual(refused(line), [], line)

    def test_the_command_is_the_one_after_the_last_run(self):
        self.assertEqual(refused('execute as @a[tag=x] run attribute @s minecraft:scale base set 1'), [])         # le @a est derrière `as`
        self.assertEqual(refused('execute as @a[tag=x] run attribute @a[tag=x] minecraft:scale base set 1'), ['@a[tag=x]'])

    def test_limit_helper(self):
        for letter, inner, want in (('a', None, True), ('a', 'limit=1', False), ('a', 'tag=x,limit=2', True), ('e', 'limit=1,type=pig', False),
                                    ('p', None, False), ('p', 'limit=2', True), ('r', 'limit=1', False), ('a', 'limit=$(n)', True),
                                    ('s', None, False)):
            with self.subTest((letter, inner)):
                self.assertEqual(multi(letter, inner), want)


class RealFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not OWNED.exists():                             # suivi par git : son absence est une erreur, pas une raison de ne rien contrôler
            raise AssertionError('tools/floaty/owned.txt absent : le garde-fou ne saurait pas quels espaces de noms parcourir')
        names = {l.strip().split('/')[1] for l in OWNED.read_text(encoding='utf-8').split('\n') if l.strip().startswith('data/')}
        cls.files = sorted(p for ns in sorted((names - {'minecraft'}) | {'floaty'}) for p in (DATA / ns / 'function').rglob('*.mcfunction'))

    def test_no_function_gives_a_multi_target_selector_to_a_single_target_command(self):
        bad, read = [], 0
        for p in self.files:
            read += 1
            rel = p.relative_to(DATA).as_posix()
            name = rel.replace('/function/', '/', 1)[:-len('.mcfunction')]
            for n, line in enumerate(p.read_text(encoding='utf-8').split('\n'), 1):
                if AT_SELECTOR.search(line) and not line.lstrip().startswith('#'):
                    bad += ['%s:%d %s' % (name, n, sel) for sel in refused(line)]
        self.assertGreater(read, 100, 'trop peu de fichiers lus : le parcours est cassé')
        self.assertEqual(bad, [], '%d commande(s) à cible unique avec un sélecteur multi-cibles' % len(bad))


if __name__ == '__main__':
    unittest.main()
