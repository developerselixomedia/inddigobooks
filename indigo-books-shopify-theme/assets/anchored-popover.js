// Anchored Popovers
export class AnchoredPopover extends HTMLElement {
  connectedCallback() {
    this.button = this.querySelector('[popovertarget]');
  }
}
if (!customElements.get('anchored-popover')) customElements.define('anchored-popover', AnchoredPopover);
