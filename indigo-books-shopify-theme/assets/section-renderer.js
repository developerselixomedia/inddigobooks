// Section Rendering API Wrapper
export function fetchSection(sectionId, url = window.location.href) {
  const fetchUrl = `${url}${url.includes('?') ? '&' : '?'}section_id=${sectionId}`;
  return fetch(fetchUrl).then(r => r.text());
}
