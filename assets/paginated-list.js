// Paginated List Controller
export class PaginatedList extends HTMLElement {
  loadNextPage(url) {
    return fetch(url).then(r => r.text());
  }
}
if (!customElements.get('paginated-list')) customElements.define('paginated-list', PaginatedList);
