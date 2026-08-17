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
