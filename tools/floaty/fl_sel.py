"""Analyse d'une ligne de .mcfunction : sélecteurs (@a @e...), ' run ' et chaînes `Command:"..."` — et confinement des sélecteurs à mg:floaty.

    spans, runs, cmds = fl_sel.scan(ligne, stats)      # stats : objet avec .warn(raison, ligne) et .str_skipped / .str_examples
    ligne2 = fl_sel.apply(ligne, stats)                # sélecteurs réécrits (stats.sel_player / sel_entity / sel_json)

- joueurs (@a, @p, @r sans type ou type=player) : `tag=mg.flw` fusionné dans les crochets (créés au besoin).
- entités (@e, @n, @p/@r avec un autre type) : `distance=0..` si aucun argument positionnel (x y z dx dy dz distance) — un sélecteur sans
  position balaie TOUTES les dimensions, `distance` le limite à celle de la source. @n est un sélecteur d'ENTITÉ (« @n[tag=npc] »).
- @s : jamais touché. Dans une chaîne : seul « "selector":"@x[...]" » est réécrit ; tout autre @x entre guillemets est laissé tel quel
  et compté (str_skipped). Les chaînes `Command:"..."` / `Command:'...'` (blocs de commande) sont renvoyées dans cmds : fl_rewrite les
  réécrit comme une ligne à part.
"""
import re

TAG = 'mg.flw'
POS = {'x', 'y', 'z', 'dx', 'dy', 'dz', 'distance'}
_STR_SEL = re.compile(r'@([aeprsn])(?:\[(.*)\])?$')
_KEY = re.compile(r'"?selector"?\s*:\s*$')
_CMD_KEY = re.compile(r'(?<!\w)["\']?Command["\']?\s*:\s*$')      # clé SNBT nue ou entre guillemets
_LAST_OUTPUT = re.compile(r'(,?)\s*(?<!\w)["\']?LastOutput["\']?\s*:\s*(?=["\'])')
_AT_IN_STR = re.compile(r'(?<![\w@])@[aeprn](?![\w])')
_TEXT_CMD = re.compile(r'(?:tell|msg|w|me|teammsg|tm)\s')     # commandes dont la fin de ligne est du texte libre (voir text_start)
_LEAD = re.compile(r'\s*[/$]?\s*')                              # espaces, `/` ou `$` de macro en tête de ligne


def skip_str(s, i):
    """Index qui suit la chaîne ouverte en s[i] (guillemet " ou '), antislash géré ; -1 si elle n'est pas fermée."""
    q, j = s[i], i + 1
    while j < len(s):
        if s[j] == '\\':
            j += 2
        elif s[j] == q:
            return j + 1
        else:
            j += 1
    return -1


def outside_strings(s):
    """s dont le contenu des chaînes entre guillemets est vidé (les guillemets restent) : pour chercher un motif hors chaînes.
    Une chaîne non fermée est vidée jusqu'à la fin de la ligne."""
    out, i = [], 0
    while i < len(s):
        if s[i] in '"\'':
            j = skip_str(s, i)
            out.append(s[i] + s[i])
            i = len(s) if j < 0 else j
        else:
            out.append(s[i])
            i += 1
    return ''.join(out)


def sub_outside(rx, repl, s):
    """re.subn de rx -> repl sur s, HORS des chaînes entre guillemets (laissées telles quelles ; une chaîne non fermée va jusqu'à la fin de
    la ligne) -> (texte, nombre de remplacements)."""
    out, n, i, start = [], 0, 0, 0
    while i < len(s):
        if s[i] in '"\'':
            j = skip_str(s, i)
            end = len(s) if j < 0 else j
            text, k = rx.subn(repl, s[start:i])
            out += [text, s[i:end]]
            n += k
            i = start = end
        else:
            i += 1
    text, k = rx.subn(repl, s[start:])
    return ''.join(out) + text, n + k


def text_start(s):
    """Index où commence le texte LIBRE d'une commande de message (`tell` `msg` `w` `me` `teammsg` `tm`, en tête de ligne ou derrière un
    ` run `) ; len(s) si la ligne n'en a pas. Ce qui suit n'est pas une commande : `msg @p go back in overworld` ne désigne aucune dimension.
    La première commande de message de la chaîne d'execute gagne (un ` run ` du texte libre ne compte donc pas)."""
    for k in [_LEAD.match(s).end()] + scan(s)[1]:
        if _TEXT_CMD.match(s, k):
            return k
    return len(s)


def strip_last_output(s):
    """Retire les propriétés NBT `LastOutput:'...'` / `LastOutput:"..."` (dernier message d'un bloc de commande : bruit, et l'UUID
    de l'auteur), virgule voisine comprise. Une chaîne non fermée laisse la ligne telle quelle."""
    pos = 0
    while True:
        m = _LAST_OUTPUT.search(s, pos)
        if not m:
            return s
        end = skip_str(s, m.end())
        if end < 0:
            return s
        a = m.start()
        if not m.group(1) and s[end:end + 1] == ',':
            end += 1                                    # première propriété : on retire la virgule qui la suit
        s = s[:a] + s[end:]
        pos = a


def close(s, k):
    """Index du ] qui ferme le [ de s[k] (imbrication [] {} et chaînes NBT/JSON gérées) ; -1 si déséquilibré."""
    depth, i = 0, k
    while i < len(s):
        c = s[i]
        if c in '"\'':
            i = skip_str(s, i)
            if i < 0:
                return -1
            continue
        if c in '[{':
            depth += 1
        elif c in ']}':
            depth -= 1
            if depth == 0:
                return i if c == ']' else -1
        i += 1
    return -1


def split_args(inner):
    """Arguments de premier niveau d'un crochet de sélecteur (virgules hors [] {} et chaînes) ; None si chaîne non fermée."""
    out, depth, start, i = [], 0, 0, 0
    while i < len(inner):
        c = inner[i]
        if c in '"\'':
            i = skip_str(inner, i)
            if i < 0:
                return None
            continue
        if c in '[{':
            depth += 1
        elif c in ']}':
            depth -= 1
        elif c == ',' and depth == 0:
            out.append(inner[start:i])
            start = i + 1
        i += 1
    out.append(inner[start:])
    return [p for p in out if p.strip()]


def fix_selector(letter, inner):
    """(lettre, texte entre crochets ou None) -> (nouveau texte entre crochets, 'player'|'entity'|None) ; None = inchangé."""
    if letter == 's':
        return None, None
    parts = split_args(inner or '')
    if parts is None:
        return None, None
    pairs = [(p.split('=', 1)[0].strip(), p.split('=', 1)[1].strip() if '=' in p else '') for p in parts]
    types = [v for k, v in pairs if k == 'type']
    if letter == 'a' or (letter in 'pr' and all(t in ('player', 'minecraft:player') for t in types)):
        kind, add = 'player', f'tag={TAG}'
        if ('tag', TAG) in pairs:
            return None, None
    else:
        kind, add = 'entity', 'distance=0..'
        if any(k in POS for k, _ in pairs):
            return None, None
    base = inner.rstrip().rstrip(',') if inner else ''
    return (f'{base},{add}' if base.strip() else add), kind


def scan(s, st=None):
    """-> (spans, runs, cmds) : spans [(début, fin, lettre, intérieur des crochets|None, json)] des sélecteurs à examiner ;
    runs = index qui suit chaque ' run ' (hors chaînes) ; cmds [(début, fin, guillemet)] des corps de chaînes `Command:`.
    Les autres chaînes sont sautées (sauf "selector":"@x") ; st reçoit les avertissements."""
    spans, runs, cmds, i, n = [], [], [], 0, len(s)
    while i < n:
        c = s[i]
        if c in '"\'':
            j = skip_str(s, i)
            if j < 0:
                if st:
                    st.warn('chaîne non fermée', s)
                break
            body = s[i + 1:j - 1]
            m = _STR_SEL.match(body) if c == '"' and _KEY.search(s[:i]) else None
            if _CMD_KEY.search(s[:i]):
                cmds.append((i + 1, j - 1, c))
            elif m and '\\' not in body:
                spans.append((i + 1, j - 1, m.group(1), m.group(2), True))
            elif _AT_IN_STR.search(body) and st:
                st.str_skipped += 1
                if len(st.str_examples) < 12:
                    st.str_examples.append(s[:150])
            i = j
        elif c == '@' and i + 1 < n and s[i + 1] in 'aeprsn' and not (i and (s[i - 1].isalnum() or s[i - 1] in '_@')) \
                and not (i + 2 < n and (s[i + 2].isalnum() or s[i + 2] == '_')):
            if i + 2 < n and s[i + 2] == '[':
                e = close(s, i + 2)
                if e < 0:
                    if st:
                        st.warn('crochet de sélecteur déséquilibré', s)
                    i += 2
                    continue
                spans.append((i, e + 1, s[i + 1], s[i + 3:e], False))
                i = e + 1
            else:
                spans.append((i, i + 2, s[i + 1], None, False))
                i += 2
        elif s.startswith(' run ', i):
            runs.append(i + 5)
            i += 5
        else:
            i += 1
    return spans, runs, cmds


def apply(s, st):
    """Réécrit les sélecteurs de la ligne s (compteurs dans st)."""
    out, last = [], 0
    for a, b, letter, inner, js in scan(s, st)[0]:
        new, kind = fix_selector(letter, inner)
        if new is None:
            continue
        out += [s[last:a], f'@{letter}[{new}]']
        last = b
        if kind == 'player':
            st.sel_player += 1
        else:
            st.sel_entity += 1
        st.sel_json += js
    return ''.join(out) + s[last:]
