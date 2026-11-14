// QR Code Generator for UPI / Instant Checkout
export function generateUPIQr(upiId, amount, name = 'Indigo Books') {
  const upiUrl = `upi://pay?pa=${encodeURIComponent(upiId)}&pn=${encodeURIComponent(name)}&am=${amount}&cu=INR`;
  return `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(upiUrl)}`;
}
