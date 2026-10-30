r"""Traduction française des textes visibles de la carte « Scourge of the Floaty Isles » : lignes de .mcfunction et advancements (fonctions pures).

    prot, st0 = fl_tr.protected_keys(lignes, arbres)       # clés à ne jamais traduire (écrit dans protected.txt par le générateur) ; st0.warns :
                                                           # lignes illisibles (toutes leurs chaînes sont protégées par défaut), à afficher
    tb = fl_tr.Table.load(fr_dir, ctx_path, prot)          # fr/*.json {anglais: français} + ctx.json {"ns:chemin": {anglais: français}}
    st = fl_tr.Stats(tb)                                   # compteurs : translated, missing, refused, errors (+ missing_keys, warns)
    ligne = fl_tr.translate_line(ligne, 'ns:chemin', st)   # la ligne, À L'IDENTIQUE si rien n'est traduit ou si elle est illisible
    arbre = fl_tr.translate_tree(arbre, 'ns:chemin', st)   # advancement chargé (json.load) : display.title / display.description

Où sont les textes (tellraw, title, bossbar, custom_name, lore, CustomName, messages de panneau, text_display, `Command:` imbriqué...) et
quelles zones sont protégées (liste complète : docstring de fl_scan) : fl_scan. Ici : la table et la traduction.
Chaîne d'un emplacement qui contient un composant JSON (ancien format : `custom_name='{"text":"x"}'`, `lore=['"x"']`) : traduite à l'intérieur
et ré-écrite avec le même guillemet ; `Command:'...'` est traduit comme une ligne. Encodage : guillemet d'origine, \ / guillemet / \n échappés,
UTF-8 en clair.
Parcours d'un composant : `text`, `extra`, éléments de liste, `hover_event.value` / `contents` (show_text). Jamais `click_event`, `score`,
`selector`, `nbt`, `keybind`, `translate`. Un texte sans lettre (« < », « . », emoji, nombre) n'est ni traduit ni compté manquant.
Clé de la table : le texte sans espaces de bord ni préfixe de dialogue `> ` (remis à l'identique à l'application). Une clé de la table qui
figure dans l'ensemble protégé est refusée au chargement (Table.refused) et comptée (st.refused) quand le texte apparaît ailleurs : traduire un
nom d'objet casserait le verrou ou le test qui le compare.
"""
import json
from collections import Counter
from pathlib import Path

import fl_scan as C
import fl_snbt as S

norm = C.norm
_HOVER = (('hover_event', ('value', 'contents')), ('hoverEvent', ('contents', 'value')))     # (clé, sous-clés qui portent un composant)


class Stats:
    """Compteurs d'un passage (un objet partagé par tous les appels) ; table : la Table consultée."""

    def __init__(self, table):
        self.table = table
        self.translated = self.missing = self.refused = self.errors = 0
        self.missing_keys = Counter()       # clé normalisée -> occurrences : ce qu'il reste à traduire
        self.warns = []                     # (motif, ligne) : lignes illisibles rendues intactes

    def warn(self, why, line):
        self.errors += 1
        self.warns.append((why, line))


class Table:
    """glob {clé: français}, ctx {'ns:chemin': {clé: français}} (prioritaire), refused : clés écartées car protégées."""

    def __init__(self, protected=()):
        self.glob, self.ctx, self.refused, self.src = {}, {}, set(), {}
        self.protected = frozenset(protected)

    def add(self, key, fr, src, ctx_id=None):
        """Ajoute une entrée ; ValueError si la même clé a déjà un AUTRE français (même contexte) ; ignorée (refused) si protégée."""
        k = norm(key)[1]
        if not k:
            return
        if k in self.protected:
            self.refused.add(k)
            return
        dest = self.glob if ctx_id is None else self.ctx.setdefault(ctx_id, {})
        if dest.get(k, fr) != fr:
            raise ValueError(f'doublon en conflit pour {k!r} ({ctx_id or "global"}) : {self.src[(ctx_id, k)]} et {src}')
        dest[k] = fr
        self.src[(ctx_id, k)] = src

    @classmethod
    def load(cls, fr_dir, ctx_path=None, protected=()):
        if not Path(fr_dir).is_dir():
            raise ValueError(f'{fr_dir} : dossier des traductions introuvable')
        t = cls(protected)
        for p in sorted(Path(fr_dir).glob('*.json')):
            for k, v in _pairs(p):
                t.add(k, _text_of(v, p), p.name)
        if ctx_path and Path(ctx_path).exists():
            for cid, d in _pairs(Path(ctx_path)):
                for k, v in d:
                    t.add(k, _text_of(v, ctx_path), Path(ctx_path).name, cid)
        return t

    def get(self, ctx_id, key):
        return self.ctx.get(ctx_id, {}).get(key, self.glob.get(key))


def _pairs(path):
    """Fichier JSON -> liste de paires (les doublons de clé d'un même fichier restent visibles : ils font un conflit dans Table.add)."""
    data = json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=list)
    if not isinstance(data, list):
        raise ValueError(f'{path} : un objet JSON est attendu')
    return data


def _text_of(v, path):
    if not isinstance(v, str):
        raise ValueError(f'{path} : le français doit être une chaîne, pas {v!r}')
    return v


def _splice(text, edits):
    for a, b, new in sorted(edits, reverse=True):
        text = text[:a] + new + text[b:]
    return text


def _text(s, ctx_id, st):
    """Texte visible -> son français, ou None s'il n'y a rien à changer (compte traduits / manquants / refusés)."""
    lead, key, trail = norm(s)
    if not any(c.isalpha() for c in key):
        return None
    if key in st.table.protected:           # jamais traduite : refusée si la table la contenait, sinon rien à traduire (ni manquante)
        st.refused += key in st.table.refused
        return None
    fr = st.table.get(ctx_id, key)
    if fr is None:
        st.missing += 1
        st.missing_keys[key] += 1
        return None
    st.translated += 1
    return lead + fr + trail


def _comp(node, fn, top=False):
    """Parcours sémantique d'un composant (lu par fl_snbt ou JSON chargé) : chaque texte (Leaf / str) est remplacé par fn(texte, top) ;
    top : emplacement lui-même ou élément de liste de l'emplacement. Rend le noeud (modifié sur place)."""
    if isinstance(node, (S.Leaf, str)):
        return fn(node, top)
    if isinstance(node, list):
        for i, x in enumerate(node):
            node[i] = _comp(x, fn, top)
    elif isinstance(node, dict):
        for k in ('text', 'extra'):
            if k in node:
                node[k] = _comp(node[k], fn)
        for hk, subs in _HOVER:
            h = node.get(hk)
            if not isinstance(h, dict):
                continue
            act = h.get('action', 'show_text')
            if getattr(act, 'v', act) == 'show_text':       # show_item / show_entity : pas un composant
                for sk in subs:
                    if sk in h:
                        h[sk] = _comp(h[sk], fn)
    return node


def _leaf_fn(ctx_id, st, edits):
    """fn de _comp pour un composant lu par fl_snbt : accumule dans edits les (début, fin, texte) à écrire."""
    def fn(leaf, top):
        new = None
        if top and C.json_of(leaf.v) is not None:                # composant JSON dans la chaîne (ancien format)
            r, sub = S.parse(leaf.v), []
            if r is None:
                st.warn('composant JSON illisible dans une chaîne', leaf.v)
            else:
                _comp(r[0], _leaf_fn(ctx_id, st, sub), True)
                new = _splice(leaf.v, sub) if sub else None
        else:
            new = _text(leaf.v, ctx_id, st)
        if new is not None:
            edits.append((leaf.a, leaf.b, S.encode(new, leaf.q)))
        return leaf
    return fn


def translate_line(line, ctx_id, st):
    """Ligne de .mcfunction -> la ligne avec ses textes visibles traduits ; identique si rien n'est traduit ou si la ligne est illisible."""
    try:
        items = C.scan(line, set())
    except C.Bad as e:
        st.warn(str(e), line)
        return line
    edits = []
    for kind, node in items:
        if kind == 'text':
            _comp(node, _leaf_fn(ctx_id, st, edits), True)
        else:
            new = translate_line(node.v, ctx_id, st)
            if new != node.v:
                edits.append((node.a, node.b, S.encode(new, node.q)))
    return _splice(line, edits)


def translate_tree(tree, ctx_id, st):
    """Advancement chargé (json.load) -> le même arbre, display.title / display.description traduits (chaîne ou composant)."""
    def fn(s, top):
        new = _text(s, ctx_id, st)
        return s if new is None else new
    d = tree.get('display') if isinstance(tree, dict) else None
    for k in ('title', 'description'):
        if isinstance(d, dict) and k in d:
            d[k] = _comp(d[k], fn, True)
    return tree


def _protect_line(line, out, st):
    try:
        items = C.scan(line, out)
    except C.Bad as e:
        st.warn(str(e), line)
        C._strings(line, out)           # ligne illisible : on ne sait pas où sont ses zones protégées, toutes ses chaînes le deviennent
        return
    for kind, node in items:
        if kind == 'cmd':
            _protect_line(node.v, out, st)


def protected_keys(lines, trees=()):
    """Lot de lignes (et d'advancements chargés) -> (clés protégées, Stats) : les clés (normalisées) sont les chaînes des zones protégées, JSON
    imbriqué compris ; Stats.warns liste les lignes illisibles, dont TOUTES les chaînes sont protégées par défaut (à afficher par l'appelant).
    À passer à Table.load : une clé protégée n'y est jamais traduite."""
    out, st = set(), Stats(None)
    for line in lines:
        _protect_line(line, out, st)
    for tree in trees:
        C.protect_tree(tree, out)
    return out, st
