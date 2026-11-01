import os
import subprocess

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OLUŞTURULDU] {path}")

def main():
    root = os.getcwd()
    print(f"Çalışma dizini: {root}")

    # 1. assets/js/config.js
    config_content = """window.RT_CONFIG = {
    API_URL: 'https://sauciness-aerobics-boxcar.ngrok-free.dev/api'
};
"""
    create_file(os.path.join(root, "assets", "js", "config.js"), config_content)

    # 2. server/server.js
    server_code = """const express = require('express');
const cors = require('cors');
const ngrok = require('@ngrok/ngrok');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

const users = [];

app.get('/api/health', (req, res) => {
    res.json({ status: 'success', message: 'RT Store API aktif ve kararlı.' });
});

app.post('/api/register', (req, res) => {
    const { username, email, password } = req.body;
    if (!username || !email || !password) {
        return res.status(400).json({ status: 'error', message: 'Tüm alanların doldurulması zorunludur.' });
    }
    const existingUser = users.find(u => u.email === email || u.username === username);
    if (existingUser) {
        return res.status(400).json({ status: 'error', message: 'Bu kullanıcı adı veya e-posta zaten kayıtlı.' });
    }
    users.push({ username, email, password });
    console.log('Yeni kullanıcı kaydedildi:', username);
    res.json({ status: 'success', message: 'Kayıt başarılı.', token: 'mock-token-' + username });
});

app.post('/api/login', (req, res) => {
    const { usernameOrEmail, password } = req.body;
    const user = users.find(u => (u.username === usernameOrEmail || u.email === usernameOrEmail) && u.password === password);
    if (!user) {
        return res.status(401).json({ status: 'error', message: 'Geçersiz kullanıcı adı veya şifre.' });
    }
    console.log('Kullanıcı giriş yaptı:', user.username);
    res.json({ status: 'success', message: 'Giriş başarılı.', token: 'mock-token-' + user.username });
});

app.listen(PORT, async () => {
    console.log('RT Store sunucusu ' + PORT + ' portunda çalışıyor.');
    try {
        await ngrok.authtoken('3LUnB99ES0TT0R5QPfokIxlnz2n_7beKyZMdHP8sFziwJQJSj');
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'sauciness-aerobics-boxcar.ngrok-free.dev'
        });
        console.log('Ngrok tüneli aktif: ' + listener.url());
    } catch (err) {
        console.error('Ngrok tüneli başlatılamadı:', err.message);
    }
});
"""
    create_file(os.path.join(root, "server", "server.js"), server_code)

    # 3. index.html (Ana Karşılama ve Yönlendirme Sayfası)
    index_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Ana Sayfa</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container" style="text-align:center; margin-top:50px;">
        <h1>RT Store Mağazasına Hoş Geldiniz</h1>
        <p>Lütfen devam etmek için bir işlem seçin:</p>
        <div style="margin-top:20px;">
            <a href="login.html" class="btn" style="padding:10px 20px; background:#007bff; color:#fff; text-decoration:none; border-radius:5px; margin-right:10px;">Giriş Yap</a>
            <a href="register.html" class="btn" style="padding:10px 20px; background:#28a745; color:#fff; text-decoration:none; border-radius:5px;">Kayıt Ol</a>
        </div>
    </div>
    <div id="server-status" style="position:fixed; bottom:10px; right:10px; padding:5px 10px; font-size:12px; background:#333; color:#fff; border-radius:4px;">Sunucu Bağlantısı Kontrol Ediliyor...</div>
    <script src="assets/js/config.js"></script>
    <script>
        fetch(window.RT_CONFIG.API_URL + '/health')
            .then(res => res.json())
            .then(data => {
                const el = document.getElementById('server-status');
                el.style.background = 'green';
                el.innerText = 'Sunucu Bağlı';
            })
            .catch(() => {
                const el = document.getElementById('server-status');
                el.style.background = 'red';
                el.innerText = 'Sunucu Bağlantı Hatası';
            });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "index.html"), index_html)

    # 4. register.html (Kayıt Olma Sayfası)
    register_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Kayıt Ol</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container" style="max-width:400px; margin:50px auto; padding:20px; border:1px solid #ccc; border-radius:5px;">
        <h2>Kayıt Ol</h2>
        <form id="register-form">
            <div style="margin-bottom:15px;">
                <label>Kullanıcı Adı</label><br>
                <input type="text" id="username" required style="width:100%; padding:8px; margin-top:5px;">
            </div>
            <div style="margin-bottom:15px;">
                <label>E-posta Adresi</label><br>
                <input type="email" id="email" required style="width:100%; padding:8px; margin-top:5px;">
            </div>
            <div style="margin-bottom:15px;">
                <label>Şifre (8-16 Karakter)</label><br>
                <input type="password" id="password" required style="width:100%; padding:8px; margin-top:5px;">
            </div>
            <button type="submit" style="width:100%; padding:10px; background:#28a745; color:#fff; border:none; border-radius:5px; cursor:pointer;">Kayıt Ol</button>
        </form>
        <p style="margin-top:15px; text-align:center;">Zaten hesabın var mı? <a href="login.html">Giriş Yap</a></p>
    </div>
    <script src="assets/js/config.js"></script>
    <script>
        document.getElementById('register-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch(window.RT_CONFIG.API_URL + '/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const data = await response.json();
                if (response.ok) {
                    alert('Kayıt başarılı! Giriş sayfasına yönlendiriliyorsunuz.');
                    window.location.href = 'login.html';
                } else {
                    alert('Hata: ' + data.message);
                }
            } catch (err) {
                alert('Sunucu bağlantı hatası.');
            }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "register.html"), register_html)

    # 5. login.html (Giriş Yapma Sayfası - Sadece kullanıcı adı/şifre)
    login_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Giriş Yap</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container" style="max-width:400px; margin:50px auto; padding:20px; border:1px solid #ccc; border-radius:5px;">
        <h2>Giriş Yap</h2>
        <form id="login-form">
            <div style="margin-bottom:15px;">
                <label>Kullanıcı Adı veya E-posta</label><br>
                <input type="text" id="usernameOrEmail" required style="width:100%; padding:8px; margin-top:5px;">
            </div>
            <div style="margin-bottom:15px;">
                <label>Şifre</label><br>
                <input type="password" id="password" required style="width:100%; padding:8px; margin-top:5px;">
            </div>
            <button type="submit" style="width:100%; padding:10px; background:#007bff; color:#fff; border:none; border-radius:5px; cursor:pointer;">Giriş Yap</button>
        </form>
        <p style="margin-top:15px; text-align:center;">Hesabın yok mu? <a href="register.html">Kayıt Ol</a></p>
    </div>
    <script src="assets/js/config.js"></script>
    <script>
        document.getElementById('login-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const usernameOrEmail = document.getElementById('usernameOrEmail').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch(window.RT_CONFIG.API_URL + '/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ usernameOrEmail, password })
                });
                const data = await response.json();
                if (response.ok) {
                    alert('Giriş başarılı! Mağazaya yönlendiriliyorsunuz.');
                    window.location.href = 'index.html';
                } else {
                    alert('Hata: ' + data.message);
                }
            } catch (err) {
                alert('Sunucu bağlantı hatası.');
            }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "login.html"), login_html)

    print("\\n[BİLGİ] Tüm dosyalar başarıyla güncellendi.")
    
    # Git işlemleri
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Refactor: Kayit ve giris ekranlari ayrildi"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[BAŞARILI] Değişiklikler GitHub deposuna gönderildi.")
    except Exception as e:
        print(f"[UYARI] Git komutları otomatik çalıştırılamadı: {e}")

if __name__ == "__main__":
    main()