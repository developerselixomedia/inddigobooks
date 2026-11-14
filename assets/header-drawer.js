// Header Mobile Drawer
export class HeaderDrawer extends HTMLElement {
  open() { this.classList.add('open'); }
  close() { this.classList.remove('open'); }
}
if (!customElements.get('header-drawer')) customElements.define('header-drawer', HeaderDrawer);
