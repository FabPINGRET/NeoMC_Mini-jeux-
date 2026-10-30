r"""Où sont les textes visibles d'une ligne de .mcfunction, et quelles chaînes sont protégées (fonctions pures, aucune traduction ici ; sert fl_tr).

    items = fl_scan.scan(ligne, prot)          # [('text', composant lu par fl_snbt) | ('cmd', Leaf de `Command:`)] ; prot (set) reçoit les clés protégées
    k = fl_scan.norm(texte)[1]                 # (début, clé, fin) : espaces de bord et préfixe de dialogue `> ` retirés de la clé
    fl_scan.json_of(chaîne)                    # la valeur JSON qu'une chaîne contient (ancien format), sinon None
    fl_scan.jstrings(json, prot) / fl_scan.protect_tree(advancement, prot)

Emplacements de texte (le reste de la ligne n'est jamais lu ; un commentaire `#...` rend []) : `tellraw <sel> <composant>`,
`title <sel> title|subtitle|actionbar <composant>`, `bossbar add <id> <composant>`, `bossbar set <id> name <composant>`, `custom_name=` /
`item_name=` / `lore=`, les clés `custom_name|item_name|lore` (avec ou sans `minecraft:`, entre guillemets ou non), `CustomName`, `messages`
(panneaux), `text` (text_display). Une commande n'est reconnue qu'en début de ligne ou après `run` (macro `$` et `/` admis).
Zones PROTÉGÉES, sautées sans être lues : sous `lock:` (clé nue ou entre guillemets), `nbt=` / `name=` d'un sélecteur, chemin d'un
`if|unless data`, prédicat d'un `if|unless items`, d'un `if|unless block` (4e mot, après les 3 coordonnées) et d'un `clear`, filtre de
`fill ... replace` et de `clone ... filtered`. Leurs chaînes (JSON imbriqué compris) vont dans prot, normalisées.
Une ligne illisible (chaîne non fermée, crochet manquant) lève Bad : l'appelant la rend intacte.
"""
import json
import re

import fl_snbt as S

KEYS = frozenset(('custom_name', 'item_name', 'lore', 'CustomName', 'messages', 'text'))      # clés SNBT dont la valeur est un texte
TITLE = frozenset(('title', 'subtitle', 'actionbar'))
_EV = re.compile(
    r'(?P<q>["\'])'
    r'|(?<![\w.:/-])/?(?P<cmd>tellraw|title|bossbar|clear|fill|clone)(?=\s|$)'     # `/` de tête admis ; `a:b/clear` (chemin de fonction) refusé
    r'|(?<![\w.:/-])(?:if|unless)\s+(?P<chk>data|items|block)(?=\s)'
    r'|(?P<sel>@[aeprsn])(?=\[)'
    r'|(?<![\w.:/-])(?P<lock>lock)\s*:'
    r'|(?<![\w.:/-])(?P<cmdkey>Command)\s*:'
    r'|(?<![\w.:-])(?:minecraft:)?(?P<key>custom_name|item_name|lore|CustomName|messages|text)\s*:'
    r'|(?<![\w.:-])(?:minecraft:)?(?P<eq>custom_name|item_name|lore)=')
_POS = re.compile(r'(?:^[$/]?|\brun)\s*$')                 # ce qui précède une commande : début de ligne (macro `$`, `/`) ou `run`
_SELKEY = re.compile(r'(?<![\w.])(?:nbt|name)=!?')
_NORM = re.compile(r'(\s*(?:> )?\s*)(.*?)(\s*)', re.S)
_WS = re.compile(r'\s*')
_QUOTE = re.compile(r'["\']')


class Bad(Exception):
    """Ligne illisible (chaîne non fermée, crochet manquant...) : traduite nulle part, rendue intacte."""


def norm(s):
    """Texte -> (début, clé, fin) : début = espaces et préfixe `> `, fin = espaces ; début + clé + fin == s."""
    return _NORM.fullmatch(s).groups()


def json_of(s):
    """Texte d'une chaîne qui contient un composant JSON (ancien format) -> sa valeur, sinon None."""
    if s.lstrip()[:1] not in ('{', '[', '"'):
        return None
    try:
        return json.loads(s)
    except (ValueError, RecursionError):
        return None


def _add(s, out):
    k = norm(s)[1]
    if k:
        out.add(k)
    inner = json_of(s)
    if inner is not None:
        jstrings(inner, out)


def jstrings(node, out):
    """Toutes les chaînes (valeurs) d'un JSON chargé -> out (clés normalisées)."""
    if isinstance(node, str):
        _add(node, out)
    elif isinstance(node, dict):
        for v in node.values():
            jstrings(v, out)
    elif isinstance(node, list):
        for v in node:
            jstrings(v, out)


def _strings(text, out):
    """Toutes les chaînes entre guillemets d'un morceau de ligne -> out."""
    i = 0
    while True:
        m = _QUOTE.search(text, i)
        leaf = S.string(text, m.start()) if m else None
        if leaf is None:
            return
        _add(leaf.v, out)
        i = leaf.b


def _sel_zone(text, out):
    """Texte d'un sélecteur -> out : les chaînes de nbt= et de name= (SNBT, chaîne ou mot nu)."""
    for m in _SELKEY.finditer(text):
        j = m.end()
        if text[j:j + 1] in ('{', '['):
            r = S.parse(text, j)
            _strings(text[j:r[1]] if r else text[j:], out)
        elif text[j:j + 1] in ('"', "'"):
            leaf = S.string(text, j)
            if leaf is None:        # illisible : tout le reste du sélecteur est protégé
                _strings(text[j:], out)
            else:
                _add(leaf.v, out)
        else:
            w = re.match(r'[^\s,\]]+', text[j:])
            if w:
                _add(w.group(), out)


def protect_tree(node, out):
    """Advancement chargé -> out : les chaînes de ses `criteria` (conditions : noms d'objets comparés)."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'criteria':
                jstrings(v, out)
            else:
                protect_tree(v, out)
    elif isinstance(node, list):
        for v in node:
            protect_tree(v, out)


def _close(t, j):
    """t[j] ouvre `[` ou `{` -> position après son fermant (chaînes sautées)."""
    depth, i = 0, j
    while i < len(t):
        if t[i] in '"\'':
            i = _str(t, i).b
            continue
        depth += (t[i] in '[{') - (t[i] in ']}')
        i += 1
        if depth == 0:
            return i
    raise Bad('crochet non fermé')


def _str(t, i):
    w = []
    leaf = S.string(t, i, w)
    if leaf is None:
        raise Bad(w[0])
    return leaf


def _tok(t, i):
    """-> (début, fin) du mot qui suit t[i] (séparé par des espaces hors crochets et chaînes), ou None en fin de ligne."""
    i = _WS.match(t, i).end()
    j = i
    while j < len(t) and not t[j].isspace():
        if t[j] in '[{':
            j = _close(t, j)
        elif t[j] in '"\'':
            j = _str(t, j).b
        else:
            j += 1
    return (i, j) if j > i else None


def _toks(t, i, n):
    out = []
    while len(out) < n:
        tok = _tok(t, out[-1][1] if out else i)
        if tok is None:
            break
        out.append(tok)
    return out


def _slot(t, i, items):
    """Valeur d'un emplacement de texte qui commence en t[i] -> items ; rend la position de fin."""
    i = _WS.match(t, i).end()
    if t[i:i + 1] in ('', '$'):         # rien (fin de ligne) ou paramètre de macro : pas un texte lisible
        return i
    w = []
    r = S.parse(t, i, w)
    if r is None:
        raise Bad(w[0])
    items.append(('text', r[0]))
    return r[1]


def _filter(t, m, prot, skip):
    """`fill <6 coordonnées> <bloc> replace <filtre>` / `clone <coordonnées> filtered <filtre>` : le filtre (prédicat de bloc) est une zone protégée,
    ajoutée à skip ; le reste de la ligne (le bloc posé de fill, par exemple) reste lu."""
    fill = m.group('cmd') == 'fill'
    toks = _toks(t, m.end(), 9 if fill else 16)
    words = [t[a:b] for a, b in toks]
    if fill:
        at = 7 if len(words) > 8 and words[7] == 'replace' else None          # 6 coordonnées, le bloc, puis le mode
    else:
        at = next((k for k in range(9, len(words) - 1) if words[k] == 'filtered'), None)       # 9 coordonnées, plus `from|to <dimension>` et `strict` (16 mots au plus)
    if at is not None:
        a, b = toks[at + 1]
        _strings(t[a:b], prot)
        skip.append((a, b))
    return m.end()


def _command(t, m, items, prot, skip):
    if not _POS.search(t[:m.start()]):          # `schedule clear`, un mot ordinaire : pas la commande
        return m.end()
    if m.group('cmd') in ('fill', 'clone'):
        return _filter(t, m, prot, skip)
    name, toks = m.group('cmd'), _toks(t, m.end(), 3)
    words = [t[a:b] for a, b in toks]
    if name != 'bossbar' and toks:              # le premier mot est le sélecteur (nbt= / name= protégés)
        _sel_zone(words[0], prot)
    if name == 'tellraw' and toks:
        return _slot(t, toks[0][1], items)
    if name == 'title' and len(toks) > 1 and words[1] in TITLE:
        return _slot(t, toks[1][1], items)
    if name == 'bossbar' and len(toks) > 1 and words[0] == 'add':
        return _slot(t, toks[1][1], items)
    if name == 'bossbar' and len(toks) > 2 and words[0] == 'set' and words[2] == 'name':
        return _slot(t, toks[2][1], items)
    if name == 'clear' and len(toks) > 1:
        _strings(t[toks[1][0]:toks[1][1]], prot)
    return toks[-1][1] if toks else m.end()


def _lock(t, i, prot):
    """Valeur d'un `lock` qui commence en t[i] : ses chaînes sont protégées ; rend la position de fin."""
    v = S.parse(t, i)
    if v is None:
        raise Bad(f'valeur illisible après lock en {i}')
    _strings(t[i:v[1]], prot)
    return v[1]


def _check(t, m, prot):
    """`if|unless data ...` / `items ...` / `block ...` : la cible (sélecteur) et le chemin / prédicat sont des zones protégées."""
    if m.group('chk') == 'block':           # block <x> <y> <z> <bloc>{nbt} : trois coordonnées (`~` / `^` compris), puis le prédicat
        toks = _toks(t, m.end(), 4)
        if len(toks) < 4:
            return m.end()
        _strings(t[toks[3][0]:toks[3][1]], prot)
        return toks[3][1]
    toks = _toks(t, m.end(), 6)
    if len(toks) < 2:
        return m.end()
    n = 3 if t[toks[0][0]:toks[0][1]] == 'block' else 1
    for a, b in toks[1:1 + n]:
        _sel_zone(t[a:b], prot)
    rest = toks[1 + n:]
    want = 0 if m.group('chk') == 'data' else 1         # data : le chemin ; items : le prédicat, après l'emplacement
    if len(rest) > want:
        _strings(t[rest[want][0]:rest[want][1]], prot)
        return rest[want][1]
    return (toks[:1 + n] or toks)[-1][1]


def scan(t, prot):
    """Ligne -> [('text', composant lu par fl_snbt) | ('cmd', Leaf de `Command:`)] ; les zones protégées alimentent prot. Bad : illisible."""
    items, skip, i = [], [], 0          # skip : zones protégées (début, fin) déjà relevées, qu'un événement ne doit pas lire
    if t.lstrip()[:1] == '#':
        return items
    while True:
        m = _EV.search(t, i)
        if not m:
            return items
        inside = [b for a, b in skip if a <= m.start() < b]
        if inside:
            i = max(inside)
            continue
        g, i = m.lastgroup, m.end()
        if g == 'q':
            leaf = _str(t, m.start())
            j = _WS.match(t, leaf.b).end()
            key = leaf.v.removeprefix('minecraft:') if t[j:j + 1] == ':' else None
            if key == 'lock':           # `"lock":` entre guillemets : même zone protégée que `lock:`
                i = _lock(t, j + 1, prot)
            else:
                i = _slot(t, j + 1, items) if key in KEYS else leaf.b
        elif g == 'cmd':
            i = _command(t, m, items, prot, skip)
        elif g == 'chk':
            i = _check(t, m, prot)
        elif g == 'sel':
            i = _close(t, i)
            _sel_zone(t[m.end():i], prot)
        elif g == 'lock':
            i = _lock(t, i, prot)
        elif g == 'cmdkey':
            v = S.parse(t, i)
            if v is None:
                raise Bad(f'valeur illisible après Command en {i}')
            i = v[1]
            if isinstance(v[0], S.Leaf):
                items.append(('cmd', v[0]))
        else:
            i = _slot(t, i, items)
