// Custom Accordion for Book Specs
class CustomAccordion extends HTMLElement {
  connectedCallback() {
    this.querySelectorAll('details').forEach(el => {
      el.addEventListener('toggle', () => {
        if (el.open && this.hasAttribute('data-single-open')) {
          this.querySelectorAll('details').forEach(other => { if (other !== el) other.removeAttribute('open'); });
        }
      });
    });
  }
}
customElements.define('custom-accordion', CustomAccordion);
