"""Controles de la Course d'elytres qui lisent le depot (gen_elyrace.py --check), a lancer apres wire_elyrace*.py,
gen_setup_watch.py et gen_variants.py : ids de lancement (core/go, core/request), ouvertures de fenetre (forme finale de
gen_rating.py), drapeaux du suivi de mg:setup. Ces fichiers ne sont pas produits par le generateur de la course.
Python stdlib uniquement (compatible 3.8).
"""
import os
import re

import game as G
import menus as M

VARIANT_IDS = (100, 196)            # ids de lancement des variantes (tools/variantes/gen_variants.py), remappes par mg:var/remap
WATCH = 'data/mg/function/core/setup_watch.mcfunction'     # sortie de tools/setup/gen_setup_watch.py


def read_text(path):
    with open(path, encoding='utf-8', newline='') as fh:
        return fh.read().replace('\r\n', '\n')


def id_problems(root, specs):
    """Ids de lancement des parcours (menus.route_id) : dans la plage de core/go, convertis en jeu 66 par core/request, et
    absents de ses autres remappages (TNT Tag, Bedwars, Elytra, Quakecraft sniper 79..80...) comme des variantes 100..196
    (remappees par mg:var/remap). Lit le depot : a lancer apres wire_elyrace2.py."""
    bad = []
    ids = {s.NUM: M.route_id(s) for s in specs}
    ids[0] = G.GAME_ID                    # 0 = au hasard : id 66, pas converti
    for num, i in sorted(ids.items()):
        if VARIANT_IDS[0] <= i <= VARIANT_IDS[1]:
            bad.append('l\'id %d (parcours %d) est dans la plage des variantes %d..%d' % (i, num, VARIANT_IDS[0], VARIANT_IDS[1]))
    base = os.path.join(root, 'data', 'mg', 'function', 'core')
    go = read_text(os.path.join(base, 'go.mcfunction'))
    top = re.search(r'mg\.go matches 1\.\.(\d+)', go)
    if not top or max(ids.values()) > int(top.group(1)):
        bad.append('core/go : la plage acceptee (%s) ne couvre pas les ids %s' % (top and top.group(0), sorted(ids.values())))
    ranges, ours = [], []
    lines = [l for l in read_text(os.path.join(base, 'request.mcfunction')).split('\n') if l and not l.startswith('#')]
    for line in lines:
        m = re.search(r'matches (\d+)(?:\.\.(\d+))? run scoreboard players set \$game mg\.st (\d+)\s*$', line)
        if m:
            lo, hi, target = int(m.group(1)), int(m.group(2) or m.group(1)), int(m.group(3))
            (ours if target == G.GAME_ID else ranges).append((lo, hi))
    for num, i in sorted(ids.items()):
        if num and not any(lo <= i <= hi for lo, hi in ours):
            bad.append('core/request : l\'id %d (parcours %d) n\'est pas converti en jeu %d' % (i, num, G.GAME_ID))
        for lo, hi in ranges:
            if lo <= i <= hi:
                bad.append('core/request : l\'id %d (parcours %d) est deja remappe (%d..%d)' % (i, num, lo, hi))
    bad += request_order_problems(lines)
    return bad


def request_order_problems(lines):
    """Bloc de conversion de core/request, dans l'ordre : $xc remis a 0, $xc = id, $xc - ID_BASE, $game = 66 (sinon un id
    de parcours donnerait un mauvais parcours, ou un lancement ordinaire garderait le $xc de la partie precedente)."""
    def first(pattern):
        found = [i for i, l in enumerate(lines) if re.search(pattern, l)]
        return found[0] if found else None
    steps = [('remise a 0 de $xc', r'^scoreboard players set \$xc mg\.st 0$'),
             ('$xc = $game', r'matches \d+\.\.\d+ run scoreboard players operation \$xc mg\.st = \$game mg\.st$'),
             ('$xc - %d' % M.ID_BASE, r'matches \d+\.\.\d+ run scoreboard players remove \$xc mg\.st %d$' % M.ID_BASE),
             ('$game = %d' % G.GAME_ID, r'matches \d+\.\.\d+ run scoreboard players set \$game mg\.st %d$' % G.GAME_ID)]
    pos = [first(p) for _, p in steps]
    bad = ['core/request : etape de conversion absente : %s' % name for (name, _), i in zip(steps, pos) if i is None]
    if not bad and pos != sorted(pos):
        bad.append('core/request : conversion des ids de parcours dans le mauvais ordre (%s)' % ', '.join(n for n, _ in steps))
    test66 = first(r'\$game mg\.st matches %d\b' % G.GAME_ID)
    if not bad and test66 is not None and test66 < pos[-1]:
        bad.append('core/request : une ligne teste le jeu %d avant la fin de la conversion des ids de parcours' % G.GAME_ID)
    return bad


def rate_problems(root, files):
    """Ouvertures de fenetres sous leur forme finale (celle de gen_rating.py, que gen_variants.py relance) : aucun `dialog show @s mg:X`
    restant, et chaque `function mg:rate/d/X` avec `with storage mg:rate lab` si, et seulement si, la 1re ligne de code de
    rate/d/X.mcfunction est une macro (commence par `$`). Lit le depot : rate/d/ est produit par gen_rating.py, pas par ce generateur."""
    bad = []
    for rel, text in sorted(files.items()):
        if not rel.endswith('.mcfunction'):
            continue
        if re.search(r'\bdialog show @s mg:', text):
            bad.append('%s : `dialog show @s mg:...` : ecrire `function mg:rate/d/<fenetre>` (menus.rate_call), forme finale de gen_rating.py' % rel)
        for m in re.finditer(r'\bfunction mg:rate/d/([a-z_0-9]+)( with storage mg:rate lab)?(?=\s|$)', text):
            path = os.path.join(root, 'data', 'mg', 'function', 'rate', 'd', m.group(1) + '.mcfunction')
            if not os.path.exists(path):
                bad.append('%s : mg:rate/d/%s absent du depot (lancer gen_variants.py, qui relance gen_rating.py)' % (rel, m.group(1)))
                continue
            code = [l for l in read_text(path).split('\n') if l and not l.startswith('#')]
            macro = bool(code) and code[0].startswith('$')
            if macro != bool(m.group(2)):
                bad.append('%s : mg:rate/d/%s est %s mais l\'appel est %s `with storage mg:rate lab`' % (
                    rel, m.group(1), 'une macro' if macro else 'statique', 'sans' if macro else 'avec'))
    return bad


def setup_problems(root, specs):
    """Suivi de la fin de /function mg:setup (core/setup_watch, ecrit par tools/setup/gen_setup_watch.py avec la liste de drapeaux
    codee en dur dans JOBS) : il doit tester exactement les drapeaux FLAG des parcours (storage mg:elyrace), sinon la generation
    n'est jamais annoncee terminee (drapeau jamais pose) ou l'est trop tot."""
    path = os.path.join(root, WATCH)
    if not os.path.exists(path):
        return ['%s : absent (lancer tools/setup/gen_setup_watch.py)' % WATCH]
    tested = set(re.findall(r'if data storage mg:elyrace (\S+)', read_text(path)))
    own = {s.FLAG: s for s in specs}
    fix = ' : mettre a jour JOBS dans tools/setup/gen_setup_watch.py puis le relancer (PYTHONUTF8=1)'
    bad = ['core/setup_watch : le drapeau %s du parcours %d (%s) n\'est pas teste (storage mg:elyrace)%s' % (f, s.NUM, s.NAME, fix)
           for f, s in sorted(own.items()) if f not in tested]
    bad += ['core/setup_watch : teste le drapeau %s de mg:elyrace, qu\'aucun parcours ne pose%s' % (f, fix) for f in sorted(tested - set(own))]
    return bad
