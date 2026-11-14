// Section Lazy Hydration via IntersectionObserver
export function hydrateOnVisible(el, hydrateFn) {
  const obs = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      obs.disconnect();
      hydrateFn();
    }
  });
  obs.observe(el);
}
