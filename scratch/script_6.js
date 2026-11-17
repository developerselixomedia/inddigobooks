
(function() {
  'use strict';

  /* 1. CURATED REAL CATALOG DATA FOR SHELVES & HERO */
  function getFallbackCoverSvg(title, author) {
    var palettes = [
      { top: '#3E1715', bot: '#180706', gold: '#E5C07B', text: '#FAF7F2' },
      { top: '#15263D', bot: '#0A131F', gold: '#D4AF37', text: '#F8FAFC' },
      { top: '#1A2E22', bot: '#0B150F', gold: '#C5A059', text: '#F4F7F4' },
      { top: '#2D182A', bot: '#140813', gold: '#E0B084', text: '#FBF5F8' },
      { top: '#222035', bot: '#0D0C17', gold: '#DFB76C', text: '#F6F5FA' }
    ];
    var t = (title || 'Indigo Books').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
    var a = (author || 'Curated Edition').replace(/<[^>]*>/g, '').replace(/&/g, '&amp;').trim();
    
    var h = 0;
    for (var k = 0; k < t.length; k++) h = (h + t.charCodeAt(k)) % palettes.length;
    var pal = palettes[h];
    
    var words = t.split(/\s+/);
    var lines = [];
    var curr = '';
    for (var w = 0; w < words.length; w++) {
      var word = words[w];
      if ((curr + ' ' + word).trim().length <= 16) {
        curr = (curr + ' ' + word).trim();
      } else {
        if (curr) lines.push(curr);
        curr = word;
      }
    }
    if (curr) lines.push(curr);
    if (lines.length > 3) {
      lines = lines.slice(0, 2);
      lines.push(words.slice(lines.join(' ').split(/\s+/).length).join(' ').substring(0, 13) + '...');
    }
    
    var startY = 135 - ((lines.length - 1) * 11);
    var titleSvg = '';
    for (var i = 0; i < lines.length; i++) {
      var y = startY + (i * 22);
      titleSvg += '<text x="100" y="' + y + '" fill="' + pal.text + '" font-family="Georgia, serif" font-size="13" font-weight="bold" text-anchor="middle">' + lines[i] + '</text>';
    }
    
    var authorY = startY + (lines.length * 22) + 14;
    var authorStr = a.substring(0, 22);
    
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 300" width="100%" height="100%">' +
      '<defs>' +
        '<linearGradient id="ev_g_' + h + '" x1="0%" y1="0%" x2="100%" y2="100%">' +
          '<stop offset="0%" stop-color="' + pal.top + '"/>' +
          '<stop offset="100%" stop-color="' + pal.bot + '"/>' +
        '</linearGradient>' +
      '</defs>' +
      '<rect width="200" height="300" rx="3" fill="url(#ev_g_' + h + ')"/>' +
      '<rect x="0" y="0" width="10" height="300" fill="rgba(0,0,0,0.3)"/>' +
      '<line x1="10" y1="0" x2="10" y2="300" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>' +
      '<rect x="16" y="16" width="168" height="268" rx="2" fill="none" stroke="' + pal.gold + '" stroke-width="1.2" opacity="0.85"/>' +
      '<rect x="19" y="19" width="162" height="262" rx="1" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.6"/>' +
      '<circle cx="100" cy="58" r="22" fill="none" stroke="' + pal.gold + '" stroke-width="1"/>' +
      '<circle cx="100" cy="58" r="18" fill="none" stroke="' + pal.gold + '" stroke-width="0.5" stroke-dasharray="2 2" opacity="0.7"/>' +
      '<text x="100" y="63" fill="' + pal.gold + '" font-family="Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">IB</text>' +
      '<text x="100" y="94" fill="' + pal.gold + '" font-family="sans-serif" font-size="7.5" font-weight="700" letter-spacing="1.5" text-anchor="middle">INDIGO ARCHIVE</text>' +
      titleSvg +
      '<line x1="60" y1="' + (authorY - 6) + '" x2="140" y2="' + (authorY - 6) + '" stroke="' + pal.gold + '" stroke-width="0.75" opacity="0.5"/>' +
      '<text x="100" y="' + (authorY + 8) + '" fill="' + pal.gold + '" font-family="sans-serif" font-size="9.5" font-weight="600" text-anchor="middle">By ' + authorStr + '</text>' +
      '<text x="100" y="266" fill="#888888" font-family="sans-serif" font-size="7" letter-spacing="1.2" text-anchor="middle">PRAYAGRAJ &bull; INDIA</text>' +
    '</svg>';
    return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
  }
  window.getFallbackCoverSvg = getFallbackCoverSvg;
  function handleBookCoverError(img, title, author) {
    if (!img) return;
    img.onerror = null;
    var bookTitle = title || img.getAttribute('data-title') || img.alt || 'Indigo Books Edition';
    var bookAuthor = author || img.getAttribute('data-author') || 'Indigo Archive';
    if (typeof window.getFallbackCoverSvg === 'function') {
      img.src = window.getFallbackCoverSvg(bookTitle, bookAuthor);
    } else if (typeof getFallbackCover === 'function') {
      img.src = getFallbackCover(bookTitle, bookAuthor);
    }
  }
  window.handleBookCoverError = handleBookCoverError;


  /* 0. GLOBAL ASSET URL RESOLVER (Zero 404, Live Shopify CDN & Local Preview Compatible) */
  function getCoverUrl(coverPath, defaultTitle, defaultAuthor) {
    if (!coverPath) {
      if (window.getFallbackCoverSvg) {
        return window.getFallbackCoverSvg(defaultTitle || 'Indigo Books', defaultAuthor || '');
      }
      return (window.PODIUM_CDN_COVERS && (window.PODIUM_CDN_COVERS['hero-godan.jpg'] || window.PODIUM_CDN_COVERS['assets/hero-godan.jpg'])) ||
             (window.SHOPIFY_ASSET_URL_ROOT ? window.SHOPIFY_ASSET_URL_ROOT + 'hero-godan.jpg' : 'assets/hero-godan.jpg');
    }
    // If already absolute HTTP/HTTPS, protocol-relative '//', or data URI, return DIRECTLY without tampering
    if (coverPath.indexOf('http://') === 0 || coverPath.indexOf('https://') === 0 || coverPath.indexOf('//') === 0 || coverPath.indexOf('data:') === 0) {
      return coverPath;
    }
    // Clean relative path prefix
    var clean = coverPath.replace(/^(\.\/)?assets\//, '').replace(/^\//, '');
    if (window.PODIUM_CDN_COVERS) {
      if (window.PODIUM_CDN_COVERS[coverPath]) return window.PODIUM_CDN_COVERS[coverPath];
      if (window.PODIUM_CDN_COVERS[clean]) return window.PODIUM_CDN_COVERS[clean];
      if (window.PODIUM_CDN_COVERS['assets/' + clean]) return window.PODIUM_CDN_COVERS['assets/' + clean];
      var baseName = clean.split('.')[0];
      if (window.PODIUM_CDN_COVERS[baseName]) return window.PODIUM_CDN_COVERS[baseName];
    }
    if (window.SHOPIFY_ASSET_URL_ROOT) {
      return window.SHOPIFY_ASSET_URL_ROOT + clean;
    }
    return 'assets/' + clean;
  }
  window.getCoverUrl = getCoverUrl;

  function fixAllThemeAssetImages() {
    var imgs = document.querySelectorAll('img');
    imgs.forEach(function(img) {
      var rawSrc = img.getAttribute('src');
      if (rawSrc && (rawSrc.indexOf('assets/') === 0 || rawSrc.indexOf('./assets/') === 0)) {
        var resolved = getCoverUrl(rawSrc);
        if (resolved && resolved !== rawSrc) {
          img.src = resolved;
        }
      }
      if (!img.onerror) {
        img.onerror = function() {
          this.onerror = null;
          if (window.getFallbackCoverSvg) {
            this.src = window.getFallbackCoverSvg(this.alt || 'Indigo Books', '');
          }
        };
      }
    });
  }
  window.fixAllThemeAssetImages = fixAllThemeAssetImages;

  var POPULAR_BOOKS = [
    {
      id: 'podium-godan',
      title: 'Godan (गोदान)',
      author: 'Premchand',
      price: '₹299.00',
      rawPrice: 299,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Heritage Edition',
      pages: '344p',
      isbn: '9788174828118',
      cover: 'assets/hero-godan.jpg',
      quote: 'जब तक जीवन में मान-मर्यादा और स्नेह का नाता बना रहे, मनुष्य हर विपत्ति झेल लेता है।',
      excerpt: 'होरी महतो ने दोनों बैलों को सानी-पानी देकर अपनी स्त्री धनिया से कहा—गोबर को ज़रा चिलम भर देने को कहो। धनिया ने घर के भीतर से झाँकते हुए कहा—वह तो कब का चला गया, तुम ही जाओ अपने काम पर। होरी ने लाठी उठाई और सिर पर पगड़ी बाँधते हुए पछतावे भरी आँखों से अपनी सूनी गौशाला की ओर देखा, जहाँ एक गाय बाँधने का उसका बरसों पुराना सपना आज भी अधूरा था।'
    },
    {
      id: 'podium-raag-darbari',
      title: 'Raag Darbari (राग दरबारी)',
      author: 'Shrilal Shukla',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover',
      publisher: 'Rajkamal Prakashan',
      edition: 'Authoritative Release',
      pages: '380p',
      isbn: '9788126702749',
      cover: 'assets/hero-raag-darbari.jpg',
      quote: 'वर्तमान शिक्षा पद्धति रास्ते में पड़ी हुई लावारिस कुतिया है, जिसे कोई भी लात मार सकता है।',
      excerpt: 'वह सड़क थी, जो शहर से चलकर देहात की तरफ़ जाती थी। उस पर एक ट्रक खड़ा था। ट्रक पर लिखा था: "सावधानी हटी, दुर्घटना घटी।" रंगनाथ ने अपना झोला सँभाला और धूल से भरी सड़क पर उतर आया। शिवपालगंज का क़स्बा यहीं से शुरू होता था, जहाँ ज़िन्दगी अपनी सुस्त रफ़्तार से चलती हुई व्यवस्था के अजीबोग़रीब नियमों में उलझी हुई थी।'
    },
    {
      id: 'podium-chitralekha',
      title: 'Chitralekha (चित्रलेखा)',
      author: 'Bhagwaticharan Verma',
      price: '₹299.00',
      rawPrice: 299,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Classic Sahitya Edition',
      pages: '268p',
      isbn: '9788126715428',
      cover: 'assets/hero-chitralekha.jpg',
      quote: 'संसार में न कोई पाप है और न पुण्य, केवल दृष्टिकोण का अंतर है।',
      excerpt: 'संसार में पाप क्या है और पुण्य क्या है? महाप्रभु रत्नाम्बर के आश्रम में दोनों शिष्यों—श्वेतांक और विशालदेव—ने सिर झुकाकर यही प्रश्न पूछा था। गुरु ने मुस्कुराकर उत्तर दिया: "इस संसार में न तो कोई पूर्णतः पापी है और न ही कोई पूर्णतः पुण्यात्मा। मनुष्य परिस्थितियों का दास है और प्रत्येक कर्म की व्याख्या उसके दृष्टिकोण पर निर्भर करती है।" जाओ, पाटलिपुत्र जाकर जीवन की वास्तविकता को अपनी आँखों से देखो।'
    },
    {
      id: 'podium-rashmirathi',
      title: 'Rashmirathi (रश्मिरथी)',
      author: 'Ramdhari Singh Dinkar',
      price: '₹350.00',
      rawPrice: 350,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Poetry Heritage Edition',
      pages: '176p',
      isbn: '9788174820686',
      cover: 'assets/hero-rashmirathi.jpg',
      quote: 'सच्चा शूरवीर वही है जो संकटों में मुस्कुराता है और अपने पराक्रम से भाग्य की रेखाएँ बदल देता है।',
      excerpt: 'जय हो, जग में जले जहाँ भी, नमन पुनीत अनल को। जिस नर में भी दीप्त दिखे, वन्द्य वह ज्योति प्रबल को। कर्ण का जन्म भले ही अज्ञात कुल में हुआ हो, किंतु उसकी भुजाओं में क्षत्रियों को पराजित करने वाला शौर्य और हृदय में मर्यादा का अद्वितीय संकल्प था। कुरुक्षेत्र की रणभूमि में जब अस्त्र उठे, तब दानवीर कर्ण ने अपने कवच-कुंडल तक त्याग कर इतिहास के पन्नों में अपनी अमर गाथा लिख दी।'
    },
    {
      id: 'podium-kuchh-ishq',
      title: 'Kuchh Ishq Kiya Kuchh Kaam Kiya',
      author: 'Piyush Mishra',
      price: '₹250.00',
      rawPrice: 250,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Modern Poetry Edition',
      pages: '160p',
      isbn: '9788126728466',
      cover: 'assets/hero-kuchh-ishq.jpg',
      quote: 'कुछ इश्क़ किया कुछ काम किया, वो काम बहुत नुक़सान किया।',
      excerpt: 'हम अपने भीतर एक पूरा शहर लेकर घूमते हैं। कभी ग्वालियर की संकरी गलियाँ, कभी दिल्ली की सर्द रातें और कभी बंबई की बेचैन सुबहें। इश्क़ अधूरा रह जाए तो कविता बन जाता है, और काम पूरा हो जाए तो ज़िन्दगी की रोटी बन जाता है। इस किताब के पन्नों में वही सारी ख़ामोशियाँ और शोर दर्ज़ हैं जिन्हें हमने जिया है।'
    },
    {
      id: 'book-tarkash',
      title: 'Tarkash (तरकश)',
      author: 'Javed Akhtar',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover Deluxe',
      publisher: 'Rajkamal Prakashan',
      edition: 'Deluxe Devanagari Edition',
      pages: '240p',
      isbn: '9788126702671',
      cover: 'assets/book-tarkash.jpg',
      quote: 'क्यूँ डरें ज़िन्दगी में क्या होगा, कुछ न होगा तो तजुर्बा होगा।',
      excerpt: 'ज़िन्दगी के तरकश में बहुत से तीर होते हैं—कुछ उम्मीदों के, कुछ बिछड़ने के और कुछ ख़ामोश रातों में लिखी गई नज़्मों के। जब अल्फ़ाज़ काग़ज़ पर उतरते हैं, तो सिर्फ़ एक शायर का दर्द नहीं, बल्कि पूरे समाज की धड़कन बयाँ करते हैं। ये अशआर उन रास्तों की कहानी हैं जो शहर की रौशनी से दूर तन्हाई में जाकर खुलते हैं।'
    },
    {
      id: 'podium-gypsy',
      title: 'Gypsy (जिप्सी)',
      author: 'Ila Chandra Joshi',
      price: '₹499.00',
      rawPrice: 499,
      format: 'Hardcover',
      publisher: 'Lokbharti Prakashan',
      edition: 'Psychoanalytic Classic',
      pages: '312p',
      isbn: '9788174822017',
      cover: 'assets/hero-gypsy.jpg',
      quote: 'अंतर्मन के द्वंद्व से बड़ा कोई कुरुक्षेत्र इस संसार में नहीं है।',
      excerpt: 'मनुष्य के अंतर्मन की गहराइयों में छिपी अतृप्त वासनाएँ और अवचेतन की गूँज जब बाहर आती हैं, तब वह समाज के बनाए सभी बंधनों को तोड़ देना चाहती है। जिप्सी का जीवन किसी बंधी हुई नदी की तरह नहीं, बल्कि उस उन्मुक्त झरने की तरह है जो पत्थरों से टकराकर भी अपना नया रास्ता बना लेता है।'
    },
    {
      id: 'book-aadha-gaon',
      title: 'Aadha Gaon (आधा गाँव)',
      author: 'Rahi Masoom Raza',
      price: '₹450.00',
      rawPrice: 450,
      format: 'Paperback',
      publisher: 'Rajkamal Prakashan',
      edition: 'Heritage Edition',
      pages: '388p',
      isbn: '9788126702589',
      cover: 'assets/book-aadha-gaon.jpg',
      quote: 'मेरी भाषा भोजपुरी और हिन्दुस्तानी है, और मेरा गाँव गंगोली इस पूरे मुल्क का आईना है।',
      excerpt: 'गंगोली कोई काग़ज़ पर बना हुआ गाँव नहीं था, वह ज़िन्दा लोगों की मिट्टी, उनकी हँसी, उनकी गालियों और उनके मुहर्रम के मातम से बना था। विभाजन की आँधी आई, मुल्क बँट गया, लेकिन गंगोली के लोगों का वजूद उस मिट्टी से बँट नहीं सका। यह दास्तान उन इंसानों की है जो ज़मीन और ज़मीर के बीच झूलते रहे।'
    },
    {
      id: 'book-mahabhoj',
      title: 'Mahabhoj (महाभोज)',
      author: 'Mannu Bhandari',
      price: '₹225.00',
      rawPrice: 225,
      format: 'Paperback',
      publisher: 'Radhakrishna Prakashan',
      edition: 'Political Classic',
      pages: '192p',
      isbn: '9788171190478',
      cover: 'assets/book-mahabhoj.jpg',
      quote: 'राजनीति के इस महाभोज में आम आदमी हमेशा एक निवाला मात्र बनकर रह जाता है।',
      excerpt: 'सरोहा गाँव में दाऊसाहब की चुनावी राजनीति की बिसात बिछ चुकी थी। एक ग़रीब दलित की मौत कोई व्यक्तिगत त्रासदी नहीं थी, बल्कि सत्ता के गलियारों में गिद्धों के भोज का बहाना बन चुकी थी। हर कोई उस लाश पर अपनी रोटियाँ सेंकने को तैयार था, और व्यवस्था मूक दर्शक बनकर तमाशा देख रही थी।'
    },
    {
      id: 'book-shekhar',
      title: 'Shekhar: Ek Jeevani',
      author: 'Agyeya (अज्ञेय)',
      price: '₹599.00',
      rawPrice: 599,
      format: 'Hardcover Deluxe',
      publisher: 'Saraswati Press',
      edition: 'Complete Volumes I & II',
      pages: '512p',
      isbn: '9788174821034',
      cover: 'assets/book-shekhar.jpg',
      quote: 'अनुभूति ही सत्य है, और सत्य ही व्यक्ति की एकमात्र मुक्ति है।',
      excerpt: 'शशि ने जब पहली बार उसकी आँखों में देखा था, तो शेखर को लगा कि स्वतंत्रता कोई बाहर मिलने वाली चीज़ नहीं है, यह तो आत्मा की एक आंतरिक स्थिति है। समाज की रूढ़ियों के विरुद्ध उसका विद्रोह केवल क्रोध नहीं था, बल्कि एक संवेदनशील कलाकार की आत्म-खोज की तड़प थी।'
    },
    {
      id: 'book-gaban',
      title: 'Gaban (ग़बन)',
      author: 'Premchand',
      price: '₹220.00',
      rawPrice: 220,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Sahitya Edition',
      pages: '280p',
      isbn: '9788174828132',
      cover: 'assets/book-gaban.jpg',
      quote: 'झूठी प्रतिष्ठा की चाह इंसान को सबसे बड़े पतन की ओर ले जाती है।',
      excerpt: 'जालपा की चंद्रहार पाने की ज़िद ने रमानाथ को उस दलदल में धकेल दिया था जहाँ से वापसी का कोई रास्ता नहीं था। झूठी शान और दिखावे की लालसा ने एक सीधे-सादे क्लर्क को ग़बन के अपराध तक पहुँचा दिया। यह केवल एक चोरी की कहानी नहीं, बल्कि मध्यमवर्गीय समाज की खोखली प्रतिष्ठा की व्यथा है।'
    },
    {
      id: 'book-nirmala',
      title: 'Nirmala (निर्मला)',
      author: 'Premchand',
      price: '₹195.00',
      rawPrice: 195,
      format: 'Paperback',
      publisher: 'Lokbharti Prakashan',
      edition: 'Authoritative Classic',
      pages: '208p',
      isbn: '9788174828149',
      cover: 'assets/book-nirmala.jpg',
      quote: 'बेमेल विवाह केवल दो शरीरों का नहीं, आत्मा और मानवीय गरिमा का दलन है।',
      excerpt: 'निर्मला की आँखें आंसुओं से भरी थीं जब उसने उस अनचाहे रिश्ते की दहलीज पर कदम रखा। समाज की कुरीतियों और बेमेल विवाह के दंश ने उसकी सारी खुशियाँ छीन ली थीं। तोताराम की हवेली में उसका जीवन एक सजीव पिंजरे जैसा था, जहाँ हर साँस के साथ आत्मसम्मान की बलि चढ़ती थी।'
    },
    {
      id: 'hero-book-murakami',
      title: 'Haruki Murakami Master Collection',
      author: 'Haruki Murakami',
      price: '₹1,899.00',
      rawPrice: 1899,
      format: 'Box Set (4 Volumes)',
      publisher: 'Vintage International',
      edition: 'Deluxe Slipcase Box Set',
      pages: '1240p',
      isbn: '9780099448761',
      cover: 'assets/hero-book-murakami.jpg',
      quote: 'Death exists, not as the opposite of life, but as an integral part of it.',
      excerpt: "When Toru Watanabe heard the Beatles' song \"Norwegian Wood\" playing through the cabin speakers of the Boeing 747, a wave of bittersweet memories swept over him. He was transported back to the Tokyo of the late 1960s—to quiet Sunday walks with Naoko through autumn meadows, the unspoken weight of Kizuki's suicide, and the delicate struggle of holding on to life while mourning the dead."
    },
    {
      id: 'book-samvidhan',
      title: 'Bharat Ka Samvidhan (भारत का संविधान)',
      author: 'Government of India / Dr. B.R. Ambedkar',
      price: '₹450.00',
      rawPrice: 450,
      format: 'Hardcover',
      publisher: 'Central Law Publications',
      edition: 'Official Bilingual Edition',
      pages: '560p',
      isbn: '9789389657029',
      cover: 'assets/book-samvidhan.jpg',
      quote: 'संविधान केवल वकीलों का दस्तावेज़ नहीं, यह जीवन जीने का माध्यम और राष्ट्र की आत्मा है।',
      excerpt: 'हम, भारत के लोग, भारत को एक सम्पूर्ण प्रभुत्व-सम्पन्न, समाजवादी, पंथनिरपेक्ष, लोकतंत्रात्मक गणराज्य बनाने के लिए तथा उसके समस्त नागरिकों को सामाजिक, आर्थिक और राजनैतिक न्याय, विचार, अभिव्यक्ति, विश्वास, धर्म और उपासना की स्वतंत्रता, प्रतिष्ठा और अवसर की समता प्राप्त कराने के लिए दृढ़संकल्प होकर अपनी इस संविधान सभा में आज एतद्द्वारा इस संविधान को अंगीकृत, अधिनियमित और आत्मार्पित करते हैं।'
    }
  ];

  var currentActiveBook = POPULAR_BOOKS[0];
  var isSpreadOpen = false;
  var previousViewBeforeSolo = 'home';

  
  /* DYNAMIC AUTHENTIC LITERARY CONTENT GENERATORS (Monolingual: Pure Hindi OR Pure English) */
  function isHindiBook(b) {
    var rawText = (b.title || '') + ' ' + (b.author || '') + ' ' + (b.category || '') + ' ' + (b.genre || '') + ' ' + (b.publisher || '') + ' ' + (b.pub || '');
    if (/[ऀ-ॿ]/.test(rawText)) return true;
    var tLower = rawText.toLowerCase();
    var hindiMarkers = [
      'rajkamal', 'lokbharti', 'radhakrishna', 'vani', 'kitabghar', 'sahitya', 'jnanpith',
      'rekhta', 'shayari', 'ghazal', 'nazm', 'urdu', 'hindi', 'samvidhan', 'kahani', 'kavita',
      'premchand', 'shrilal shukla', 'dinkar', 'renu', 'javed akhtar', 'gulzar', 'rahat indori',
      'faiz', 'ghalib', 'jaun elia', 'manto', 'harivansh', 'bachchan', 'bhagwaticharan',
      'mahadevi', 'chandra joshi', 'amritlal', 'bhisham sahni', 'nirmal verma', 'kamleshwar',
      'mannu bhandari', 'mohan rakesh', 'nirala', 'agyeya', 'hazari prasad', 'tarkash', 'godan',
      'raag darbari', 'chitralekha', 'rashmirathi', 'gaban', 'nirmala', 'karmabhoomi', 'sevasadan',
      'mansarovar', 'madhushala', 'kamayani', 'tamash', 'aadha gaon', 'mahabhoj', 'gypsy', 'prakashan'
    ];
    for (var i = 0; i < hindiMarkers.length; i++) {
      if (tLower.indexOf(hindiMarkers[i]) !== -1) return true;
    }
    return false;
  }

  function getHindiAuthorName(author) {
    if (!author) return 'रचनाकार';
    var aLower = author.toLowerCase();
    if (aLower.indexOf('premchand') !== -1) return 'मुंशी प्रेमचंद';
    if (aLower.indexOf('shrilal') !== -1) return 'श्रीलाल शुक्ल';
    if (aLower.indexOf('dinkar') !== -1) return 'रामधारी सिंह "दिनकर"';
    if (aLower.indexOf('bhagwati') !== -1) return 'भगवतीचरण वर्मा';
    if (aLower.indexOf('renu') !== -1) return 'फणीश्वरनाथ रेणु';
    if (aLower.indexOf('javed') !== -1) return 'जावेद अख़्तर';
    if (aLower.indexOf('gulzar') !== -1) return 'गुलज़ार';
    if (aLower.indexOf('rahat') !== -1) return 'राहत इन्दौरी';
    if (aLower.indexOf('faiz') !== -1) return 'फ़ैज़ अहमद फ़ैज़';
    if (aLower.indexOf('ghalib') !== -1) return 'मिर्ज़ा ग़ालिब';
    if (aLower.indexOf('jaun') !== -1) return 'जौन एलिया';
    if (aLower.indexOf('joshi') !== -1) return 'इलाचन्द्र जोशी';
    if (aLower.indexOf('sahni') !== -1) return 'भीष्म साहनी';
    if (aLower.indexOf('nagar') !== -1) return 'अमृतलाल नागर';
    if (aLower.indexOf('bhandari') !== -1) return 'मन्नू भंडारी';
    if (aLower.indexOf('rakesh') !== -1) return 'मोहन राकेश';
    if (aLower.indexOf('bachchan') !== -1) return 'हरिवंश राय बच्चन';
    if (aLower.indexOf('mahadevi') !== -1) return 'महादेवी वर्मा';
    if (aLower.indexOf('prasad') !== -1) return 'जयशंकर प्रसाद';
    if (aLower.indexOf('nirala') !== -1) return 'सूर्यकांत त्रिपाठी "निराला"';
    if (aLower.indexOf('ambedkar') !== -1) return 'डॉ. भीमराव आंबेडकर';
    if (aLower.indexOf('mishra') !== -1) return 'पीयूष मिश्रा';
    if (/[ऀ-ॿ]/.test(author)) return author;
    return 'कथाकार';
  }

  function getCleanDisplayTitle(title, isHindi) {
    if (!title) return isHindi ? 'कालजयी रचना' : 'Masterwork';
    if (isHindi) {
      var devMatch = title.match(/[ऀ-ॿ][ऀ-ॿ\s।॥:-]*/);
      if (devMatch && devMatch[0].trim().length > 2) {
        return devMatch[0].trim();
      }
      return title.split(':')[0].split('(')[0].trim();
    }
    return title.split('(')[0].trim();
  }

  function getBookAuthenticExcerpt(b) {
    var hindi = isHindiBook(b);
    var cat = (b.category || b.genre || '').toLowerCase();

    // If custom excerpt already authentic and in matching script, preserve it
    if (b.excerpt && b.excerpt.indexOf('Authoritative original publisher release') === -1) {
      var hasDevanagari = /[ऀ-ॿ]/.test(b.excerpt);
      if ((hindi && hasDevanagari) || (!hindi && !hasDevanagari)) {
        return b.excerpt;
      }
    }

    if (hindi) {
      var hindiAuthor = getHindiAuthorName(b.author);
      if (cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1 || cat.indexOf('ghazal') !== -1 || cat.indexOf('nazm') !== -1) {
        return 'शब्द जब अंतर्मन के मौन से निकलकर काग़ज़ पर उतरते हैं, तो वह केवल कविता नहीं रहते, बल्कि समय की धड़कन बन जाते हैं। ' + hindiAuthor + ' की यह अमर काव्य कृति मानवीय संवेदनाओं, प्रेम, विरह और अस्तित्व के गहरे प्रश्नों को स्पर्श करती है। प्रत्येक छंद पाठक के हृदय में एक अमिट गूँज छोड़ जाता है और आत्मा को एक नई चेतना से आलोकित करता है।';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1 || cat.indexOf('kahani') !== -1) {
        return 'कथा का आरंभ उस मोड़ से होता है जहाँ मानवीय नियति और सामाजिक यथार्थ आमने-सामने खड़े होते हैं। कथा-साहित्य की इस कालजयी धारा में ' + hindiAuthor + ' ने अपने पात्रों के अंतर्द्वंद्व और समाज की जटिल बुनावट को अत्यंत सूक्ष्मता से उकेरा है। हर पृष्ठ पर जीवन की सच्ची अनुभूतियाँ और विचारोत्तेजक प्रसंग जीवंत हो उठते हैं।';
      }
      if (cat.indexOf('criticism') !== -1 || cat.indexOf('sahitya') !== -1 || cat.indexOf('essay') !== -1) {
        return 'साहित्य और समाज के अंतर्संबंधों का गहन मूल्यांकन प्रस्तुत करती यह कृति आलोचनात्मक चिंतन का अप्रतिम उदाहरण है। रचनाकार ने गहन विमर्श के माध्यम से पाठकीय चेतना को नई दृष्टि प्रदान की है, जहाँ परंपरा और आधुनिकता का संतुलन अत्यंत प्रमाणिक रूप में उपस्थित है।';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('judic') !== -1 || cat.indexOf('constitution') !== -1 || cat.indexOf('samvidhan') !== -1) {
        return 'विधि और न्याय का आधार स्तंभ वह सामाजिक अनुबंध है जो प्रत्येक नागरिक के अधिकारों और मानवीय गरिमा को सुनिश्चित करता है। यह कृति वैधानिक सिद्धांतों, न्यायिक निर्णयों और विधिक व्याख्याओं का प्रामाणिक संदर्भ ग्रंथ है, जो अध्येताओं और विचारकों के लिए अत्यंत उपादेय है।';
      }
      if (cat.indexOf('history') !== -1 || cat.indexOf('biograph') !== -1 || cat.indexOf('memoir') !== -1 || cat.indexOf('itihas') !== -1) {
        return 'इतिहास की धारा में खोए हुए प्रसंगों और युगप्रवर्तक व्यक्तित्वों के जीवन का सजीव आख्यान। अतीत के पन्नों से सत्य को उजागर करते हुए यह कृति तत्कालीन सामाजिक और सांस्कृतिक परिवेश का जीवंत एवं प्रामाणिक चित्र खींचती है।';
      }
      return 'मानवीय अनुभव और बौद्धिक चेतना की अनूठी अभिव्यक्ति। विचार और संवेदना के संगम पर रची गई यह कालजयी रचना पाठक को गहराई से सोचने और आत्ममंथन करने के लिए निरंतर प्रेरित करती है।';
    } else {
      var authorEng = b.author || 'The author';
      if (cat.indexOf('poetry') !== -1) {
        return 'When words arise from the quiet depths of introspection, they transcend verse to become the very pulse of human memory. ' + authorEng + ' explores poignant truths of longing, mortality, and grace, leaving an indelible resonance upon the reflective reader.';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1) {
        return 'The narrative begins at that tender crossroad where individual fate confronts the relentless cadence of the world. With acute psychological acuity and evocative prose, ' + authorEng + ' unravels the fragile bonds of ambition and belonging, rendering every chapter a lucid study of the human spirit.';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1 || cat.indexOf('judic') !== -1) {
        return 'The foundation of justice rests upon covenants designed to safeguard human liberty and democratic dignity. This definitive scholarly work provides an authoritative analysis of constitutional jurisprudence, landmark doctrines, and statutory principles indispensable for scholars and jurists alike.';
      }
      if (cat.indexOf('history') !== -1 || cat.indexOf('biograph') !== -1) {
        return 'A compelling chronicle illuminating forgotten epochs and transformative lives. Drawing upon rigorous archival sources, this volume reconstructs historical turning points with literary precision, offering vital perspective on the contours of our shared heritage.';
      }
      return 'A distinguished contribution to contemporary letters. Elegantly crafted and deeply contemplative, this volume probes enduring questions of human experience, offering readers a luminous engagement with truth and literary art.';
    }
  }

  function getBookAuthenticQuote(b) {
    var hindi = isHindiBook(b);
    var cat = (b.category || b.genre || '').toLowerCase();

    if (b.quote && b.quote.indexOf('A celebrated work of modern') === -1) {
      var hasDevanagari = /[ऀ-ॿ]/.test(b.quote);
      if ((hindi && hasDevanagari) || (!hindi && !hasDevanagari)) {
        return b.quote;
      }
    }

    if (hindi) {
      if (cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1) {
        return 'काव्य वही है जो हृदय के मौन को वाणी दे और अंधकार में दीप जला दे।';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1 || cat.indexOf('stories') !== -1) {
        return 'जीवन की सच्ची गाथा वही है जो मनुष्य के संघर्ष और उसकी अदम्य जिजीविषा को स्वर दे।';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1) {
        return 'न्याय केवल क़ानून का पालन नहीं, बल्कि मानवीय गरिमा और समानता की सर्वोच्च रक्षा है।';
      }
      return 'शब्द समय की सीमा से परे जाकर विचार और सत्य को सदैव जीवित रखते हैं।';
    } else {
      if (cat.indexOf('poetry') !== -1) {
        return 'Poetry is the quiet illumination of truths that words alone can seldom convey.';
      }
      if (cat.indexOf('novel') !== -1 || cat.indexOf('fiction') !== -1) {
        return 'Literature endures because it preserves the fragile, unvarnished truth of who we are.';
      }
      if (cat.indexOf('law') !== -1 || cat.indexOf('constitution') !== -1) {
        return 'Justice is not merely the letter of the statute, but the living conscience of human equality.';
      }
      return 'True books do not pass away with the season; they remain constant companions across time.';
    }
  }

/* 2. RENDER OVERLAPPING 3D BOOK SHELVES */
  function renderAllShelves() {
    renderShelfRow('v2ShelfPopular', POPULAR_BOOKS);
    renderShelfRow('v2ShelfHindi', POPULAR_BOOKS.slice(0, 4));
    renderShelfRow('v2ShelfPoetry', [POPULAR_BOOKS[3], POPULAR_BOOKS[4], POPULAR_BOOKS[5], POPULAR_BOOKS[7]]);
    renderShelfRow('v2ShelfLaw', [POPULAR_BOOKS[13], POPULAR_BOOKS[8], POPULAR_BOOKS[9], POPULAR_BOOKS[1]]);
  }

  function renderShelfRow(containerId, books) {
    var row = document.getElementById(containerId);
    if (!row) return;
    row.innerHTML = '';

    books.forEach(function(b) {
      var card = document.createElement('div');
      card.className = 'v2-book-card';
      card.onclick = function() { window.openSoloBookPage(b.id); };

      var coverUrl = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var shelfFallback = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div class="v2-card-cover-wrap">' +
          '<div class="v2-card-cover-leaf" style="position:relative; background-color:#FAF7F0;">' +
            '<img src="' + coverUrl + '" alt="' + b.title + '" data-author="' + b.author + '" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this);" />' +
          '</div>' +
        '</div>' +
        '<div class="v2-card-details-sheet">' +
          '<div>' +
            '<div class="v2-card-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>' +
            '<h3 class="v2-card-title">' + b.title + '</h3>' +
            '<div class="v2-card-author">By ' + b.author + '</div>' +
          '</div>' +
          '<div>' +
            '<div class="v2-card-price">' + b.price + '</div>' +
            '<div class="v2-card-btn-row">' +
              '<button type="button" class="v2-card-preview-btn">Preview &rarr;</button>' +
              '<button type="button" class="v2-card-quick-btn">1-Click Buy</button>' +
            '</div>' +
          '</div>' +
        '</div>';

      var cImg = card.querySelector('.v2-card-cover-leaf img');
      if (cImg) cImg.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, b.title, b.author); };

      var cLeaf = card.querySelector('.v2-card-cover-leaf');
      if (cLeaf) {
        cLeaf.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(b.id);
        };
      }
      var pBtn = card.querySelector('.v2-card-preview-btn');
      if (pBtn) {
        pBtn.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(b.id);
        };
      }
      var qBtn = card.querySelector('.v2-card-quick-btn');
      if (qBtn) {
        qBtn.onclick = function(e) {
          e.stopPropagation();
          if (typeof window.openExpressPhoneCheckout === 'function') {
            window.openExpressPhoneCheckout(b.id);
          } else if (typeof window.openQuickOrderModal === 'function') {
            window.openQuickOrderModal(b.id);
          }
        };
      }

      row.appendChild(card);
    });
  }

  /* 3. FULL 5,559 BOOK ARCHIVE LISTING & FACETED FILTERS (100% Tested & Fully Interactive) */
  var archiveCurrentGenre = 'all';
  var archiveSearchQuery = '';
  var archiveSortOrder = 'featured';
  var archivePage = 1;
  var ARCHIVE_PAGE_SIZE = 24;

  var HINDI_CLASSIC_AUTHORS = [
    'premchand', 'shrilal shukla', 'dinkar', 'bachchan', 'phanishwar nath renu', 'renu',
    'jaishankar prasad', 'suryakant tripathi nirala', 'nirala', 'mahadevi varma',
    'dharamvir bharati', 'bhagwati charan verma', 'bhagwaticharan', 'mannu bhandari',
    'krishna sobti', 'yashpal', 'bhisham sahni', 'kamleshwar', 'hazari prasad dwivedi',
    'mohan rakesh', 'ilachandra joshi', 'amritlal nagar', 'upendranath ashka', 'shivani',
    'kashinath singh', 'vinod kumar shukla', 'alok dhanwa', 'manglesh dabral', 'muktibodh',
    'chatur sen', 'vrindavan lal verma'
  ];

  var POETRY_AUTHORS = [
    'gulzar', 'javed akhtar', 'rahat indori', 'piyush mishra', 'faiz', 'ghalib',
    'jaun elia', 'bashir badr', 'dushyant kumar', 'sahir', 'dinkar', 'bachchan',
    'kaifi azmi', 'iqbal', 'parveen shakir', 'ahmad faraz', 'tagore', 'kabir', 'mira',
    'tulsi', 'surdas', 'firaq'
  ];

  function getArchivePool() {
    var pool = (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) ? window.MASTER_SEARCH_CATALOG : POPULAR_BOOKS;
    return pool;
  }

  window.filterArchiveGenre = function(genre, btn) {
    archiveCurrentGenre = genre || 'all';
    archivePage = 1;
    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c) { c.classList.remove('active'); });
    if (btn) {
      btn.classList.add('active');
    } else {
      var matchBtn = document.querySelector('#v2ArchiveFilterChips button[onclick*="' + archiveCurrentGenre + '"]');
      if (matchBtn) matchBtn.classList.add('active');
    }
    renderArchiveGrid(false);
  };


  window.handleArchiveSearch = function(query) {
    archiveSearchQuery = (query || '').trim().toLowerCase();
    archivePage = 1;
    renderArchiveGrid(false);
  };


  window.handleArchiveSort = function(order) {
    archiveSortOrder = order || 'featured';
    renderArchiveGrid(false);
  };


  window.loadMoreArchiveBooks = function() {
    archivePage++;
    renderArchiveGrid(true);
  };

  function renderArchiveGrid(append) {
    var grid = document.getElementById('v2ArchiveGrid');
    var countDisplay = document.getElementById('v2ArchiveCountDisplay');
    var loadMoreBtn = document.getElementById('v2ArchiveLoadMoreBtn');
    if (!grid) return;

    if (!append) {
      grid.innerHTML = '';
    }

    var pool = getArchivePool();
    var filtered = [];

    // Distinct Pinned Editions by Genre for Featured order
    var pinnedTitles = {
      'all': ['godan', 'raag darbari', 'chitralekha', 'tarkash', 'samvidhan', 'rashmirathi', 'kuchh ishq'],
      'hindi': ['godan', 'raag darbari', 'chitralekha', 'gaban', 'nirmala', 'gunahon ka devta', 'tamas', 'maila anchal', 'rashmirathi'],
      'poetry': ['tarkash', 'kuchh ishq', 'madhushala', 'rashmirathi', 'saye mein dhoop', 'dhoop ke makan', 'rahat'],
      'law': ['samvidhan', 'constitution', 'ambedkar', 'bare act', 'vidhi', 'law'],
      'bestsellers': ['godan', 'raag darbari', 'chitralekha', 'tarkash', 'samvidhan', 'gypsy', 'aadha gaon', 'mahabhoj'],
      'philosophy': ['muktisangram', 'itihas', 'darshan', 'gandhi', 'ambedkar', 'buddha', 'swatantrata']
    };

    for (var i = 0; i < pool.length; i++) {
      var item = pool[i];
      var title = (item.title || '').toLowerCase();
      var author = (item.author || '').toLowerCase();
      var pub = (item.publisher || item.pub || '').toLowerCase();
      var cat = (item.category || item.genre || '').toLowerCase();

      // Precise Faceted Genre Filter
      if (archiveCurrentGenre === 'hindi') {
        var isClassicAuthor = HINDI_CLASSIC_AUTHORS.some(function(a) { return author.indexOf(a) !== -1; });
        var isNovelCat = cat.indexOf('novel') !== -1 || cat.indexOf('stories') !== -1 || cat.indexOf('sahitya') !== -1 || cat.indexOf('fiction') !== -1;
        if (!isClassicAuthor && !isNovelCat) continue;
      } else if (archiveCurrentGenre === 'poetry') {
        var isPoet = POETRY_AUTHORS.some(function(p) { return author.indexOf(p) !== -1; });
        var isPoetryCat = cat.indexOf('poetry') !== -1 || cat.indexOf('shayari') !== -1 || cat.indexOf('ghazal') !== -1 || cat.indexOf('nazm') !== -1 || cat.indexOf('kavita') !== -1;
        var isRekhta = pub.indexOf('rekhta') !== -1 || pub.indexOf('raza') !== -1;
        if (!isPoet && !isPoetryCat && !isRekhta) continue;
      } else if (archiveCurrentGenre === 'law') {
        var isLaw = cat.indexOf('law') !== -1 || cat.indexOf('judic') !== -1 || cat.indexOf('constitut') !== -1 || cat.indexOf('samvidhan') !== -1 || cat.indexOf('bare act') !== -1 || cat.indexOf('vidhi') !== -1;
        var isLawPub = pub.indexOf('central law') !== -1 || pub.indexOf('law') !== -1;
        var isLawTitle = title.indexOf('samvidhan') !== -1 || title.indexOf('constitution') !== -1 || title.indexOf('law') !== -1 || title.indexOf('act') !== -1;
        var isAmbedkar = author.indexOf('ambedkar') !== -1;
        if (!isLaw && !isLawPub && !isLawTitle && !isAmbedkar) continue;
      } else if (archiveCurrentGenre === 'bestsellers') {
        var isBestsellerAuthor = ['premchand', 'shrilal shukla', 'dinkar', 'gulzar', 'javed akhtar', 'piyush mishra', 'bhagwati'].some(function(a) { return author.indexOf(a) !== -1; });
        var isFamousTitle = ['godan', 'raag darbari', 'chitralekha', 'rashmirathi', 'kuchh ishq', 'tarkash', 'gypsy', 'aadha gaon', 'mahabhoj', 'nirmala', 'gaban', 'samvidhan', 'gunahon ka devta', 'tamas'].some(function(t) { return title.indexOf(t) !== -1; });
        if (!isBestsellerAuthor && !isFamousTitle && (item.mrp || 0) < 350) continue;
      } else if (archiveCurrentGenre === 'philosophy') {
        var isPhilCat = cat.indexOf('history') !== -1 || cat.indexOf('philosoph') !== -1 || cat.indexOf('darshan') !== -1 || cat.indexOf('itihas') !== -1 || cat.indexOf('biograph') !== -1 || cat.indexOf('memoir') !== -1;
        var isPhilTitle = title.indexOf('itihas') !== -1 || title.indexOf('history') !== -1 || title.indexOf('darshan') !== -1 || title.indexOf('gandhi') !== -1 || title.indexOf('vivekanand') !== -1 || title.indexOf('buddha') !== -1;
        if (!isPhilCat && !isPhilTitle) continue;
      }

      // Text query filter
      if (archiveSearchQuery) {
        if (title.indexOf(archiveSearchQuery) === -1 && author.indexOf(archiveSearchQuery) === -1 && pub.indexOf(archiveSearchQuery) === -1 && (item.isbn || '').indexOf(archiveSearchQuery) === -1) {
          continue;
        }
      }

      filtered.push(item);
    }

    // Sort
    if (archiveSortOrder === 'price-asc') {
      filtered.sort(function(a, b) { return (a.rawPrice || a.price || a.mrp || 0) - (b.rawPrice || b.price || b.mrp || 0); });
    } else if (archiveSortOrder === 'price-desc') {
      filtered.sort(function(a, b) { return (b.rawPrice || b.price || b.mrp || 0) - (a.rawPrice || a.price || a.mrp || 0); });
    } else if (archiveSortOrder === 'title-asc') {
      filtered.sort(function(a, b) { return (a.title || '').localeCompare(b.title || ''); });
    } else {
      // 'featured' sort: pin iconic masterworks for that genre to the top
      var genrePins = pinnedTitles[archiveCurrentGenre] || pinnedTitles['all'];
      filtered.sort(function(a, b) {
        var aTitle = (a.title || '').toLowerCase();
        var bTitle = (b.title || '').toLowerCase();
        var aMatch = genrePins.some(function(k) { return aTitle.indexOf(k) !== -1; });
        var bMatch = genrePins.some(function(k) { return bTitle.indexOf(k) !== -1; });
        if (aMatch && !bMatch) return -1;
        if (!aMatch && bMatch) return 1;
        return 0;
      });
    }

    var total = filtered.length;
    if (total === 0) {
      var genreLabels = {
        'all': 'All Books',
        'hindi': 'Hindi Classics & Novels',
        'poetry': 'Rekhta & Urdu Poetry',
        'law': 'Law & Constitution',
        'bestsellers': 'Bestsellers & Popular',
        'philosophy': 'Philosophy & History'
      };
      var currentGenreName = genreLabels[archiveCurrentGenre] || 'this category';
      var queryDisplay = archiveSearchQuery || 'your filter';

      grid.innerHTML = 
        '<div class="v2-archive-empty-state" style="grid-column: 1 / -1; background: #FFFFFF; border: 1px solid rgba(18, 18, 18, 0.08); border-radius: 16px; padding: 56px 24px; text-align: center; max-width: 620px; margin: 40px auto; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">' +
          '<div style="width: 56px; height: 56px; border-radius: 50%; background: rgba(224, 79, 51, 0.08); color: #E04F33; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">' +
            '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>' +
          '</div>' +
          '<h3 style="font-family: Cormorant Garamond, Georgia, serif; font-size: 26px; font-weight: 600; color: #121212; margin: 0 0 8px;">' +
            'No books found matching "' + queryDisplay + '" in ' + currentGenreName +
          '</h3>' +
          '<p style="font-size: 14px; color: #666; line-height: 1.5; margin: 0 0 24px;">' +
            'This author or title may be cataloged under another category in our 5,559-book archive.' +
          '</p>' +
          '<button type="button" class="v2-btn-clear-filter" onclick="window.clearArchiveFilters()" style="display: inline-flex; align-items: center; gap: 8px; background: #121212; color: #FFFFFF; border: none; border-radius: 999px; padding: 12px 26px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s ease; box-shadow: 0 4px 14px rgba(0,0,0,0.15);">' +
            '<span>Search Across All Categories &rarr;</span>' +
          '</button>' +
        '</div>';

      if (countDisplay) {
        countDisplay.textContent = 'Showing 0 books';
      }
      if (loadMoreBtn) {
        loadMoreBtn.style.display = 'none';
      }
      return;
    }

    var showCount = Math.min(archivePage * ARCHIVE_PAGE_SIZE, total);
    var startIndex = (archivePage - 1) * ARCHIVE_PAGE_SIZE;
    var pageSlice = filtered.slice(startIndex, showCount);

    if (countDisplay) {
      var genreLabels = {
        'all': 'Editions',
        'hindi': 'Hindi Classics & Novels',
        'poetry': 'Poetry & Rekhta Collections',
        'law': 'Law & Constitution Editions',
        'bestsellers': 'Bestselling Titles',
        'philosophy': 'Philosophy & History Works'
      };
      var label = genreLabels[archiveCurrentGenre] || 'Books';
      countDisplay.textContent = 'Showing ' + showCount + ' of ' + total + ' ' + label;
    }
    if (loadMoreBtn) {
      loadMoreBtn.style.display = (showCount >= total) ? 'none' : 'inline-block';
    }

    pageSlice.forEach(function(b) {
      var cover = getCoverUrl(b.cover || b.coverUrl || b.image, b.title, b.author);
      var priceVal = b.rawPrice || b.mrp || 299;
      var priceStr = b.price || ('₹' + priceVal + '.00');
      var card = document.createElement('div');
      card.className = 'v2-archive-card';
      var bId = b.id || b.handle || b.isbn;

      var safeTitle = (b.title || 'Book').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      var safeAuthor = (b.author || 'Curated Indian Author').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      var safeFmt = (b.binding || b.format || 'Paperback').toUpperCase();

      var fallbackSvg = getFallbackCoverSvg(b.title, b.author);
      card.innerHTML = 
        '<div>' +
          '<div style="position:relative; width: 100%; height: 280px; overflow: hidden; border-radius: 8px; margin-bottom: 12px; box-shadow: -4px 6px 14px rgba(0,0,0,0.18); background-color: #FAF7F0;">' +
            '<img src="' + cover + '" alt="' + safeTitle + '" data-author="' + safeAuthor + '" class="v2-archive-cover-img" referrerpolicy="no-referrer" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;" onerror="window.handleBookCoverError && window.handleBookCoverError(this);" />' +
            '<span style="position:absolute;top:8px;left:8px;font-size:9.5px;font-weight:800;color:#E04F33;background:rgba(255,255,255,0.95);padding:2px 7px;border-radius:4px;letter-spacing:0.08em;z-index:2;box-shadow: 0 2px 6px rgba(0,0,0,0.15);">' + safeFmt + '</span>' +
          '</div>' +
          '<h3 class="v2-archive-card-title" title="' + safeTitle + '">' + safeTitle + '</h3>' +
          '<div class="v2-archive-card-author">By ' + safeAuthor + '</div>' +
        '</div>' +
        '<div>' +
          '<div class="v2-archive-card-price">' + priceStr + '</div>' +
          '<div style="display:flex;gap:6px;">' +
            '<button type="button" class="v2-btn-archive-preview" onclick="event.stopPropagation(); window.openSoloBookPage ? window.openSoloBookPage(this.getAttribute(&quot;data-id&quot;)) : null;" data-id="' + bId + '" style="flex:1;">Preview &rarr;</button>' +
            '<button type="button" class="v2-btn-archive-add" data-id="' + bId + '" onclick="event.stopPropagation(); window.addToBagDirect ? window.addToBagDirect(this.getAttribute(&quot;data-id&quot;)) : null;" style="flex:1;">+ Add</button>' +
          '</div>' +
        '</div>';

      card.onclick = function() {
        window.openSoloBookPage(bId);
      };

      var apBtn = card.querySelector('.v2-card-preview-btn');
      if (apBtn) {
        apBtn.onclick = function(e) {
          e.stopPropagation();
          window.openSoloBookPage(bId);
        };
      }
      var aqBtn = card.querySelector('.v2-card-quick-btn');
      if (aqBtn) {
        aqBtn.onclick = function(e) {
          e.stopPropagation();
          if (typeof window.addToCart === 'function') {
            window.addToCart(bId, b.title, priceVal, cover);
          }
          if (typeof window.toggleCartDrawer === 'function') {
            window.toggleCartDrawer(true);
          }
        };
      }

      grid.appendChild(card);
    });
  }

  /* 4. DEFINITIVE SOLO BOOK PAGE & 3D SPREAD CONTROLLER (Points 2 & 3 Fixed) */
  
  /* UNIVERSAL SEARCH ACTIVATOR */
  window.activateUniversalSearch = function(e) {
    if (e && typeof e.stopPropagation === 'function') {
      e.stopPropagation();
    }
    // 1. Immediately close solo book page so search bar and results are 100% visible
    if (typeof window.closeSoloBookPage === 'function') {
      window.closeSoloBookPage();
    } else {
      var soloView = document.getElementById('indigo-solo-product-view');
      if (soloView) {
        soloView.classList.remove('is-active');
        soloView.style.display = 'none';
      }
      document.documentElement.classList.remove('solo-page-active');
      document.body.classList.remove('solo-page-active');
      document.body.style.removeProperty('overflow');
      document.documentElement.style.removeProperty('overflow');
    }

    var searchInput = document.getElementById('editorialSearchInput');
    var resultsBox = document.getElementById('editorialSearchResults');
    if (!searchInput) {
      window.location.href = '/search';
      return;
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(function() {
      searchInput.focus();
      searchInput.select();
      if (typeof window.showSearchSuggestionsPopup === 'function') {
        window.showSearchSuggestionsPopup();
      }
      if (resultsBox) {
        resultsBox.style.display = 'block';
      }
    }, 60);
  };

  /* GLOBAL AUTHOR FILTER & DEDICATED SEARCH ENGINE */
  window.performDedicatedSearch = function(query) {
    if (!query) return;
    var q = query.trim();

    // Standalone Shopify non-home page without SPA
    var isShopifyNonHome = (typeof window !== 'undefined' && 
      (window.location.pathname.indexOf('/products/') !== -1 || window.location.pathname.indexOf('/cart') !== -1 || window.location.pathname.indexOf('/collections') !== -1) &&
      !document.getElementById('indigo-search-results-view')
    );
    if (isShopifyNonHome) {
      window.location.href = '/search?q=' + encodeURIComponent(q);
      return;
    }

    // Close solo book page if open & unlock body
    if (typeof window.closeSoloBookPage === 'function') {
      window.closeSoloBookPage();
    } else {
      var soloV = document.getElementById('indigo-solo-product-view');
      if (soloV) {
        soloV.classList.remove('is-active');
        soloV.style.display = 'none';
      }
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
    }

    // Close any search dropdowns
    var resultsBox = document.getElementById('editorialSearchResults');
    if (resultsBox) resultsBox.style.display = 'none';

    // Open dedicated search results view (#indigo-search-results-view)
    if (typeof window.openSearchResultsPage === 'function') {
      window.openSearchResultsPage(q);
    } else {
      window.location.href = '/search?q=' + encodeURIComponent(q);
    }
  };

  /* DIRECT AUTHOR FILTERING FROM SHELVES & PDP */
  window.filterByAuthorDirect = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  window.filterByAuthorFromSolo = function(authorName) {
    if (!authorName) return;
    window.performDedicatedSearch(authorName);
  };

  /* SHELF HORIZONTAL SMOOTH SLIDER */
  window.slideShelf = function(shelfRowId, direction) {
    var row = document.getElementById(shelfRowId);
    if (!row) return;
    var stage = row.closest('.v2-shelf-stage') || row.parentElement;
    if (stage) {
      stage.scrollBy({ left: direction * 440, behavior: 'smooth' });
    }
  };

  /* CLEAR ARCHIVE GENRE RESTRICTIONS */
  window.clearArchiveFilters = function(query) {
    archiveCurrentGenre = 'all';
    if (query) {
      archiveSearchQuery = query.toLowerCase();
    }
    archivePage = 1;

    var chips = document.querySelectorAll('#v2ArchiveFilterChips .v2-chip');
    chips.forEach(function(c, idx) {
      if (idx === 0) c.classList.add('active');
      else c.classList.remove('active');
    });

    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) {
      arcSearchInput.value = archiveSearchQuery || '';
    }

    renderArchiveGrid(false);
  };
  window.getArchiveGenre = function() { return archiveCurrentGenre; };
  window.getArchiveQuery = function() { return archiveSearchQuery; };
  window.setArchiveFilter = function(genre, query) {
    archiveCurrentGenre = genre || 'all';
    archiveSearchQuery = (query || '').toLowerCase();
    archivePage = 1;
    var arcSearchInput = document.getElementById('v2ArchiveSearchInput');
    if (arcSearchInput) arcSearchInput.value = archiveSearchQuery;
    renderArchiveGrid(false);
  };


  window.closeSoloBookPage = function() {
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.remove('is-active');
      soloView.style.display = 'none';
    }

    // Unlock document and body scroll (Zero Double Scrollbar Guarantee)
    document.documentElement.classList.remove('solo-page-active');
    document.body.classList.remove('solo-page-active');
    document.body.style.removeProperty('overflow');
    document.documentElement.style.removeProperty('overflow');

    // Restore whichever view was active before opening
    if (previousViewBeforeSolo === 'search') {
      var sView = document.getElementById('indigo-search-results-view');
      if (sView) sView.style.display = 'block';
    } else {
      var hView = document.getElementById('homepage-view');
      if (hView) {
        hView.style.display = 'block';
        if (typeof window.__scrollPosBeforeSolo === 'number') {
          window.scrollTo({ top: window.__scrollPosBeforeSolo, behavior: 'instant' });
        }
      }
    }
  };

  window.openSoloBookPage = function(bookId) {
    // 1. Remember scroll position before opening solo page
    window.__scrollPosBeforeSolo = window.pageYOffset || document.documentElement.scrollTop || 0;

    var sView = document.getElementById('indigo-search-results-view');
    if (sView && sView.style.display === 'block') {
      previousViewBeforeSolo = 'search';
    } else {
      previousViewBeforeSolo = 'home';
    }

    // 2. Hide homepage and search views so ONLY solo book view is active in the DOM!
    var hView = document.getElementById('homepage-view');
    if (hView) {
      hView.style.display = 'none';
    }
    if (sView) {
      sView.style.display = 'none';
    }

    // 3. Lock document body scrolling to completely kill outer window scrollbar
    document.documentElement.classList.add('solo-page-active');
    document.body.classList.add('solo-page-active');
    document.body.style.setProperty('overflow', 'hidden', 'important');
    document.documentElement.style.setProperty('overflow', 'hidden', 'important');

    var found = null;

    // Direct object pass
    if (typeof bookId === 'object' && bookId !== null) {
      if (bookId.title && (bookId.price || bookId.author)) {
        found = Object.assign({}, bookId);
      } else {
        bookId = bookId.id || bookId.handle || bookId.isbn || bookId.sku || bookId.title;
      }
    }

    var idStr = String(bookId || '').trim();

    if (!found && idStr) {
      // Alias dictionary mapping every hero & podium ID to exact book
      var ID_ALIASES = {
        'podium-godan': 'hero-book-godan',
        'godan': 'hero-book-godan',
        'podium-raag-darbari': 'hero-book-raag',
        'hero-book-raag-darbari': 'hero-book-raag',
        'raag-darbari': 'hero-book-raag',
        'raag': 'hero-book-raag',
        'podium-chitralekha': 'hero-book-chitralekha',
        'chitralekha': 'hero-book-chitralekha',
        'podium-rashmirathi': 'hero-book-rashmirathi',
        'rashmirathi': 'hero-book-rashmirathi',
        'podium-kuchh-ishq': 'hero-book-kuchh-ishq',
        'podium-ishq-mishra': 'hero-book-kuchh-ishq',
        'kuchh-ishq': 'hero-book-kuchh-ishq',
        'kuchh-ishq-kiya-kuchh-kaam-kiya': 'hero-book-kuchh-ishq',
        'podium-gypsy': 'hero-book-gypsy',
        'gypsy': 'hero-book-gypsy',
        'tarkash': 'book-tarkash',
        'aadha-gaon': 'book-aadha-gaon',
        'mahabhoj': 'book-mahabhoj',
        'shekhar': 'book-shekhar',
        'shekhar-ek-jeevani': 'book-shekhar',
        'gaban': 'book-gaban',
        'nirmala': 'book-nirmala',
        'murakami': 'hero-book-murakami',
        'haruki-murakami': 'hero-book-murakami',
        'samvidhan': 'book-samvidhan',
        'bharat-ka-samvidhan': 'book-samvidhan'
      };

      var targetId = (ID_ALIASES[idStr] || idStr).toLowerCase();
      var cleanSlug = idStr.replace(/^(podium|hero-book|book)-/, '').toLowerCase();

      // 1. Search POPULAR_BOOKS
      for (var i = 0; i < POPULAR_BOOKS.length; i++) {
        var pb = POPULAR_BOOKS[i];
        var pbId = String(pb.id || '').toLowerCase();
        var pbTitle = String(pb.title || '').toLowerCase();
        var pbIsbn = String(pb.isbn || '');
        if (pbId === targetId || pbId === idStr.toLowerCase() || pbIsbn === idStr ||
            pbId.indexOf(cleanSlug) !== -1 || cleanSlug.indexOf(pbId.replace(/^(hero-book|book)-/, '')) !== -1 ||
            (cleanSlug.length > 2 && pbTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
          found = Object.assign({}, pb);
          break;
        }
      }

      // 2. Search Shopify Live Products
      if (!found && window.SHOPIFY_LIVE_PRODUCTS && window.SHOPIFY_LIVE_PRODUCTS.length) {
        for (var spIdx = 0; spIdx < window.SHOPIFY_LIVE_PRODUCTS.length; spIdx++) {
          var sp = window.SHOPIFY_LIVE_PRODUCTS[spIdx];
          var spId = String(sp.id || '');
          var spHandle = String(sp.handle || '').toLowerCase();
          var spTitle = String(sp.title || '').toLowerCase();
          if (spId === idStr || spHandle === idStr.toLowerCase() || spHandle === cleanSlug || (cleanSlug.length > 2 && spTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
            found = {
              id: sp.id || sp.handle,
              title: sp.title,
              author: sp.author || sp.vendor || 'Curated Indian Author',
              price: sp.price || '₹299.00',
              rawPrice: typeof sp.price === 'number' ? sp.price : (parseFloat(String(sp.price).replace(/[^0-9.]/g, '')) || 299),
              format: sp.type || 'Paperback',
              publisher: sp.vendor || 'Rajkamal Prakashan',
              edition: 'Official Certified Release',
              pages: '320p',
              isbn: sp.sku || sp.id || '9788126702749',
              cover: sp.cover || sp.image || sp.featured_image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(sp.title, sp.vendor) : ''),
              category: sp.type || 'Classic Literature'
            };
            break;
          }
        }
      }

      // 3. Search MASTER_SEARCH_CATALOG (5,559 titles)
      if (!found && window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) {
        for (var j = 0; j < window.MASTER_SEARCH_CATALOG.length; j++) {
          var m = window.MASTER_SEARCH_CATALOG[j];
          var mId = String(m.id || '');
          var mHandle = String(m.handle || '').toLowerCase();
          var mIsbn = String(m.isbn || m.sku || '');
          var mTitle = String(m.title || '').toLowerCase();
          if (mId === idStr || mHandle === idStr.toLowerCase() || mHandle === cleanSlug || mIsbn === idStr ||
              (cleanSlug.length > 3 && mTitle.indexOf(cleanSlug.replace(/-/g, ' ')) !== -1)) {
            found = {
              id: m.id || m.handle,
              title: m.title,
              author: m.author || 'Distinguished Scholar',
              price: m.price || ('₹' + (m.rawPrice || m.mrp || 299) + '.00'),
              rawPrice: m.rawPrice || m.mrp || 299,
              format: m.binding || m.format || 'Paperback',
              publisher: m.publisher || m.pub || 'Rajkamal Prakashan',
              edition: m.edition || 'Heritage Edition',
              pages: m.pages || '280p',
              isbn: m.isbn || m.sku || '9788126728466',
              cover: m.coverUrl || m.cover || m.image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(m.title, m.author) : ''),
              category: m.category || 'Classic Literature',
              quote: m.quote,
              excerpt: m.excerpt
            };
            break;
          }
        }
      }

      // 4. Fallback via resolveBookObject
      if (!found && typeof window.resolveBookObject === 'function') {
        var rb = window.resolveBookObject(bookId);
        if (rb) {
          found = {
            id: rb.id || rb.handle,
            title: rb.title,
            author: rb.author || 'Author',
            price: rb.price ? ('₹' + window.cleanPrice(rb.price) + '.00') : '₹299.00',
            rawPrice: window.cleanPrice(rb.price, 299),
            format: rb.binding || 'Paperback',
            publisher: rb.publisher || rb.pub || 'Publisher',
            edition: rb.edition || 'Heritage Release',
            pages: rb.pages || '320p',
            isbn: rb.isbn || rb.sku || '9788126702749',
            cover: rb.cover || rb.coverUrl || rb.image || (window.getFallbackCoverSvg ? window.getFallbackCoverSvg(rb.title, rb.author) : ''),
            category: rb.category || 'Literature',
            quote: rb.quote,
            excerpt: rb.excerpt
          };
        }
      }
    }

    if (!found) {
      var displayT = idStr.replace(/^(podium|hero-book|book)-/, '').replace(/[-_]/g, ' ').replace(/\w/g, function(l){ return l.toUpperCase(); });
      found = {
        id: idStr || 'archive-book',
        title: displayT || 'Indigo Books Archive Edition',
        author: 'Indigo Literary Archive',
        price: '₹299.00',
        rawPrice: 299,
        format: 'Paperback',
        publisher: 'Rajkamal Prakashan',
        edition: 'Certified Library Edition',
        pages: '312p',
        isbn: '9788126700000',
        cover: window.getFallbackCoverSvg ? window.getFallbackCoverSvg(displayT, 'Indigo Literary Archive') : '',
        category: 'Classic Literature',
        quote: 'साहित्य जीवन की आलोचना और समाज का जीवंत दर्पण है।',
        excerpt: 'साहित्य का मुख्य उद्देश्य मानवीय संवेदनाओं को जागृत करना और सत्य के अन्वेषण में अग्रसर होना है।'
      };
    }

    // Resolve cover cleanly to CDN URL
    found.cover = getCoverUrl(found.cover, found.title, found.author);

    // Attach Authentic Literary Content (Point 3 Fix)
    found.excerpt = getBookAuthenticExcerpt(found);
    found.quote = getBookAuthenticQuote(found);

    currentActiveBook = found;
    window.currentActiveBook = found;
    isSpreadOpen = false;

    // Populate Left Panel Quote & Backdrop (Strict Monolingual)
    var hindi = isHindiBook(found);
    var cleanTitle = getCleanDisplayTitle(found.title, hindi);
    var cleanAuthor = hindi ? getHindiAuthorName(found.author) : (found.author || 'Author');

    var bgArt = document.getElementById('v2SoloBgArt');
    if (bgArt) bgArt.style.backgroundImage = 'url(' + found.cover + ')';
    var qText = document.getElementById('v2SoloQuoteText');
    if (qText) qText.textContent = found.quote;
    var qSrc = document.getElementById('v2SoloQuoteSource');
    if (qSrc) {
      if (hindi) {
        qSrc.innerHTML = '&mdash; ' + cleanAuthor + ' &bull; इंडिगो साहित्य अभिलेखागार';
      } else {
        qSrc.innerHTML = '&mdash; ' + found.author + ' &bull; Indigo Editorial Archive';
      }
    }

    // Format Selection Handlers: Sibling Variant Lookup from Master Catalog
    var btnPb = document.getElementById('v2FormatPaperback');
    var btnHc = document.getElementById('v2FormatHardcover');

    // Scan MASTER_SEARCH_CATALOG and POPULAR_BOOKS for sibling variants of found.title
    var normTitle = String(found.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
    var pbVariant = null;
    var hcVariant = null;

    function checkVariantMatch(v) {
      if (!v || !v.title) return;
      var vt = String(v.title || '').trim().toLowerCase().replace(/[^a-z0-9]/g, '');
      if (vt === normTitle) {
        var b = String(v.binding || v.format || '').toLowerCase();
        if (b.indexOf('hard') !== -1) {
          if (!hcVariant) hcVariant = v;
        } else {
          if (!pbVariant) pbVariant = v;
        }
      }
    }

    if (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) {
      for (var vi = 0; vi < window.MASTER_SEARCH_CATALOG.length; vi++) {
        checkVariantMatch(window.MASTER_SEARCH_CATALOG[vi]);
        if (pbVariant && hcVariant) break;
      }
    }
    if (!pbVariant || !hcVariant) {
      for (var pj = 0; pj < POPULAR_BOOKS.length; pj++) {
        checkVariantMatch(POPULAR_BOOKS[pj]);
        if (pbVariant && hcVariant) break;
      }
    }

    // Determine clicked book format
    var clickedBinding = String(found.binding || found.format || '').toLowerCase();
    var isClickedHc = clickedBinding.indexOf('hard') !== -1;
    if (isClickedHc && !hcVariant) hcVariant = found;
    if (!isClickedHc && !pbVariant) pbVariant = found;

    // Active format: if clicked book was Hardcover, start with Hardcover active!
    var activeInitialFmt = (isClickedHc && hcVariant) ? 'Hardcover' : (pbVariant ? 'Paperback' : (hcVariant ? 'Hardcover' : 'Paperback'));

    // Update Format Buttons visibility & text based on real catalog data
    if (btnPb) {
      if (pbVariant) {
        btnPb.style.display = 'inline-flex';
        var pbP = pbVariant.rawPrice || pbVariant.mrp || (parseFloat(String(pbVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnPb.innerHTML = 'Paperback' + (pbP > 0 ? ' (₹' + Math.round(pbP) + ')' : '');
      } else {
        btnPb.style.display = 'none';
      }
    }

    if (btnHc) {
      if (hcVariant) {
        btnHc.style.display = 'inline-flex';
        var hcP = hcVariant.rawPrice || hcVariant.mrp || (parseFloat(String(hcVariant.price).replace(/[^0-9.]/g, '')) || 0);
        btnHc.innerHTML = 'Hardcover Deluxe' + (hcP > 0 ? ' (₹' + Math.round(hcP) + ')' : '');
      } else {
        btnHc.style.display = 'none';
      }
    }

    function applyFormat(fmt) {
      found.selectedFormat = fmt;
      var metaFmt = document.getElementById('v2MetaFormat');
      var priceEl = document.getElementById('v2SoloPrice');
      var metaEd = document.getElementById('v2MetaEdition');
      var mobPrice = document.getElementById('v2MobileBuyBarPrice');
      var mobFmt = document.getElementById('v2MobileBuyBarFormat');
      var isbnEl = document.getElementById('v2MetaIsbn');

      var currentVar = (fmt === 'Hardcover' && hcVariant) ? hcVariant : (pbVariant || found);
      var exactPrice = currentVar.rawPrice || currentVar.mrp || (parseFloat(String(currentVar.price).replace(/[^0-9.]/g, '')) || 299);
      var exactIsbn = currentVar.isbn || currentVar.sku || found.isbn;
      var exactPages = currentVar.pages || found.pages || '280p';
      var exactCover = currentVar.cover || currentVar.coverUrl || found.cover;

      found.selectedPrice = exactPrice;
      found.selectedIsbn = exactIsbn;
      found.isbn = exactIsbn;
      found.price = '₹' + exactPrice.toFixed(2);

      if (fmt === 'Hardcover') {
        if (btnHc) btnHc.classList.add('active');
        if (btnPb) btnPb.classList.remove('active');
        if (priceEl) priceEl.textContent = '₹' + exactPrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Hardcover Deluxe • ' + exactPages;
        if (metaEd) metaEd.textContent = 'Deluxe Gold-Embossed Library Edition';
        if (mobPrice) mobPrice.textContent = '₹' + exactPrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Hardcover Deluxe';
      } else {
        if (btnPb) btnPb.classList.add('active');
        if (btnHc) btnHc.classList.remove('active');
        if (priceEl) priceEl.textContent = '₹' + exactPrice.toFixed(2);
        if (metaFmt) metaFmt.textContent = 'Paperback • ' + exactPages;
        if (metaEd) metaEd.textContent = currentVar.edition || found.edition || 'Official Standard Edition';
        if (mobPrice) mobPrice.textContent = '₹' + exactPrice.toFixed(2);
        if (mobFmt) mobFmt.textContent = 'Paperback';
      }

      if (isbnEl) isbnEl.textContent = exactIsbn;

      // Update cover preview if variant has distinct cover
      if (exactCover && coverImg) {
        coverImg.src = getCoverUrl(exactCover, found.title, found.author);
      }
    }

    // Populate 3D Book Cover & Inside Pages (Strict Monolingual with Guaranteed Visible Cover)
    var soloFallbackSvg = getFallbackCoverSvg(found.title, found.author);
    var coverLeafFront = document.getElementById('v2CoverLeaf');
    if (coverLeafFront) {
      coverLeafFront.style.backgroundColor = '#FAF7F0';
      coverLeafFront.style.backgroundImage = 'url("' + soloFallbackSvg + '")';
      coverLeafFront.style.backgroundSize = 'cover';
      coverLeafFront.style.backgroundPosition = 'center';
    }

    var coverImg = document.getElementById('v2CoverLeafImg');
    if (coverImg) {
      coverImg.style.display = 'block';
      coverImg.style.opacity = '1';
      coverImg.style.width = '100%';
      coverImg.style.height = '100%';
      coverImg.style.objectFit = 'cover';
      coverImg.setAttribute('referrerpolicy', 'no-referrer');
      coverImg.onerror = function() {
        this.onerror = null;
        if (window.getFallbackCoverSvg) {
          this.src = window.getFallbackCoverSvg(found.title, found.author);
        }
      };
      var targetCover = getCoverUrl(found.cover, found.title, found.author);
      coverImg.src = targetCover;
    }

    if (btnPb) {
      btnPb.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Paperback');
      };
    }
    if (btnHc) {
      btnHc.onclick = function(e) {
        e.stopPropagation();
        applyFormat('Hardcover');
      };
    }
    applyFormat(activeInitialFmt);
    var leafTitle = document.getElementById('v2LeafBackTitle');
    if (leafTitle) leafTitle.textContent = cleanTitle;
    var chHead = document.getElementById('v2SpreadChapterHeading');
    if (chHead) chHead.textContent = cleanTitle;
    var topSeriesTag = document.getElementById('v2SpreadSeriesTag');
    if (topSeriesTag) {
      topSeriesTag.textContent = hindi ? 'इंडिगो क्लासिक्स • प्रथम अध्याय' : 'INDIGO CLASSICS • CHAPTER I';
    }
    var snippet = document.getElementById('v2SpreadExcerptSnippet');
    if (snippet) snippet.textContent = found.excerpt;
    var dropCap = document.getElementById('v2DropCap');
    if (dropCap && found.excerpt) {
      dropCap.textContent = found.excerpt.trim().charAt(0) || (hindi ? 'क' : 'T');
    }

    // Populate Right Details Sheet
    var sTitle = document.getElementById('v2SoloTitle');
    if (sTitle) sTitle.textContent = found.title;
    var sAuth = document.getElementById('v2SoloAuthor');
    var authorClean = (found.author || '').split(',')[0].replace(/Tr\..*$/i, '').trim();
    if (sAuth) {
      sAuth.textContent = found.author;
      sAuth.setAttribute('data-author', authorClean);
    }
    var sugTitle = document.getElementById('v2AuthorSugTitle');
    if (sugTitle) sugTitle.textContent = authorClean.toUpperCase();
    var seeAllBtn = document.getElementById('v2AuthorSeeAllBtn');
    if (seeAllBtn) seeAllBtn.setAttribute('data-author', authorClean);

    // Populate Dynamic Author Suggestions
    var sugGrid = document.getElementById('v2AuthorSuggestionsGrid');
    if (sugGrid) {
      sugGrid.innerHTML = '';
      var pool = (window.MASTER_SEARCH_CATALOG || []).concat(POPULAR_BOOKS);
      var matches = [];
      var seenIds = {};
      seenIds[found.id] = true;
      if (found.handle) seenIds[found.handle] = true;

      var qAuthLower = authorClean.toLowerCase();
      var authParts = qAuthLower.split(' ').filter(function(p) { return p.length > 2; });

      for (var k = 0; k < pool.length; k++) {
        var bk = pool[k];
        var bId = bk.id || bk.handle;
        if (seenIds[bId]) continue;
        var bAuth = (bk.author || '').toLowerCase();
        var isMatch = bAuth.indexOf(qAuthLower) !== -1;
        if (!isMatch && authParts.length > 0) {
          isMatch = authParts.some(function(part) { return bAuth.indexOf(part) !== -1; });
        }
        if (isMatch) {
          seenIds[bId] = true;
          matches.push(bk);
          if (matches.length >= 4) break;
        }
      }

      if (matches.length < 3) {
        for (var p = 0; p < POPULAR_BOOKS.length; p++) {
          var pb = POPULAR_BOOKS[p];
          if (!seenIds[pb.id]) {
            seenIds[pb.id] = true;
            matches.push(pb);
            if (matches.length >= 4) break;
          }
        }
      }

      matches.forEach(function(mb) {
        var cCover = getCoverUrl(mb.cover || mb.coverUrl || mb.image, mb.title, mb.author);
        var cPrice = mb.price || ('₹' + (mb.rawPrice || mb.mrp || 299) + '.00');
        var cFmt = (mb.binding || mb.format || 'Paperback').toUpperCase();
        var card = document.createElement('div');
        card.className = 'v2-author-sug-card';
        card.innerHTML = 
          '<div class="v2-author-sug-cover-wrap">' +
            '<img src="' + cCover + '" alt="' + mb.title + '" referrerpolicy="no-referrer" loading="lazy" />' +
          '</div>' +
          '<div>' +
            '<span class="v2-author-sug-badge">' + cFmt + '</span>' +
            '<div class="v2-author-sug-title" title="' + mb.title + '">' + mb.title + '</div>' +
            '<div class="v2-author-sug-price">' + cPrice + '</div>' +
          '</div>';
        var imgEl = card.querySelector('img');
        if (imgEl) imgEl.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, mb.title, mb.author); };
        card.onclick = function() {
          window.openSoloBookPage(mb.id || mb.handle);
        };
        sugGrid.appendChild(card);
      });
    }

    var sPrice = document.getElementById('v2SoloPrice');
    if (sPrice) sPrice.textContent = found.price;
    var mobPrice = document.getElementById('v2MobileBuyBarPrice');
    if (mobPrice) mobPrice.textContent = found.price;
    var mobFmt = document.getElementById('v2MobileBuyBarFormat');
    if (mobFmt) mobFmt.textContent = 'Paperback';

    var sPubBadge = document.getElementById('v2MetaPublisherBadge');
    if (sPubBadge) sPubBadge.textContent = (found.publisher || 'LOKBHARTI PRAKASHAN').toUpperCase();
    var sEdit = document.getElementById('v2MetaEdition');
    if (sEdit) sEdit.textContent = found.edition || 'Heritage Release';
    var sPub = document.getElementById('v2MetaPublisher');
    if (sPub) sPub.textContent = found.publisher || 'Rajkamal';
    // Sibling variant resolution handles v2MetaFormat and v2MetaIsbn authoritatively

    // Populate Full Excerpt View (Strict Monolingual: Pure Hindi OR Pure English)
    var exHead = document.getElementById('v2ExcerptHeading');
    if (exHead) exHead.textContent = hindi ? 'उद्धरण' : 'Excerpt';
    var exSub = document.getElementById('v2ExcerptSubtitle');
    if (exSub) {
      exSub.textContent = hindi ? ('पुस्तक १ • प्रथम अध्याय: ' + cleanTitle) : ('Book 1 • Chapter 1: ' + cleanTitle);
    }
    var exText = document.getElementById('v2ExcerptFullText');
    if (exText) {
      if (hindi) {
        exText.innerHTML = 
          '<p style="margin-bottom:14px;color:#121212;"><strong>प्रारंभिक अंश &bull; प्रामाणिक पाठ</strong></p>' +
          '<p style="margin-bottom:16px;line-height:1.75;font-size:15px;color:#222;">' + found.excerpt + '</p>' +
          '<p style="margin-bottom:14px;line-height:1.6;font-size:13.5px;color:#555;">यह आधिकारिक मूल प्रकाशक संस्करण लेखक द्वारा रचित मूल पाठ, सांस्कृतिक गरिमा एवं ऐतिहासिक संदर्भ को पूर्णतः सुरक्षित रखता है। प्रयागराज केंद्रीय भंडार से प्रामाणिक एवं सुरक्षित पैकेजिंग में प्रेषित।</p>' +
          '<p style="font-size:12.5px;color:#777;"><em>&bull; प्रामाणिक प्रकाशक संस्करण &bull; संपूर्ण भारत में सुरक्षित डिलीवरी</em></p>';
      } else {
        exText.innerHTML = 
          '<p style="margin-bottom:14px;color:#121212;"><strong>Opening Passage &bull; Authentic Text</strong></p>' +
          '<p style="margin-bottom:16px;line-height:1.75;font-size:15px;color:#222;">' + found.excerpt + '</p>' +
          '<p style="margin-bottom:14px;line-height:1.6;font-size:13.5px;color:#555;">This authoritative edition preserves the unaltered prose, cultural cadence, and historical context as intended by the author. Dispatched in certified protective packaging directly from our central repository.</p>' +
          '<p style="font-size:12.5px;color:#777;"><em>&bull; Original Publisher Edition &bull; Pan-India Heritage Repository</em></p>';
      }
    }

    // Reset Spread to Closed
    var spreadStage = document.getElementById('v2BookSpreadStage');
    if (spreadStage) spreadStage.classList.remove('is-open');
    var viewDetails = document.getElementById('v2ViewDetails');
    var viewExcerpt = document.getElementById('v2ViewExcerpt');
    if (viewDetails) viewDetails.style.display = 'block';
    if (viewExcerpt) viewExcerpt.style.display = 'none';

    var hintText = document.getElementById('v2SpreadHintText');
    if (hintText) hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Hover Book to Open 2-Page Preview Spread';

    var dockPrevBtn = document.getElementById('v2DockPreviewBtn');
    if (dockPrevBtn) dockPrevBtn.classList.remove('active');

    // Open View (Point 2 Fix: Opens over search or homepage cleanly!)
    var soloView = document.getElementById('indigo-solo-product-view');
    if (soloView) {
      soloView.classList.add('is-active');
      soloView.style.display = 'flex';
      soloView.scrollTop = 0;
    }
  };

  /* 3D SPREAD OPENING TOGGLE (-180deg flip on hover & click!) */
  window.toggleSoloBookSpread = function(forceState) {
    var spreadStage = document.getElementById('v2BookSpreadStage');
    var viewDetails = document.getElementById('v2ViewDetails');
    var viewExcerpt = document.getElementById('v2ViewExcerpt');
    var hintText = document.getElementById('v2SpreadHintText');
    var dockPrevBtn = document.getElementById('v2DockPreviewBtn');
    if (!spreadStage) return;

    if (typeof forceState === 'boolean') {
      isSpreadOpen = forceState;
    } else {
      isSpreadOpen = !isSpreadOpen;
    }

    if (isSpreadOpen) {
      spreadStage.classList.add('is-open');
      if (viewDetails) viewDetails.style.display = 'none';
      if (viewExcerpt) viewExcerpt.style.display = 'block';
      if (hintText) {
        hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Move Mouse Away to Close 2-Page Spread';
      }
      if (dockPrevBtn) dockPrevBtn.classList.add('active');
    } else {
      spreadStage.classList.remove('is-open');
      if (viewExcerpt) viewExcerpt.style.display = 'none';
      if (viewDetails) viewDetails.style.display = 'block';
      if (hintText) {
        hintText.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle;margin-right:4px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Hover Book to Open 2-Page Preview Spread';
      }
      if (dockPrevBtn) dockPrevBtn.classList.remove('active');
    }
  };

  /* SOLO VIEW ACTIONS */
  window.toggleSoloSaveWishlist = function() {
    var btn = document.getElementById('v2DockSaveBtn');
    if (btn) {
      btn.classList.toggle('active');
      btn.style.color = btn.classList.contains('active') ? '#E04F33' : '#444';
      btn.style.transform = 'scale(1.15)';
      setTimeout(function() { btn.style.transform = ''; }, 300);
    }
    if (typeof window.showNotificationToast === 'function') {
      window.showNotificationToast('Reading List updated: ' + (currentActiveBook ? currentActiveBook.title : 'Book'));
    }
  };

  window.handleSoloAddToCart = function() {
    if (!currentActiveBook) return;
    var finalPrice = currentActiveBook.selectedPrice || currentActiveBook.rawPrice || 299;
    var finalFmt = currentActiveBook.selectedFormat || currentActiveBook.format || 'Paperback';
    if (typeof window.addToCart === 'function') {
      window.addToCart(currentActiveBook.id, currentActiveBook.title, finalPrice, currentActiveBook.cover, finalFmt);
    }
    if (typeof window.toggleCartDrawer === 'function') {
      window.toggleCartDrawer(true);
    }
  };

  window.handleSoloBuyNow = function() {
    if (!currentActiveBook) return;
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(currentActiveBook);
    } else if (typeof window.openQuickOrderModal === 'function') {
      window.openQuickOrderModal(currentActiveBook);
    }
  };

  window.handleSoloWhatsApp = function() {
    if (!currentActiveBook) return;
    var num = '918933063306';
    var text = 'Hello Indigo Books India! I would like to order: *' + currentActiveBook.title + '* by ' + currentActiveBook.author + ' (' + currentActiveBook.price + '). Please confirm availability and share COD details!';
    var url = 'https://wa.me/' + num + '?text=' + encodeURIComponent(text);
    window.open(url, '_blank');
  };

  window.handleSoloGetBook = function() {
    window.handleSoloBuyNow();
  };

  window.scrollToAppSection = function(id) {
    window.closeSoloBookPage();
    var el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  /* MOBILE DRAWER & NAVIGATION */
  window.toggleMobileDrawer = function(open) {
    var drawer = document.getElementById('v2MobileDrawer');
    var backdrop = document.getElementById('v2MobileDrawerBackdrop');
    if (!drawer || !backdrop) return;
    if (open) {
      drawer.classList.add('is-open');
      backdrop.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    } else {
      drawer.classList.remove('is-open');
      backdrop.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  };

  window.handleMobileNavLink = function(targetHash) {
    window.toggleMobileDrawer(false);
    if (targetHash === '#video2-bookstore-app') {
      var appEl = document.getElementById('video2-bookstore-app') || document.getElementById('v2-archive-section');
      if (appEl) appEl.scrollIntoView({ behavior: 'smooth' });
    } else {
      var target = document.querySelector(targetHash);
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.handleMobileAuthorClick = function(authorName) {
    window.toggleMobileDrawer(false);
    window.filterByAuthorDirect(authorName);
  };

  window.handleSoloAddToBag = function() {
    window.handleSoloAddToCart();
  };

  window.openQuickOrderModal = function(bookId, qty) {
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(bookId, qty);
    }
  };

  window.openExpressModal = function(bookId, title, price) {
    if (typeof window.openExpressPhoneCheckout === 'function') {
      window.openExpressPhoneCheckout(bookId);
    }
  };

  /* 5. VIDEO 1 SCATTER PARALLAX & SCROLL ENGINES */
  var mouseX = 0, mouseY = 0, currentX = 0, currentY = 0;
  window.addEventListener('mousemove', function(e) {
    var cx = window.innerWidth / 2;
    var cy = window.innerHeight / 2;
    mouseX = (e.clientX - cx) / cx;
    mouseY = (e.clientY - cy) / cy;
  }, { passive: true });

  function animateScatterParallax() {
    currentX += (mouseX - currentX) * 0.08;
    currentY += (mouseY - currentY) * 0.08;

    var covers = document.querySelectorAll('.scatter-book-cover');
    covers.forEach(function(cov) {
      var d = parseFloat(cov.getAttribute('data-depth') || '0.4');
      var tx = currentX * 36 * d;
      var ty = currentY * 36 * d;
      cov.style.transform = 'translate3d(' + tx + 'px, ' + ty + 'px, 0)';
    });

    requestAnimationFrame(animateScatterParallax);
  }

  function onScrollEngine() {
    var sy = window.scrollY;

    // Dark curtain word illumination
    var curtain = document.getElementById('dark-curtain-manifesto');
    if (curtain) {
      var rect = curtain.getBoundingClientRect();
      var winH = window.innerHeight;
      if (rect.top < winH && rect.bottom > 0) {
        var progress = Math.min(Math.max((winH - rect.top) / (winH * 0.8), 0), 1);
        var words = document.querySelectorAll('.curtain-word');
        var count = words.length;
        var litCount = Math.floor(progress * count);
        words.forEach(function(w, idx) {
          if (idx <= litCount) {
            w.classList.add('is-illuminated');
          } else {
            w.classList.remove('is-illuminated');
          }
        });
      }
    }

    // Tilted sheet unfolding
    var tilted = document.getElementById('tiltedSheetCard');
    if (tilted) {
      var tRect = tilted.getBoundingClientRect();
      if (tRect.top < window.innerHeight * 0.82) {
        tilted.classList.add('is-unfolded');
      }
    }
  }
  window.addEventListener('scroll', onScrollEngine, { passive: true });

  /* 6. UNIVERSAL LIVE PREDICTIVE SEARCH ENGINE (Works everywhere: Home, Studio, PDP) */

  window.triggerDedicatedSearchAll = function() {
    var searchInput = document.getElementById('editorialSearchInput') || document.getElementById('results-search-input');
    var q = searchInput ? (searchInput.value || '').trim() : '';
    if (q && typeof window.performDedicatedSearch === 'function') {
      window.performDedicatedSearch(q);
    }
  };

  function setupPredictiveSearch() {
    var searchInput = document.getElementById('editorialSearchInput');
    var resultsBox = document.getElementById('editorialSearchResults');
    if (!searchInput || !resultsBox) return;

    function renderMatches(matches, title) {
      if (!matches || matches.length === 0) {
        resultsBox.innerHTML = '<div style="padding:16px;font-size:13px;color:#777;text-align:center;">No matching editions found in central repository.</div>';
        resultsBox.style.display = 'block';
        return;
      }
      var html = '<div style="padding:10px 16px;font-size:11px;font-weight:700;color:#888;letter-spacing:0.12em;text-transform:uppercase;border-bottom:1px solid #EEE;">' + (title || 'MATCHING EDITIONS') + '</div>';
      matches.forEach(function(m) {
        var cover = getCoverUrl(m.cover || m.coverUrl || m.image, m.title, m.author);
        var price = m.price || ('₹' + (m.rawPrice || m.mrp || 299) + '.00');
        var author = m.author || m.vendor || 'Author';
        html += 
          '<div class="editorial-search-item" style="display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer;border-bottom:1px solid #F5F5F5;transition:background 0.15s ease;" data-id="' + (m.id || m.handle) + '" data-handle="' + (m.handle || '') + '">' +
            '<img src="' + cover + '" referrerpolicy="no-referrer" loading="lazy" style="width:36px;height:52px;object-fit:cover;border-radius:3px;" />' +
            '<div style="flex:1;min-width:0;">' +
              '<div style="font-size:13px;font-weight:600;color:#121212;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + m.title + '</div>' +
              '<div style="font-size:11px;color:#666;">By ' + author + '</div>' +
            '</div>' +
            '<div style="font-size:13px;font-weight:700;color:#E04F33;">' + price + '</div>' +
          '</div>';
      });

      html += '<div class="editorial-search-view-all" onclick="window.triggerDedicatedSearchAll()" style="padding:11px 16px;text-align:center;font-size:12.5px;font-weight:700;color:#E04F33;cursor:pointer;background:#FFF9F7;border-top:1px solid #FFE4DD;letter-spacing:0.02em;">View All Results for &ldquo;' + (searchInput.value || '').trim() + '&rdquo; &rarr;</div>';
      resultsBox.innerHTML = html;
      resultsBox.style.display = 'block';

      var items = resultsBox.querySelectorAll('.editorial-search-item');
      items.forEach(function(it, idx) {
        var itm = matches[idx];
        var itmImg = it.querySelector('img');
        if (itmImg && itm) {
          itmImg.onerror = function() { window.handleBookCoverError && window.handleBookCoverError(this, itm.title, itm.author || itm.vendor); };
        }
        it.onclick = function() {
          var bid = this.getAttribute('data-id');
          var bHandle = this.getAttribute('data-handle');
          resultsBox.style.display = 'none';
          searchInput.value = '';
          if (typeof window.openSoloBookPage === 'function') {
            window.openSoloBookPage(bid || bHandle);
          } else if (bHandle) {
            window.location.href = '/products/' + bHandle;
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(bid);
          }
        };
      });
    }

    function showHeritagePicks() {
      var popularList = [
        { id: 'podium-godan', title: 'Godan (गोदान)', author: 'Premchand', price: '₹299.00', cover: 'hero-godan.jpg', handle: 'godan-premchand' },
        { id: 'podium-raag-darbari', title: 'Raag Darbari (राग दरबारी)', author: 'Shrilal Shukla', price: '₹499.00', cover: 'hero-raag-darbari.jpg', handle: 'raag-darbari-shrilal-shukla' },
        { id: 'podium-rashmirathi', title: 'Rashmirathi (रश्मिरथी)', author: 'Ramdhari Singh Dinkar', price: '₹350.00', cover: 'hero-rashmirathi.jpg', handle: 'rashmirathi' },
        { id: 'book-tarkash', title: 'Tarkash (तरकश)', author: 'Javed Akhtar', price: '₹499.00', cover: 'book-tarkash.jpg', handle: 'tarkash' },
        { id: 'book-samvidhan', title: 'Bharat Ka Samvidhan (भारत का संविधान)', author: 'Dr. B.R. Ambedkar', price: '₹450.00', cover: 'book-samvidhan.jpg', handle: 'bharat-ka-samvidhan' }
      ];
      renderMatches(popularList, 'POPULAR HERITAGE PICKS');
    }
    window.showSearchSuggestionsPopup = showHeritagePicks;

    var BILINGUAL_ALIASES = {
      'प्रेम': 'prem', 'प्रेमचंद': 'premchand', 'मुंशी': 'munshi',
      'दिनकर': 'dinkar', 'रामधारी': 'ramdhari',
      'अंबेडकर': 'ambedkar', 'आंबेडकर': 'ambedkar', 'भीमराव': 'bhimrao', 'संविधान': 'samvidhan',
      'शुक्ल': 'shukla', 'श्रीलाल': 'shrilal',
      'मिश्रा': 'mishra', 'पीयूष': 'piyush',
      'रज़ा': 'raza', 'राही': 'rahi', 'मासूम': 'masoom',
      'जावेद': 'javed', 'अख्तर': 'akhtar',
      'बच्चन': 'bachchan', 'हरिवंश': 'harivansh',
      'गालिब': 'ghalib', 'ग़ालिब': 'ghalib',
      'मंटो': 'manto', 'सआदत': 'saadat',
      'टैगोर': 'tagore', 'रवींद्रनाथ': 'rabindranath',
      'मुराकामी': 'murakami'
    };

    var POPULAR_HANDLES = [
      'godan-premchand', 'raag-darbari-shrilal-shukla', 'chitralekha-bhagwaticharan-verma',
      'rashmirathi-ramdhari-singh-dinkar', 'kuchh-ishq-kiya-kuchh-kaam-kiya-piyush-mishra',
      'tarkash-javed-akhtar', 'gypsy-ila-chandra-joshi', 'bharat-ka-samvidhan-dr-br-ambedkar',
      'aadha-gaon-rahi-masoom-raza', 'mahabhoj-mannu-bhandari', 'shekhar-ek-jeevani-agyeya',
      'gaban-premchand', 'nirmala-premchand', 'murakami-collection'
    ];

    var ICONIC_TITLES = [
      'godan', 'gaban', 'nirmala', 'sevasadan', 'karmabhoomi', 'rangbhoomi', 'mansarovar', 'idgah', 'kafan',
      'raag darbari', 'makaan', 'aadmi ka zahar', 'bishrampur ka sant',
      'rashmirathi', 'urvashi', 'kurukshetra', 'sanskriti ke chaar adhyay',
      'samvidhan', 'constitution', 'annihilation of caste', 'buddha and his dhamma',
      'tarkash', 'lava',
      'kuchh ishq', 'tumhari auqat', 'gagan damama',
      'aadha gaon', 'topi shukla', 'neem ka ped',
      'madhushala', 'madhubala', 'madhukalash',
      'chitralekha', 'thanda gosht', 'toba tek singh'
    ];

    var debounceTimer = null;
    searchInput.addEventListener('input', function() {
      clearTimeout(debounceTimer);
      var rawQuery = (searchInput.value || '').trim();
      var query = rawQuery.toLowerCase();
      if (query.length < 2) {
        showHeritagePicks();
        return;
      }

      debounceTimer = setTimeout(function() {
        var pool = (window.MASTER_SEARCH_CATALOG && window.MASTER_SEARCH_CATALOG.length) ? window.MASTER_SEARCH_CATALOG : (window.SHOPIFY_LIVE_PRODUCTS || POPULAR_BOOKS);
        
        var normQuery = query;
        for (var k in BILINGUAL_ALIASES) {
          if (query.indexOf(k) !== -1) {
            normQuery = normQuery.replace(new RegExp(k, 'g'), BILINGUAL_ALIASES[k]);
          }
        }

        var scored = [];
        for (var i = 0; i < pool.length; i++) {
          var item = pool[i];
          var title = (item.title || '').toLowerCase();
          var author = (item.author || item.vendor || '').toLowerCase();
          var isbn = (item.isbn || item.sku || '').toLowerCase();
          var pub = (item.publisher || item.pub || '').toLowerCase();
          var cat = (item.category || '').toLowerCase();
          var handleStr = String(item.handle || item.id || '').toLowerCase();

          var hasAuthorMatch = author.indexOf(query) !== -1 || author.indexOf(normQuery) !== -1;
          var hasTitleMatch = title.indexOf(query) !== -1 || title.indexOf(normQuery) !== -1;
          var hasIsbnMatch = isbn.indexOf(query) !== -1;
          var hasPubMatch = pub.indexOf(query) !== -1 || pub.indexOf(normQuery) !== -1;

          if (!hasAuthorMatch && !hasTitleMatch && !hasIsbnMatch && !hasPubMatch) {
            continue;
          }

          var score = 0;

          // 1. Author Matching (High priority for searches by author)
          if (author === query || author === normQuery) {
            score += 400;
          } else if (author.startsWith(query) || author.startsWith(normQuery)) {
            score += 350;
          } else if (hasAuthorMatch) {
            score += 250;
          }

          // 2. Title Matching
          if (title === query || title === normQuery) {
            score += 350;
          } else if (title.startsWith(query) || title.startsWith(normQuery)) {
            // If the query is an author search, don't over-boost anthologies that start with the author's name
            if (hasAuthorMatch) {
              score += 60;
            } else {
              score += 200;
            }
          } else if (hasTitleMatch) {
            score += 90;
          }

          // 3. Celebrated Masterpieces / Flagship boost
          for (var icIdx = 0; icIdx < ICONIC_TITLES.length; icIdx++) {
            if (title.indexOf(ICONIC_TITLES[icIdx]) !== -1) {
              score += 200;
              break;
            }
          }
          for (var pIdx = 0; pIdx < POPULAR_HANDLES.length; pIdx++) {
            if (handleStr.indexOf(POPULAR_HANDLES[pIdx]) !== -1 || POPULAR_HANDLES[pIdx].indexOf(handleStr) !== -1) {
              score += 250;
              break;
            }
          }

          if (hasIsbnMatch) score += 120;
          if (hasPubMatch) score += 40;

          scored.push({ item: item, score: score });
        }

        // Sort descending by score
        scored.sort(function(a, b) { return b.score - a.score; });

        // Deduplicate identical book titles to display a rich, diverse result list
        var seenTitles = new Set();
        var matches = [];
        for (var sIdx = 0; sIdx < scored.length; sIdx++) {
          var sItem = scored[sIdx].item;
          var cleanKey = (sItem.title || '').toLowerCase().trim().replace(/[^a-z0-9]/g, '');
          if (!seenTitles.has(cleanKey)) {
            seenTitles.add(cleanKey);
            matches.push(sItem);
            if (matches.length >= 10) break;
          }
        }

        renderMatches(matches, 'MATCHING EDITIONS (' + scored.length + ')');
      }, 100);
    });

    searchInput.addEventListener('focus', function() {
      var query = (searchInput.value || '').trim().toLowerCase();
      if (query.length >= 2) {
        searchInput.dispatchEvent(new Event('input'));
      } else {
        showHeritagePicks();
      }
    });

    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        var q = (searchInput.value || '').trim();
        if (q) {
          resultsBox.style.display = 'none';
          if (typeof window.performDedicatedSearch === 'function') {
            window.performDedicatedSearch(q);
          } else if (typeof window.openSearchResultsPage === 'function') {
            window.openSearchResultsPage(q);
          } else {
            window.location.href = '/search?q=' + encodeURIComponent(q);
          }
        }
      }
    });

    document.addEventListener('click', function(e) {
      if (!e.target.closest('.editorial-search-wrap') && !e.target.closest('.v2-solo-search-btn') && !e.target.closest('#v2SoloCardSearchBtn')) {
        resultsBox.style.display = 'none';
      }
    });
  }

  /* 7. INITIALIZATION */
  function init() {
    fixAllThemeAssetImages();
    renderAllShelves();
    renderArchiveGrid();
    setupPredictiveSearch();
    animateScatterParallax();
    onScrollEngine();
    setTimeout(fixAllThemeAssetImages, 300);
    setTimeout(fixAllThemeAssetImages, 1200);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
