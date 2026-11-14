const PODIUM_BOOKS = [{"id": "podium-godan", "rank": "#1", "tag": "ALL-TIME CLASSIC", "title": "Godan", "author": "Premchand", "rating": "4.9 (12,840)", "price": "₹299.00", "oldPrice": "₹403.00", "discount": "26% OFF", "badge": "NATIONAL BESTSELLER", "cover": "assets/hero-godan.jpg", "coverUrl": "assets/hero-godan.jpg", "stock": "In Stock • Ships in 24 Hrs", "firstPageExcerpt": "होरी जब घर से निकला, तो उसके दिल में एक ही तमन्ना थी कि किसी तरह एक गाय मिल जाए। उसका जीवन गाय की लालसा में ही बीत गया था।", "spineBg": "#1E3A8A", "genre": "Fiction : Novel", "isbn": "9789389742152", "pages": "312p", "publisher": "Lokbharti Prakashan", "edition": "4th Edition (1936)", "quote": "The greatest epic of rural India, depicting peasant resilience and societal injustice.", "blurb": "Premchand's crowning masterpiece exploring Indian agrarian life, caste, debt, and the unyielding human spirit."}, {"id": "podium-raag-darbari", "rank": "#2", "tag": "GREATEST SATIRE", "title": "Raag Darbari", "author": "Shrilal Shukla", "rating": "4.9 (9,650)", "price": "₹499.00", "oldPrice": "₹648.00", "discount": "23% OFF", "badge": "SAHITYA AKADEMI", "cover": "assets/hero-raag-darbari.jpg", "coverUrl": "assets/hero-raag-darbari.jpg", "stock": "In Stock • Ships in 24 Hrs", "firstPageExcerpt": "यह कहानी शिवपालगंज की है जहाँ सड़क के किनारे का कॉलेज हर साल नए क्रांतिकारी और बेरोजगार पैदा करता है। रंगनाथ ने जब गाँव में कदम रखा...", "spineBg": "#B45309", "genre": "Fiction : Novel", "isbn": "9788126713967", "pages": "423p", "publisher": "Rajkamal Prakashan", "edition": "55th Edition (1983)", "quote": "A razor-sharp satire of post-independence Indian politics and administrative decay.", "blurb": "Set in Shivpalganj, Shrilal Shukla's biting magnum opus on power, bureaucracy, and rural reality."}, {"id": "podium-chitralekha", "rank": "#3", "tag": "PHILOSOPHICAL NOVEL", "title": "Chitralekha", "author": "Bhagwaticharan Verma", "rating": "4.8 (8,420)", "price": "₹299.00", "oldPrice": "₹403.00", "discount": "25% OFF", "badge": "LITERARY CLASSIC", "cover": "assets/hero-chitralekha.jpg", "coverUrl": "assets/hero-chitralekha.jpg", "stock": "In Stock • Ships in 24 Hrs", "firstPageExcerpt": "संसार में पाप क्या है और पुण्य क्या है? क्या संयम ही जीवन है या वासना का उपभोग? पाटलिपुत्र के महान सामंत बीजगुप्त और नर्तकी चित्रलेखा...", "spineBg": "#0F172A", "genre": "Fiction : Novel", "isbn": "9788126715855", "pages": "200p", "publisher": "Rajkamal Prakashan", "edition": "32nd Edition (1993)", "quote": "What is virtue and what is sin? A timeless quest across Maurya-era Pataliputra.", "blurb": "Bhagwaticharan Verma's masterpiece interrogating asceticism, desire, and moral righteousness."}, {"id": "podium-rashmirathi", "rank": "#4", "tag": "EPIC POETRY", "title": "Rashmirathi : Dinkar Granthmala", "author": "Ramdhari Singh 'Dinkar'", "rating": "5.0 (15,200)", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "22% OFF", "badge": "NATIONAL FAVORITE", "cover": "assets/hero-rashmirathi.jpg", "coverUrl": "assets/hero-rashmirathi.jpg", "stock": "In Stock • Ships in 24 Hrs", "firstPageExcerpt": "वर्षों तक वन में घूम-घूम, बाधा-विघ्नों को चूम-चूम, सह धूप-घाम, पानी-पत्थर, पांडव आये कुछ और निखर। सौभाग्य न सब दिन सोता है, देखें आगे क्या होता है...", "spineBg": "#831843", "genre": "Poetry", "isbn": "9788180313639", "pages": "192p", "publisher": "Lokbharti Prakashan", "edition": "31st Edition (2009)", "quote": "जब नाश मनुज पर छाता है, पहले विवेक मर जाता है। Karna's immortal heroic saga.", "blurb": "Ramdhari Singh Dinkar's fiery verses celebrating Karna's valour, righteousness, and tragic grandeur."}, {"id": "podium-ishq-mishra", "rank": "#5", "tag": "MODERN POETRY", "title": "Kuchh Ishq Kiya Kuchh Kaam Kiya", "author": "Piyush Mishra", "rating": "4.9 (6,110)", "price": "₹250.00", "oldPrice": "₹337.00", "discount": "25% OFF", "badge": "YOUTH ANTHEM", "cover": "assets/hero-kuchh-ishq.jpg", "coverUrl": "assets/hero-kuchh-ishq.jpg", "stock": "In Stock • Ships in 24 Hrs", "firstPageExcerpt": "कुछ इश्क़ किया कुछ काम किया, वो काम बहुत नुक़सान किया, दोनों ही किए अधूरे से, ना इश्क़ हुआ ना काम हुआ। एक उम्र कटी अफ़सोस में...", "spineBg": "#14532D", "genre": "Poetry/Shayari", "isbn": "9788126728435", "pages": "147p", "publisher": "Rajkamal Prakashan", "edition": "15th Edition (2016)", "quote": "Raw, rebellious, heartfelt poetry and theatre verses from Piyush Mishra's soul.", "blurb": "Piyush Mishra's beloved anthology of verses capturing love, longing, bohemian rebellion, and Delhi winters."}];
    const POET_SHAYARI_DATA = {"all": {"name": "Mehfil-e-Rekhta Anthology", "pen": "अदबी विरासत (ग़ालिब • मंटो • फ़राज़ • एलिया)", "couplets": [{"urdu": "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے\nبہت نکلے مرے ارمان لیکن پھر بھی کم نکلے", "hindi": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले", "eng": "Thousands of desires, each worth dying for;\nMany of my longings were fulfilled, yet so few they were.", "attr": "— MIRZA GHALIB (मिर्ज़ा ग़ालिब)", "ghazal": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले\n\nडरे क्यों मेरा क़ातिल क्या रहेगा उसकी गर्दन पर\nवो ख़ूँ जो चश्म-ए-तर से उम्र भर यूँ दम-ब-दम निकले\n\nनिकलना ख़ुल्द से आदम का सुनते आए हैं लेकिन\nबहुत बे-आबरू होकर तिरे कूचे से हम निकले"}, {"urdu": "شاید مجھے کسی سے محبت نہیں ہوئی\nلیکن یقیں سب کو دلاتا رہا ہوں میں", "hindi": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं", "eng": "Perhaps I never fell in love with anyone;\nYet I kept assuring everyone that I did.", "attr": "— JAUN ELIA (जौन एलिया)", "ghazal": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं\n\nजो गुज़री न जा सकी हमसे\nहमने वो ज़िंदगी गुज़ारी है\n\nक्या सितम है कि अब तिरी सूरत\nग़ौर करने पे याद आती है"}]}, "elia": {"name": "Jaun Elia (जौन एलिया)", "pen": "फना, फलसफा और बेबाक इश्क़", "couplets": [{"urdu": "بے دلی کیا یوں ہی دن گزر جائیں گے\nصرف زندہ رہے ہم تو مر جائیں گے", "hindi": "बे-दिली क्या यूँ ही दिन गुज़र जाएँगे\nसिर्फ़ ज़िंदा रहे हम तो मर जाएँगे", "eng": "Will days pass in such heartlessness?\nIf we only remain alive, we will die of grief.", "attr": "— JAUN ELIA (जौन एलिया)", "ghazal": "बे-दिली क्या यूँ ही दिन गुज़र जाएँगे\nसिर्फ़ ज़िंदा रहे हम तो मर जाएँगे\n\nसारी दुनिया के ग़म हमारे हैं\nऔर सितम ये कि हम तुम्हारे हैं\n\nक्या तमाशा है इस अदालत में\nसब वकील अपने ख़िलाफ़ खड़े हैं"}, {"urdu": "شاید مجھے کسی से मोहब्बत नहीं हुई\nلیکن یقیں سب को دلاتا رہا ہوں میں", "hindi": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं", "eng": "Perhaps I never fell in love with anyone;\nYet I kept assuring everyone that I did.", "attr": "— JAUN ELIA (जौन एलिया)", "ghazal": "शायद मुझे किसी से मोहब्बत नहीं हुई\nलेकिन यक़ीं सब को दिलाता रहा हूँ मैं\n\nजो गुज़री न जा सकी हमसे\nहमने वो ज़िंदगी गुज़ारी है"}]}, "faraz": {"name": "Ahmad Faraz (अहमद फ़राज़)", "pen": "रोमांस, दर्द और मुक़द्दस अल्फ़ाज़", "couplets": [{"urdu": "रंजिश ही सही दिल ही दुखाने के लिए आ\nआ फिर से मुझे छोड़ के जाने के लिए आ", "hindi": "रंजिश ही सही दिल ही दुखाने के लिए आ\nआ फिर से मुझे छोड़ के जाने के लिए आ", "eng": "Even if with estrangement, come just to break my heart;\nCome, even if only to leave me all over again.", "attr": "— AHMAD FARAZ (अहमद फ़राज़)", "ghazal": "रंजिश ही सही दिल ही दुखाने के लिए आ\nआ फिर से मुझे छोड़ के जाने के लिए आ\n\nकुछ तो मिरे पिंदार-ए-मोहब्बत का भरम रख\nतू भी तो कभी मुझ को मनाने के लिए आ\n\nपहले से मरासिम न सही फिर भी कभी तो\nरस्म ओ रह-ए-दुनिया ही निभाने के लिए आ"}]}, "ghalib": {"name": "Mirza Ghalib (मिर्ज़ा ग़ालिब)", "pen": "सदाबहार दार्शनिक और शायरी के शहंशाह", "couplets": [{"urdu": "ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے\nبہت نکلے مرے ارمان لیکن پھر بھی کم نکلے", "hindi": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले", "eng": "Thousands of desires, each worth dying for;\nMany of my longings were fulfilled, yet so few they were.", "attr": "— MIRZA GHALIB (मिर्ज़ा ग़ालिब)", "ghazal": "हज़ारों ख़्वाहिशें ऐसी कि हर ख़्वाहिश पे दम निकले\nबहुत निकले मिरे अरमान लेकिन फिर भी कम निकले\n\nमोहब्बत में नहीं है फ़र्क़ जीने और मरने का\nउसी को देख कर जीते हैं जिस काफ़िर पे दम निकले"}]}, "manto": {"name": "Saadat Hasan Manto (सआदत हसन मंटो)", "pen": "अफ़सानानिगार: बेबाक सच और मानवीय त्रासदी", "couplets": [{"urdu": "زمانے کے जिस दौर से हम गुज़र रहे हैं...\nअगर आप मेरे अफ़सानों को बर्दाश्त नहीं कर सकते तो इसका मतलब यह है कि जमाना नाक़ाबिल-ए-बर्दाश्त है।", "hindi": "अगर आप मेरे अफ़सानों को बर्दाश्त नहीं कर सकते तो इसका मतलब यह है कि ज़माना नाक़ाबिल-ए-बर्दाश्त है।", "eng": "If you cannot tolerate my stories, it means this era is intolerable.", "attr": "— SAADAT HASAN MANTO (सआदत हसन मंटो)", "ghazal": "मैं उस सोसायटी की चोली क्या उतारूँगा जो पहले से ही नंगी है... मुझे उसे कपड़े पहनाने की कोशिश भी नहीं करनी चाहिए, क्योंकि यह मेरा काम नहीं, दर्ज़ियों का काम है।"}]}};
    const VAULT_BOOKS = {"law": [{"id": "vault-law-highcourt", "badge": "HIGH COURT PRACTICE", "title": "Bharatiya Bhasha Mein High Court Ki Vakalat", "author": "Anoop Baranwal Deshbandhu", "price": "₹350.00", "oldPrice": "₹472.00", "coverUrl": "assets/book-highcourt.jpg"}, {"id": "vault-law-constitution", "badge": "CONSTITUTION MANUAL", "title": "Bharat Ka Samvidhan : Sankshipt Parichay", "author": "Subhash Kashyap", "price": "₹195.00", "oldPrice": "₹263.00", "coverUrl": "assets/book-samvidhan.jpg"}, {"id": "vault-law-ucc", "badge": "LEGAL TREATISE", "title": "Samaan Nagrik Sanhita : Chunautiya Aur Samadhan", "author": "Anoop Baranwal", "price": "₹399.00", "oldPrice": "₹538.00", "coverUrl": "assets/book-highcourt.jpg"}, {"id": "vault-law-judiciary", "badge": "JUDICIAL CRITIQUE", "title": "Nyayapalika Kasauti Par", "author": "Kamlesh Jain, Edi. ranjeet verma ", "price": "₹199.00", "oldPrice": "₹268.00", "coverUrl": "assets/book-samvidhan.jpg"}], "sahitya": [{"id": "vault-sah-gyan", "badge": "PHILOSOPHY & LITERARY CRITICISM", "title": "Gyan Aur Karm", "author": "Vishnukant Shastri", "price": "₹299.00", "oldPrice": "₹403.00", "coverUrl": "assets/book-gyan-aur-karm.jpg"}, {"id": "vault-sah-shilp", "badge": "NARRATIVE CRAFT", "title": "Hindi Kahaniyon Ki Shilp-Vidhi Ka Vikas", "author": "Laxmi Narayan Lal", "price": "₹195.00", "oldPrice": "₹263.00", "coverUrl": "assets/book-gyan-aur-karm.jpg"}, {"id": "vault-sah-itihas", "badge": "LITERARY HISTORY", "title": "Aadhunik Hindi Sahitya Ka Itihas", "author": "Bachchan Singh", "price": "₹950.00", "oldPrice": "₹1282.00", "coverUrl": "assets/book-gyan-aur-karm.jpg"}, {"id": "vault-sah-anusandhan", "badge": "RESEARCH METHODOLOGY", "title": "Anusandhan Pravidhi : Siddhant Aur Prakariya", "author": "S.N.Ganeshan", "price": "₹400.00", "oldPrice": "₹540.00", "coverUrl": "assets/book-gyan-aur-karm.jpg"}], "civil": [{"id": "vault-civ-hadappa", "badge": "ANCIENT VEDIC HISTORY", "title": "Hadappa Sabhyata Aur Vaidik Sahitya", "author": "Bhagwan Singh", "price": "₹599.00", "oldPrice": "₹808.00", "coverUrl": "assets/book-hadappa.jpg"}, {"id": "vault-civ-badalata", "badge": "SOCIAL ESSAYS & CIVIC REFORM", "title": "Badalata Hua Desh", "author": "Manoj Kumar Pandey", "price": "₹150.00", "oldPrice": "₹202.00", "coverUrl": "assets/book-hadappa.jpg"}, {"id": "vault-civ-nyay", "badge": "POLITICAL THOUGHT", "title": "Nyay Ka Sangharsh", "author": "Yashpal", "price": "₹395.00", "oldPrice": "₹533.00", "coverUrl": "assets/book-hadappa.jpg"}, {"id": "vault-civ-soochana", "badge": "CIVIL GOVERNANCE", "title": "Soochana Ka Adhikar", "author": "Vishnu Rajgadhiya, Arvind Kejariwal, Ed. Harivansh", "price": "₹175.00", "oldPrice": "₹236.00", "coverUrl": "assets/book-hadappa.jpg"}], "history": [{"id": "vault-his-savarkar", "badge": "HISTORICAL BIOGRAPHY", "title": "Savarkar : Kalapani Aur Uske Baad", "author": "Ashok Kumar Pandey", "price": "₹299.00", "oldPrice": "₹403.00", "coverUrl": "assets/book-savarkar.jpg"}, {"id": "vault-his-haashiye", "badge": "MEMOIRS & SOCIAL RECORD", "title": "Haashiye Par Padi Duniya", "author": "Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi", "price": "₹600.00", "oldPrice": "₹810.00", "coverUrl": "assets/book-haashiye.jpg"}, {"id": "vault-his-azad", "badge": "FREEDOM STRUGGLE", "title": "Amar Shahid Chandrashekhar Azad", "author": "Vishwanath Vaishampayan Ed. Sudhir Vidyarthi", "price": "₹399.00", "oldPrice": "₹538.00", "coverUrl": "assets/book-savarkar.jpg"}, {"id": "vault-his-haadse", "badge": "TRIBAL & DALIT VOICE", "title": "Haadse", "author": "Ramanika Gupta", "price": "₹350.00", "oldPrice": "₹472.00", "coverUrl": "assets/book-haadse.jpg"}]};
    const CATALOG_BOOKS = [{"id": "cat-book-1-9788180317040", "title": "Halyog", "author": "Markandey", "price": "₹95.00", "oldPrice": "₹123.00", "discount": "23% OFF", "coverUrl": "assets/book-halyog.jpg", "type": "Fiction : Stories", "tags": ["bestseller", "fiction"], "isbn": "9788180317040", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-2-9788126727445", "title": "Halant", "author": "Hrishikesh Sulabh", "price": "₹250.00", "oldPrice": "₹325.00", "discount": "23% OFF", "coverUrl": "assets/book-halant.jpg", "type": "Fiction : Stories", "tags": ["fiction", "literature"], "isbn": "9788126727445", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-3-9788195948444", "title": "Halaq Ka Darogha", "author": "Maloy Jain", "price": "₹250.00", "oldPrice": "₹325.00", "discount": "23% OFF", "coverUrl": "assets/book-halaq.jpg", "type": "Satire / Humour", "tags": ["satire", "fiction"], "isbn": "9788195948444", "publisher": "Radhakrishna Prakashan"}, {"id": "cat-book-4-9788183618649", "title": "Hadappa Sabhyata Aur Vaidik Sahitya", "author": "Bhagwan Singh", "price": "₹599.00", "oldPrice": "₹778.00", "discount": "23% OFF", "coverUrl": "assets/book-hadappa.jpg", "type": "History", "tags": ["academic", "history"], "isbn": "9788183618649", "publisher": "Radhakrishna Prakashan"}, {"id": "cat-book-5-9788126724598", "title": "Haashiye Par Padi Duniya", "author": "Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi", "price": "₹600.00", "oldPrice": "₹780.00", "discount": "23% OFF", "coverUrl": "assets/book-haashiye.jpg", "type": "Memoirs", "tags": ["memoir", "history"], "isbn": "9788126724598", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-6-9788183610025", "title": "Haadse", "author": "Ramanika Gupta", "price": "₹350.00", "oldPrice": "₹455.00", "discount": "23% OFF", "coverUrl": "assets/book-haadse.jpg", "type": "Autobiography", "tags": ["dalit", "autobiography"], "isbn": "9788183610025", "publisher": "Radhakrishna Prakashan"}, {"id": "cat-book-7-9789352210053", "title": "Gypsy", "author": "Ila chandra Joshi", "price": "₹499.00", "oldPrice": "₹648.00", "discount": "23% OFF", "coverUrl": "assets/hero-gypsy.jpg", "type": "Fiction : Novel", "tags": ["fiction", "classic"], "isbn": "9789352210053", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-8-9789387462717", "title": "Gyarahaveen-A ke Ladke", "author": "Gaurav Solanki", "price": "₹150.00", "oldPrice": "₹195.00", "discount": "23% OFF", "coverUrl": "assets/book-gyarahaveen.jpg", "type": "Fiction : Stories", "tags": ["bestseller", "youth", "fiction"], "isbn": "9789387462717", "publisher": "Sarthak (An imprint of Rajkamal Prakashan)"}, {"id": "cat-book-9-9788180314646", "title": "Gyandan", "author": "Yashpal", "price": "₹95.00", "oldPrice": "₹123.00", "discount": "23% OFF", "coverUrl": "assets/book-gyandan.jpg", "type": "Fiction : Stories", "tags": ["classic", "fiction"], "isbn": "9788180314646", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-10-9788119996445", "title": "Gyan Aur Karm", "author": "Vishnukant Shastri", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "23% OFF", "coverUrl": "assets/book-gyan-aur-karm.jpg", "type": "Literary Criticism", "tags": ["academic", "philosophy"], "isbn": "9788119996445", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-11-9789388933278", "title": "Guzare Lamhe", "author": "Ashok Yadav", "price": "₹395.00", "oldPrice": "₹513.00", "discount": "23% OFF", "coverUrl": "assets/book-guzare-lamhe.jpg", "type": "Ghazal/Poetry", "tags": ["poetry", "rekhta"], "isbn": "9789388933278", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-12-9788126704965", "title": "Guzara Hua Zamana", "author": "Krishna Baldev Vaid", "price": "₹995.00", "oldPrice": "₹1293.00", "discount": "23% OFF", "coverUrl": "assets/book-guzara-hua-zamana.jpg", "type": "Fiction : Novel", "tags": ["fiction", "modern"], "isbn": "9788126704965", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-13-9789389742152", "title": "Godan", "author": "Premchand", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "23% OFF", "coverUrl": "assets/hero-godan.jpg", "type": "Fiction : Novel", "tags": ["bestseller", "classic", "fiction"], "isbn": "9789389742152", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-14-9788126713967", "title": "Raag Darbari", "author": "Shrilal Shukla", "price": "₹499.00", "oldPrice": "₹648.00", "discount": "23% OFF", "coverUrl": "assets/hero-raag-darbari.jpg", "type": "Fiction : Novel", "tags": ["bestseller", "satire", "fiction"], "isbn": "9788126713967", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-15-9788126715831", "title": "Chitralekha", "author": "Bhagwati charan Verma", "price": "₹695.00", "oldPrice": "₹903.00", "discount": "23% OFF", "coverUrl": "assets/hero-chitralekha.jpg", "type": "Fiction : Novel", "tags": ["bestseller", "classic", "fiction"], "isbn": "9788126715831", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-16-9788180313639", "title": "Rashmirathi : Dinkar Granthmala", "author": "Ramdhari Singh 'Dinkar'", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "23% OFF", "coverUrl": "assets/hero-rashmirathi.jpg", "type": "Poetry", "tags": ["bestseller", "poetry", "epic"], "isbn": "9788180313639", "publisher": "Lokbharti Prakashan"}, {"id": "cat-book-17-9788126728435", "title": "Kuchh Ishq Kiya Kuchh Kaam Kiya", "author": "Piyush Mishra", "price": "₹250.00", "oldPrice": "₹325.00", "discount": "23% OFF", "coverUrl": "assets/hero-kuchh-ishq.jpg", "type": "Poetry/Shayari", "tags": ["bestseller", "poetry", "youth"], "isbn": "9788126728435", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-18-9788126707263", "title": "Tarkash", "author": "Javed Akhtar", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "23% OFF", "coverUrl": "assets/book-tarkash.jpg", "type": "Shayari", "tags": ["rekhta", "poetry", "bestseller"], "isbn": "9788126707263", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-19-9788126715022", "title": "Aadha Gaon", "author": "Rahi Masoom Raza", "price": "₹450.00", "oldPrice": "₹585.00", "discount": "23% OFF", "coverUrl": "assets/book-aadha-gaon.jpg", "type": "Fiction : Novel", "tags": ["fiction", "partition", "classic"], "isbn": "9788126715022", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-20-9788183610926", "title": "Mahabhoj", "author": "Mannu Bhandari", "price": "₹250.00", "oldPrice": "₹325.00", "discount": "23% OFF", "coverUrl": "assets/book-mahabhoj.jpg", "type": "Fiction : Novel", "tags": ["fiction", "politics", "drama"], "isbn": "9788183610926", "publisher": "Radhakrishna Prakashan"}, {"id": "cat-book-21-9788126727360", "title": "Shekhar Ek Jeevani : Part-1", "author": "Sachchidananda Hirananda Vatsyayan 'Ajneya'", "price": "₹695.00", "oldPrice": "₹903.00", "discount": "23% OFF", "coverUrl": "assets/book-shekhar.jpg", "type": "Fiction : Novel", "tags": ["fiction", "classic"], "isbn": "9788126727360", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-22-9789393768056", "title": "Savarkar : Kalapani Aur Uske Baad", "author": "Ashok Kumar Pandey", "price": "₹299.00", "oldPrice": "₹388.00", "discount": "23% OFF", "coverUrl": "assets/book-savarkar.jpg", "type": "History", "tags": ["academic", "history", "biography"], "isbn": "9789393768056", "publisher": "Rajkamal Prakashan"}, {"id": "cat-book-23-9789390971480", "title": "Bharat Ka Samvidhan : Sankshipt Parichay", "author": "Subhash Kashyap", "price": "₹195.00", "oldPrice": "₹253.00", "discount": "23% OFF", "coverUrl": "assets/book-samvidhan.jpg", "type": "History/Constitutional History", "tags": ["law", "academic", "constitution"], "isbn": "9789390971480", "publisher": "Rajkamal Prakashan, Akshar"}, {"id": "cat-book-24-9788197989667", "title": "Bharatiya Bhasha Mein High Court Ki Vakalat", "author": "Anoop Baranwal Deshbandhu", "price": "₹350.00", "oldPrice": "₹455.00", "discount": "23% OFF", "coverUrl": "assets/book-highcourt.jpg", "type": "Law", "tags": ["law", "judiciary", "academic"], "isbn": "9788197989667", "publisher": "Lokbharti Prakashan"}];
    const MODAL_METADATA_DATABASE = {"cat-book-1-9788180317040": {"title": "Halyog", "author": "Markandey", "price": 95.0, "mrp": 123, "discount": "23% OFF", "cover": "assets/book-halyog.jpg", "isbn": "9788180317040", "pages": "153p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Markandey. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9788180317040 • 153p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-2-9788126727445": {"title": "Halant", "author": "Hrishikesh Sulabh", "price": 250.0, "mrp": 325, "discount": "23% OFF", "cover": "assets/book-halant.jpg", "isbn": "9788126727445", "pages": "107p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Hrishikesh Sulabh. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126727445 • 107p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-3-9788195948444": {"title": "Halaq Ka Darogha", "author": "Maloy Jain", "price": 250.0, "mrp": 325, "discount": "23% OFF", "cover": "assets/book-halaq.jpg", "isbn": "9788195948444", "pages": "184p Pages", "pub": "Radhakrishna Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Maloy Jain. Published by Radhakrishna Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Radhakrishna Prakashan", "ISBN: 9788195948444 • 184p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-4-9788183618649": {"title": "Hadappa Sabhyata Aur Vaidik Sahitya", "author": "Bhagwan Singh", "price": 599.0, "mrp": 778, "discount": "23% OFF", "cover": "assets/book-hadappa.jpg", "isbn": "9788183618649", "pages": "527p Pages", "pub": "Radhakrishna Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Bhagwan Singh. Published by Radhakrishna Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Radhakrishna Prakashan", "ISBN: 9788183618649 • 527p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-5-9788126724598": {"title": "Haashiye Par Padi Duniya", "author": "Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi", "price": 600.0, "mrp": 780, "discount": "23% OFF", "cover": "assets/book-haashiye.jpg", "isbn": "9788126724598", "pages": "372p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126724598 • 372p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-6-9788183610025": {"title": "Haadse", "author": "Ramanika Gupta", "price": 350.0, "mrp": 455, "discount": "23% OFF", "cover": "assets/book-haadse.jpg", "isbn": "9788183610025", "pages": "267p Pages", "pub": "Radhakrishna Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Ramanika Gupta. Published by Radhakrishna Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Radhakrishna Prakashan", "ISBN: 9788183610025 • 267p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-7-9789352210053": {"title": "Gypsy", "author": "Ila chandra Joshi", "price": 499.0, "mrp": 648, "discount": "23% OFF", "cover": "assets/hero-gypsy.jpg", "isbn": "9789352210053", "pages": "375p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Ila chandra Joshi. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9789352210053 • 375p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-8-9789387462717": {"title": "Gyarahaveen-A ke Ladke", "author": "Gaurav Solanki", "price": 150.0, "mrp": 195, "discount": "23% OFF", "cover": "assets/book-gyarahaveen.jpg", "isbn": "9789387462717", "pages": "144p Pages", "pub": "Sarthak (An imprint of Rajkamal Prakashan)", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Gaurav Solanki. Published by Sarthak (An imprint of Rajkamal Prakashan), this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Sarthak (An imprint of Rajkamal Prakashan)", "ISBN: 9789387462717 • 144p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-9-9788180314646": {"title": "Gyandan", "author": "Yashpal", "price": 95.0, "mrp": 123, "discount": "23% OFF", "cover": "assets/book-gyandan.jpg", "isbn": "9788180314646", "pages": "148p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Yashpal. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9788180314646 • 148p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-10-9788119996445": {"title": "Gyan Aur Karm", "author": "Vishnukant Shastri", "price": 299.0, "mrp": 388, "discount": "23% OFF", "cover": "assets/book-gyan-aur-karm.jpg", "isbn": "9788119996445", "pages": "280p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Vishnukant Shastri. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9788119996445 • 280p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-11-9789388933278": {"title": "Guzare Lamhe", "author": "Ashok Yadav", "price": 395.0, "mrp": 513, "discount": "23% OFF", "cover": "assets/book-guzare-lamhe.jpg", "isbn": "9789388933278", "pages": "131p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Ashok Yadav. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9789388933278 • 131p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-12-9788126704965": {"title": "Guzara Hua Zamana", "author": "Krishna Baldev Vaid", "price": 995.0, "mrp": 1293, "discount": "23% OFF", "cover": "assets/book-guzara-hua-zamana.jpg", "isbn": "9788126704965", "pages": "360p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Krishna Baldev Vaid. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126704965 • 360p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-13-9789389742152": {"title": "Godan", "author": "Premchand", "price": 299.0, "mrp": 388, "discount": "23% OFF", "cover": "assets/hero-godan.jpg", "isbn": "9789389742152", "pages": "312p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Premchand. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9789389742152 • 312p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-14-9788126713967": {"title": "Raag Darbari", "author": "Shrilal Shukla", "price": 499.0, "mrp": 648, "discount": "23% OFF", "cover": "assets/hero-raag-darbari.jpg", "isbn": "9788126713967", "pages": "423p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Shrilal Shukla. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126713967 • 423p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-15-9788126715831": {"title": "Chitralekha", "author": "Bhagwati charan Verma", "price": 695.0, "mrp": 903, "discount": "23% OFF", "cover": "assets/hero-chitralekha.jpg", "isbn": "9788126715831", "pages": "202p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Bhagwati charan Verma. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126715831 • 202p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-16-9788180313639": {"title": "Rashmirathi : Dinkar Granthmala", "author": "Ramdhari Singh 'Dinkar'", "price": 299.0, "mrp": 388, "discount": "23% OFF", "cover": "assets/hero-rashmirathi.jpg", "isbn": "9788180313639", "pages": "192p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Ramdhari Singh 'Dinkar'. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9788180313639 • 192p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-17-9788126728435": {"title": "Kuchh Ishq Kiya Kuchh Kaam Kiya", "author": "Piyush Mishra", "price": 250.0, "mrp": 325, "discount": "23% OFF", "cover": "assets/hero-kuchh-ishq.jpg", "isbn": "9788126728435", "pages": "147p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Piyush Mishra. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126728435 • 147p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-18-9788126707263": {"title": "Tarkash", "author": "Javed Akhtar", "price": 299.0, "mrp": 388, "discount": "23% OFF", "cover": "assets/book-tarkash.jpg", "isbn": "9788126707263", "pages": "167p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Javed Akhtar. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126707263 • 167p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-19-9788126715022": {"title": "Aadha Gaon", "author": "Rahi Masoom Raza", "price": 450.0, "mrp": 585, "discount": "23% OFF", "cover": "assets/book-aadha-gaon.jpg", "isbn": "9788126715022", "pages": "344p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Rahi Masoom Raza. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126715022 • 344p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-20-9788183610926": {"title": "Mahabhoj", "author": "Mannu Bhandari", "price": 250.0, "mrp": 325, "discount": "23% OFF", "cover": "assets/book-mahabhoj.jpg", "isbn": "9788183610926", "pages": "168p Pages", "pub": "Radhakrishna Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Mannu Bhandari. Published by Radhakrishna Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Radhakrishna Prakashan", "ISBN: 9788183610926 • 168p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-21-9788126727360": {"title": "Shekhar Ek Jeevani : Part-1", "author": "Sachchidananda Hirananda Vatsyayan 'Ajneya'", "price": 695.0, "mrp": 903, "discount": "23% OFF", "cover": "assets/book-shekhar.jpg", "isbn": "9788126727360", "pages": "240p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Hardcover", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Sachchidananda Hirananda Vatsyayan 'Ajneya'. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9788126727360 • 240p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-22-9789393768056": {"title": "Savarkar : Kalapani Aur Uske Baad", "author": "Ashok Kumar Pandey", "price": 299.0, "mrp": 388, "discount": "23% OFF", "cover": "assets/book-savarkar.jpg", "isbn": "9789393768056", "pages": "256p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Ashok Kumar Pandey. Published by Rajkamal Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan", "ISBN: 9789393768056 • 256p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-23-9789390971480": {"title": "Bharat Ka Samvidhan : Sankshipt Parichay", "author": "Subhash Kashyap", "price": 195.0, "mrp": 253, "discount": "23% OFF", "cover": "assets/book-samvidhan.jpg", "isbn": "9789390971480", "pages": "184p Pages", "pub": "Rajkamal Prakashan, Akshar", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Subhash Kashyap. Published by Rajkamal Prakashan, Akshar, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Rajkamal Prakashan, Akshar", "ISBN: 9789390971480 • 184p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "cat-book-24-9788197989667": {"title": "Bharatiya Bhasha Mein High Court Ki Vakalat", "author": "Anoop Baranwal Deshbandhu", "price": 350.0, "mrp": 455, "discount": "23% OFF", "cover": "assets/book-highcourt.jpg", "isbn": "9788197989667", "pages": "216p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authentic work by Anoop Baranwal Deshbandhu. Published by Lokbharti Prakashan, this authoritative volume represents an essential edition in Indian literature and scholarly thought.", "highlights": ["Official Edition from Lokbharti Prakashan", "ISBN: 9788197989667 • 216p Standard Print Pages", "Verified Authentic Text with Complete Unabridged Content", "Express Dispatch with Protective Moisture-Proof Bookstore Packaging"]}, "podium-godan": {"title": "Godan", "author": "Premchand", "price": 299.0, "mrp": 403.0, "discount": "26% OFF", "cover": "assets/hero-godan.jpg", "isbn": "9789389742152", "pages": "312p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback / Library Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Premchand's crowning masterpiece exploring Indian agrarian life, caste, debt, and the unyielding human spirit.", "highlights": ["National Bestseller • ALL-TIME CLASSIC", "ISBN: 9789389742152 • 312p Pages", "Publisher: Lokbharti Prakashan", "Pristine Bookstore Packaging & Safe COD Delivery Available"]}, "podium-raag-darbari": {"title": "Raag Darbari", "author": "Shrilal Shukla", "price": 499.0, "mrp": 648.0, "discount": "23% OFF", "cover": "assets/hero-raag-darbari.jpg", "isbn": "9788126713967", "pages": "423p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback / Library Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Set in Shivpalganj, Shrilal Shukla's biting magnum opus on power, bureaucracy, and rural reality.", "highlights": ["National Bestseller • GREATEST SATIRE", "ISBN: 9788126713967 • 423p Pages", "Publisher: Rajkamal Prakashan", "Pristine Bookstore Packaging & Safe COD Delivery Available"]}, "podium-chitralekha": {"title": "Chitralekha", "author": "Bhagwaticharan Verma", "price": 299.0, "mrp": 403.0, "discount": "25% OFF", "cover": "assets/hero-chitralekha.jpg", "isbn": "9788126715855", "pages": "200p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback / Library Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Bhagwaticharan Verma's masterpiece interrogating asceticism, desire, and moral righteousness.", "highlights": ["National Bestseller • PHILOSOPHICAL NOVEL", "ISBN: 9788126715855 • 200p Pages", "Publisher: Rajkamal Prakashan", "Pristine Bookstore Packaging & Safe COD Delivery Available"]}, "podium-rashmirathi": {"title": "Rashmirathi : Dinkar Granthmala", "author": "Ramdhari Singh 'Dinkar'", "price": 299.0, "mrp": 388.0, "discount": "22% OFF", "cover": "assets/hero-rashmirathi.jpg", "isbn": "9788180313639", "pages": "192p Pages", "pub": "Lokbharti Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback / Library Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Ramdhari Singh Dinkar's fiery verses celebrating Karna's valour, righteousness, and tragic grandeur.", "highlights": ["National Bestseller • EPIC POETRY", "ISBN: 9788180313639 • 192p Pages", "Publisher: Lokbharti Prakashan", "Pristine Bookstore Packaging & Safe COD Delivery Available"]}, "podium-ishq-mishra": {"title": "Kuchh Ishq Kiya Kuchh Kaam Kiya", "author": "Piyush Mishra", "price": 250.0, "mrp": 337.0, "discount": "25% OFF", "cover": "assets/hero-kuchh-ishq.jpg", "isbn": "9788126728435", "pages": "147p Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback / Library Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Piyush Mishra's beloved anthology of verses capturing love, longing, bohemian rebellion, and Delhi winters.", "highlights": ["National Bestseller • MODERN POETRY", "ISBN: 9788126728435 • 147p Pages", "Publisher: Rajkamal Prakashan", "Pristine Bookstore Packaging & Safe COD Delivery Available"]}, "rekhta-tarkash": {"title": "Tarkash", "author": "Javed Akhtar", "price": 299.0, "mrp": 403.0, "discount": "26% OFF", "cover": "assets/book-tarkash.jpg", "isbn": "978-REKHTA-IND", "pages": "220 Pages", "pub": "Rajkamal / Rekhta Books", "lang": "Urdu / Hindi (Devanagari)", "binding": "Paperback / Deluxe", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Timeless nazms and ghazals of love, parting, and existential contemplation.", "highlights": ["Mehfil-e-Rekhta Curated Classic Collection", "Original Shayari, Ghazals & Nazms with Commentary", "Collector Quality Printing with Aesthetic Typography"]}, "rekhta-ishq-mishra": {"title": "Kuchh Ishq Kiya Kuchh Kaam Kiya", "author": "Piyush Mishra", "price": 250.0, "mrp": 325.0, "discount": "23% OFF", "cover": "assets/hero-kuchh-ishq.jpg", "isbn": "978-REKHTA-IND", "pages": "220 Pages", "pub": "Rajkamal / Rekhta Books", "lang": "Urdu / Hindi (Devanagari)", "binding": "Paperback / Deluxe", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Beloved theatrical verses, nostalgic laments, and bohemian stage lyrics.", "highlights": ["Mehfil-e-Rekhta Curated Classic Collection", "Original Shayari, Ghazals & Nazms with Commentary", "Collector Quality Printing with Aesthetic Typography"]}, "rekhta-guzare-lamhe": {"title": "Guzare Lamhe", "author": "Ashok Yadav", "price": 395.0, "mrp": 533.0, "discount": "26% OFF", "cover": "assets/book-guzare-lamhe.jpg", "isbn": "978-REKHTA-IND", "pages": "220 Pages", "pub": "Rajkamal / Rekhta Books", "lang": "Urdu / Hindi (Devanagari)", "binding": "Paperback / Deluxe", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Soulful ghazals and nazms reviving classical Awadhi and Hindustani poetic traditions.", "highlights": ["Mehfil-e-Rekhta Curated Classic Collection", "Original Shayari, Ghazals & Nazms with Commentary", "Collector Quality Printing with Aesthetic Typography"]}, "rekhta-rashmirathi": {"title": "Rashmirathi : Dinkar Granthmala", "author": "Ramdhari Singh 'Dinkar'", "price": 299.0, "mrp": 388.0, "discount": "22% OFF", "cover": "assets/hero-rashmirathi.jpg", "isbn": "978-REKHTA-IND", "pages": "220 Pages", "pub": "Rajkamal / Rekhta Books", "lang": "Urdu / Hindi (Devanagari)", "binding": "Paperback / Deluxe", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Immortal verses of valour, dignity, and righteous courage in Karna's epic voice.", "highlights": ["Mehfil-e-Rekhta Curated Classic Collection", "Original Shayari, Ghazals & Nazms with Commentary", "Collector Quality Printing with Aesthetic Typography"]}, "rekhta-kyon": {"title": "क्यों (Kyon)", "author": "Jaun Elia", "price": 395.0, "mrp": 495.0, "discount": "20% OFF", "cover": "assets/book-kyon-jaun-elia.jpg", "isbn": "978-9389742015", "pages": "288 Pages", "pub": "Rekhta Publications", "lang": "Urdu / Hindi (Devanagari)", "binding": "Hardbound / Collector Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "The haunting, iconoclastic philosophical poetry collection of Jaun Elia, presenting his razor-sharp introspection and existential laments.", "highlights": ["Authentic Rekhta Poetry Archive Edition", "Comprehensive Devanagari transliteration with glossary", "Special gold foil typography on jacket"]}, "rekhta-ranjish": {"title": "रंजिश ही सही (Ranjish Hi Sahi)", "author": "Ahmad Faraz", "price": 350.0, "mrp": 450.0, "discount": "22% OFF", "cover": "assets/book-ranjish-hi-sahi.jpg", "isbn": "978-9389742022", "pages": "240 Pages", "pub": "Rekhta Publications", "lang": "Urdu / Hindi (Devanagari)", "binding": "Paperback / Deluxe", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Immortal ghazals and romantic elegies by Pakistan's legendary poet Ahmad Faraz, capturing resistance, passion, and longing.", "highlights": ["Includes famous ghazal 'Ranjish Hi Sahi'", "Critical appreciation by renowned Urdu scholars", "High quality paper with Smyth-sewn binding"]}, "rekhta-dozakhnama": {"title": "दोज़ख़नामा (Dozakhnama)", "author": "Rabisankar Bal", "price": 450.0, "mrp": 599.0, "discount": "25% OFF", "cover": "assets/hero-book-dozakh.jpg", "isbn": "978-9389742039", "pages": "376 Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (Trans. Arunava Sinha)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "A wondrous novel of conversations from the grave between Mirza Ghalib and Saadat Hasan Manto, exploring love, Delhi, Lahore, and memory.", "highlights": ["Winner of Crossword Book Award", "Deep literary tribute to Ghalib and Manto", "Direct dispatch from Prayagraj warehouse"]}, "rekhta-thanda-ghost": {"title": "ठंडा गोश्त (Thanda Gosht)", "author": "Saadat Hasan Manto", "price": 299.0, "mrp": 399.0, "discount": "25% OFF", "cover": "assets/hero-book-thanda-ghost.jpg", "isbn": "978-9389742046", "pages": "210 Pages", "pub": "Rajkamal Prakashan", "lang": "Urdu / Hindi", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "The groundbreaking, fearless partition narrative that redefined progressive Urdu literature and challenged societal orthodoxy.", "highlights": ["Manto's most celebrated and controversial masterpiece", "Includes original court deposition essays", "Collector's edition with authentic cover art"]}, "rekhta-dhuaan": {"title": "धुआँ (Dhuaan)", "author": "Saadat Hasan Manto", "price": 299.0, "mrp": 399.0, "discount": "25% OFF", "cover": "assets/hero-book-dhuaan.jpg", "isbn": "978-9389742053", "pages": "220 Pages", "pub": "Rajkamal Prakashan", "lang": "Urdu / Hindi", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Unfiltered, evocative psychological short stories laying bare human nature and the complexities of desire.", "highlights": ["Complete unabridged collection of Manto's stories", "Crisp Devanagari typography", "100% Authentic Publisher Edition"]}, "bundle-premchand": {"title": "Munshi Premchand Definitive Collection", "author": "Munshi Premchand", "price": 799.0, "mrp": 1099.0, "discount": "27% OFF", "cover": "assets/hero-godan.jpg", "isbn": "978-BOXSET-IND", "pages": "3 Complete Volumes", "pub": "Indigo Curated Collector Sets", "lang": "Hindi (देवनागरी)", "binding": "Box Set (3 Volumes)", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Exclusive 3-volume collector box set featuring Godan (गोदान), Gaban (ग़बन), Nirmala (निर्मला). Save up to 27% OFF with bundle pricing.", "highlights": ["Includes 3 Complete Landmark Volumes: Godan (गोदान), Gaban (ग़बन), Nirmala (निर्मला)", "Special Slipcase / Collector Packaging", "Exclusive Multi-Book Bundle Discount of 27% OFF"]}, "bundle-satire": {"title": "Indian Satire & Classic Fiction Set", "author": "Shrilal Shukla, Bhagwaticharan Verma, Rahi Masoom Raza", "price": 899.0, "mrp": 1199.0, "discount": "25% OFF", "cover": "assets/hero-raag-darbari.jpg", "isbn": "978-BOXSET-IND", "pages": "3 Complete Volumes", "pub": "Indigo Curated Collector Sets", "lang": "Hindi (देवनागरी)", "binding": "Box Set (3 Volumes)", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Exclusive 3-volume collector box set featuring Raag Darbari, Chitralekha, Aadha Gaon. Save up to 25% OFF with bundle pricing.", "highlights": ["Includes 3 Complete Landmark Volumes: Raag Darbari, Chitralekha, Aadha Gaon", "Special Slipcase / Collector Packaging", "Exclusive Multi-Book Bundle Discount of 25% OFF"]}, "bundle-poetry": {"title": "Great Indian Verse & Shayari Anthology", "author": "Javed Akhtar, Ramdhari Singh Dinkar, Piyush Mishra", "price": 699.0, "mrp": 899.0, "discount": "22% OFF", "cover": "assets/book-tarkash.jpg", "isbn": "978-BOXSET-IND", "pages": "3 Complete Volumes", "pub": "Indigo Curated Collector Sets", "lang": "Hindi (देवनागरी)", "binding": "Box Set (3 Volumes)", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Exclusive 3-volume collector box set featuring Tarkash (तरकश), Rashmirathi (रश्मिरथी), Kuchh Ishq Kiya. Save up to 22% OFF with bundle pricing.", "highlights": ["Includes 3 Complete Landmark Volumes: Tarkash (तरकश), Rashmirathi (रश्मिरथी), Kuchh Ishq Kiya", "Special Slipcase / Collector Packaging", "Exclusive Multi-Book Bundle Discount of 22% OFF"]}, "feat-raag-darbari": {"title": "Raag Darbari", "author": "Shrilal Shukla", "price": 499.0, "mrp": 673.0, "discount": "26% OFF", "cover": "assets/hero-raag-darbari.jpg", "isbn": "9789392757242", "pages": "380 Pages", "pub": "Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Deluxe Edition", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "A razor-sharp satire of post-independence Indian politics, governance, and rural education system.", "highlights": ["Sahitya Akademi Award-Winning Masterpiece", "Standard Edition with Unabridged Text", "Verified Rajkamal Prakashan Landmark Publication"]}, "hindi-gypsy": {"title": "Gypsy", "author": "Ila chandra Joshi", "price": 499.0, "mrp": 648.0, "discount": "23% OFF", "cover": "assets/hero-gypsy.jpg", "isbn": "978-HINDI-IND", "pages": "260 Pages", "pub": "Lokbharti / Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Psychological exploration of love, non-conformity, and vagabond human spirit.", "highlights": ["Modern Hindi Classic Fiction", "Official Unabridged Edition", "High Quality Print & Acid-Free Paper"]}, "hindi-aadha-gaon": {"title": "Aadha Gaon", "author": "Rahi Masoom Raza", "price": 450.0, "mrp": 585.0, "discount": "23% OFF", "cover": "assets/book-aadha-gaon.jpg", "isbn": "978-HINDI-IND", "pages": "260 Pages", "pub": "Lokbharti / Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Heartbreaking saga of Ganga-Jamuni tehzeeb and partition trauma in rural Ghazipur.", "highlights": ["Modern Hindi Classic Fiction", "Official Unabridged Edition", "High Quality Print & Acid-Free Paper"]}, "hindi-mahabhoj": {"title": "Mahabhoj", "author": "Mannu Bhandari", "price": 250.0, "mrp": 337.0, "discount": "23% OFF", "cover": "assets/book-mahabhoj.jpg", "isbn": "978-HINDI-IND", "pages": "260 Pages", "pub": "Lokbharti / Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Fiery political classic exposing electoral hypocrisy and Dalit exploitation.", "highlights": ["Modern Hindi Classic Fiction", "Official Unabridged Edition", "High Quality Print & Acid-Free Paper"]}, "hindi-shekhar": {"title": "Shekhar Ek Jeevani : Part-1", "author": "Sachchidananda Hirananda Vatsyayan 'Ajneya'", "price": 695.0, "mrp": 903.0, "discount": "23% OFF", "cover": "assets/book-shekhar.jpg", "isbn": "978-HINDI-IND", "pages": "260 Pages", "pub": "Lokbharti / Rajkamal Prakashan", "lang": "Hindi (देवनागरी)", "binding": "Paperback", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Ajneya's existential milestone on intellectual rebellion, memory, and youth.", "highlights": ["Modern Hindi Classic Fiction", "Official Unabridged Edition", "High Quality Print & Acid-Free Paper"]}, "vault-law-highcourt": {"title": "Bharatiya Bhasha Mein High Court Ki Vakalat", "author": "Anoop Baranwal Deshbandhu", "price": 350.0, "mrp": 472.0, "discount": "26% OFF", "cover": "assets/book-highcourt.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in LAW: Bharatiya Bhasha Mein High Court Ki Vakalat by Anoop Baranwal Deshbandhu. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: HIGH COURT PRACTICE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-law-constitution": {"title": "Bharat Ka Samvidhan : Sankshipt Parichay", "author": "Subhash Kashyap", "price": 195.0, "mrp": 263.0, "discount": "26% OFF", "cover": "assets/book-samvidhan.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in LAW: Bharat Ka Samvidhan : Sankshipt Parichay by Subhash Kashyap. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: CONSTITUTION MANUAL", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-law-ucc": {"title": "Samaan Nagrik Sanhita : Chunautiya Aur Samadhan", "author": "Anoop Baranwal", "price": 399.0, "mrp": 538.0, "discount": "26% OFF", "cover": "assets/book-highcourt.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in LAW: Samaan Nagrik Sanhita : Chunautiya Aur Samadhan by Anoop Baranwal. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: LEGAL TREATISE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-law-judiciary": {"title": "Nyayapalika Kasauti Par", "author": "Kamlesh Jain, Edi. ranjeet verma ", "price": 199.0, "mrp": 268.0, "discount": "26% OFF", "cover": "assets/book-samvidhan.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in LAW: Nyayapalika Kasauti Par by Kamlesh Jain, Edi. ranjeet verma . Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: JUDICIAL CRITIQUE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-sah-gyan": {"title": "Gyan Aur Karm", "author": "Vishnukant Shastri", "price": 299.0, "mrp": 403.0, "discount": "26% OFF", "cover": "assets/book-gyan-aur-karm.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in SAHITYA: Gyan Aur Karm by Vishnukant Shastri. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: PHILOSOPHY & LITERARY CRITICISM", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-sah-shilp": {"title": "Hindi Kahaniyon Ki Shilp-Vidhi Ka Vikas", "author": "Laxmi Narayan Lal", "price": 195.0, "mrp": 263.0, "discount": "26% OFF", "cover": "assets/book-gyan-aur-karm.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in SAHITYA: Hindi Kahaniyon Ki Shilp-Vidhi Ka Vikas by Laxmi Narayan Lal. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: NARRATIVE CRAFT", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-sah-itihas": {"title": "Aadhunik Hindi Sahitya Ka Itihas", "author": "Bachchan Singh", "price": 950.0, "mrp": 1282.0, "discount": "26% OFF", "cover": "assets/book-gyan-aur-karm.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in SAHITYA: Aadhunik Hindi Sahitya Ka Itihas by Bachchan Singh. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: LITERARY HISTORY", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-sah-anusandhan": {"title": "Anusandhan Pravidhi : Siddhant Aur Prakariya", "author": "S.N.Ganeshan", "price": 400.0, "mrp": 540.0, "discount": "26% OFF", "cover": "assets/book-gyan-aur-karm.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in SAHITYA: Anusandhan Pravidhi : Siddhant Aur Prakariya by S.N.Ganeshan. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: RESEARCH METHODOLOGY", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-civ-hadappa": {"title": "Hadappa Sabhyata Aur Vaidik Sahitya", "author": "Bhagwan Singh", "price": 599.0, "mrp": 808.0, "discount": "26% OFF", "cover": "assets/book-hadappa.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in CIVIL: Hadappa Sabhyata Aur Vaidik Sahitya by Bhagwan Singh. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: ANCIENT VEDIC HISTORY", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-civ-badalata": {"title": "Badalata Hua Desh", "author": "Manoj Kumar Pandey", "price": 150.0, "mrp": 202.0, "discount": "26% OFF", "cover": "assets/book-hadappa.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in CIVIL: Badalata Hua Desh by Manoj Kumar Pandey. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: SOCIAL ESSAYS & CIVIC REFORM", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-civ-nyay": {"title": "Nyay Ka Sangharsh", "author": "Yashpal", "price": 395.0, "mrp": 533.0, "discount": "26% OFF", "cover": "assets/book-hadappa.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in CIVIL: Nyay Ka Sangharsh by Yashpal. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: POLITICAL THOUGHT", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-civ-soochana": {"title": "Soochana Ka Adhikar", "author": "Vishnu Rajgadhiya, Arvind Kejariwal, Ed. Harivansh", "price": 175.0, "mrp": 236.0, "discount": "26% OFF", "cover": "assets/book-hadappa.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in CIVIL: Soochana Ka Adhikar by Vishnu Rajgadhiya, Arvind Kejariwal, Ed. Harivansh. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: CIVIL GOVERNANCE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-his-savarkar": {"title": "Savarkar : Kalapani Aur Uske Baad", "author": "Ashok Kumar Pandey", "price": 299.0, "mrp": 403.0, "discount": "26% OFF", "cover": "assets/book-savarkar.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in HISTORY: Savarkar : Kalapani Aur Uske Baad by Ashok Kumar Pandey. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: HISTORICAL BIOGRAPHY", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-his-haashiye": {"title": "Haashiye Par Padi Duniya", "author": "Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi", "price": 600.0, "mrp": 810.0, "discount": "26% OFF", "cover": "assets/book-haashiye.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in HISTORY: Haashiye Par Padi Duniya by Balkrishna Gupta, Ed. Sarang Upadhyay, Anurag Chaturvedi. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: MEMOIRS & SOCIAL RECORD", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-his-azad": {"title": "Amar Shahid Chandrashekhar Azad", "author": "Vishwanath Vaishampayan Ed. Sudhir Vidyarthi", "price": 399.0, "mrp": 538.0, "discount": "26% OFF", "cover": "assets/book-savarkar.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in HISTORY: Amar Shahid Chandrashekhar Azad by Vishwanath Vaishampayan Ed. Sudhir Vidyarthi. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: FREEDOM STRUGGLE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}, "vault-his-haadse": {"title": "Haadse", "author": "Ramanika Gupta", "price": 350.0, "mrp": 472.0, "discount": "26% OFF", "cover": "assets/book-haadse.jpg", "isbn": "978-VAULT-IND", "pages": "360 Pages", "pub": "Radhakrishna / Rajkamal / Lokbharti", "lang": "Hindi / English", "binding": "Paperback / Hardbound", "dispatch": "Ships in 24 Hours from Prayagraj Hub", "overview": "Authoritative work in HISTORY: Haadse by Ramanika Gupta. Recommended for advocates, researchers, and civil services candidates.", "highlights": ["Essential Reference: TRIBAL & DALIT VOICE", "Institutional & High Court Chamber Preferred Edition", "Authentic Unabridged Text with Verified Citations"]}};


// =========================================================================
// INDIGO BOOKS INDIA - PURE VANILLA JS ENGINE (UNIFIED & COMPLETE)
// =========================================================================

// --- UNIVERSAL ASSET URL RESOLVER ---
function getAssetUrl(url) {
  if (!url) return '';
  if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('data:')) return url;
  let clean = url.replace(/^assets\//, '')
                 .replace(/^\{\{\s*['"]?/, '')
                 .replace(/['"]?\s*\|\s*asset_url\s*\}\}$/, '')
                 .trim();
  if (typeof window !== 'undefined' && window.SHOPIFY_ASSET_URL_ROOT) {
    return window.SHOPIFY_ASSET_URL_ROOT + clean;
  }
  return 'assets/' + clean;
}

// --- 0. HERO 3x2 SEQUENTIAL SPOTLIGHT ENGINE (EXACT VIDEO MATCH) ---
let heroSpotlightTimeouts = [];
let isUserInteractingHero = false;

function clearHeroSpotlightTimers() {
  heroSpotlightTimeouts.forEach(function(t) { clearTimeout(t); });
  heroSpotlightTimeouts = [];
}

function setHeroSpotlitBook(index) {
  const grid = document.getElementById('heroBooksGrid');
  const cards = document.querySelectorAll('.hero-video-book-card');
  if (!cards.length) return;

  if (index === null || index === -1 || index === undefined) {
    if (grid) grid.classList.remove('spotlight-mode');
    cards.forEach(function(card) { card.classList.remove('is-spotlit'); });
    return;
  }

  if (grid) grid.classList.add('spotlight-mode');
  cards.forEach(function(card, idx) {
    if (idx === index) {
      card.classList.add('is-spotlit');
    } else {
      card.classList.remove('is-spotlit');
    }
  });
}

function runVideoIntroSpotlightTour() {
  clearHeroSpotlightTimers();
  if (isUserInteractingHero) return;

  setHeroSpotlitBook(null);

  // 1. Top-Right Book (index 2) for 900ms
  var t1 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(2);
  }, 700);

  // 2. Bottom-Right Book (index 5) for 900ms
  var t2 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(5);
  }, 1600);

  // 3. Bottom-Center Book (index 4) for 900ms
  var t3 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(4);
  }, 2500);

  // 4. Smoothly restore all 6 books to resting state
  var t4 = setTimeout(function() {
    if (!isUserInteractingHero) setHeroSpotlitBook(null);
  }, 3400);

  heroSpotlightTimeouts.push(t1, t2, t3, t4);
}

function handleHeroBookHover(index) {
  isUserInteractingHero = true;
  clearHeroSpotlightTimers();
  setHeroSpotlitBook(index);
}

function handleHeroGridMouseLeave() {
  setHeroSpotlitBook(null);
}


// --- 1. THE PODIUM CAROUSEL ENGINE ---
let currentPodiumIndex = 0;

function getPodiumData() {
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length >= 5) {
    return window.SHOPIFY_LIVE_PRODUCTS.slice(0, 5).map(function(prod, idx) {
      const fallback = (typeof PODIUM_BOOKS !== 'undefined' && PODIUM_BOOKS[idx]) ? PODIUM_BOOKS[idx] : {};
      return {
        id: prod.id ? String(prod.id) : (fallback.id || 'podium-' + idx),
        variantId: prod.variantId || fallback.variantId || '',
        handle: prod.handle || fallback.handle || '',
        title: prod.title || fallback.title || 'Featured Classic',
        author: prod.author || fallback.author || 'Renowned Author',
        price: prod.price || fallback.price || '₹299.00',
        oldPrice: prod.oldPrice || fallback.oldPrice || '₹400.00',
        discount: prod.discount || fallback.discount || '25% OFF',
        badge: idx === 0 ? "NATIONAL BESTSELLER" : (idx === 1 ? "SAHITYA AKADEMI" : (idx === 2 ? "TIMELESS CLASSIC" : "TOP TRENDING")),
        rating: fallback.rating || "4.9 (10,000+)",
        stock: "In Stock • Ships in 24 Hrs",
        coverUrl: prod.coverUrl || fallback.coverUrl || '',
        cover: prod.coverUrl || fallback.coverUrl || '',
        firstPageExcerpt: fallback.firstPageExcerpt || prod.description || "A masterwork of Indian literature capturing the essence of storytelling.",
        quote: fallback.quote || (prod.description ? prod.description.slice(0, 100) + '...' : "Essential reading for every book lover in India."),
        pages: fallback.pages || "320p",
        publisher: fallback.publisher || prod.author || "Lokbharti / Rajkamal",
        genre: prod.type || fallback.genre || "Fiction : Classic",
        url: prod.url || fallback.url || ''
      };
    });
  }
  return typeof PODIUM_BOOKS !== 'undefined' ? PODIUM_BOOKS : [];
}

function selectPodiumBook(index) {
  const books = getPodiumData();
  if (!books.length) return;
  if (index < 0 || index >= books.length) return;
  currentPodiumIndex = index;
  const book = books[index];

  // Update center book 3D cover & text
  const elCoverImg = document.getElementById('podium-cover-img');
  const elInsideThumb = document.getElementById('podium-inside-thumb');
  const elInsideTitle = document.getElementById('podium-inside-title');
  const elInsideAuthor = document.getElementById('podium-inside-author');
  const elPageTitle = document.getElementById('podium-page-title');
  const elPageExcerpt = document.getElementById('podium-page-excerpt');
  const el3dBook = document.getElementById('podium-3d-book');

  const resolvedCover = getAssetUrl(book.coverUrl || book.cover);

  if (elCoverImg) {
    elCoverImg.src = resolvedCover;
    elCoverImg.alt = book.title;
  }
  if (elInsideThumb) {
    elInsideThumb.src = resolvedCover;
    elInsideThumb.alt = book.title;
  }
  if (elInsideTitle) elInsideTitle.textContent = book.title;
  if (elInsideAuthor) elInsideAuthor.textContent = book.author;
  if (elPageTitle) elPageTitle.textContent = book.title;
  if (elPageExcerpt) elPageExcerpt.textContent = book.firstPageExcerpt;
  if (el3dBook) el3dBook.classList.remove('is-open');

  // Update Right Spotlight Card
  const elBadge = document.getElementById('podiumSpotBadge');
  const elStock = document.getElementById('podiumSpotStock');
  const elHeading = document.getElementById('podiumSpotHeading');
  const elAuthor = document.getElementById('podiumSpotAuthor');
  const elRating = document.getElementById('podiumSpotRating');
  const elQuote = document.getElementById('podiumSpotQuote');
  const elPages = document.getElementById('podiumSpotPages');
  const elPublisher = document.getElementById('podiumSpotPublisher');
  const elPrice = document.getElementById('podiumSpotPrice');
  const elOldPrice = document.getElementById('podiumSpotOldPrice');
  const elDiscount = document.getElementById('podiumSpotDiscount');

  if (elBadge) elBadge.textContent = book.badge;
  if (elStock) elStock.textContent = book.stock;
  if (elHeading) elHeading.textContent = book.title;
  if (elAuthor) elAuthor.textContent = book.author;
  if (elRating) elRating.textContent = book.rating;
  if (elQuote) elQuote.textContent = '"' + book.quote + '"';
  if (elPages) elPages.textContent = book.pages;
  if (elPublisher) elPublisher.textContent = book.publisher;
  if (elPrice) elPrice.textContent = book.price;
  if (elOldPrice) elOldPrice.textContent = book.oldPrice;
  if (elDiscount) elDiscount.textContent = book.discount;

  // Update Flanking Books positions
  const count = books.length;
  const fL2 = (index - 2 + count) % count;
  const fL1 = (index - 1 + count) % count;
  const fR1 = (index + 1) % count;
  const fR2 = (index + 2) % count;

  const imgL2 = document.getElementById('flankImgL2');
  const imgL1 = document.getElementById('flankImgL1');
  const imgR1 = document.getElementById('flankImgR1');
  const imgR2 = document.getElementById('flankImgR2');

  if (imgL2) { imgL2.src = getAssetUrl(books[fL2].coverUrl || books[fL2].cover); imgL2.alt = books[fL2].title; }
  if (imgL1) { imgL1.src = getAssetUrl(books[fL1].coverUrl || books[fL1].cover); imgL1.alt = books[fL1].title; }
  if (imgR1) { imgR1.src = getAssetUrl(books[fR1].coverUrl || books[fR1].cover); imgR1.alt = books[fR1].title; }
  if (imgR2) { imgR2.src = getAssetUrl(books[fR2].coverUrl || books[fR2].cover); imgR2.alt = books[fR2].title; }

  // Update Dots
  const dots = document.querySelectorAll('.podium-dot');
  dots.forEach(function(dot, i) {
    if (i === index) dot.classList.add('active');
    else dot.classList.remove('active');
  });
}

function prevPodiumBook() {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex - 1 + count) % count);
}

function nextPodiumBook() {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex + 1) % count);
}

function selectPodiumByFlank(slotOffset) {
  const books = getPodiumData();
  const count = books.length;
  selectPodiumBook((currentPodiumIndex + slotOffset + count) % count);
}

function togglePodiumCover(e) {
  if (e) e.stopPropagation();
  const el = document.getElementById('podium-3d-book');
  if (el) el.classList.toggle('is-open');
}

function addCurrentPodiumToCart() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  if (book.variantId) {
    addShopifyVariantToCart(book.variantId, 1);
  } else {
    addToCart(book.id || 'podium-' + currentPodiumIndex);
  }
}

function openCurrentPodiumOverview() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  openOverviewModal(book);
}

function orderCurrentPodiumWhatsApp() {
  const books = getPodiumData();
  if (!books.length) return;
  const book = books[currentPodiumIndex];
  const url = book.url ? (window.location.origin + book.url) : window.location.href;
  const lines = [
    "Hello Indigo Books India!",
    "I would like to order this book from The Podium:",
    "*Book:* " + book.title,
    "*Author:* " + book.author,
    "*Price:* " + book.price,
    "*Format:* Paperback",
    "*URL:* " + url,
    "Please confirm availability and share COD / Payment details!"
  ];
  const msg = lines.join("\n");
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(msg), '_blank');
}


// --- 2. MEHFIL-E-REKHTA STATE & FUNCTIONS ---
let currentPoetKey = 'all';
let currentSherIndex = 0;

function switchPoet(poetKey) {
  if (typeof POET_SHAYARI_DATA !== 'undefined' && POET_SHAYARI_DATA[poetKey]) {
    currentPoetKey = poetKey;
    currentSherIndex = 0;
    renderCurrentSher();
  }

  // Update active pill
  document.querySelectorAll('.poet-pill').forEach(function(btn) {
    if (btn.getAttribute('data-poet') === poetKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  // Filter / Spotlight the 5 authentic Urdu titles
  const cards = document.querySelectorAll('.rekhta-book-card');
  cards.forEach(function(card) {
    const cardPoet = card.getAttribute('data-poet');
    if (poetKey === 'all' || cardPoet === poetKey) {
      card.classList.remove('dimmed');
      card.classList.add('highlighted');
    } else {
      card.classList.remove('highlighted');
      card.classList.add('dimmed');
    }
  });
}

function renderCurrentSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const poet = POET_SHAYARI_DATA[currentPoetKey];
  const couplets = poet.couplets;
  if (!couplets || couplets.length === 0) return;

  const sher = couplets[currentSherIndex % couplets.length];

  const elUrdu = document.getElementById('rekhtaUrdu');
  const elHindi = document.getElementById('rekhtaHindi');
  const elEng = document.getElementById('rekhtaEng');
  const elAttr = document.getElementById('rekhtaAttr');
  const elFull = document.getElementById('rekhtaFullGhazal');

  if (elUrdu) elUrdu.textContent = sher.urdu;
  if (elHindi) elHindi.textContent = sher.hindi;
  if (elEng) elEng.textContent = sher.eng;
  if (elAttr) elAttr.textContent = sher.attr;
  if (elFull) elFull.textContent = sher.ghazal;

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function nextSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex + 1) % couplets.length;
  renderCurrentSher();
}

function prevSher() {
  if (typeof POET_SHAYARI_DATA === 'undefined' || !POET_SHAYARI_DATA[currentPoetKey]) return;
  const couplets = POET_SHAYARI_DATA[currentPoetKey].couplets;
  currentSherIndex = (currentSherIndex - 1 + couplets.length) % couplets.length;
  renderCurrentSher();
}

function toggleGhazalDrawer() {
  const el = document.getElementById('rekhtaFullGhazal');
  if (el) el.classList.toggle('is-open');
}


// --- 3. ACADEMIC & LAW VAULT STATE & FUNCTIONS ---
let currentVaultTab = 'law';

function switchVaultTab(tabKey) {
  if (typeof VAULT_BOOKS === 'undefined' || !VAULT_BOOKS[tabKey]) return;
  currentVaultTab = tabKey;

  // Update tab buttons
  document.querySelectorAll('.vault-tab-btn').forEach(function(btn) {
    if (btn.getAttribute('data-tab') === tabKey) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  // Render 4 books
  const books = VAULT_BOOKS[tabKey];
  const container = document.getElementById('vaultCardsContainer');
  if (!container) return;

  container.innerHTML = books.map(function(book) {
    const cover = getAssetUrl(book.coverUrl || book.cover);
    return `
      <div class="vault-card">
        <div class="vault-card-thumb">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" />
        </div>
        <div class="vault-card-body">
          <div style="font-size: 10px; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 4px;">
            ${book.badge}
          </div>
          <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px;">
            ${book.title}
          </h3>
          <div style="font-size: 12px; color: #64748B; margin-bottom: 12px;">
            ${book.author}
          </div>
          <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
            <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
            <span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>
          </div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            <button type="button" class="btn-overview" onclick="openOverviewModal('${book.id}')">
              <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
            </button>
            <button type="button" class="btn-add-cart" onclick="addToCart('${book.id}')">
              <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 4. PAN-INDIA CATALOG FILTERING ---
let currentCatalogCategory = 'all';
let currentCatalogQuery = '';

function filterCatalog(category) {
  currentCatalogCategory = category;

  document.querySelectorAll('.cat-pill').forEach(function(btn) {
    if (btn.getAttribute('data-cat') === category) btn.classList.add('active');
    else btn.classList.remove('active');
  });

  renderCatalog();
}

function handleCatalogSearch(e) {
  currentCatalogQuery = e.target.value.toLowerCase().trim();
  renderCatalog();
}

function handleHeroSearch(e) {
  if (e.key === 'Enter') {
    performHeroSearch();
  }
}

function performHeroSearch() {
  const input = document.getElementById('hero-search-input');
  if (input) {
    const val = input.value.trim();
    currentCatalogQuery = val.toLowerCase();
    const catInput = document.getElementById('catalog-search-input');
    if (catInput) catInput.value = val;

    if (typeof window !== 'undefined' && val.length > 0 && (window.location.hostname.includes('myshopify.com') || window.location.hostname.includes('indigobooks'))) {
      const source = getCatalogData();
      const hasLocalMatch = source.some(function(b) {
        return b.title.toLowerCase().includes(currentCatalogQuery) || (b.author && b.author.toLowerCase().includes(currentCatalogQuery));
      });
      if (!hasLocalMatch) {
        window.location.href = '/search?q=' + encodeURIComponent(val) + '&type=product';
        return;
      }
    }

    scrollToCatalog('all');
    renderCatalog();
  }
}

function getCatalogData() {
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS) && window.SHOPIFY_LIVE_PRODUCTS.length > 0) {
    return window.SHOPIFY_LIVE_PRODUCTS;
  }
  return typeof CATALOG_BOOKS !== 'undefined' ? CATALOG_BOOKS : [];
}

function handleBookAction(bookId, bookUrl) {
  if (bookUrl && typeof bookUrl === 'string' && bookUrl.startsWith('/products/')) {
    window.location.href = bookUrl;
    return;
  }
  openOverviewModal(bookId);
}

function renderCatalog() {
  const container = document.getElementById('catalogGridContainer');
  if (!container) return;

  const catalogSource = getCatalogData();

  const filtered = catalogSource.filter(function(book) {
    const bTags = Array.isArray(book.tags) ? book.tags : (typeof book.tags === 'string' ? book.tags.split(',') : []);
    const matchesCat = currentCatalogCategory === 'all' || 
      bTags.some(function(t) { return t.trim().toLowerCase() === currentCatalogCategory; }) ||
      (book.type && book.type.toLowerCase().includes(currentCatalogCategory));
    const matchesQuery = !currentCatalogQuery || 
      book.title.toLowerCase().includes(currentCatalogQuery) || 
      (book.author && book.author.toLowerCase().includes(currentCatalogQuery));
    return matchesCat && matchesQuery;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px; background: #FFFFFF; border-radius: 12px; border: 1px dashed #CBD5E1;">
        <i data-lucide="search-x" style="width: 36px; height: 36px; color: #94A3B8; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 18px; color: #0F172A; margin-bottom: 6px;">No books found</h4>
        <p style="font-size: 13px; color: #64748B;">Try adjusting your search terms or category filter.</p>
        <a href="/collections/all" style="display: inline-block; margin-top: 14px; font-size: 13px; font-weight: 700; color: #B45309; text-decoration: underline;">Search across all 5,500+ books on the catalog page &rarr;</a>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  container.innerHTML = filtered.map(function(book) {
    const cover = getAssetUrl(book.coverUrl || book.cover);
    return `
      <div class="catalog-card">
        <div class="catalog-thumb" onclick="handleBookAction('${book.id}', '${book.url || ''}')" style="${book.url ? 'cursor: pointer;' : ''}">
          <img referrerpolicy="no-referrer" src="${cover}" alt="${book.title}" loading="lazy" />
        </div>
        <div style="font-size: 10.5px; font-weight: 700; color: #B45309; text-transform: uppercase; margin-bottom: 4px;">
          ${book.discount || 'IN STOCK'}
        </div>
        <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 15px; font-weight: 700; color: #0F172A; line-height: 1.3; margin-bottom: 4px; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
          ${book.url ? `<a href="${book.url}" style="color: inherit; text-decoration: none;">${book.title}</a>` : book.title}
        </h3>
        <div style="font-size: 12px; color: #64748B; margin-bottom: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
          ${book.author}
        </div>
        <div style="display: flex; align-items: baseline; gap: 8px; margin-top: auto; margin-bottom: 14px;">
          <span style="font-size: 18px; font-weight: 800; color: #0F172A;">${book.price}</span>
          ${book.oldPrice ? `<span style="font-size: 12px; text-decoration: line-through; color: #94A3B8;">${book.oldPrice}</span>` : ''}
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
          <button type="button" class="btn-overview" onclick="openOverviewModal('${book.id}')">
            <i data-lucide="book-open" style="width: 14px; height: 14px;"></i> Overview
          </button>
          <button type="button" class="btn-add-cart" onclick="addToCart('${book.id}')">
            <i data-lucide="shopping-bag" style="width: 14px; height: 14px;"></i> Add
          </button>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 5. UNIVERSAL MINI OVERVIEW MODAL ---
function findBookMetadata(arg) {
  if (!arg) return null;
  if (typeof arg === 'object' && arg.title) {
    const rawPrice = arg.price ? String(arg.price).replace(/[^0-9.]/g, '') : '299.00';
    const rawMrp = arg.oldPrice ? String(arg.oldPrice).replace(/[^0-9.]/g, '') : (Number(rawPrice) * 1.3).toFixed(2);
    return {
      id: arg.id || '',
      title: arg.title,
      author: arg.author || 'Renowned Author',
      price: rawPrice,
      mrp: rawMrp,
      discount: arg.discount || '25% OFF',
      cover: arg.coverUrl || arg.cover || '',
      lang: 'Hindi / Hindustani',
      binding: arg.format || 'Paperback',
      pages: arg.pages || '320p',
      pub: arg.publisher || arg.author || 'Lokbharti / Rajkamal',
      dispatch: 'Same-Day Dispatch from Prayagraj Hub',
      overview: arg.blurb || arg.description || arg.quote || 'An essential literary work published and archived by Indigo Books India.',
      highlights: [
        '100% Authentic Publisher Edition guaranteed',
        'Direct dispatch from Prayagraj literary warehouse',
        'Eligible for Cash on Delivery (COD) & WhatsApp Ordering'
      ]
    };
  }

  const idStr = String(arg);

  if (typeof MODAL_METADATA_DATABASE !== 'undefined' && MODAL_METADATA_DATABASE[idStr]) {
    return MODAL_METADATA_DATABASE[idStr];
  }

  // Check PODIUM_BOOKS
  if (typeof PODIUM_BOOKS !== 'undefined') {
    const b = PODIUM_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  // Check REKHTA_BOOKS
  if (typeof REKHTA_BOOKS !== 'undefined') {
    const b = REKHTA_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  // Check VAULT_BOOKS
  if (typeof VAULT_BOOKS !== 'undefined') {
    for (const cat in VAULT_BOOKS) {
      const b = VAULT_BOOKS[cat].find(function(x) { return String(x.id) === idStr; });
      if (b) return findBookMetadata(b);
    }
  }

  // Check live products / catalog
  if (typeof window !== 'undefined' && Array.isArray(window.SHOPIFY_LIVE_PRODUCTS)) {
    const b = window.SHOPIFY_LIVE_PRODUCTS.find(function(x) {
      return String(x.id) === idStr || String(x.variantId) === idStr || x.handle === idStr;
    });
    if (b) return findBookMetadata(b);
  }

  if (typeof CATALOG_BOOKS !== 'undefined') {
    const b = CATALOG_BOOKS.find(function(x) { return String(x.id) === idStr; });
    if (b) return findBookMetadata(b);
  }

  if (typeof MODAL_METADATA_DATABASE !== 'undefined') {
    const keys = Object.keys(MODAL_METADATA_DATABASE);
    if (keys.length > 0) return MODAL_METADATA_DATABASE[keys[0]];
  }

  return null;
}

function openOverviewModal(bookArg) {
  const book = findBookMetadata(bookArg);
  if (!book) return;

  const modal = document.getElementById('overviewModalOverlay');
  if (!modal) return;

  const coverEl = document.getElementById('modalCover');
  if (coverEl) {
    coverEl.src = getAssetUrl(book.cover);
    coverEl.alt = book.title;
  }
  const titleEl = document.getElementById('modalTitle');
  if (titleEl) titleEl.textContent = book.title;
  const authorEl = document.getElementById('modalAuthor');
  if (authorEl) authorEl.textContent = book.author;
  const discEl = document.getElementById('modalDiscount');
  if (discEl) discEl.textContent = book.discount || '25% OFF';
  const priceEl = document.getElementById('modalPrice');
  if (priceEl) priceEl.textContent = '₹' + Number(book.price).toFixed(2);
  const mrpEl = document.getElementById('modalMRP');
  if (mrpEl) mrpEl.textContent = '₹' + Number(book.mrp).toFixed(2);

  const langEl = document.getElementById('modalLang');
  if (langEl) langEl.textContent = book.lang || 'Hindi';
  const bindEl = document.getElementById('modalBinding');
  if (bindEl) bindEl.textContent = book.binding || 'Paperback';
  const pagesEl = document.getElementById('modalPages');
  if (pagesEl) pagesEl.textContent = book.pages || '320p';
  const pubEl = document.getElementById('modalPublisher');
  if (pubEl) pubEl.textContent = book.pub || 'Lokbharti / Rajkamal';
  const dispEl = document.getElementById('modalDispatch');
  if (dispEl) dispEl.textContent = book.dispatch || 'Same-Day Prayagraj';

  const overviewEl = document.getElementById('modalOverviewText');
  if (overviewEl) overviewEl.textContent = book.overview || '';

  const highlightsContainer = document.getElementById('modalHighlightsList');
  if (highlightsContainer && book.highlights) {
    highlightsContainer.innerHTML = book.highlights.map(function(h) {
      return `
        <li style="display: flex; align-items: flex-start; gap: 8px; font-size: 12.5px; color: #334155;">
          <i data-lucide="check" style="width: 16px; height: 16px; color: #16A34A; flex-shrink: 0; margin-top: 2px;"></i>
          <span>${h}</span>
        </li>
      `;
    }).join('');
  }

  // Update modal actions
  const addBtn = document.getElementById('modalAddToCartBtn');
  if (addBtn) {
    addBtn.onclick = function() {
      addToCart(book.id || bookArg);
      closeOverviewModal();
    };
  }

  const waBtn = document.getElementById('modalWhatsAppBtn');
  if (waBtn) {
    const lines = [
      "Hello Indigo Books India!",
      "I would like to order this book:",
      "*Book:* " + book.title,
      "*Author:* " + book.author,
      "*Price:* ₹" + Number(book.price).toFixed(2),
      "*Format:* " + (book.binding || 'Paperback'),
      "Please confirm availability and share COD / Payment details!"
    ];
    const msg = lines.join("\n");
    waBtn.href = "https://wa.me/918933063306?text=" + encodeURIComponent(msg);
  }

  modal.classList.add('is-active');
  document.body.style.overflow = 'hidden';

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function closeOverviewModal() {
  const modal = document.getElementById('overviewModalOverlay');
  if (modal) modal.classList.remove('is-active');
  document.body.style.overflow = '';
}


// --- 6. SHOPPING CART DRAWER ---
let cart = [];

function addShopifyVariantToCart(variantId, qty) {
  fetch('/cart/add.js', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id: variantId, quantity: qty || 1 })
  })
  .then(function(res) { return res.json(); })
  .then(function(item) {
    addToCart(item.id || variantId);
  })
  .catch(function(err) {
    addToCart(variantId);
  });
}

function addToCart(bookId) {
  let meta = findBookMetadata(bookId);
  if (!meta) {
    meta = {
      id: bookId,
      title: 'Selected Book',
      author: 'Indigo Books India',
      price: '299.00',
      cover: 'assets/hero-godan.jpg'
    };
  }

  const idStr = String(bookId);
  const existing = cart.find(function(item) { return String(item.id) === idStr; });

  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({
      id: idStr,
      title: meta.title,
      author: meta.author,
      price: parseFloat(meta.price) || 299.00,
      cover: getAssetUrl(meta.cover),
      qty: 1
    });
  }

  updateCartUI();
  toggleCartDrawer(true);
}

function updateCartQty(bookId, delta) {
  const idStr = String(bookId);
  const item = cart.find(function(i) { return String(i.id) === idStr; });
  if (!item) return;

  item.qty += delta;
  if (item.qty <= 0) {
    cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  }
  updateCartUI();
}

function removeFromCart(bookId) {
  const idStr = String(bookId);
  cart = cart.filter(function(i) { return String(i.id) !== idStr; });
  updateCartUI();
}

function updateCartUI() {
  const countEl = document.getElementById('cartTotalCount');
  const priceEl = document.getElementById('cartTotalPrice');
  const badgeEl = document.getElementById('cartDrawerBadge');
  const subtotalEl = document.getElementById('cartDrawerSubtotal');
  const list = document.getElementById('cartDrawerItemsList');

  const totalCount = cart.reduce(function(sum, item) { return sum + item.qty; }, 0);
  const totalPrice = cart.reduce(function(sum, item) { return sum + (item.price * item.qty); }, 0);

  if (countEl) countEl.textContent = totalCount;
  if (priceEl) priceEl.textContent = '₹' + totalPrice.toFixed(2);
  if (badgeEl) badgeEl.textContent = totalCount;
  if (subtotalEl) subtotalEl.textContent = '₹' + totalPrice.toFixed(2);

  if (!list) return;

  if (cart.length === 0) {
    list.innerHTML = `
      <div style="text-align: center; padding: 48px 16px; color: #64748B;">
        <i data-lucide="shopping-bag" style="width: 48px; height: 48px; color: #CBD5E1; margin: 0 auto 12px;"></i>
        <h4 style="font-family: 'Merriweather', serif; font-size: 16px; color: #0F172A; margin-bottom: 4px;">Your cart is empty</h4>
        <p style="font-size: 13px;">Add some books to read!</p>
      </div>
    `;
    if (typeof lucide !== 'undefined') lucide.createIcons();
    return;
  }

  list.innerHTML = cart.map(function(item) {
    return `
      <div style="display: flex; gap: 14px; padding-bottom: 14px; border-bottom: 1px solid #F1F5F9;">
        <div style="width: 60px; height: 85px; border-radius: 4px; overflow: hidden; flex-shrink: 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
          <img referrerpolicy="no-referrer" src="${getAssetUrl(item.cover)}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;" />
        </div>
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h4 style="font-family: 'Merriweather', Georgia, serif; font-size: 14px; font-weight: 700; color: #0F172A; line-height: 1.25; margin-bottom: 2px;">
              ${item.title}
            </h4>
            <div style="font-size: 11px; color: #64748B;">${item.author}</div>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 8px;">
            <div style="font-size: 14px; font-weight: 800; color: #0F172A;">
              ₹${(item.price * item.qty).toFixed(2)}
            </div>
            <div style="display: flex; align-items: center; gap: 8px; background: #F1F5F9; border-radius: 6px; padding: 2px 8px;">
              <button type="button" onclick="updateCartQty('${item.id}', -1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">-</button>
              <span style="font-size: 12px; font-weight: 700; color: #0F172A;">${item.qty}</span>
              <button type="button" onclick="updateCartQty('${item.id}', 1)" style="border: none; background: none; cursor: pointer; font-size: 14px; font-weight: bold; color: #475569;">+</button>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');

  if (typeof lucide !== 'undefined') lucide.createIcons();
}

function toggleCartDrawer(forceOpen) {
  const drawer = document.getElementById('cartDrawerOverlay');
  if (!drawer) return;

  if (forceOpen === true) {
    drawer.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  } else if (forceOpen === false) {
    drawer.classList.remove('is-open');
    document.body.style.overflow = '';
  } else {
    drawer.classList.toggle('is-open');
    document.body.style.overflow = drawer.classList.contains('is-open') ? 'hidden' : '';
  }
}

function checkoutWhatsApp() {
  if (cart.length === 0) {
    alert("Your shopping cart is empty!");
    return;
  }

  const lines = [
    "Hello Indigo Books India (Prayagraj)!",
    "I want to place an order via Cash on Delivery (COD):",
    ""
  ];
  let total = 0;

  cart.forEach(function(item, index) {
    const lineTotal = item.price * item.qty;
    total += lineTotal;
    lines.push((index + 1) + ". *" + item.title + "* x" + item.qty + " — ₹" + lineTotal.toFixed(2));
  });

  lines.push("");
  lines.push("*Cart Subtotal:* ₹" + total.toFixed(2));
  lines.push("*Dispatch Location:* Prayagraj Hub");
  lines.push("");
  lines.push("Please confirm delivery time & COD address!");

  const text = lines.join("\n");
  window.open("https://wa.me/918933063306?text=" + encodeURIComponent(text), '_blank');
}


// --- 7. MEMBER LOGIN MODAL ---
function toggleLoginModal() {
  const modal = document.getElementById('loginModalOverlay');
  if (!modal) return;
  modal.classList.toggle('is-active');
  document.body.style.overflow = modal.classList.contains('is-active') ? 'hidden' : '';
  if (typeof lucide !== 'undefined') lucide.createIcons();
}


// --- 8. SMOOTH SCROLL & FILTER HELPERS ---
function scrollToCatalog(category) {
  filterCatalog(category);
  const el = document.getElementById('shop-all-catalog');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function scrollToVault(tabKey) {
  switchVaultTab(tabKey);
  const el = document.getElementById('law-academic-vault');
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}


// --- 9. DOM INITIALIZATION ---
function initIndigoStore() {
  try { runVideoIntroSpotlightTour(); } catch(e) { console.warn("Spotlight:", e); }
  try { selectPodiumBook(0); } catch(e) { console.warn("Podium:", e); }
  try { switchPoet('all'); } catch(e) { console.warn("Poet:", e); }
  try { switchVaultTab('law'); } catch(e) { console.warn("Vault:", e); }
  try { renderCatalog(); } catch(e) { console.warn("Catalog:", e); }
  try { updateCartUI(); } catch(e) { console.warn("Cart:", e); }

  if (typeof lucide !== 'undefined') {
    try { lucide.createIcons(); } catch(e) {}
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initIndigoStore);
} else {
  initIndigoStore();
}

window.addEventListener('load', function() {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});