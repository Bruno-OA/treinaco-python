/* BLUE REP — JavaScript pequeno apenas para o que precisa de interação.
   Todo o conteúdo de treino é definido nos arquivos Python em /data. */
(() => {
  'use strict';
  const PREFIX = 'bluerep:v1:';
  const storage = {
    get(key, fallback) { try { const saved = localStorage.getItem(PREFIX + key); return saved === null ? fallback : JSON.parse(saved); } catch { return fallback; } },
    set(key, value) { try { localStorage.setItem(PREFIX + key, JSON.stringify(value)); } catch { /* Navegador pode bloquear armazenamento. */ } },
    remove(key) { try { localStorage.removeItem(PREFIX + key); } catch { /* sem armazenamento */ } }
  };

  const page = document.querySelector('[data-workout-id]');
  const homeCards = document.querySelectorAll('[data-home-workout]');

  // Exibe o progresso nos cards da tela inicial.
  homeCards.forEach(card => {
    const id = card.dataset.homeWorkout;
    const state = storage.get(`check:${id}`, {});
    const done = Object.values(state).filter(Boolean).length;
    const total = Number(card.dataset.totalSeries) || 1;
    const label = card.querySelector('[data-card-progress]');
    if (label) label.textContent = `${Math.round(done / total * 100)}% FEITO`;
  });

  if (!page) return;

  const treino = page.dataset.workoutId;
  const checks = [...page.querySelectorAll('.series-check input[type="checkbox"]')];
  const pesos = [...page.querySelectorAll('.weight-input')];
  const progressFill = page.querySelector('#progress-fill');
  const progressNumber = page.querySelector('#done-count');
  let currentChecks = storage.get(`check:${treino}`, {});
  let currentWeights = storage.get(`weight:${treino}`, {});

  const keyForCheck = input => `${input.closest('[data-exercise-id]').dataset.exerciseId}:${input.dataset.series}`;
  const updateProgress = () => {
    const done = checks.filter(check => check.checked).length;
    progressNumber.textContent = done;
    progressFill.style.width = `${checks.length ? done / checks.length * 100 : 0}%`;
  };

  checks.forEach(input => {
    input.checked = Boolean(currentChecks[keyForCheck(input)]);
    input.addEventListener('change', () => {
      currentChecks[keyForCheck(input)] = input.checked;
      storage.set(`check:${treino}`, currentChecks);
      updateProgress();
    });
  });

  pesos.forEach(input => {
    const exerciseId = input.closest('[data-exercise-id]').dataset.exerciseId;
    if (currentWeights[exerciseId] !== undefined) input.value = currentWeights[exerciseId];
    input.addEventListener('input', () => {
      currentWeights[exerciseId] = input.value;
      storage.set(`weight:${treino}`, currentWeights);
    });
  });
  updateProgress();

  const reset = page.querySelector('#reset-workout');
  reset?.addEventListener('click', () => {
    if (!window.confirm('Reiniciar as marcações das séries deste treino? As cargas registradas serão mantidas.')) return;
    currentChecks = {};
    storage.remove(`check:${treino}`);
    checks.forEach(input => { input.checked = false; });
    updateProgress();
  });

  // Cronômetro único: permanece visível na parte inferior até terminar ou ser fechado.
  const timer = document.getElementById('rest-timer');
  const timerDisplay = document.getElementById('timer-display');
  const timerName = document.getElementById('timer-exercise-name');
  const timerToggle = document.getElementById('timer-toggle');
  const timerClose = document.getElementById('timer-close');
  let intervalId = null;
  let remaining = 0;
  let deadline = 0;
  let paused = false;
  const format = seconds => `${String(Math.floor(seconds / 60)).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;
  const stopInterval = () => { if (intervalId !== null) clearInterval(intervalId); intervalId = null; };

  const paintTimer = () => { timerDisplay.textContent = format(remaining); };
  const tick = () => {
    remaining = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
    paintTimer();
    if (remaining === 0) {
      stopInterval();
      timerName.textContent = 'DESCANSO CONCLUÍDO ✓';
      timerToggle.textContent = 'CONCLUÍDO';
      timerToggle.disabled = true;
    }
  };

  const startTimer = (seconds, name) => {
    stopInterval();
    remaining = Number(seconds);
    deadline = Date.now() + remaining * 1000;
    paused = false;
    timerName.textContent = name.toUpperCase();
    timerToggle.textContent = 'PAUSAR';
    timerToggle.disabled = false;
    timer.hidden = false;
    paintTimer();
    intervalId = setInterval(tick, 250);
  };

  page.querySelectorAll('.start-rest').forEach(button => {
    button.addEventListener('click', () => startTimer(button.dataset.rest, button.dataset.exerciseName));
  });

  timerToggle?.addEventListener('click', () => {
    if (paused) {
      deadline = Date.now() + remaining * 1000;
      intervalId = setInterval(tick, 250);
      timerToggle.textContent = 'PAUSAR';
      paused = false;
    } else {
      tick();
      stopInterval();
      timerToggle.textContent = 'RETOMAR';
      paused = true;
    }
  });
  timerClose?.addEventListener('click', () => { stopInterval(); timer.hidden = true; });
  document.addEventListener('visibilitychange', () => { if (!document.hidden && !paused && intervalId !== null) tick(); });
})();
