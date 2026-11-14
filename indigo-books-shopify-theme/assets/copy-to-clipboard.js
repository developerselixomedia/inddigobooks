// Copy to Clipboard
export function copyToClipboard(text, el) {
  navigator.clipboard.writeText(text).then(() => {
    if (el) {
      const orig = el.innerText;
      el.innerText = 'Copied!';
      setTimeout(() => el.innerText = orig, 2000);
    }
  });
}
