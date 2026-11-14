// Popover Polyfill
if (!HTMLElement.prototype.hasOwnProperty('popover')) {
  HTMLElement.prototype.showPopover = function() { this.style.display = 'block'; };
  HTMLElement.prototype.hidePopover = function() { this.style.display = 'none'; };
}
