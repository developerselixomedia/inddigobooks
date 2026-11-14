# -*- coding: utf-8 -*-
"""
Generate Complete Indigo Books Store (preview.html + Shopify theme)
"""

import os
import re
import json

# =========================================================================
# DATA DEFINITIONS
# =========================================================================

PODIUM_BOOKS_DATA = [
    {
        "id": "podium-kasaibada",
        "title": "कसाईबाड़ा (Kasaibada)",
        "author": "मनोज राजन त्रिपाठी (Manoj Rajan Tripathi)",
        "badge": "#1 IN CONTEMPORARY FICTION",
        "rating": "5.0 (1,120+ verified reviews)",
        "stock": "22 copies in Prayagraj",
        "quote": '"कसाईबाड़ा सत्ता, समाज और व्यवस्था के वीभत्स सच का वह आईना है जिसे देखकर मुंह फेर लेना नामुमकिन है।"',
        "firstPageExcerpt": '"कसाईबाड़ा सिर्फ एक जगह नहीं, एक व्यवस्था है। जहाँ हर कोई अपनी जान बचाने के लिए दूसरे की गर्दन काटने को तैयार खड़ा है। लेखक ने ग्रामीण राजनीति की नब्ज को जिस बेबाकी से पकड़ा है, वह समकालीन हिंदी साहित्य में एक मील का पत्थर है।"',
        "pages": "210 Pages · Deluxe Hardcover",
        "publisher": "वाणी प्रकाशन (Vani Prakashan)",
        "price": "₹299.00",
        "oldPrice": "₹395.00",
        "discount": "24% OFF",
        "coverUrl": "assets/hero-book-kasaibada.jpg"
    },
    {
        "id": "podium-ujli-raaten",
        "title": "उजली रातें (Ujli Raaten)",
        "author": "फ़्योदोर दोस्तोयेव्स्की (Fyodor Dostoevsky)",
        "badge": "#1 IN HINDI TRANSLATION",
        "rating": "4.9 (640+ verified reviews)",
        "stock": "14 copies in Prayagraj",
        "quote": '"श्वेत रातों की एक भावुक कहानी, जहां एकांत और प्रेम के बीच का अंतर केवल एक अजनबी की मुस्कान तय करती है..."',
        "firstPageExcerpt": '"वह एक अद्भुत रात थी, ऐसी रात जो केवल तब आती है जब हम युवा होते हैं। आकाश इतना उज्ज्वल और तारों भरा था कि उसे देखकर कोई भी सोचने पर मजबूर हो जाता कि क्या ऐसे आकाश के नीचे क्रोधी और दुष्ट लोग भी रह सकते हैं?"',
        "pages": "160 Pages · Hardcover Classic",
        "publisher": "Penguin Swadesh",
        "price": "₹179.00",
        "oldPrice": "₹199.00",
        "discount": "10% OFF",
        "coverUrl": "assets/hero-book-ujli-raaten.jpg"
    },
    {
        "id": "podium-wimpy-kid",
        "title": "Diary of a Wimpy Kid: Fight or Flight",
        "author": "Jeff Kinney",
        "badge": "#1 IN CHILDREN FICTION",
        "rating": "4.8 (890+ verified reviews)",
        "stock": "18 copies in Prayagraj",
        "quote": '"First of all, let me get something straight: this is a JOURNAL, not a diary. The hilarious airborne adventures of Greg Heffley continue."',
        "firstPageExcerpt": '"First of all, let me get something straight: this is a JOURNAL, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn\'t say \'diary\' on it."',
        "pages": "224 Pages · Illustrated Edition",
        "publisher": "Puffin Books",
        "price": "₹489.00",
        "oldPrice": "₹699.00",
        "discount": "30% OFF",
        "coverUrl": "assets/hero-book-wimpy-kid.jpg"
    },
    {
        "id": "podium-dozakhnama",
        "title": "दोज़ख़नामा (Dozakhnama)",
        "author": "रविशंकर बल (Rabisankar Bal)",
        "badge": "#1 IN HISTORICAL LITERARY FICTION",
        "rating": "4.9 (1,450+ verified reviews)",
        "stock": "16 copies in Prayagraj",
        "quote": '"गालिब और मंटो के बीच कब्रों से होता हुआ एक अमर संवाद — दो सदी, दो अज़ीम शायर, और एक दास्तान।"',
        "firstPageExcerpt": '"मुर्दों की कोई ज़बान नहीं होती, लेकिन जब मिर्ज़ा नौशा और सआदत हसन मंटो अपनी क़ब्रों से गुफ़्तगू करते हैं, तो दिल्ली और लाहौर की सरहदों के सारे दर्द कागज़ पर उतर आते हैं।"',
        "pages": "380 Pages · Rekhta Edition",
        "publisher": "Rekhta Publications",
        "price": "₹649.00",
        "oldPrice": "₹749.00",
        "discount": "13% OFF",
        "coverUrl": "assets/hero-book-dozakh.jpg"
    },
    {
        "id": "podium-ratan-tata",
        "title": "Ratan Tata: A Life",
        "author": "Dr. Thomas Mathew",
        "badge": "#1 IN BUSINESS & BIOGRAPHY",
        "rating": "4.9 (1,890+ verified reviews)",
        "stock": "25 copies in Prayagraj",
        "quote": '"The definitive authorized biography of India\'s most revered industrialist, visionary philanthropist, and symbol of ethical leadership."',
        "firstPageExcerpt": '"I do not believe in taking right decisions. I take decisions and then make them right. From the historic corridors of Bombay House to the global acquisition of Jaguar Land Rover, this is the unvarnished story of quiet resilience."',
        "pages": "560 Pages · Executive Hardcover",
        "publisher": "HarperCollins India",
        "price": "₹1,124.00",
        "oldPrice": "₹1,499.00",
        "discount": "25% OFF",
        "coverUrl": "assets/book-ratan-tata.jpg"
    }
]

POET_SHAYARI_DATA = {
    "all": {
        "name": "Mehfil-e-Rekhta Anthology",
        "pen": "अदबी विरासत (ग़ालिब • मंटो • फ़राज़ • एलिया)",
        "couplets": [
            {
                "urdu": "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے\nبہت نکلے مرے ارمان لیکن پھر بھی کم نکلے",
                "hindi": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
                "eng": "Thousands of desires, each worth dying for;\nMany of my longings were fulfilled, yet so few they were.",
                "attr": "— MIRZA GHALIB (मिर्ज़ा ग़ालिब)",
                "ghazal": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले\n\nडरे क्यों मेरा क़ातिल क्या रहेगा उसकी गर्दन पर\nवो ख़ूँ जो चश्म-ए-तर से उम्र भर यूँ दम-ब-दम निकले\n\nनिकलना ख़ुल्द से आदम का सुनते आए हैं लेकिन\nबहुत बे-आबरू होकर तिरे कूचे से हम निकले"
            },
            {
                "urdu": "شاید مجھے کسی سے محبت نہیں ہوئی\nلیکن یقیں سب کو دلاتا رہا ہوں میں",
                "hindi": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं",
                "eng": "Perhaps I never fell in love with anyone;\nYet I kept assuring everyone that I did.",
                "attr": "— JAUN ELIA (जौन एलिया)",
                "ghazal": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं\n\nजो गुज़री न जा सकी हमसे\nहमने वो ज़िंदगी गुज़ारी है\n\nक्या सितम है कि अब तिरी सूरत\nग़ौर करने पे याद आती है"
            }
        ]
    },
    "elia": {
        "name": "Jaun Elia (जौन एलिया)",
        "pen": "फना, फलसफा और बेबाक इश्क़",
        "couplets": [
            {
                "urdu": "بے دلی کیا یوں ہی دن گزر جائیں گے\nصرف زندہ رہے ہم تو مر جائیں گے",
                "hindi": "बे-दिली क्या यूँ ही दिन गुज़र जाएँगे\nसिर्फ़ ज़िंदा रहे हम तो मर जाएँगे",
                "eng": "Will days pass in such heartlessness?\nIf we only remain alive, we will die of grief.",
                "attr": "— JAUN ELIA (जौन एलिया)",
                "ghazal": "बे-दिली क्या यूँ ही दिन गुज़र जाएँगे\nसिर्फ़ ज़िंदा रहे हम तो मर जाएँगे\n\nसारी दुनिया के ग़म हमारे हैं\nऔर सितम ये कि हम तुम्हारे हैं\n\nक्या तमाशा है इस अदालत में\nसब वकील अपने ख़िलाफ़ खड़े हैं"
            },
            {
                "urdu": "شاید مجھے کسی سے محبت نہیں ہوئی\nلیکن یقیں سب کو دلاتا رہا ہوں میں",
                "hindi": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं",
                "eng": "Perhaps I never fell in love with anyone;\nYet I kept assuring everyone that I did.",
                "attr": "— JAUN ELIA (जौन एलिया)",
                "ghazal": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं"
            }
        ]
    },
    "faraz": {
        "name": "Ahmad Faraz (अहमद फ़राज़)",
        "pen": "रोमांस, बगावत और दर्दे-दिल",
        "couplets": [
            {
                "urdu": "رنجش ہی سہی دل ہی دکھانے کے لیے آ\nآ پھر سے مجھے چھوڑ کے جانے کے لیے آ",
                "hindi": "रंजिश ही सही दिल ही दुखाने के लिए आ\nआ फिर से मुझे छोड़ के जाने के लिए आ",
                "eng": "Even if in resentment, come just to hurt my heart;\nCome, even if only to leave me once again.",
                "attr": "— AHMAD FARAZ (अहमद फ़राज़)",
                "ghazal": "रंजिश ही सही दिल ही दुखाने के लिए आ\nआ फिर से मुझे छोड़ के जाने के लिए आ\n\nपहले से मरासिम न सही फिर भी कभी तो\nरस्म-ओ-रह-ए-दुनिया ही निभाने के लिए आ\n\nकिस किस को बताएँगे जुदाई का सबब हम\nतू मुझ से ख़फ़ा है तो ज़माने के लिए आ"
            }
        ]
    },
    "manto": {
        "name": "Saadat Hasan Manto (सआदत हसन मंटो)",
        "pen": "तल्ख़ हक़ीक़त, तरक़्क़ीपसंद अदब",
        "couplets": [
            {
                "urdu": "اگر آپ میرے افسانوں کو برداشت نہیں کر سکتے\nتو اس کا مطلب ہے کہ زمانہ ہی ناقابل برداشت ہے",
                "hindi": "अगर आप मेरे अफ़सानों को बर्दाश्त नहीं कर सकते,\nतो इसका मतलब है कि ज़माना ही नाक़ाबिल-ए-बर्दाश्त है।",
                "eng": "If you cannot bear my stories, it means\nthe times we live in are unbearable.",
                "attr": "— SAADAT HASAN MANTO (सआदत हसन मंटो)",
                "ghazal": "मंटो एक इंसान था और एक आईना था। जब ज़माना अपने चेहरे पर कालिख पोत लेता है, तो आईना तोड़ने से चेहरा साफ़ नहीं होता। 'ठंडा गोश्त' और 'खोल दो' समाज के उसी चेहरे का अक्स हैं जिसे देखने से दुनिया कतराती है।"
            }
        ]
    },
    "ghalib": {
        "name": "Mirza Ghalib (मिर्ज़ा ग़ालिब)",
        "pen": "शायरी का खुदा, दबिस्तान-ए-दिल्ली",
        "couplets": [
            {
                "urdu": "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے\nبہت نکلے مرے ارمان لیکن پھر بھی کم نکلے",
                "hindi": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले",
                "eng": "Thousands of desires, each worth dying for;\nMany of my longings were fulfilled, yet so few they were.",
                "attr": "— MIRZA GHALIB (मिर्ज़ा ग़ालिब)",
                "ghazal": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले\n\nमोहब्बत में नहीं है फ़र्क़ जीने और मरने का\nउसी को देख कर जीते हैं जिस काफ़िर पे दम निकले"
            }
        ]
    }
}

ALL_BOOKS_DATABASE = {
    "podium-kasaibada": {
        "title": "कसाईबाड़ा (Kasaibada)",
        "author": "मनोज राजन त्रिपाठी (Manoj Rajan Tripathi)",
        "price": 299, "mrp": 395, "discount": "24% OFF",
        "cover": "assets/hero-book-kasaibada.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Deluxe Hardcover", "pages": "210 Pages",
        "pub": "वाणी प्रकाशन (Vani Prakashan)", "dispatch": "Same-Day Dispatch from Prayagraj",
        "overview": "कसाईबाड़ा समकालीन हिंदी साहित्य का एक अत्यंत प्रभावशाली और निर्भीक सामाजिक उपन्यास है। लेखक मनोज राजन त्रिपाठी ने ग्रामीण एवं अर्ध-शहरी भारत में सत्ता, राजनीति और आम आदमी के संघर्ष को अनावृत किया है। यह कहानी व्यवस्था की क्रूरता और मानवीय संवेदना के अंतर्विरोधों का दस्तावेज़ है।",
        "highlights": [
            "ग्रामीण व्यवस्था और सत्ता के क्रूर यथार्थ का प्रामाणिक दस्तावेज़",
            "राष्ट्रीय पुरस्कार विजेता समकालीन हिंदी साहित्य कृति",
            "राजनीति, समाजशास्त्र और साहित्य प्रेमियों के लिए अनिवार्य पठन"
        ]
    },
    "podium-ujli-raaten": {
        "title": "उजली रातें (Ujli Raaten)",
        "author": "फ़्योदोर दोस्तोयेव्स्की (Fyodor Dostoevsky)",
        "price": 179, "mrp": 199, "discount": "10% OFF",
        "cover": "assets/hero-book-ujli-raaten.jpg",
        "lang": "Hindi / Russian Classic", "binding": "Hardcover Classic", "pages": "160 Pages",
        "pub": "Penguin Swadesh", "dispatch": "Express 24-Hr Dispatch",
        "overview": "सेंट पीटर्सबर्ग की श्वेत रातों की पृष्ठभूमि पर रचित दोस्तोयेव्स्की की यह सर्वकालिक कालजयी कृति एक भावुक स्वप्नदृष्टा और एक रहस्यमयी युवती नास्तेनका के बीच चार रातों के संवाद की अमर गाथा है। यह प्रेम, अकेलेपन और आत्म-बलिदान की संवेदनशील अभिव्यक्ति है।",
        "highlights": [
            "दोस्तोयेव्स्की की विश्वप्रसिद्ध लघु कृति का प्रामाणिक हिंदी अनुवाद",
            "मानवीय अकेलेपन और आत्मिक प्रेम की मार्मिक दास्तान",
            "पेंग्विन क्लासिक्स की विशेष हार्डकवर विरासत संस्करण"
        ]
    },
    "podium-wimpy-kid": {
        "title": "Diary of a Wimpy Kid: Fight or Flight",
        "author": "Jeff Kinney",
        "price": 489, "mrp": 699, "discount": "30% OFF",
        "cover": "assets/hero-book-wimpy-kid.jpg",
        "lang": "English", "binding": "Illustrated Hardcover", "pages": "224 Pages",
        "pub": "Puffin Books India", "dispatch": "In Stock at Prayagraj Hub",
        "overview": "Greg Heffley and his chaotic family are back in this hilarious airborne misadventure. When an unexpected vacation goes hilariously sideways at 30,000 feet, Greg must survive airport security, runaway luggage, and cramped economy seats.",
        "highlights": [
            "Worldwide #1 Bestselling Graphic Novel Franchise",
            "Laugh-out-loud illustrations on every single page",
            "Perfect read for young adults and reluctant readers alike"
        ]
    },
    "podium-dozakhnama": {
        "title": "दोज़ख़नामा (Dozakhnama)",
        "author": "रविशंकर बल (Rabisankar Bal)",
        "price": 649, "mrp": 749, "discount": "13% OFF",
        "cover": "assets/hero-book-dozakh.jpg",
        "lang": "Hindi / Urdu Rekhta", "binding": "Rekhta Hardcover Edition", "pages": "380 Pages",
        "pub": "Rekhta Publications", "dispatch": "Direct from Rekhta Archive",
        "overview": "दोज़ख़नामा मिर्ज़ा ग़ालिब और सआदत हसन मंटो के बीच कब्रों से होता हुआ एक जादुई संवाद है। दो शताब्दियों के दो महानतम रचनाकार दिल्ली और लाहौर की सरहदों, विभाजन के दर्द, और शायरी के फलसफे पर गुफ़्तगू करते हैं। यह उपन्यास भारतीय उपमहाद्वीप के सांस्कृतिक इतिहास का दर्पण है।",
        "highlights": [
            "ग़ालिब और मंटो के बीच का अमर काल्पनिक संवाद",
            "रेख्ता बुक्स का विशेष संग्राहक संस्करण",
            "उर्दू और हिंदी साहित्य के पाठकों के लिए एक ऐतिहासिक धरोहर"
        ]
    },
    "podium-ratan-tata": {
        "title": "Ratan Tata: A Life",
        "author": "Dr. Thomas Mathew",
        "price": 1124, "mrp": 1499, "discount": "25% OFF",
        "cover": "assets/book-ratan-tata.jpg",
        "lang": "English", "binding": "Executive Hardcover with Foil", "pages": "560 Pages",
        "pub": "HarperCollins India", "dispatch": "Collector Packaging Guaranteed",
        "overview": "The definitive, authorized biography of India's most revered industrial visionary and philanthropist. Featuring unprecedented access to personal letters, archival board minutes, and quiet moments behind iconic acquisitions like Jaguar Land Rover and Tetley.",
        "highlights": [
            "Official authorized biography with rare archival documents",
            "In-depth look into ethical leadership and nation-building",
            "Deluxe hardbound presentation with photographic plates"
        ]
    },
    "rekhta-kyon": {
        "title": "क्यों (Kyon) — जौन एलिया",
        "author": "जौन एलिया (Jaun Elia)",
        "price": 320, "mrp": 395, "discount": "19% OFF",
        "cover": "assets/book-kyon-jaun-elia.jpg",
        "lang": "Devanagari Hindi & Urdu", "binding": "Paperback Heritage Edition", "pages": "224 Pages",
        "pub": "रेख्ता पब्लिकेशन्स (Rekhta)", "dispatch": "Same-Day Dispatch",
        "overview": "जौन एलिया की बेबाक, विद्रोही और फलसफियाना शायरी का कालजयी संग्रह। 'क्यों' में उनके जीवन के अंतिम दौर की वो नज़्में और ग़ज़लें संकलित हैं जिन्होंने उर्दू अदब में निराशा और आत्मान्वेषण की नई परिभाषा गढ़ी।",
        "highlights": ["जौन एलिया का अंतिम एवं अत्यंत चर्चित काव्य संग्रह", "देवनागरी लिपि में सटीक अर्थ एवं संदर्भ सहित", "रेख्ता फ़ाउंडेशन का आधिकारिक संस्करण"]
    },
    "rekhta-ranjish": {
        "title": "रंजिश ही सही (Ranjish Hi Sahi)",
        "author": "अहमद फ़राज़ (Ahmad Faraz)",
        "price": 280, "mrp": 350, "discount": "20% OFF",
        "cover": "assets/book-ranjish-hi-sahi.jpg",
        "lang": "Hindi / Urdu Poetry", "binding": "Paperback Classic", "pages": "192 Pages",
        "pub": "रेख्ता पब्लिकेशन्स (Rekhta)", "dispatch": "Same-Day Dispatch",
        "overview": "अहमद फ़राज़ की रूमानी और बगावती ग़ज़लों का प्रतिनिधि संग्रह। 'रंजिश ही सही' प्रेम में टूटे हुए दिलों का वह गीत है जो दशकों से उपमहाद्वीप की रूह में गूँज रहा है।",
        "highlights": ["अहमद फ़राज़ की चुनिंदा शाहकार ग़ज़लें", "रोमांस और सामाजिक चेतना का अद्भुत संगम", "देवनागरी लिपि में सरल शब्दार्थ सहित"]
    },
    "rekhta-thanda-ghost": {
        "title": "ठंडा गोश्त (Thanda Gosht)",
        "author": "सआदत हसन मंटो (Saadat Hasan Manto)",
        "price": 199, "mrp": 250, "discount": "20% OFF",
        "cover": "assets/hero-book-thanda-ghost.jpg",
        "lang": "Hindi Fiction", "binding": "Paperback", "pages": "144 Pages",
        "pub": "वाणी प्रकाशन (Vani Prakashan)", "dispatch": "Express 24-Hr Dispatch",
        "overview": "विभाजन की विभीषिका और मानवीय विकृतियों पर मंटो की सबसे निर्भीक और विवादित कहानियों का संकलन। मंटो ने समाज के उस पाखंड को बेनकाब किया जिस पर अदालतें भी कांप उठी थीं।",
        "highlights": ["मंटो के सबसे चर्चित 12 अफ़साने", "विभाजन के खूनी सच का मनोवैज्ञानिक विश्लेषण", "हिंदी साहित्य का अनिवार्य मील का पत्थर"]
    },
    "rekhta-dhuaan": {
        "title": "धुआँ (Dhuaan)",
        "author": "सआदत हसन मंटो (Saadat Hasan Manto)",
        "price": 180, "mrp": 225, "discount": "20% OFF",
        "cover": "assets/hero-book-dhuaan.jpg",
        "lang": "Hindi Fiction", "binding": "Paperback", "pages": "160 Pages",
        "pub": "वाणी प्रकाशन (Vani Prakashan)", "dispatch": "Express 24-Hr Dispatch",
        "overview": "मंटो के मनोवैज्ञानिक अफ़सानों का अनूठा संग्रह जहाँ किशोरावस्था की जिज्ञासाओं, सामाजिक दमन और दबी हुई इच्छाओं को सूक्ष्मता से उभारा गया है।",
        "highlights": ["मंटो के मनोवैज्ञानिक अध्ययन वाले अफ़साने", "किशोरावस्था और समाज के अंतर्द्वंद्व", "सुलगती हुई यथार्थवादी भाषा"]
    },
    "bundle-arundhati": {
        "title": "Arundhati Roy Definitive Duo (2 Books)",
        "author": "Arundhati Roy",
        "price": 799, "mrp": 1198, "discount": "33% OFF",
        "cover": "assets/hero-book-arundhati.jpg",
        "lang": "English", "binding": "Box Set / 2 Volumes", "pages": "760 Pages Total",
        "pub": "Penguin India", "dispatch": "Gift Box Packaged",
        "overview": "Includes the Booker Prize-winning masterwork 'The God of Small Things' alongside Roy's epic second novel 'The Ministry of Utmost Happiness'. An unforgettable voyage through Kerala's backwaters and Delhi's secret graveyards.",
        "highlights": ["Includes complete Booker Prize winner", "Collector's dual slipcase presentation", "Essential modern Indian Anglophone literature"]
    },
    "bundle-acotar": {
        "title": "A Court of Thorns and Roses (5-Book Box Set)",
        "author": "Sarah J. Maas",
        "price": 1899, "mrp": 2999, "discount": "37% OFF",
        "cover": "assets/book-acotar.jpg",
        "lang": "English", "binding": "Collector Box Set (5 Books)", "pages": "3,400 Pages Total",
        "pub": "Bloomsbury Publishing", "dispatch": "Shrink-Wrapped Pristine Box",
        "overview": "The #1 New York Times bestselling fantasy phenomenon that captured readers across the globe. Follow Feyre's breathtaking journey from mortal huntress to high fae across Prythian's dangerous, seductive courts.",
        "highlights": ["Complete 5-volume fantasy epic", "Specially designed collector packaging", "Global bestselling BookTok sensation"]
    },
    "bundle-murakami": {
        "title": "Best of Haruki Murakami (3-Book Trio)",
        "author": "Haruki Murakami",
        "price": 1299, "mrp": 1899, "discount": "32% OFF",
        "cover": "assets/hero-book-murakami.jpg",
        "lang": "English", "binding": "3-Volume Paperback Set", "pages": "1,240 Pages Total",
        "pub": "Vintage Classics", "dispatch": "Pristine Collector Condition",
        "overview": "A curated three-novel gateway into magical realism: 'Norwegian Wood', 'Kafka on the Shore', and '1Q84'. Hypnotic journeys through lost memory, talking cats, and twin moons.",
        "highlights": ["3 defining works of Japanese magical realism", "Beautiful vintage cover typography", "Ideal introduction for literature enthusiasts"]
    },
    "hindi-cheelwali": {
        "title": "चीलवाली कोठी (Cheelwali Kothi)",
        "author": "सारा राय (Sara Rai)",
        "price": 299, "mrp": 395, "discount": "24% OFF",
        "cover": "assets/book-cheelwali-kothi.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Paperback Original", "pages": "224 Pages",
        "pub": "राजकमल प्रकाशन (Rajkamal)", "dispatch": "Same-Day Dispatch from Prayagraj",
        "overview": "प्रेमचंद की पौत्री सारा राय द्वारा रचित 'चीलवाली कोठी' एक पुराने खानदान, बिखरती हवेलियों और स्मृति के गलियारों की एक सम्मोहक दास्तान है। भाषा की नज़ाकत और यादों की परछाइयाँ इस उपन्यास को अनूठा बनाती हैं।",
        "highlights": ["समकालीन हिंदी साहित्य का अत्यंत प्रशंसित उपन्यास", "इलाहाबाद और बनारस की सांस्कृतिक स्मृतियों का संगम", "संवेदनशील और काव्यात्मक गद्य शैली"]
    },
    "hindi-nar-nareeshwar": {
        "title": "नर-नारीश्वर (Nar-Nareeshwar)",
        "author": "विष्णु प्रभाकर (Vishnu Prabhakar)",
        "price": 380, "mrp": 450, "discount": "16% OFF",
        "cover": "assets/book-nar-nareeshwar.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Hardcover Edition", "pages": "320 Pages",
        "pub": "राजकमल प्रकाशन (Rajkamal)", "dispatch": "Express 24-Hr Dispatch",
        "overview": "साहित्य अकादमी पुरस्कार से सम्मानित विष्णु प्रभाकर का यह उपन्यास पुरुष और स्त्री के आंतरिक सामंजस्य, अर्ध-नारीश्वर की दार्शनिक संकल्पना और आधुनिक रिश्तों के द्वंद्व का गहन विश्लेषण प्रस्तुत करता है।",
        "highlights": ["साहित्य अकादमी पुरस्कार विजेता उपन्यास", "स्त्री-पुरुष के अस्तित्ववादी संबंधों की पड़ताल", "हिंदी का क्लासिक उपन्यास"]
    },
    "hindi-patthar": {
        "title": "पत्थर और अलपत्थर (Patthar aur Alpatthar)",
        "author": "अशोक कुमार पाण्डेय (Ashok Kumar Pandey)",
        "price": 260, "mrp": 325, "discount": "20% OFF",
        "cover": "assets/book-patthar-alpatthar.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Paperback", "pages": "180 Pages",
        "pub": "वाणी प्रकाशन (Vani Prakashan)", "dispatch": "Express 24-Hr Dispatch",
        "overview": "कश्मीर के समकालीन यथार्थ, वहाँ के आम जनजीवन, पीड़ा और उम्मीदों को रेखांकित करती अत्यंत संवेदनशील कहानियाँ। लेखक ने राजनीतिक नारों से परे इंसानी ज़िंदगी के दर्द को स्वर दिया है।",
        "highlights": ["कश्मीर के सामाजिक यथार्थ पर प्रामाणिक आख्यान", "राजनीतिक शोर से परे इंसानी रिश्तों की दास्तान", "प्रशंसित इतिहासकार एवं लेखक की कृति"]
    },
    "hindi-aurat-farosh": {
        "title": "औरत फ़रोश (Aurat Farosh)",
        "author": "किशन सिंह (Kishan Singh)",
        "price": 220, "mrp": 275, "discount": "20% OFF",
        "cover": "assets/book-aurat-farosh.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Paperback", "pages": "160 Pages",
        "pub": "वाणी प्रकाशन (Vani Prakashan)", "dispatch": "Express 24-Hr Dispatch",
        "overview": "समाज के स्याह कोनों, मानव तस्करी और स्त्री शोषण के कटु यथार्थ को उजागर करता झकझोरने वाला उपन्यास। व्यवस्था के संवेदनहीन तंत्र पर एक कड़ा प्रहार।",
        "highlights": ["सामाजिक कुरीतियों पर तीखा प्रहार", "यथार्थवादी और साहसिक आख्यान", "सामाजिक कार्यकर्ताओं के लिए विचारणीय कृति"]
    },
    "hindi-lagbhag-single": {
        "title": "लगभग सिंगल (Lagbhag Single)",
        "author": "सत्य व्यास (Satya Vyas)",
        "price": 199, "mrp": 250, "discount": "20% OFF",
        "cover": "assets/book-lagbhag-single.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Paperback", "pages": "190 Pages",
        "pub": "हिंद युग्म (Hind Yugm)", "dispatch": "Same-Day Dispatch",
        "overview": "'बनारस टॉकीज़' और 'चौरासी' फेम सत्य व्यास का यह युवा उपन्यास आज की पीढ़ी के प्यार, करियर, हॉस्टल लाइफ और असमंजस को हास्य और चुटीले अंदाज में बयां करता है।",
        "highlights": ["युवा पाठकों का अत्यंत लोकप्रिय बेस्टसेलर", "सत्य व्यास का चिरपरिचित हास्य और देसी संवाद", "कॉलेज और युवा जीवन का सजीव चित्रण"]
    },
    "vault-bench-bar": {
        "title": "Bench & Bar: Constitutional Reflections",
        "author": "Justice V. R. Krishna Iyer",
        "price": 850, "mrp": 995, "discount": "15% OFF",
        "cover": "assets/book-bench-bar.jpg",
        "lang": "English Legal", "binding": "Lawyer Hardcover", "pages": "450 Pages",
        "pub": "Universal Law Publishing", "dispatch": "Same-Day High Court Dispatch",
        "overview": "A monumental constitutional treatise exploring judicial activism, public interest litigation, and the humanization of the Indian penal system by one of India's most celebrated jurists.",
        "highlights": ["Essential reading for High Court advocates & judges", "Deep insights into constitutional jurisprudence", "Authoritative citations on human rights law"]
    },
    "vault-medical-jur": {
        "title": "Medical Jurisprudence & Toxicology",
        "author": "Dr. K. S. Narayan Reddy",
        "price": 1150, "mrp": 1395, "discount": "18% OFF",
        "cover": "assets/book-medical-jurisprudence.jpg",
        "lang": "English", "binding": "Deluxe Legal Edition", "pages": "680 Pages",
        "pub": "LexisNexis India", "dispatch": "Express Dispatch",
        "overview": "The definitive medico-legal reference cited in landmark Indian courtroom trials. Covers forensic pathology, autopsy protocols, forensic DNA evidence, and post-mortem evaluation.",
        "highlights": ["Standard textbook referenced across Supreme Court rulings", "Comprehensive forensic case studies and colour plates", "Indispensable for criminal trial advocates"]
    },
    "vault-10-faisle": {
        "title": "10 फ़ैसले जिसने देश बदल दिया",
        "author": "ज़िया उस सलाम (Ziya Us Salam)",
        "price": 450, "mrp": 550, "discount": "18% OFF",
        "cover": "assets/book-10-faisle.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Paperback", "pages": "280 Pages",
        "pub": "प्रभात प्रकाशन (Prabhat)", "dispatch": "Same-Day Dispatch",
        "overview": "केशवानंद भारती, शाह बानो, तीन तलाक़ और निजता के अधिकार जैसे भारत के 10 सबसे ऐतिहासिक सुप्रीम कोर्ट फैसलों का सरल, रोचक और विश्लेषणात्मक कानूनी अध्ययन।",
        "highlights": ["सर्वोच्च न्यायालय के 10 ऐतिहासिक फैसलों का विश्लेषण", "UPSC एवं न्यायिक सेवा परीक्षा हेतु अत्यंत उपयोगी", "सरल हिंदी में संविधान और कानून की समझ"]
    },
    "vault-lawful-awful": {
        "title": "Lawful / Awful: Vignettes of Courtroom",
        "author": "Fali S. Nariman",
        "price": 399, "mrp": 495, "discount": "19% OFF",
        "cover": "assets/book-lawful-awful.jpg",
        "lang": "English", "binding": "Hardcover", "pages": "240 Pages",
        "pub": "Hay House India", "dispatch": "Express 24-Hr Dispatch",
        "overview": "Witty, candid, and profoundly insightful anecdotes from sixty years at the Indian Bar by the legendary senior advocate Fali S. Nariman.",
        "highlights": ["Unfiltered reflections from India's greatest constitutional lawyer", "Behind-the-scenes legal history and courtroom wit", "Inspirational reading for every law student"]
    },
    "vault-sahitya-itihas": {
        "title": "हिंदी साहित्य का इतिहास",
        "author": "आचार्य रामचंद्र शुक्ल (Ramchandra Shukla)",
        "price": 350, "mrp": 450, "discount": "22% OFF",
        "cover": "assets/book-hindi-sahitya-itihas.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Hardcover", "pages": "480 Pages",
        "pub": "नागरी प्रचारिणी सभा / राजकमल", "dispatch": "In Stock at Prayagraj",
        "overview": "हिंदी साहित्य के काल-विभाजन, कवियों के मूल्यांकन और आलोचनात्मक इतिहास का वह सर्वमान्य ग्रंथ जो एक सदी से विश्वविद्यालयीन परीक्षाओं और UPSC का आधार स्तंभ रहा है।",
        "highlights": ["आचार्य शुक्ल का अमर आलोचनात्मक इतिहास", "UPSC, NET/JRF एवं प्राध्यापक परीक्षा हेतु अनिवार्य", "हिंदी साहित्य की सबसे प्रामाणिक पुस्तक"]
    },
    "vault-hindi-vyakaran": {
        "title": "वृहद हिंदी व्याकरण",
        "author": "कामता प्रसाद गुरु (Kamta Prasad Guru)",
        "price": 420, "mrp": 500, "discount": "16% OFF",
        "cover": "assets/book-hindi-vyakaran.jpg",
        "lang": "Hindi (हिंदी)", "binding": "Hardcover Deluxe", "pages": "560 Pages",
        "pub": "नागरी प्रचारिणी सभा", "dispatch": "In Stock at Prayagraj",
        "overview": "हिंदी भाषा का सबसे विशद, प्रामाणिक और वैज्ञानिक व्याकरण ग्रंथ। पाणिनीय परंपरा और आधुनिक भाषाशास्त्र का ऐसा समन्वय अन्यत्र दुर्लभ है।",
        "highlights": ["हिंदी का 'पाणिनीय' प्रामाणिक व्याकरण", "संधि, समास, रस, छंद और अलंकार का विस्तृत विवेचन", "प्रतियोगी परीक्षाओं के लिए निर्विवाद संदर्भ"]
    },
    "vault-kabira-khada": {
        "title": "कबीरा खड़ा बाज़ार में",
        "author": "भीष्म साहनी (Bhisham Sahni)",
        "price": 240, "mrp": 295, "discount": "19% OFF",
        "cover": "assets/book-kabira-khada.jpg",
        "lang": "Hindi Play (नाटक)", "binding": "Paperback", "pages": "150 Pages",
        "pub": "राजकमल प्रकाशन", "dispatch": "Same-Day Dispatch",
        "overview": "कबीर के क्रांतिकारी व्यक्तित्व, धार्मिक आडंबरों पर उनके तीखे प्रहार और सत्य के लिए उनके एकाकी संघर्ष को जीवंत करता भीष्म साहनी का कालजयी नाटक।",
        "highlights": ["हिंदी रंगमंच का सबसे चर्चित ऐतिहासिक नाटक", "कबीर के निर्भीक सामाजिक दर्शन की प्रस्तुति", "विश्वविद्यालयों के पाठ्यक्रम में शामिल"]
    },
    "vault-hindi-bhasha": {
        "title": "हिंदी भाषा का विकास",
        "author": "डॉ. धीरेंद्र वर्मा (Dr. Dhirendra Verma)",
        "price": 290, "mrp": 350, "discount": "17% OFF",
        "cover": "assets/book-hindi-bhasha.jpg",
        "lang": "Hindi Linguistics", "binding": "Paperback", "pages": "230 Pages",
        "pub": "हिंदुस्तानी एकेडेमी, प्रयागराज", "dispatch": "Direct from Prayagraj",
        "overview": "प्रयागराज विश्वविद्यालय के मूर्धन्य भाषाविद् डॉ. धीरेंद्र वर्मा द्वारा रचित हिंदी भाषा, उसकी बोलियों और ऐतिहासिक विकास क्रम का अत्यंत प्रामाणिक शोध ग्रंथ।",
        "highlights": ["प्रयागराज की हिंदुस्तानी एकेडेमी की प्रतिष्ठित कृति", "अपभ्रंश, अवधी, ब्रज और खड़ी बोली का ऐतिहासिक अध्ययन", "भाषा विज्ञान के शोधार्थियों हेतु अमूल्य"]
    }
}

print(f"Loaded {len(ALL_BOOKS_DATABASE)} book metadata profiles.")

