document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('frm');
  const txt = document.getElementById('txt');
  const translatedDiv = document.getElementById('translated');
  const player = document.getElementById('player');
  const submitBtn = document.getElementById('submitBtn');
  const statusSpan = document.getElementById('status');
  const copyBtn = document.getElementById('copyBtn');
  const charCount = document.getElementById('charCount');

  function setLoading(on) {
    submitBtn.disabled = on;
    submitBtn.classList.toggle('disabled', on);
    statusSpan.innerHTML = on ? '<span class="spinner"></span> Working...' : '';
  }

  txt.addEventListener('input', () => {
    charCount.textContent = txt.value.length + ' chars';
  });

  copyBtn.addEventListener('click', async () => {
    const text = translatedDiv.textContent.trim();
    if (!text) return;
    try {
      await navigator.clipboard.writeText(text);
      copyBtn.textContent = 'Copied';
      setTimeout(()=> copyBtn.textContent = 'Copy', 1500);
    } catch (e) {
      alert('Copy failed');
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = txt.value.trim();
    if (!text) return alert('Enter text to translate');
    setLoading(true);
    translatedDiv.textContent = '';
    player.src = '';
    try {
      const res = await fetch('/api/translate', {
        method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({text})
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Server error');
      translatedDiv.textContent = data.translated;
      player.src = data.audio;
      player.load();
      statusSpan.innerHTML = '';
    } catch (err) {
      translatedDiv.textContent = 'Error: ' + err.message;
      statusSpan.innerHTML = '';
    } finally {
      setLoading(false);
    }
  });
});
