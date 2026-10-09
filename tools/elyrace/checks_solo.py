"""Controles statiques du contre-la-montre solo et des records (appeles par checks.py) : le solo partage $game 66 et $state avec la
course de groupe, il ne tient donc que par des gardes sur $xs ; chacune est verifiee ici, ainsi que les 4 branchements dans le moteur
(core/tick, countdown, begin, reconnect), poses par wire_elyrace3.py. Aucun import de checks.py (il importe ce module).
Python stdlib uniquement (compatible 3.8).
"""
import os
import re

import course_common as CC
import game as G
import menus as M

NOT_SOLO = 'unless score $xs mg.st matches 1'
DRAW_TARGETS = {'draw': {'draw'}, 'end': {'draw', 'win_player'}, 'timeout': {'draw', 'win_player'}}    # fonction elyrace -> appels core/ permis
REFUSAL = re.compile(r'^execute .* run return run tellraw @s ')


def code(text):
    return [l for l in text.split('\n') if l and not l.startswith('#')]


def fn_code(files, name):
    return code(files[CC.FN + name + '.mcfunction'])


def repo_code(root, rel):
    with open(os.path.join(root, 'data', 'mg', 'function', rel + '.mcfunction'), encoding='utf-8', newline='') as fh:
        return code(fh.read().replace('\r\n', '\n'))


def draw_problems(files):
    """core/draw et core/win_player ne sont appeles que par elyrace/draw, end et timeout, dont la 1re commande renvoie vers solo/end en solo."""
    bad = []
    for rel, text in sorted(files.items()):
        if rel.endswith('.mcfunction'):
            name = rel[len(CC.FN):-len('.mcfunction')]
            for line in code(text):
                for target in re.findall(r'\bfunction mg:core/(draw|win_player)\b', line):
                    if target not in DRAW_TARGETS.get(name, ()):
                        bad.append('%s : appelle core/%s sans passer par la garde du solo : %s' % (rel, target, line))
    for name in ('end', 'timeout'):
        if fn_code(files, name)[:1] != [G.SOLO_GUARD]:
            bad.append('elyrace/%s : la premiere commande doit etre la garde du solo (%s)' % (name, G.SOLO_GUARD))
    if not fn_code(files, 'draw')[:1] or not fn_code(files, 'draw')[0].startswith('execute if score $xs mg.st matches 1 run return run function mg:elyrace/solo/end'):
        bad.append('elyrace/draw : la premiere commande doit renvoyer vers solo/end quand $xs vaut 1')
    return bad


def records_problems(files):
    """Records et drapeau du solo : jamais remis a zero par une preparation de partie (prepare remet G.OBJECTIVES a zero a chaque depart)."""
    bad = ['G.OBJECTIVES contient mg.%s : prepare le remettrait a zero a chaque depart' % n for n, _, _ in G.OBJECTIVES if n == 'xs' or re.match(r'xr\d+$', n)]
    for line in fn_code(files, 'prepare'):
        if re.search(r'\bmg\.(xs|xr\d+)\b', line):
            bad.append('elyrace/prepare : touche un record ou le trigger du solo : %s' % line)
    for rel, text in sorted(files.items()):
        if rel.endswith('.mcfunction'):
            for line in code(text):
                if re.search(r'scoreboard players (set|reset|add|remove) \S+ mg\.xr\d', line):
                    bad.append('%s : modifie un record autrement que par operation : %s' % (rel, line))
    return bad


def trigger_problems(files, specs):
    """Chaque valeur de /trigger mg.xs set <v> ecrite par le generateur (fonctions et fenetres) est traitee par solo/cmd, et par solo/start au-dela de 10."""
    handled = []
    for line in fn_code(files, 'solo/cmd'):
        m = re.search(r'#xv mg\.st matches (\d+)(\.\.)?\s', line)
        if m:
            handled.append((int(m.group(1)), bool(m.group(2))))
    top = M.SOLO_RANDOM + len(specs)
    bad, seen = [], set()
    for rel, text in sorted(files.items()):
        for v in re.findall(r'trigger mg\.xs set (\d+)', text):
            v = int(v)
            if v in seen:
                continue
            seen.add(v)
            if not any(v == lo or (opened and v >= lo) for lo, opened in handled):
                bad.append('%s : trigger mg.xs set %d n\'est traite par aucune ligne de solo/cmd' % (rel, v))
            if v >= M.SOLO_RANDOM and v > top:
                bad.append('%s : trigger mg.xs set %d : au-dela du dernier parcours (%d)' % (rel, v, top))
    if not seen:
        bad.append('aucun trigger mg.xs set <v> dans les fichiers generes (menus absents ?)')
    return bad


def hooks_problems(root):
    """Les 4 branchements du moteur (wire_elyrace3.py) sont presents dans le depot."""
    bad, hint = [], ' (lancer wire_elyrace3.py)'
    tick = repo_code(root, 'core/tick')
    for want in ('scoreboard players enable @a mg.xs', 'execute as @a[scores={mg.xs=1..}] run function mg:elyrace/solo/cmd'):
        if want not in tick:
            bad.append('core/tick : ligne absente : %s%s' % (want, hint))
    cd = repo_code(root, 'core/countdown')
    hook = 'execute if score $xs mg.st matches 1 if score $game mg.st matches 66 run return run function mg:elyrace/solo/countdown'
    dec = 'scoreboard players remove $timer mg.st 1'
    if hook not in cd or dec not in cd or cd.index(hook) > cd.index(dec):
        bad.append('core/countdown : l\'aiguillage vers solo/countdown doit preceder « %s » (sinon le chrono baisse deux fois)%s' % (dec, hint))
    stats = [l for l in repo_code(root, 'core/begin') if 'mg.stp' in l]
    if len(stats) != 2 or any(NOT_SOLO not in l for l in stats):
        bad.append('core/begin : les 2 lignes de statistique mg.stp doivent porter « %s » : %s%s' % (NOT_SOLO, stats, hint))
    horn = [l for l in repo_code(root, 'core/begin') if 'event.raid.horn' in l]
    own = 'execute if score $xs mg.st matches 1 as @a[tag=mg.play] at @s run playsound'
    if len(horn) != 2 or sum(l.startswith('execute ' + NOT_SOLO + ' ') for l in horn) != 1 or sum(l.startswith(own) for l in horn) != 1:
        bad.append('core/begin : le cor de raid doit etre joue a tout le lobby hors solo, et au joueur du solo seulement sinon : %s%s' % (horn, hint))
    spec = [l for l in repo_code(root, 'core/reconnect') if 'core/reconnect_spec' in l]
    if len(spec) != 1 or NOT_SOLO not in spec[0]:
        bad.append('core/reconnect : l\'appel de reconnect_spec doit porter « %s » : %s%s' % (NOT_SOLO, spec, hint))
    return bad


def order_problems(files):
    """Ordre de solo/start : refus, puis $xs, puis $state, puis prepare ; $xs remis a 0 par cleanup et announce."""
    bad = []
    lines = fn_code(files, 'solo/start')
    find = lambda s: lines.index(s) if s in lines else None
    xs, state, prep = find('scoreboard players set $xs mg.st 1'), find('scoreboard players set $state mg.st 1'), find('function mg:elyrace/prepare')
    if None in (xs, state, prep) or not xs < state < prep:
        bad.append('solo/start : l\'ordre doit etre $xs 1, $state 1, prepare (les gardes de end, timeout et cleanup lisent $xs)')
    elif any(REFUSAL.match(l) for l in lines[xs:]):
        bad.append('solo/start : un refus suit la pose de $xs (il laisserait le solo a moitie lance)')
    for name in ('cleanup', 'announce'):
        if 'scoreboard players set $xs mg.st 0' not in fn_code(files, name):
            bad.append('elyrace/%s : doit remettre $xs a 0' % name)
    return bad


def objective_problems(files):
    """Chaque objectif cree par elyrace est retire par uninstall."""
    removed = set(re.findall(r'scoreboard objectives remove (mg\.\w+)', '\n'.join(fn_code(files, 'uninstall'))))
    added = set()
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            added.update(re.findall(r'scoreboard objectives add (mg\.\w+)', text))
    return ['uninstall : objectif %s cree mais jamais retire' % o for o in sorted(added - removed)]


def problems(root, files, specs):
    return (draw_problems(files) + records_problems(files) + trigger_problems(files, specs) + hooks_problems(root)
            + order_problems(files) + objective_problems(files))
