// Focus Trap
export function trapFocus(container) {
  const elements = container.querySelectorAll('a, button, input, textarea, select');
  if (elements.length) elements[0].focus();
}
