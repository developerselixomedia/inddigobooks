// Recently Viewed Books using localStorage
const STORAGE_KEY = 'indigo_recently_viewed_books';
export function recordBookView(productHandle) {
  let list = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
  list = [productHandle, ...list.filter(h => h !== productHandle)].slice(0, 8);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
}
export function getRecentlyViewed() {
  return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
}
