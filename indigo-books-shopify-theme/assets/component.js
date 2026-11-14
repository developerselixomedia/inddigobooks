// Base Horizon Component
export class HorizonComponent extends HTMLElement {
  get sectionId() { return this.dataset.sectionId || ''; }
}
