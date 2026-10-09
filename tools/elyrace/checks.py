"""Controles statiques de la Course d'elytres (gen_elyrace.py --check) : coherence des fonctions generees, desinstallation,
zones de construction, budget des tranches, fichiers du depot a jour, pilote automatique. Boucle sur tous les parcours.
Le contre-la-montre solo et les branchements du moteur sont controles par checks_solo.py.
Python stdlib uniquement (compatible 3.8).
"""
import os
import re

import build_chain as B
import checks_solo as CS
import course_common as CC
import course_fns as CF
import dispatch as D
import game as G
import menus as M
import records as RC
import verify as V

LOADED_LINE = re.compile(r'execute store success score \$xbl mg\.st unless block -?\d+ %d -?\d+ minecraft:bedrock$' % B.PROBE_Y)
CHUNK = 16
Y_MIN, Y_MAX = -64, 319             # hauteur du monde : toute commande generee doit y tenir
GAP = 2 * CHUNK                     # ecart minimal entre les bandes de deux parcours
RESERVED_GAP = 16                   # marge minimale avec la zone d'un autre jeu
VARIANT_IDS = (100, 196)            # ids de lancement des variantes (tools/variantes/gen_variants.py), remappes par mg:var/remap
RESERVED = [                        # zones des autres jeux voisines : (nom, x1, x2, z1, z2), bornes incluses
    ('TNT Tag 1', -25, 25, 26475, 26525), ('TNT Tag 2', -25, 25, 26775, 26825), ('TNT Tag 3', -25, 25, 27375, 27425),
    ('Elytra (mg:sky)', -205, 205, 27590, 29091),     # sortie de tools/sky/gen_sky.py : courses x -200..200 z 27600..28400, survie centree (0, 29000)
]


def code_lines(files, name):
    return [l for l in files[CC.FN + name + '.mcfunction'].split('\n') if l and not l.startswith('#')]


def reachable(files, start):
    """Fonctions mg: atteintes transitivement depuis `start` (les fonctions hors generateur sont atteintes mais pas suivies),
    lignes `forceload add` rencontrees et `schedule clear` rencontres dans les fonctions generees suivies."""
    seen, todo, adds, clears = set(), [start], [], set()
    while todo:
        name = todo.pop()
        if name in seen:
            continue
        seen.add(name)
        rel = 'data/mg/function/' + name + '.mcfunction'
        if rel not in files:
            continue
        for line in files[rel].split('\n'):
            if line and not line.startswith('#'):
                if re.search(r'\bforceload add\b', line):
                    adds.append('%s : %s' % (name, line))
                clears.update(re.findall(r'\bschedule clear mg:([a-z_0-9/]+)', line))
                todo += re.findall(r'\bfunction mg:([a-z_0-9/]+)', line)
    return seen, adds, clears


def uninstall_problems(files):
    bad = []
    seen, adds, clears = reachable(files, 'elyrace/uninstall')
    if 'core/forceloads' in seen or adds:
        bad.append('uninstall ne doit atteindre ni core/forceloads ni forceload add (desinstaller vient de tout retirer) : %s'
                   % (['core/forceloads'] * ('core/forceloads' in seen) + adds))
    scheduled = set()
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            scheduled.update(re.findall(r'\bschedule function mg:([a-z_0-9/]+)', text))
    for name in sorted(scheduled - clears):
        bad.append('schedule function mg:%s n\'a pas son schedule clear atteint depuis uninstall' % name)
    return bad


def spec_problems(specs):
    """Convention commune des specs et zones des parcours."""
    bad = []
    nums = [s.NUM for s in specs]
    if nums != list(range(1, len(specs) + 1)) or len(specs) > D.N_ROUTES:
        bad.append('NUM des parcours : %s (attendu 1..%d, au plus %d)' % (nums, len(specs), D.N_ROUTES))
    for s in specs:
        if (s.EDGE_X, s.GATE_X) != (G.EDGE_X, G.GATE_X):
            bad.append('parcours %d : plateforme de depart non standard (EDGE_X %d, GATE_X %d)' % (s.NUM, s.EDGE_X, s.GATE_X))
        if not s.X0 < s.EDGE_X < s.X1 < 2000:
            bad.append('parcours %d : X0 %d, EDGE_X %d, X1 %d : il faut X0 < EDGE_X < X1 < 2000 (cle de classement du temps ecoule)' % (s.NUM, s.X0, s.EDGE_X, s.X1))
        if sorted(s.R_UP) != sorted(s.CPS):
            bad.append('parcours %d : R_UP doit avoir exactement une entree par point de reprise %s' % (s.NUM, sorted(s.CPS)))
        for what, chunk_aligned in (('X0', s.X0), ('Z0', s.Z0)):
            if chunk_aligned % CHUNK:
                bad.append('parcours %d : %s %d n\'est pas aligne sur un chunk' % (s.NUM, what, chunk_aligned))
        if not (s.Z0 <= s.CZ - 32 and s.CZ + 32 < s.Z1):
            bad.append('parcours %d : la zone de depart (CZ +- 32) sort de la bande z' % s.NUM)
        for sl in range(1, B.n_slices(s) + 1):          # aucune tranche de construction ne s'approche d'un autre jeu
            xa, xb = B.slice_box(s, sl)
            for name, rx1, rx2, rz1, rz2 in RESERVED:
                if xa - RESERVED_GAP <= rx2 and rx1 <= xb + RESERVED_GAP and s.Z0 - RESERVED_GAP <= rz2 and rz1 <= s.Z1 - 1 + RESERVED_GAP:
                    bad.append('parcours %d, tranche %d : a moins de %d blocs de %s' % (s.NUM, sl, RESERVED_GAP, name))
    for i, s in enumerate(specs):
        for t in specs[i + 1:]:
            if s.Z0 - GAP < t.Z1 and t.Z0 - GAP < s.Z1:
                bad.append('bandes z des parcours %d et %d : moins de %d blocs d\'ecart' % (s.NUM, t.NUM, GAP))
    return bad


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


def course_problems(c):
    """Controles par parcours : zone chargee au depart, hauteur et emprise des commandes, budget des tranches."""
    s, bad = c.spec, []
    fx1, fz1, fx2, fz2 = CF.fl_box(s)
    last = min(2, B.n_slices(s))                  # la zone de depart chargee deborde d'un chunk sur la tranche 2 (Canyon : x -16..80)
    if fx1 // CHUNK < B.slice_box(s, 1)[0] // CHUNK or fx2 // CHUNK > B.slice_box(s, last)[1] // CHUNK or not s.Z0 <= fz1 <= fz2 < s.Z1:
        bad.append('parcours %d : fl_add (x %d..%d, z %d..%d) sort des tranches 1 a %d' % (s.NUM, fx1, fx2, fz1, fz2, last))
    # hauteurs des teleportations (pas des commandes de construction) : perchoir de depart (START_Y + 19, spawnpoint compris : +20)
    # et reprises (centre de l'anneau + R_UP, + 1 pour le corps du joueur)
    top = max([s.START_Y + 20] + [c.rings[n - 1][1] + s.R_UP[n] + 1 for n in c.cps])
    if top > Y_MAX:
        bad.append('parcours %d : une teleportation (perchoir, reprise) monte a y %d, au-dessus de la hauteur max %d' % (s.NUM, top, Y_MAX))
    cmds = [('fill',) + tuple(r) for r in c.rects] + list(c.world.cmds)
    for cmd in cmds:
        if cmd[0] == 'set':
            ys, zs = (cmd[2],), (cmd[3],)
        else:
            ys, zs = (cmd[2], cmd[5]), (cmd[3], cmd[6])
        if min(ys) < Y_MIN or max(ys) > Y_MAX:
            bad.append('parcours %d : commande hors hauteur [%d, %d] : %s' % (s.NUM, Y_MIN, Y_MAX, cmd[:7]))
            break
        if min(zs) < s.Z0 or max(zs) >= s.Z1:
            bad.append('parcours %d : commande hors de la bande z [%d, %d[ : %s' % (s.NUM, s.Z0, s.Z1, cmd[:7]))
            break
    for k in range(1, B.n_slices(s) + 1):
        n = len(B.slice_commands(c, k))
        print('  parcours %d, tranche %2d : %5d commandes' % (s.NUM, k, n))
        if n > B.SLICE_BUDGET:
            bad.append('parcours %d, tranche %d : %d commandes (budget %d)' % (s.NUM, k, n, B.SLICE_BUDGET))
    if hasattr(s, 'extra_checks'):                # controles propres au parcours (blocs interdits, lumiere de la grotte...)
        bad += ['parcours %d : %s' % (s.NUM, b) for b in s.extra_checks(c)]
    return bad


def loaded_problems(files, s):
    bad = []
    for k in range(1, B.n_slices(s) + 1):
        lines = code_lines(files, 'c%d/loaded_%d' % (s.NUM, k))
        body = lines[:-1]
        if lines[-1:] != ['return 1'] or not body or len(body) % 2:
            bad.append('c%d/loaded_%d : forme inattendue' % (s.NUM, k))
            continue
        for a, b in zip(body[::2], body[1::2]):
            if not LOADED_LINE.match(a) or b != 'execute if score $xbl mg.st matches 0 run return fail':
                bad.append('c%d/loaded_%d : sonde non conforme au motif de dropadv/loaded_all : %s' % (s.NUM, k, a))
                break
    return bad


def logic_problems(files, specs):
    """Controles statiques de la logique des fonctions, que le pilote automatique (il simule le vol, pas les fonctions) ne voit pas."""
    bad = uninstall_problems(files)
    passes = [CC.FN + 'c%d/pass.mcfunction' % s.NUM for s in specs]
    for s in specs:
        pass_lines = code_lines(files, 'c%d/pass' % s.NUM)
        if not pass_lines or pass_lines[0] != 'scoreboard players add @s mg.xa 1':
            bad.append('c%d/pass : la premiere commande doit etre « scoreboard players add @s mg.xa 1 » (sinon aucun anneau n\'est jamais compte)' % s.NUM)
    adders = sorted(rel for rel, text in files.items() if re.search(r'players add @\S+ mg\.xa ', text))
    if adders != sorted(passes):
        bad.append('mg.xa doit etre incremente par les pass des parcours seulement : %s' % adders)
    known = {'mg.' + o[0] for o in G.OBJECTIVES} | set(G.TAGS) | {'mg.xs'} | {'mg.' + RC.obj(s) for s in specs}
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            for m in sorted(set(re.findall(r'\bmg\.x[a-z0-9]+', text)) - known):
                bad.append('%s : objectif ou etiquette inconnu %s' % (rel, m))
    for s in specs:
        bad += loaded_problems(files, s)
    return bad


def check(root, courses, files):
    """Renvoie la liste des problemes (vide = tout est bon)."""
    specs = [c.spec for c in courses]
    bad = spec_problems(specs) + id_problems(root, specs) + logic_problems(files, specs) + CS.problems(root, files, specs)
    names = {rel[len('data/mg/function/'):-len('.mcfunction')] for rel in files if rel.endswith('.mcfunction')}
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            for m in re.finditer(r'\bfunction mg:([a-z_0-9/]+)', text):
                if m.group(1) not in names and not os.path.exists(os.path.join(root, 'data/mg/function', m.group(1) + '.mcfunction')):
                    bad.append('%s : fonction inconnue mg:%s' % (rel, m.group(1)))
    for c in courses:
        print('parcours %d (%s) : %d anneaux, %d anneaux d\'or, reprises apres %s' % (c.spec.NUM, c.spec.NAME, len(c.rings), len(c.golds), c.cps))
        margin_bad, info = V.speed_margins(c, G.DROP_SQ, G.DROP_REL)
        print('\n'.join('  ' + i for i in info))
        bad += ['parcours %d, repli de choc : %s' % (c.spec.NUM, b) for b in margin_bad]
        bad += course_problems(c)
        bad += ['parcours %d, pilote automatique : %s' % (c.spec.NUM, b) for b in V.verify_all(c)]
    for rel, text in files.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            bad.append('%s : absent (lancer le generateur)' % rel)
        elif read_text(p) != text:
            bad.append('%s : differe de la sortie du generateur' % rel)
    stale = sorted(stale_files(root, files))
    bad += ['%s : fichier du depot que le generateur ne produit plus (a supprimer)' % rel for rel in stale]
    return bad


def stale_files(root, files):
    """Fichiers .mcfunction de elyrace/ (sous-dossiers compris) que le generateur ne produit plus."""
    base = os.path.join(root, CC.FN)
    out = []
    for d, _, names in os.walk(base):
        for n in names:
            if n.endswith('.mcfunction'):
                rel = os.path.relpath(os.path.join(d, n), root).replace(os.sep, '/')
                if rel not in files:
                    out.append(rel)
    return out
