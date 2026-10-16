import fs from 'node:fs';
import net from 'node:net';
import path from 'node:path';
import { spawn, execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const cfg = JSON.parse(fs.readFileSync(process.env.BRIDGE_CONFIG || path.join(here, 'config.json'), 'utf8'));
const repo = path.resolve(here, cfg.repoDir || '../..');
const logFile = path.join(cfg.serverDir, 'logs', 'latest.log');
const prefix = (cfg.prefix || '!claude').toLowerCase();
const allowed = new Set((cfg.allowedPlayers || []).map(p => p.toLowerCase()));
const TAG = '[claude-bridge]';
const TRACKED = ['data', 'pack.mcmeta', 'README.md'];
const CHAT = /^\[[^\]]*\](?: \[[^\]]*\])?: (?:\[Not Secure\] )?<([\w.]{1,17})> (.*)$/;
const RELOAD_ERR = /ERROR\]|Failed to load|Whilst parsing|Couldn't (?:load|parse)|Unknown or incomplete/;
const isWin = process.platform === 'win32';
const sleep = ms => new Promise(r => setTimeout(r, ms));

// ---------- RCON ----------
function rcon(command) {
  return new Promise((resolve, reject) => {
    const sock = net.connect(cfg.rcon.port || 25575, cfg.rcon.host || '127.0.0.1');
    let buf = Buffer.alloc(0), authed = false;
    const send = (id, type, body) => {
      const b = Buffer.from(body, 'utf8');
      const p = Buffer.alloc(14 + b.length);
      p.writeInt32LE(10 + b.length, 0);
      p.writeInt32LE(id, 4);
      p.writeInt32LE(type, 8);
      b.copy(p, 12);
      sock.write(p);
    };
    sock.setTimeout(10000, () => { sock.destroy(); reject(new Error('RCON timeout')); });
    sock.on('error', reject);
    sock.on('connect', () => send(1, 3, cfg.rcon.password));
    sock.on('data', d => {
      buf = Buffer.concat([buf, d]);
      while (buf.length >= 4) {
        const len = buf.readInt32LE(0);
        if (buf.length < len + 4) break;
        const id = buf.readInt32LE(4);
        const body = buf.toString('utf8', 12, 4 + len - 2);
        buf = buf.subarray(len + 4);
        if (id === -1) { sock.destroy(); return reject(new Error('RCON : mot de passe refuse')); }
        if (id === 1 && !authed) { authed = true; send(2, 2, command); }
        else if (id === 2) { sock.end(); resolve(body); }
      }
    });
  });
}

const clean = s => String(s).replace(/\s+/g, ' ').trim().slice(0, 300);
function say(target, text, color = 'white') {
  const msg = [{ text: '[Claude] ', color: 'light_purple' }, { text: clean(text), color }];
  return rcon(`tellraw ${target} ${JSON.stringify(msg)}`).catch(e => console.error('[rcon]', e.message));
}

// ---------- Log tail ----------
const listeners = new Set();
let pos = fs.existsSync(logFile) ? fs.statSync(logFile).size : 0;
let carry = '';
setInterval(() => {
  let st;
  try { st = fs.statSync(logFile); } catch { return; }
  if (st.size < pos) { pos = 0; carry = ''; }
  if (st.size === pos) return;
  const fd = fs.openSync(logFile, 'r');
  const b = Buffer.alloc(st.size - pos);
  fs.readSync(fd, b, 0, b.length, pos);
  fs.closeSync(fd);
  pos = st.size;
  const lines = (carry + b.toString('utf8')).split(/\r?\n/);
  carry = lines.pop();
  for (const l of lines) {
    for (const fn of listeners) fn(l);
    onLine(l);
  }
}, 500);

// ---------- Git ----------
const git = (...args) => execFileSync('git', args, { cwd: repo, encoding: 'utf8' });
const repoDirty = () => git('status', '--porcelain').trim() !== '';
const packChanged = () => git('status', '--porcelain', '--', ...TRACKED).trim() !== '';
function restorePack() {
  git('checkout', '--', ...TRACKED);
  git('clean', '-fdq', '--', 'data');
}

// ---------- Claude ----------
function runClaude(prompt, resume) {
  return new Promise((resolve, reject) => {
    const q = s => (isWin ? `"${s}"` : s);
    const args = ['-p', '--bare', '--strict-mcp-config', '--output-format', 'json',
      '--permission-mode', 'acceptEdits',
      '--allowedTools', 'Read,Edit,Write,Glob,Grep',
      '--disallowedTools', 'Bash,WebFetch,WebSearch',
      '--append-system-prompt-file', q(path.join(here, 'system-prompt.md'))];
    if (cfg.model) args.push('--model', cfg.model);
    if (cfg.maxBudgetUsd) args.push('--max-budget-usd', String(cfg.maxBudgetUsd));
    if (resume) args.push('--resume', resume);
    const env = { ...process.env };
    if (cfg.anthropicApiKey) env.ANTHROPIC_API_KEY = cfg.anthropicApiKey;

    const child = spawn(cfg.claudeCommand || 'claude', args, { cwd: repo, env, shell: isWin, windowsHide: true });
    let out = '', err = '';
    const timer = setTimeout(() => child.kill(), (cfg.timeoutMinutes || 10) * 60000);
    child.stdout.on('data', d => (out += d));
    child.stderr.on('data', d => (err += d));
    child.on('error', e => { clearTimeout(timer); reject(e); });
    child.on('close', code => {
      clearTimeout(timer);
      try {
        resolve(JSON.parse(out.trim().split(/\r?\n/).pop()));
      } catch {
        reject(new Error(`claude a quitte (code ${code}) : ${clean(err || out) || 'pas de sortie'}`));
      }
    });
    child.stdin.end(prompt);
  });
}

async function reloadAndCollectErrors() {
  const errs = [];
  const fn = l => { if (RELOAD_ERR.test(l)) errs.push(l.replace(/^\[[^\]]*\](?: \[[^\]]*\])?: /, '')); };
  listeners.add(fn);
  try {
    await rcon('minecraft:reload');
    await sleep(cfg.reloadWaitMs ?? 5000);
  } finally {
    listeners.delete(fn);
  }
  return [...new Set(errs)].slice(0, 30);
}

// ---------- Jobs ----------
async function handleRequest(player, demande) {
  if (repoDirty()) return say(player, 'Le repo contient des modifs non commitees, je ne touche a rien.', 'red');
  await say('@a', `${player} demande : ${demande}`, 'gray');

  let res = await runClaude(`Demande de ${player} depuis le chat Minecraft :\n${demande}`);
  let cost = res.total_cost_usd || 0;
  let errors = [];

  if (res.is_error) {
    if (packChanged()) restorePack();
    return say(player, `Echec (${res.subtype || 'erreur'}) : ${res.result || ''}`, 'red');
  }

  for (let attempt = 0; packChanged(); attempt++) {
    errors = await reloadAndCollectErrors();
    if (!errors.length || attempt >= (cfg.maxFixAttempts ?? 2)) break;
    await say(player, `${errors.length} erreur(s) au reload, correction en cours...`, 'yellow');
    res = await runClaude(`Le /reload du serveur a produit ces erreurs, corrige-les :\n${errors.join('\n')}`, res.session_id);
    cost += res.total_cost_usd || 0;
  }

  const costTxt = ` (${cost.toFixed(2)} $)`;
  if (!packChanged()) return say(player, (res.result || 'Aucune modification.') + costTxt, 'aqua');

  git('add', '-A', '--', ...TRACKED);
  git('commit', '-q', '-m', `${TAG} ${player} : ${clean(demande).slice(0, 150)}`, '-m', clean(res.result || ''));
  await say('@a', (res.result || 'Modification appliquee.') + costTxt, 'green');
  if (errors.length) await say(player, `Il reste ${errors.length} erreur(s) au reload (voir console). "${prefix} undo" pour annuler.`, 'red');
}

async function undo(player) {
  const subject = git('log', '-1', '--format=%s').trim();
  if (!subject.startsWith(TAG)) return say(player, 'Le dernier commit ne vient pas du bridge, rien a annuler.', 'red');
  if (repoDirty()) return say(player, 'Le repo contient des modifs non commitees, annulation impossible.', 'red');
  git('revert', '--no-edit', 'HEAD');
  await reloadAndCollectErrors();
  await say('@a', `Annule : ${subject.slice(TAG.length).trim()}`, 'yellow');
}

// ---------- File d'attente ----------
const queue = [];
let busy = false;
function enqueue(player, job) {
  queue.push({ player, job });
  if (busy) say(player, `En file d'attente (position ${queue.length}).`, 'gray');
  pump();
}
async function pump() {
  if (busy || !queue.length) return;
  const t = queue.shift();
  busy = true;
  try { await t.job(); }
  catch (e) { console.error(e); await say(t.player, `Erreur : ${e.message}`, 'red'); }
  finally { busy = false; pump(); }
}

function onLine(line) {
  const m = CHAT.exec(line);
  if (!m) return;
  const [, player, msg] = m;
  const lower = msg.toLowerCase();
  if (lower !== prefix && !lower.startsWith(prefix + ' ')) return;
  if (!allowed.has(player.toLowerCase())) return say(player, "Tu n'es pas autorise a utiliser Claude.", 'red');
  const arg = msg.slice(prefix.length).trim();
  console.log(`[chat] ${player} : ${arg}`);
  if (!arg || arg === 'aide' || arg === 'help') {
    return say(player, `${prefix} <demande> : modifier le jeu | ${prefix} undo : annuler la derniere modif`, 'gray');
  }
  if (arg === 'undo') return enqueue(player, () => undo(player));
  enqueue(player, () => handleRequest(player, arg));
}

// ---------- Demarrage ----------
const branch = git('rev-parse', '--abbrev-ref', 'HEAD').trim();
console.log(`claude-bridge : repo ${repo} (branche ${branch}), log ${logFile}`);
if (['main', 'develop'].includes(branch)) console.warn('[!] Branche protegee : lance plutot le bridge sur une branche dediee (ex: live).');
if (!fs.existsSync(logFile)) console.warn(`[!] ${logFile} introuvable, en attente...`);
rcon('list').then(r => console.log(`RCON OK : ${r}`)).catch(e => console.error(`[!] RCON KO : ${e.message}`));
