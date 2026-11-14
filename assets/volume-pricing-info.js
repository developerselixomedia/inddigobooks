// Volume Pricing Info Modal
export class VolumePricingInfo extends HTMLElement {
  connectedCallback() {
    this.querySelector('[data-open-volume-pricing]')?.addEventListener('click', () => {
      this.querySelector('.volume-pricing-modal')?.classList.add('open');
    });
    this.querySelector('[data-close-volume-pricing]')?.addEventListener('click', () => {
      this.querySelector('.volume-pricing-modal')?.classList.remove('open');
    });
  }
}
if (!customElements.get('volume-pricing-info')) customElements.define('volume-pricing-info', VolumePricingInfo);
