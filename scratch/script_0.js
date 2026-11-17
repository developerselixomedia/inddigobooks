
    (function() {
      var origWarn = console.warn;
      console.warn = function() {
        if (arguments[0] && typeof arguments[0] === 'string' && arguments[0].indexOf('cdn.tailwindcss.com') !== -1) return;
        return origWarn.apply(console, arguments);
      };
    })();
  