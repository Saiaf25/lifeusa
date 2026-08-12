document.addEventListener('click', (event) => {
  const answer = event.target.closest('[data-answer]');
  if (answer) {
    const group = answer.closest('[data-quiz]');
    const feedback = group.querySelector('[data-feedback]');
    group.querySelectorAll('[data-answer]').forEach((button) => button.setAttribute('aria-pressed', 'false'));
    answer.setAttribute('aria-pressed', 'true');
    const correct = answer.dataset.answer === group.dataset.correct;
    feedback.className = `feedback show ${correct ? 'correct' : 'try-again'}`;
    feedback.innerHTML = correct
      ? '<strong>Correct.</strong> Page A is already close to page one, has substantial visibility, and earns few clicks. That makes it a practical improvement candidate.'
      : answer.dataset.answer === 'B'
        ? '<strong>Try again.</strong> Page B already performs strongly. Its low impressions may simply reflect limited demand, so it is not the clearest first opportunity.'
        : '<strong>Try again.</strong> Page C has visibility, but position 41.7 is far from page one. A title change alone is unlikely to solve the larger ranking problem.';
  }

  const copyButton = event.target.closest('[data-copy-card]');
  if (copyButton) {
    const card = document.querySelector('.record-card');
    const fields = [...card.querySelectorAll('input, textarea')];
    const output = fields.map((field) => `${field.dataset.label}: ${field.value || '[not completed]'}`).join('\n');
    const status = document.querySelector('[data-copy-status]');
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
