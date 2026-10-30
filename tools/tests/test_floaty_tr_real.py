"""tools/floaty : invariants de la table de traduction RÉELLE (tools/floaty/fr/), vérifiés sur ce qui est commité, pas sur une fixture.
Squelette du lot 1b : avec une table vide (aucun fr/*.json), chaque boucle est vide et le test passe ; il se remplit tout seul quand la
tranche pilote (étape 7) puis les lots suivants ajoutent des traductions. Conventions : voir fr/GLOSSAIRE.md.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_fr  # noqa: E402
import fl_tr  # noqa: E402

FR = ROOT / 'tools' / 'floaty' / 'fr'
PLACEHOLDER = re.compile(r'\$\([^)]*\)|%(?:\d+\$)?s|§.|\\n|\n|https?://\S+')   # jetons à conserver à l'identique
NBSP = ' '


def real_table():
    """Table réelle chargée SANS clés protégées (une clé protégée serait sinon écartée en silence : on veut la voir)."""
    return fl_tr.Table.load(FR, FR / 'ctx.json')


def all_entries(t):
    """(portée, clé, français) de toute la table : globale puis surcharges par contexte."""
    for k, v in t.glob.items():
        yield 'global', k, v
    for cid, d in t.ctx.items():
        for k, v in d.items():
            yield cid, k, v


def protected_on_disk():
    """Clés de fr/protected.txt, sections manuelle ET calculée (les lignes sans # sont des chaînes JSON)."""
    keys = set()
    for line in (FR / 'protected.txt').read_text(encoding='utf-8').splitlines():
        if line.strip() and not line.startswith('#'):
            keys.add(fl_tr.norm(json.loads(line))[1])
    return keys


class RealTable(unittest.TestCase):
    def test_loads_without_error_or_conflict(self):
        real_table()                                    # ValueError : fichier illisible, valeur non texte, doublon en conflit

    def test_protected_file_is_readable(self):
        text, manual = fl_fr.read_protected(FR)
        self.assertIn(fl_fr.MARK, (FR / 'protected.txt').read_text(encoding='utf-8'))
        self.assertLessEqual(manual, protected_on_disk())

    def test_no_protected_key_is_translated(self):
        prot = protected_on_disk()
        bad = [(s, k) for s, k, _ in all_entries(real_table()) if k in prot]
        self.assertEqual(bad, [], 'clé protégée présente dans la table : à retirer (la carte la compare)')

    def test_no_ascii_apostrophe(self):
        bad = [(s, k) for s, k, v in all_entries(real_table()) if "'" in v]
        self.assertEqual(bad, [], 'apostrophe droite dans un français : utiliser ’ (voir GLOSSAIRE.md)')

    def test_nbsp_before_high_punctuation(self):
        bad = [(s, k) for s, k, v in all_entries(real_table()) if re.search(r'[ ][:;!?»]', v)]
        self.assertEqual(bad, [], 'espace ordinaire avant : ; ! ? » : mettre une espace insécable U+00A0')
        bad = [(s, k) for s, k, v in all_entries(real_table()) if re.search(r'«[^' + NBSP + r']', v)]
        self.assertEqual(bad, [], 'espace insécable manquante après «')

    def test_no_empty_translation(self):
        bad = [(s, k) for s, k, v in all_entries(real_table()) if not v.strip()]
        self.assertEqual(bad, [])

    def test_placeholders_preserved(self):
        """$(x), %s / %1$s, §x, \\n (littéral ou saut de ligne) et URL : mêmes occurrences dans la clé (anglais) et sa valeur (français)."""
        bad = [(s, k) for s, k, v in all_entries(real_table()) if Counter(PLACEHOLDER.findall(k)) != Counter(PLACEHOLDER.findall(v))]
        self.assertEqual(bad, [], 'jeton ($(x), %s, §x, \\n, URL) perdu, ajouté ou modifié entre la clé et sa traduction : (portée, clé) fautives')

    def test_ctx_file_is_an_object(self):
        self.assertIsInstance(json.loads((FR / 'ctx.json').read_text(encoding='utf-8')), dict)


if __name__ == '__main__':
    unittest.main()
