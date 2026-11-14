// Money Formatter
export function formatMoney(cents, format = window.ShopifyTheme?.moneyFormat || '₹{{amount}}') {
  if (typeof cents === 'string') cents = cents.replace('.', '');
  const value = (cents / 100).toFixed(2);
  return format.replace('{{amount}}', value).replace('{{amount_no_decimals}}', Math.round(cents / 100));
}
