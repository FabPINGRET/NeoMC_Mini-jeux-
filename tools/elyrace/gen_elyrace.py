"""Course d'elytres (id 66) : parcours 1, le Canyon du Couchant. Usage (depuis la racine du depot) :
    python tools/elyrace/gen_elyrace.py <racine du depot>            ecrit les fichiers generes
    python tools/elyrace/gen_elyrace.py <racine du depot> --check    ne ecrit rien : budget de commandes, vol de verification
                                                                     du pilote automatique, references de fonctions, et fichiers
                                                                     du depot identiques a ce que le generateur produirait
Sortie : data/mg/function/elyrace/**, core/sub/elyrace, dialog/sub_elyrace.json, advancement/elyrace_wall.json,
tags/damage_type/elyrace_wall.json. Les fichiers generes ne se modifient jamais a la main.
Python stdlib uniquement (compatible 3.8).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_canyon as K          # noqa: E402
import game as G                   # noqa: E402
import menus as M                  # noqa: E402
import rings as R                  # noqa: E402
import terrain as T                # noqa: E402
import verify as V                 # noqa: E402

SLICE = 96                          # largeur d'une tranche de construction (6 chunks)
N_SLICES = (K.X1 - K.X0) // SLICE   # 11 : chacune est chargee de force, remplie, puis liberee
SLICE_BUDGET = 20000                # commandes par tranche (limite de la chaine de commandes : 65 536)
PROBE_Y = 310                       # au-dessus de tout decor : jamais de bedrock a cette altitude
FN = 'data/mg/function/elyrace/'


def lines_to_text(lines):
    return '\n'.join(lines) + '\n'


def slice_box(k):
    xa = K.X0 + SLICE * (k - 1)
    return xa, xa + SLICE - 1


def slice_commands(c, k):
    """Commandes de la tranche k : relief puis decors, restreints a la tranche, fills decoupes a 32 768 blocs."""
    xa, xb = slice_box(k)
    out = []
    for cmd in [('fill',) + tuple(r) for r in c.rects] + list(c.world.cmds):
        cl = T.clip_cmd(cmd, xa, xb)
        if cl is None:
            continue
        for part in (T.split_fill(cl) if cl[0] == 'fill' else [cl]):
            out.append(T.cmd_text(part))
    return out


def forceload(op, k):
    xa, xb = slice_box(k)
    return 'forceload %s %d %d %d %d' % (op, xa, K.Z0, xb, K.Z1 - 1)


def loaded_lines(k):
    xa, xb = slice_box(k)
    out = ['# Tranche %d : tous les chunks sont chargés ? Même motif que mg:dropadv/loaded_all : « unless block … bedrock » ne réussit' % k,
           '# que si le chunk est chargé (il n\'y a jamais de bedrock à y %d) ; sinon le score reste à 0 et la fonction échoue' % PROBE_Y]
    for x in range(xa + 8, xb + 1, 16):
        for z in range(K.Z0 + 8, K.Z1, 16):
            out.append('execute store success score $xbl mg.st unless block %d %d %d minecraft:bedrock' % (x, PROBE_Y, z))
            out.append('execute if score $xbl mg.st matches 0 run return fail')
    out.append('return 1')
    return out


def build_lines():
    return ['# (OP) Construit le Canyon du Couchant en %d tranches de %d blocs (chargées de force une à une)' % (N_SLICES, SLICE),
            '# pas pendant une partie de la course : build_abort libérerait la zone de départ chargée par fl_add',
            'execute if score $game mg.st matches 66 unless score $state mg.st matches 0 run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : construction impossible pendant une partie.","color":"red"}]',
            'function mg:elyrace/build_abort',
            'data remove storage mg:elyrace v1',
            'scoreboard players set $xbk mg.st 1',
            'scoreboard players set $xbw mg.st 0',
            forceload('add', 1),
            'schedule function mg:elyrace/build_wait 20t']


def build_wait_lines():
    out = ['# Attend le chargement de la tranche $xbk puis la construit']
    for k in range(1, N_SLICES + 1):
        out.append('execute if score $xbk mg.st matches %d if function mg:elyrace/loaded_%d run return run function mg:elyrace/build_%d' % (k, k, k))
    out += ['scoreboard players add $xbw mg.st 1',
            '# 2 minutes sans chargement : message, puis on libère les chargements forcés des tranches et on s\'arrête',
            'execute if score $xbw mg.st matches 120.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Course d\'élytres : zone pas chargée (tranche ","color":"red"},{"score":{"name":"$xbk","objective":"mg.st"},"color":"red"},{"text":"). Relance /function mg:elyrace/build.","color":"red"}]',
            'execute if score $xbw mg.st matches 120.. run return run function mg:elyrace/build_abort',
            'schedule function mg:elyrace/build_wait 20t']
    return out


def build_abort_lines():
    """Arret de la construction (attente expirée, nouvelle construction, désinstallation) : plus de chargement forcé de tranche."""
    out = ['# Arrête la construction : libère les chargements forcés des %d tranches puis rétablit ceux du jeu' % N_SLICES,
           'schedule clear mg:elyrace/build', 'schedule clear mg:elyrace/build_wait']
    out += [forceload('remove', k) for k in range(1, N_SLICES + 1)]
    out.append('function mg:core/forceloads')
    return out


def slice_lines(c, k):
    out = ['# Course d\'élytres : tranche %d / %d (x %d à %d)' % ((k, N_SLICES) + slice_box(k))] + slice_commands(c, k)
    out.append(forceload('remove', k))
    if k < N_SLICES:
        out += ['scoreboard players set $xbk mg.st %d' % (k + 1), 'scoreboard players set $xbw mg.st 0',
                forceload('add', k + 1), 'schedule function mg:elyrace/build_wait 20t']
    else:
        out += ['function mg:core/forceloads', 'data modify storage mg:elyrace v1 set value 1b',
                'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Course d\'élytres : Canyon du Couchant construit.","color":"green"}]']
    return out


def all_files(c):
    """Tous les fichiers generes : {chemin relatif a la racine: texte}."""
    files = {}
    fns = G.functions()
    fns.update(R.functions(c))
    fns['build'] = build_lines()
    fns['build_wait'] = build_wait_lines()
    fns['build_abort'] = build_abort_lines()
    for k in range(1, N_SLICES + 1):
        fns['build_%d' % k] = slice_lines(c, k)
        fns['loaded_%d' % k] = loaded_lines(k)
    for name, lines in fns.items():
        files[FN + name + '.mcfunction'] = lines_to_text(lines)
    files['data/mg/function/core/sub/elyrace.mcfunction'] = lines_to_text(M.sub_lines())
    files['data/mg/dialog/sub_elyrace.json'] = M.dumps(M.dialog_json())
    files['data/mg/advancement/elyrace_wall.json'] = M.dumps(M.advancement_json())
    files['data/mg/tags/damage_type/elyrace_wall.json'] = M.dumps(M.damage_tag_json())
    return files


def write_all(root, files):
    d = os.path.join(root, FN)
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):                                 # tranches disparues : on repart d'un dossier propre
        if f.endswith('.mcfunction'):
            os.remove(os.path.join(d, f))
    for rel, text in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)


TAGS = {'mg.xw1', 'mg.xtp'}         # etiquettes temporaires de la fin de course (pas des objectifs)
LOADED_LINE = re.compile(r'execute store success score \$xbl mg\.st unless block -?\d+ %d -?\d+ minecraft:bedrock$' % PROBE_Y)


def code_lines(files, name):
    return [l for l in files[FN + name + '.mcfunction'].split('\n') if l and not l.startswith('#')]


def reachable(files, start):
    """Fonctions mg: atteintes transitivement depuis `start` (les fonctions hors generateur sont atteintes mais pas suivies),
    et lignes `forceload add` rencontrees dans les fonctions generees suivies."""
    seen, todo, adds = set(), [start], []
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
                todo += re.findall(r'\bfunction mg:([a-z_0-9/]+)', line)
    return seen, adds


def logic_problems(files):
    """Controles statiques de la logique des fonctions, que le pilote automatique (il simule le vol, pas les fonctions) ne voit pas."""
    bad = []
    seen, adds = reachable(files, 'elyrace/uninstall')
    if 'core/forceloads' in seen or adds:
        bad.append('uninstall ne doit atteindre ni core/forceloads ni forceload add (desinstaller vient de tout retirer) : %s'
                   % (['core/forceloads'] * ('core/forceloads' in seen) + adds))
    pass_lines = code_lines(files, 'pass')
    if not pass_lines or pass_lines[0] != 'scoreboard players add @s mg.xa 1':
        bad.append('pass : la premiere commande doit etre « scoreboard players add @s mg.xa 1 » (sinon aucun anneau n\'est jamais compte)')
    adders = sorted(rel for rel, text in files.items() if re.search(r'players add @\S+ mg\.xa ', text))
    if adders != [FN + 'pass.mcfunction']:
        bad.append('mg.xa doit etre incremente par pass seulement : %s' % adders)
    known = {'mg.' + o[0] for o in G.OBJECTIVES} | TAGS
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            for m in sorted(set(re.findall(r'\bmg\.x[a-z0-9]+', text)) - known):
                bad.append('%s : objectif ou etiquette inconnu %s' % (rel, m))
    for k in range(1, N_SLICES + 1):
        lines = code_lines(files, 'loaded_%d' % k)
        body = lines[:-1]
        if lines[-1:] != ['return 1'] or not body or len(body) % 2:
            bad.append('loaded_%d : forme inattendue' % k)
            continue
        for a, b in zip(body[::2], body[1::2]):
            if not LOADED_LINE.match(a) or b != 'execute if score $xbl mg.st matches 0 run return fail':
                bad.append('loaded_%d : sonde non conforme au motif de dropadv/loaded_all : %s' % (k, a))
                break
    return bad


def check(root, c, files):
    """Renvoie la liste des problemes (vide = tout est bon)."""
    bad = logic_problems(files)
    margin_bad, info = V.speed_margins(c, G.DROP_SQ, G.DROP_REL)
    print('\n'.join('  ' + i for i in info))
    bad += ['repli de choc : ' + b for b in margin_bad]
    names = {rel[len('data/mg/function/'):-len('.mcfunction')] for rel in files if rel.endswith('.mcfunction')}
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            for m in re.finditer(r'\bfunction mg:([a-z_0-9/]+)', text):
                if m.group(1) not in names and not os.path.exists(os.path.join(root, 'data/mg/function', m.group(1) + '.mcfunction')):
                    bad.append('%s : fonction inconnue mg:%s' % (rel, m.group(1)))
    for k in range(1, N_SLICES + 1):
        n = len(slice_commands(c, k))
        print('  tranche %2d : %5d commandes' % (k, n))
        if n > SLICE_BUDGET:
            bad.append('tranche %d : %d commandes (budget %d)' % (k, n, SLICE_BUDGET))
    for rel, text in files.items():
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            bad.append('%s : absent (lancer le generateur)' % rel)
        elif open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n') != text:
            bad.append('%s : differe de la sortie du generateur' % rel)
    bad += ['pilote automatique : ' + b for b in V.verify_all(c)]
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1:
        raise SystemExit(__doc__)
    root = os.path.abspath(args[0])
    c = K.build()
    files = all_files(c)
    print('%d fichiers, %d anneaux, %d anneaux d\'or, reprises apres les anneaux %s' % (len(files), len(c.rings), len(c.golds), c.cps))
    if '--check' in sys.argv:
        bad = check(root, c, files)
        print('\n'.join(bad) if bad else 'CHECK OK (budget, pilote automatique, references, fichiers a jour)')
        sys.exit(1 if bad else 0)
    write_all(root, files)
    print('ecrit dans', os.path.join(root, 'data', 'mg'))


if __name__ == '__main__':
    main()
