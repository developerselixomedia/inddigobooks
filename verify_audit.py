import store_data

print("PODIUM_BOOKS count:", len(store_data.PODIUM_BOOKS))
print("Sample Podium book discount:", store_data.PODIUM_BOOKS[0].get("discount"))
print("Sample Podium book oldPrice:", store_data.PODIUM_BOOKS[0].get("oldPrice"))
print("Sample Podium book rating:", store_data.PODIUM_BOOKS[0].get("rating"))

print("CATEGORY_BENTO_DATA keys:", list(store_data.CATEGORY_BENTO_DATA.keys()))
for k, v in store_data.CATEGORY_BENTO_DATA.items():
    print(f"Category '{k}': Left='{v['left']['title']}' (Price: {v['left']['price']}), Right count={len(v['right'])}")
    for rb in v['right']:
        print(f"   Right book: {rb['title']} (Price: {rb['price']})")

print("MODAL_METADATA_DATABASE count:", len(store_data.MODAL_METADATA_DATABASE))

