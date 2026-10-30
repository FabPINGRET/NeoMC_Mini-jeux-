"""Extrait les textes visibles à traduire de la carte « Scourge of the Floaty Isles » (aucune écriture dans data/).

    python tools/floaty/fr_extract.py --map <dossier de la carte extraite> [--root <dépôt>] [--table <fr>] [--out <dossier>]

Même chaîne que gen_floaty (rewrite_map : lecture et réécriture en mémoire, puis fl_fr.translate avec une table qui ne traduit rien et note chaque
clé qu'on lui demande) : les clés extraites sont exactement celles que la vraie table rencontrera ; les clés protégées (fl_fr.protect, section
manuelle de <table>/protected.txt comprise) n'en font pas partie. Écrit dans <out> (défaut <dépôt>/cache/floaty_fr/, ignoré par git) :
- todo_<ns>.jsonl : une ligne par clé distincte de l'espace de noms (la plus fréquente d'abord) : key (clé de la table), n (occurrences),
  slot (tellraw, title, subtitle, actionbar, bossbar, custom_name, item_name, lore, CustomName, sign, text_display, advancement title|description),
  where (`ns:fonction:ligne` de la première occurrence, la ligne est celle du .mcfunction généré ; un advancement : `ns:advancement/chemin`),
  more (jusqu'à 4 autres emplacements), message (le message ENTIER de la première occurrence, fragments `text` / `extra` bout à bout : le contexte) ;
- stats.txt : occurrences et clés distinctes par espace de noms, par sous-dossier de npc, par type d'emplacement ; les clés les plus fréquentes.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'lib'))
import fl_fr  # noqa: E402
import fl_scan as C  # noqa: E402
import fl_snbt as S  # noqa: E402
import fl_tr as T  # noqa: E402
import gen_floaty as G  # noqa: E402

TOP = 80                                                              # clés les plus fréquentes listées dans stats.txt
MORE = 4                                                              # emplacements supplémentaires gardés par clé
_SLOT = re.compile(r'(?P<tell>tellraw\b)|title\s+\S+\s+(?P<title>title|subtitle|actionbar)\b|(?P<boss>bossbar\s+(?:add|set)\b)'
                   r'|\b(?P<key>custom_name|item_name|lore|CustomName|messages)["\']?\s*[:=]|\b(?P<bare>text)\s*[:=]')    # `text` : clé nue seulement
_RENAME = {'messages': 'sign'}


def plain(node):
    """Composant (lu par fl_snbt, ou JSON chargé) -> son texte entier : `text` et `extra` bout à bout (ni hover, ni score, ni keybind)."""
    if isinstance(node, str):
        return node
    if isinstance(node, S.Leaf):
        inner = C.json_of(node.v)                                     # ancien format : composant JSON dans la chaîne
        return node.v if inner is None else plain(inner)
    if isinstance(node, list):
        return ''.join(plain(x) for x in node)
    if isinstance(node, dict):
        return plain(node.get('text', '')) + plain(node.get('extra', []))
    return ''


def _kind(m):
    g = m.lastgroup
    if g == 'title':
        return m.group('title')
    if g == 'key':
        return _RENAME.get(m.group('key'), m.group('key'))
    return {'tell': 'tellraw', 'boss': 'bossbar', 'bare': 'text_display'}[g]


def slot_kind(line, node):
    """Type de l'emplacement de texte `node` de `line` : le dernier repère (tellraw, title, bossbar, clé de texte) avant sa première chaîne. Approximation
    (information pour le traducteur, pas une règle) : une clé nue `text:` après un autre repère (`messages:[{text:...}]`) ne compte pas (panneau)."""
    leaf = next(S.leaves(node), None)
    kinds = [_kind(m) for m in _SLOT.finditer(line, 0, leaf.a)] if leaf else []
    if len(set(kinds)) > 1:
        kinds = [k for k in kinds if k != 'text_display'] or kinds
    return kinds[-1] if kinds else '?'


class Probe:
    """Reçoit de fl_fr.translate l'emplacement courant (at), le type et le message de chaque emplacement (slot) puis chaque clé demandée (hit)."""

    def __init__(self):
        self.ctx, self.line = '', None
        self.kind, self.message = '?', ''
        self.rows = []                                                # (clé, ctx_id, emplacement, type, message)

    def at(self, ctx_id, n):
        self.ctx, self.line = ctx_id, n

    def slot(self, line, node, name):
        self.kind, self.message = name or slot_kind(line, node), plain(node)

    def hit(self, key):
        where = self.ctx if self.line is None else f'{self.ctx}:{self.line}'
        self.rows.append((key, self.ctx, where, self.kind, self.message))


class Rec(T.Table):
    """Table qui ne traduit rien : chaque clé qu'on lui demande est notée dans probe."""

    def __init__(self, protected, probe):
        super().__init__(protected)
        self.probe = probe

    def get(self, ctx_id, key):
        self.probe.hit(key)
        return None


def collect(rows):
    """Lignes de Probe -> {ns: {clé: {n, slot, where, more, message}}} ; la première occurrence fixe slot / where / message."""
    out = defaultdict(dict)
    for key, ctx, where, kind, message in rows:
        e = out[ctx.split(':', 1)[0]].setdefault(key, {'key': key, 'n': 0, 'slot': kind, 'where': where, 'more': [], 'message': message})
        e['n'] += 1
        if e['n'] > 1 and len(e['more']) < MORE:
            e['more'].append(where)
    return out


def stats_text(rows, by_ns, prot):
    """Texte de stats.txt : occurrences / clés distinctes (tous espaces de noms, puis chacun, puis sous-dossiers de npc et types)."""
    keys = {r[0] for r in rows}
    out = [f'occurrences : {len(rows)} ; clés distinctes : {len(keys)} ; clés protégées (jamais traduites) : {len(prot.keys)} '
           f'(calculées {len(prot.auto)}, manuelles {len(prot.manual)})', '', 'par espace de noms (occurrences / clés distinctes dans l\'espace) :']
    for ns, d in sorted(by_ns.items(), key=lambda kv: -sum(e['n'] for e in kv[1].values())):
        out.append(f'  {ns:14s} {sum(e["n"] for e in d.values()):6d} / {len(d):5d}')
    sub = defaultdict(list)
    for key, ctx, _, _, _ in rows:
        ns, _, path = ctx.partition(':')
        if ns == 'npc':
            sub[path.split('/')[0] if '/' in path else '(racine)'].append(key)
    out += ['', 'npc par sous-dossier (occurrences / clés distinctes) :']
    out += [f'  {s:24s} {len(k):6d} / {len(set(k)):5d}' for s, k in sorted(sub.items(), key=lambda kv: -len(kv[1]))]
    kinds = Counter(r[3] for r in rows)
    out += ['', 'par type d\'emplacement (occurrences) :'] + [f'  {k:24s} {c:6d}' for k, c in kinds.most_common()]
    out += ['', f'les {TOP} clés les plus fréquentes :'] + [f'  {c:5d}  {json.dumps(k, ensure_ascii=False)}' for k, c in Counter(r[0] for r in rows).most_common(TOP)]
    return '\n'.join(out) + '\n'


def extract(map_dir, root, table, out_dir):
    """Écrit todo_<ns>.jsonl et stats.txt dans out_dir ; -> (rows, texte de stats). Rien n'est écrit sous data/ ni dans la table."""
    m = G.rewrite_map(map_dir, root)
    pr = fl_fr.protect(m.fns, m.keys, table)
    probe = Probe()
    fl_fr.translate(m.fns, m.files, m.state.install, Rec(pr.keys, probe), probe)
    by_ns = collect(probe.rows)
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob('todo_*.jsonl'):                           # pas de reste d'une extraction précédente
        old.unlink()
    for ns, d in by_ns.items():
        with open(out_dir / f'todo_{ns}.jsonl', 'w', encoding='utf-8', newline='\n') as f:
            for e in sorted(d.values(), key=lambda e: (-e['n'], e['key'])):
                f.write(json.dumps(e, ensure_ascii=False) + '\n')
    text = stats_text(probe.rows, by_ns, pr)
    with open(out_dir / 'stats.txt', 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    return probe.rows, text


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--map', required=True, help='dossier de la carte extraite (contient level.dat et datapacks/)')
    ap.add_argument('--root', default=str(ROOT), help='racine du dépôt NeoMC (défaut : celle de ce script)')
    ap.add_argument('--table', default=str(G.FR_DIR), help='dossier des traductions (seule la section manuelle de protected.txt est lue)')
    ap.add_argument('--out', default=None, help='dossier de sortie (défaut : <racine>/cache/floaty_fr)')
    a = ap.parse_args()
    out = Path(a.out) if a.out else Path(a.root) / 'cache' / 'floaty_fr'
    _, text = extract(a.map, Path(a.root), Path(a.table), out)
    print(text.split('\n\n')[0])
    print(f'écrit dans {out}')


if __name__ == '__main__':
    main()
