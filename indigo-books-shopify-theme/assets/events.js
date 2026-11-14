// Central Theme Event Bus
window.ThemeEvents = {
  subscribe(event, handler) { window.addEventListener(event, handler); },
  emit(event, detail = {}) { window.dispatchEvent(new CustomEvent(event, { detail })); }
};
