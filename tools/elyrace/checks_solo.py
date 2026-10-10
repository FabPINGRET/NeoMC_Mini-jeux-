"""Controles statiques du contre-la-montre solo PAR JOUEUR et des records (appeles par checks.py). Le solo ne touche jamais la machine a
etats : il ne tient que par ses gardes, toutes verifiees ici, avec le branchement dans le moteur (core/tick, pose par wire_elyrace4.py)
et les crochets de la 2c qui doivent avoir disparu. Aucun import de checks.py (il importe ce module).
Python stdlib uniquement (compatible 3.8).
"""
import os
import re

import checks_retry as CRT
import course_common as CC
import game as G
import menus as M
import solo_run as SR

REFUSAL = re.compile(r'^execute .* run return run (tellraw @s |scoreboard players set \$xc mg\.st 0$)')   # 2e forme : refus « pas construit » (remet $xc a 0)
SOLO_RETURN = re.compile(r'^execute if entity @s\[tag=mg\.xso\] run return run function (mg:[a-z_0-9/]+)$')    # 1re ligne d'une fonction commune qui renvoie le solo vers la sienne
STATE_WRITE = re.compile(r'scoreboard players (set|add|remove|operation|reset) \$(state|game|timer)\b')
FORBIDDEN_CALL = re.compile(r'\bfunction mg:core/(countdown|begin|draw|ending|return_lobby|opt_spec|abort|win_player)\b')
PLAY_SELECTOR = re.compile(r'@[ae]\[[^\]]*tag=mg\.play')       # @a[tag=mg.play...] : un solo ne cible jamais les participants d'une partie
BUSY_WAIT = 'execute if entity @a[tag=mg.xso] run return run schedule function '
PURGE = re.compile(r'^scoreboard players reset \$xse? mg\.st$')   # seul emploi permis de $xs / $xse : la purge des anciens drapeaux (elyrace/objectives)
SOLO_ONLY = {'solo/go': 'scoreboard players set @s mg.xph 2', 'solo/arm': 'scoreboard players set @s mg.xph 1', 'solo/finish': 'scoreboard players set @s mg.xph 3',
             'solo/choice': 'scoreboard players set @s mg.xph 4'}      # phase -> seule fonction qui la pose (arm : lancement ET « Rejouer »)


def code(text):
    return [l for l in text.split('\n') if l and not l.startswith('#')]


def fn_code(files, name):
    return code(files[CC.FN + name + '.mcfunction'])


def repo_code(root, rel):
    with open(os.path.join(root, 'data', 'mg', 'function', rel + '.mcfunction'), encoding='utf-8', newline='') as fh:
        return code(fh.read().replace('\r\n', '\n'))


def names(files):
    """Noms des fonctions generees (relatifs a elyrace/)."""
    return {rel[len(CC.FN):-len('.mcfunction')]: rel for rel in files if rel.startswith(CC.FN) and rel.endswith('.mcfunction')}


def reach_lines(files, start):
    """Lignes de code atteignables depuis la fonction elyrace `start` : {nom: [lignes]}. Une fonction qui renvoie le solo vers la sienne
    (SOLO_RETURN) n'est lue que jusqu'a cette ligne : la suite n'est jamais executee pour un joueur en solo."""
    base, seen, todo = names(files), {}, [start]
    while todo:
        name = todo.pop()
        if name in seen or name not in base:
            continue
        lines = []
        for line in code(files[base[name]]):
            lines.append(line)
            if SOLO_RETURN.match(line):
                break
        seen[name] = lines
        for line in lines:
            todo += [t[len('elyrace/'):] for t in re.findall(r'\bfunction mg:(elyrace/[a-z_0-9/]+)', line)]
    return seen


def solo_problems(files):
    """Le solo n'ecrit pas la machine a etats, ne cible pas les participants, n'appelle aucune fin de partie."""
    bad = []
    for name in sorted(n for n in names(files) if n.startswith('solo/')):
        for line in fn_code(files, name):
            if STATE_WRITE.search(line):
                bad.append('elyrace/%s : ecrit $state, $game ou $timer : %s' % (name, line))
            if FORBIDDEN_CALL.search(line):
                bad.append('elyrace/%s : appelle la machine a etats ou une fin de partie : %s' % (name, line))
            if PLAY_SELECTOR.search(line) or re.search(r'tag @\S+ (add|remove) mg\.play\b', line):
                bad.append('elyrace/%s : cible ou tague les participants (mg.play) : %s' % (name, line))
    for rel, text in sorted(files.items()):
        if rel.endswith('.mcfunction'):
            for line in code(text):
                if re.search(r'\$xse?\b', line) and not (rel == CC.FN + 'objectives.mcfunction' and PURGE.match(line)):
                    bad.append('%s : $xs / $xse n\'existent plus (le solo est par joueur) : %s' % (rel, line))
    reach = reach_lines(files, 'solo/step')
    if 'solo/step' not in reach:
        return bad + ['solo/step introuvable']
    for name, lines in sorted(reach.items()):
        for line in lines:
            if re.search(r'\$(xc|xt)\b', line):
                bad.append('elyrace/%s (atteint depuis solo/step) : lit $xc ou $xt, qui sont ceux de la course de groupe : %s' % (name, line))
    return bad


def entry_exit_problems(files):
    """solo/go est la seule entree en course (phase 2), solo/stop la seule sortie (mg.xso), solo/start le seul lancement (via arm pour la phase 1) ;
    la pause est rendue par stop."""
    bad = []
    for rel, text in sorted(files.items()):
        if not rel.endswith('.mcfunction'):
            continue
        name = rel[len(CC.FN):-len('.mcfunction')]
        for line in code(text):
            if re.search(r'mg\.xph (\d)\b', line) and re.search(r'players set \S+ mg\.xph [1-4]\b', line):
                value = re.search(r'mg\.xph ([1-4])\b', line).group(1)
                want = [n for n, l in SOLO_ONLY.items() if l.endswith('mg.xph ' + value)][0]
                if name != want or line != SOLO_ONLY[want]:
                    bad.append('%s : pose la phase %s ailleurs que dans elyrace/%s : %s' % (rel, value, want, line))
            if re.search(r'tag \S+ add mg\.xso\b', line) and name != 'solo/start':
                bad.append('%s : pose mg.xso ailleurs que dans solo/start : %s' % (rel, line))
            if re.search(r'tag \S+ remove mg\.xso\b', line) and name not in ('solo/stop', 'uninstall'):
                bad.append('%s : retire mg.xso ailleurs que dans solo/stop : %s' % (rel, line))
    for want, line in SOLO_ONLY.items():
        if line not in fn_code(files, want):
            bad.append('elyrace/%s : doit poser la phase (%s)' % (want, line))
    stop = fn_code(files, 'solo/stop')
    keep = 'execute unless entity @s[tag=mg.xsp0] run tag @s remove mg.spectate'
    if keep not in stop or 'tag @s remove mg.xsp0' not in stop:
        bad.append('solo/stop : doit rendre la pause d\'avant (%s) puis oublier mg.xsp0' % keep)
    resets = [i for i, l in enumerate(stop) if l.endswith('run function mg:core/reset_player')]
    skip = ['mg.play', 'mg.out'] + [t for t, _ in SR.LEFT]
    if len(resets) != 1 or any('unless entity @s[tag=%s]' % t not in stop[resets[0]] for t in skip):
        bad.append('solo/stop : reset_player doit etre appele une fois, sauf pour un participant (mg.play), un spectateur (mg.out) '
                   'ou un joueur parti en survie, en plot ou en visite (%s)' % ', '.join(skip))
    elif 'tag @s remove mg.xso' not in stop or keep not in stop or not stop.index('tag @s remove mg.xso') < stop.index(keep) < resets[0]:
        bad.append('solo/stop : le tag mg.xso doit partir AVANT le retour de la pause et le retour au lobby (plus aucune detection)')
    start = fn_code(files, 'solo/start')
    first = [i for i, l in enumerate(start) if re.match(r'^tag @s add ', l)]
    refusals = [i for i, l in enumerate(start) if REFUSAL.match(l)]
    if not first or not refusals:
        bad.append('solo/start : refus ou lancement absents')
    elif max(refusals) > min(first):
        bad.append('solo/start : un refus suit la premiere ecriture d\'etat (il laisserait le solo a moitie lance)')
    for t, _ in SR.LEFT:        # chaque activite dont stop ne ramene pas au lobby est refusee au lancement (surtout mg.surv : start fait `clear @s`)
        ref = [i for i, l in enumerate(start) if l.startswith('execute if entity @s[tag=%s] run return run tellraw @s ' % t)]
        if not ref or (first and min(ref) > min(first)):
            bad.append('solo/start : pas de refus `execute if entity @s[tag=%s] run return run tellraw @s ...` avant la premiere ecriture d\'etat '
                       '(tag de SR.LEFT : start viderait l\'inventaire d\'un joueur parti dans cette activite)' % t)
    spectate, memo = 'tag @s add mg.spectate', 'execute if entity @s[tag=mg.spectate] run tag @s add mg.xsp0'
    if spectate not in start or memo not in start or start.index(memo) > start.index(spectate):
        bad.append('solo/start : la pause d\'avant (mg.xsp0) doit etre memorisee AVANT la pose de mg.spectate')
    return bad


def order_problems(files):
    """Ordre dans le tick du solo : seen (@a) avant step (@e[type=player]) ; dans seen, les sorties (survie / plot / visite, puis
    reconnexion, puis pause desactivee) toutes AVANT la mise a jour de mg.xsl et du chrono (la reconnexion lit l'ancien mg.xsl)."""
    bad, tick, seen = [], fn_code(files, 'solo/tick'), fn_code(files, 'solo/seen')
    passes = ['execute as @a[tag=mg.xso] run function mg:elyrace/solo/seen', 'execute as @e[type=player,tag=mg.xso] run function mg:elyrace/solo/step']
    if any(l not in tick for l in passes) or tick.index(passes[0]) > tick.index(passes[1]):
        bad.append('solo/tick : la passe seen (@a, voit les morts) doit preceder la passe step (@e[type=player]) : %s' % passes)
    stop = 'run return run function mg:elyrace/solo/stop'
    left = ['execute if entity @s[tag=%s] %s' % (t, stop) for t, _ in SR.LEFT]
    reco = 'execute unless score @s mg.xsl = #xsl mg.st ' + stop
    pause = 'execute unless entity @s[tag=mg.spectate] ' + stop
    upd = 'scoreboard players operation @s mg.xsl = $tc mg.st'
    chain = left + [reco, pause, upd]
    for l in chain:
        if l not in seen:
            bad.append('solo/seen : ligne absente : %s' % l)
    if not bad:
        idx = [seen.index(l) for l in chain]
        if not (max(idx[:len(left)]) < idx[-3] < idx[-2] < idx[-1]):
            bad.append('solo/seen : ordre attendu : sorties survie / plot / visite, reconnexion (mg.xsl = $tc - 1), pause desactivee, puis mise a jour de mg.xsl')
        if 'scoreboard players add @s mg.xst 1' not in seen or seen.index('scoreboard players add @s mg.xst 1') < idx[-1]:
            bad.append('solo/seen : le chrono (mg.xst) ne doit avancer qu\'apres toutes les sorties')
    return bad


def records_problems(files):
    """Records et etat du solo : jamais remis a zero par une preparation de partie (prepare remet G.OBJECTIVES a zero a chaque depart)."""
    extra = {n for n, _ in G.EXTRA_OBJECTIVES}
    bad = ['G.OBJECTIVES contient mg.%s : prepare le remettrait a zero a chaque depart' % n for n, _, _ in G.OBJECTIVES if n == 'xs' or n in extra or re.match(r'xr\d+$', n)]
    allowed = ('scoreboard players operation @a[tag=mg.play] mg.xcr = $xc mg.st',       # le parcours de chaque participant
               'execute as @a[tag=mg.xso] run function mg:elyrace/solo/stop')            # un depart de groupe arrete les solos
    for line in fn_code(files, 'prepare'):
        for m in re.findall(r'\bmg\.(xs\w*|xr\d+|xph|xst|xcr)\b', line):
            if line not in allowed and not (m == 'xso' and line.startswith('tellraw @a[tag=mg.xso] ')):
                bad.append('elyrace/prepare : touche un record, le trigger ou l\'etat du solo : %s' % line)
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
    if not any(lo == M.SOLO_STOP and not opened for lo, opened in handled):
        bad.append('solo/cmd : la valeur %d (arreter tous les solos) n\'est pas traitee' % M.SOLO_STOP)
    return bad


def common_problems(files, specs):
    """Les fonctions communes (finish, wall_adv, prepare, construction) savent qu'un solo existe."""
    bad = []
    if fn_code(files, 'finish')[:1] != ['execute if entity @s[tag=mg.xso] run return run function mg:elyrace/solo/finish']:
        bad.append('elyrace/finish : la premiere commande doit renvoyer le solo vers solo/finish')
    adv = fn_code(files, 'wall_adv')
    solo = [i for i, l in enumerate(adv) if 'tag=mg.xso' in l]
    other = [i for i, l in enumerate(adv) if '$game' in l]
    if len(solo) != 2 or not other or max(solo) > min(other):
        bad.append('elyrace/wall_adv : le solo (phase 2 : wall, sinon rien) doit etre traite avant les tests de $game et $state')
    prep = fn_code(files, 'prepare')
    stop = 'execute as @a[tag=mg.xso] run function mg:elyrace/solo/stop'
    setup = [i for i, l in enumerate(prep) if '/setup' in l]
    if stop not in prep or not setup or prep.index(stop) > min(setup):
        bad.append('elyrace/prepare : doit arreter les solos (%s) avant d\'installer le depart du groupe' % stop)
    xcr = 'scoreboard players operation @a[tag=mg.play] mg.xcr = $xc mg.st'
    place = [i for i, l in enumerate(prep) if 'elyrace/place_one' in l]
    if xcr not in prep or not place or prep.index(xcr) > min(place):
        bad.append('elyrace/prepare : doit poser mg.xcr (parcours de chaque participant) avant place_one (%s)' % xcr)
    waits = (['c%d/build_wait' % s.NUM for s in specs] + ['build_next']
             + sorted(n for n in names(files) if re.match(r'c\d+/clear_\d+$', n)))       # chaque passe de nettoyage suspendue pendant un solo
    for w in waits:
        if not any(l.startswith(BUSY_WAIT) for l in fn_code(files, w)):
            bad.append('elyrace/%s : la construction doit attendre aussi les solos (%s...)' % (w, BUSY_WAIT))
    for w in ['build'] + ['c%d/build' % s.NUM for s in specs]:
        if not any(l.startswith('execute if entity @a[tag=mg.xso] run return run tellraw @a[tag=mg.admin]') for l in fn_code(files, w)):
            bad.append('elyrace/%s : un build d\'admin doit etre refuse pendant un solo' % w)
    return bad


def hooks_problems(root):
    """Branchement du moteur (wire_elyrace4.py) present, crochets de la 2c disparus, core/request et le reste du moteur sans $xs."""
    bad, hint = [], ' (lancer wire_elyrace4.py)'
    tick = repo_code(root, 'core/tick')
    find = lambda s: [i for i, l in enumerate(tick) if s in l]
    hook, opt, rec, void = find('function mg:elyrace/solo/tick'), find('run function mg:core/opt'), find('run function mg:core/reconnect'), find('run function mg:core/void_catch')
    if len(hook) != 1 or tick[hook[0]] != 'execute if entity @a[tag=mg.xso] run function mg:elyrace/solo/tick':
        bad.append('core/tick : la ligne solo/tick est absente ou modifiee%s' % hint)
    elif not (opt and rec and void) or not (max(opt + rec) < hook[0] < min(void)):
        bad.append('core/tick : solo/tick doit venir apres core/opt et core/reconnect (le solo lit la pause) et avant void_catch%s' % hint)
    for l in tick:
        if re.search(r'^execute .* run clear @a\[[^\]]*\] minecraft:(elytra|firework_rocket)\[minecraft:custom_data~\{mg_elyr:1b\}\]$', l) and 'tag=!mg.xso' not in l:
            bad.append('core/tick : le nettoyage des objets mg_elyr doit epargner les joueurs en solo (tag=!mg.xso)%s : %s' % (hint, l))
    if 'scoreboard players enable @a mg.xs' not in tick or 'execute as @a[scores={mg.xs=1..}] run function mg:elyrace/solo/cmd' not in tick:
        bad.append('core/tick : activation ou appel de solo/cmd absent (wire_elyrace3.py)')
    base = os.path.join(root, 'data', 'mg', 'function', 'core')
    for fname in sorted(os.listdir(base)):
        if fname.endswith('.mcfunction'):
            rel = 'core/' + fname[:-len('.mcfunction')]
            for l in repo_code(root, rel):
                if re.search(r'\$xse?\b', l) or (rel == 'core/request' and 'xso' in l):
                    bad.append('%s : crochet de la 2c ($xs) a retirer, ou request touche au solo%s : %s' % (rel, hint, l))
    return bad


def objective_problems(files):
    """Chaque objectif cree par elyrace est retire par uninstall."""
    removed = set(re.findall(r'scoreboard objectives remove (mg\.\w+)', '\n'.join(fn_code(files, 'uninstall'))))
    added = set()
    for rel, text in files.items():
        if rel.endswith('.mcfunction'):
            added.update(re.findall(r'scoreboard objectives add (mg\.\w+)', text))
    bad = ['uninstall : objectif %s cree mais jamais retire' % o for o in sorted(added - removed)]
    gone = '\n'.join(fn_code(files, 'uninstall'))
    return bad + ['uninstall : le tag %s n\'est pas retire' % t for t in G.SOLO_TAGS if 'tag @a remove ' + t not in gone]


def problems(root, files, specs):
    return (solo_problems(files) + entry_exit_problems(files) + CRT.retry_problems(files, specs, fn_code) + order_problems(files) + records_problems(files) + trigger_problems(files, specs)
            + common_problems(files, specs) + hooks_problems(root) + objective_problems(files))
