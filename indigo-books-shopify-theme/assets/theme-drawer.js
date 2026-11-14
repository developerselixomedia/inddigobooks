// Base Drawer Component
export class ThemeDrawer extends HTMLElement {
  open() { this.setAttribute('open', ''); }
  close() { this.removeAttribute('open'); }
}
if (!customElements.get('theme-drawer')) customElements.define('theme-drawer', ThemeDrawer);
