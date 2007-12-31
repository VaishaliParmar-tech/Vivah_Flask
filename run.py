from app import app, init_db

if __name__ == '__main__':
    init_db()
    print("\n" + "="*55)
    print("  VIVAH SAREES — http://127.0.0.1:5000")
    print("  Admin: http://127.0.0.1:5000/admin/login")
    print("  Login: vivah_admin  /  Vivah@2026")
    print("="*55 + "\n")
    app.run(debug=True)
