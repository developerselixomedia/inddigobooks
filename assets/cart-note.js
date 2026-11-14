// Cart Note Saver
export function saveCartNote(note) {
  return fetch('/cart/update.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ note })
  });
}
