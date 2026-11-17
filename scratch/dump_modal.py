from store_modals_and_search import SEARCH_AND_MODALS_HTML

start = SEARCH_AND_MODALS_HTML.find('expressPhoneCheckoutModal')
end = SEARCH_AND_MODALS_HTML.find('Order Confirmation Modal')
print(SEARCH_AND_MODALS_HTML[start-10:end])
