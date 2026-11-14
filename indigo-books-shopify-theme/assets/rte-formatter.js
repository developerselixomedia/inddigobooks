// Rich Text Formatter (Wraps tables & embeds)
document.querySelectorAll('.rte table').forEach(t => {
  const wrap = document.createElement('div');
  wrap.className = 'table-responsive';
  t.parentNode.insertBefore(wrap, t);
  wrap.appendChild(t);
});
