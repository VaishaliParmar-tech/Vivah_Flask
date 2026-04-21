from app import app, db, Category

with app.app_context():
    updates = {
        'kanjivaram-sarees': 'categories/kanjivaram_1.jpeg',
        'leheriya-sarees':   'categories/leheriya_3.jpeg',
        'silk-sarees':       'categories/silk_1.jpeg',
    }
    for slug, img in updates.items():
        cat = Category.query.filter_by(slug=slug).first()
        if cat:
            cat.image = img
            print(f"✅ Updated: {cat.name} → {img}")
        else:
            print(f"❌ Not found: {slug}")
    db.session.commit()
    print("Done!")