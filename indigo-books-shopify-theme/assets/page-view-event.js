// Page View Event Dispatcher
document.addEventListener('DOMContentLoaded', () => {
  if (window.ThemeEvents) window.ThemeEvents.emit('page:view', { url: window.location.href });
});
