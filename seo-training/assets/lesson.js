const sectionIcons = {
  learn: '<span class="section-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5zM20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5z"/></svg></span>',
  practice: '<span class="section-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m8 12 2.5 2.5L16 9M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Z"/></svg></span>',
  workflow: '<span class="section-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h5a3 3 0 0 1 3 3v6a3 3 0 0 0 3 3"/></svg></span>',
  deliverable: '<span class="section-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 3h9l3 3v15H6zM15 3v4h4M9 12h6M9 16h6"/></svg></span>',
  recall: '<span class="section-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 12c2.2-3.5 4.9-5.25 8-5.25s5.8 1.75 8 5.25c-2.2 3.5-4.9 5.25-8 5.25S6.2 15.5 4 12Z"/><circle cx="12" cy="12" r="2.5"/></svg></span>',
};

function enhanceLessonSections() {
  const pathMatch = window.location.pathname.match(/lesson-(\d+)-/);
  const labelText = document.querySelector('.lesson-head .step-label')?.textContent || '';
  const number = Number(pathMatch?.[1] || labelText.match(/LESSON\s+(\d+)/i)?.[1]);
  if (!number) return;

  const toolKey = number <= 8 ? 'gsc' : number <= 12 ? 'ahrefs' : 'codex';
  document.body.classList.add('lesson-page');
  document.body.dataset.tool = toolKey;
  document.body.dataset.lesson = String(number);

  const sectionKinds = ['learn', 'practice', 'workflow', 'deliverable', 'recall'];
  document.querySelectorAll('main.shell > section.paper').forEach((section, index) => {
    const kind = sectionKinds[index] || 'learn';
    section.dataset.section = kind;
    let label = section.querySelector(':scope > .step-label');
    if (!label && index === 0) {
      label = document.createElement('p');
      label.className = 'step-label';
      label.textContent = 'LEARN · ONE IDEA';
      section.prepend(label);
    }
    if (label && !label.querySelector('.section-icon')) {
      label.classList.add('section-label');
      label.insertAdjacentHTML('afterbegin', sectionIcons[kind]);
    }
  });
}

enhanceLessonSections();

document.addEventListener('click', (event) => {
  const answer = event.target.closest('[data-answer]');
  if (answer) {
    const group = answer.closest('[data-quiz]');
    const feedback = group.querySelector('.feedback[data-feedback]');
    group.querySelectorAll('[data-answer]').forEach((button) => button.setAttribute('aria-pressed', 'false'));
    answer.setAttribute('aria-pressed', 'true');
    const correct = answer.dataset.answer === group.dataset.correct;
    feedback.className = `feedback show ${correct ? 'correct' : 'try-again'}`;
    const explanation = answer.dataset.feedback || group.dataset.feedback || '';
    feedback.innerHTML = `<strong>${correct ? 'Correct.' : 'Try again.'}</strong> ${explanation}`;
  }

  const copyButton = event.target.closest('[data-copy-card]');
  if (copyButton) {
    const section = copyButton.closest('.paper');
    const card = section.querySelector('.record-card');
    const fields = [...card.querySelectorAll('input, textarea')];
    const output = fields.map((field) => `${field.dataset.label}: ${field.value || '[not completed]'}`).join('\n');
    const status = section.querySelector('[data-copy-status]');
    const confirmCopy = () => {
      status.textContent = 'Copied. Paste it into the shared learning sheet.';
    };
    const fallbackCopy = () => {
      const helper = document.createElement('textarea');
      helper.value = output;
      helper.setAttribute('readonly', '');
      helper.style.position = 'fixed';
      helper.style.opacity = '0';
      document.body.appendChild(helper);
      helper.select();
      document.execCommand('copy');
      helper.remove();
      confirmCopy();
    };
    if (navigator.clipboard?.writeText) {
      navigator.clipboard.writeText(output).then(confirmCopy).catch(fallbackCopy);
    } else {
      fallbackCopy();
    }
  }
});
