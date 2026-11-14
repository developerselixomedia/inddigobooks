// QR Code Image Helper
class QRCodeImage extends HTMLElement {
  connectedCallback() {
    const upi = this.dataset.upi;
    const amount = this.dataset.amount;
    if (upi && amount) {
      const img = document.createElement('img');
      img.src = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=${upi}&am=${amount}`;
      this.appendChild(img);
    }
  }
}
if (!customElements.get('qr-code-image')) customElements.define('qr-code-image', QRCodeImage);
