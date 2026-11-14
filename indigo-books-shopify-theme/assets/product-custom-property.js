// Line Item Custom Properties
export function getCustomProperties(form) {
  const props = {};
  new FormData(form).forEach((val, key) => {
    if (key.startsWith('properties[')) props[key] = val;
  });
  return props;
}
