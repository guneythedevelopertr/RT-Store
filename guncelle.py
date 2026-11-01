import os
import subprocess

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"[+ OLUŞTURULDU] {path}")

def main():
    root = os.getcwd()
    print(f"=== RT Store Microsoft Store Dönüşümü Başlatılıyor: {root} ===")

    # 1. API CONFIG (assets/js/config.js)
    config_js = """
window.RT_CONFIG = {
    API_URL: 'https://sauciness-aerobics-boxcar.ngrok-free.dev/api'
};
"""
    create_file(os.path.join(root, "assets", "js", "config.js"), config_js)

    # 2. MICROSOFT STORE FLUENT DESIGN CSS (assets/css/style.css)
    style_css = """
:root {
    --bg-main: #f3f3f3;
    --card-bg: rgba(255, 255, 255, 0.75);
    --card-border: rgba(0, 0, 0, 0.08);
    --accent-color: #0067b8;
    --accent-hover: #005da6;
    --text-primary: #1b1b1b;
    --text-secondary: #5d5d5d;
    --sidebar-bg: rgba(243, 243, 243, 0.85);
    --radius: 12px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI Variable Display', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    user-select: none;
}

body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    display: flex;
    height: 100vh;
    overflow: hidden;
}

/* Sidebar */
.sidebar {
    width: 240px;
    background: var(--sidebar-bg);
    backdrop-filter: blur(20px);
    border-right: 1px solid var(--card-border);
    display: flex;
    flex-direction: column;
    padding: 20px 12px;
    justify-content: space-between;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 12px 20px 12px;
    font-size: 18px;
    font-weight: 600;
}

.brand-icon {
    width: 32px;
    height: 32px;
    background: var(--accent-color);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
}

.nav-links {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    color: var(--text-primary);
    text-decoration: none;
    border-radius: 8px;
    font-size: 14px;
    transition: all 0.2s ease;
}

.nav-item:hover {
    background: rgba(0, 0, 0, 0.05);
}

.nav-item.active {
    background: rgba(0, 0, 0, 0.07);
    font-weight: 600;
    border-left: 3px solid var(--accent-color);
}

/* Main Content Area */
.main-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
}

.top-bar {
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 32px;
    background: rgba(243, 243, 243, 0.5);
    backdrop-filter: blur(10px);
}

.search-bar {
    width: 360px;
    background: #ffffff;
    border: 1px solid var(--card-border);
    border-radius: 20px;
    padding: 8px 16px;
    font-size: 13px;
    outline: none;
    transition: 0.2s;
}

.search-bar:focus {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 2px rgba(0, 103, 184, 0.2);
}

.auth-buttons {
    display: flex;
    gap: 10px;
}

.btn {
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    text-decoration: none;
    cursor: pointer;
    border: none;
    transition: 0.2s;
}

.btn-primary {
    background: var(--accent-color);
    color: white;
}

.btn-primary:hover {
    background: var(--accent-hover);
}

.btn-secondary {
    background: rgba(0, 0, 0, 0.05);
    color: var(--text-primary);
    border: 1px solid var(--card-border);
}

.btn-secondary:hover {
    background: rgba(0, 0, 0, 0.1);
}

.content {
    padding: 32px;
    flex: 1;
}

/* Auth Cards (Fluent Glass) */
.auth-container {
    max-width: 420px;
    margin: 40px auto;
    background: var(--card-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 32px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
}

.auth-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 8px;
}

.auth-subtitle {
    font-size: 13px;
    color: var(--text-secondary);
    margin-bottom: 24px;
}

.form-group {
    margin-bottom: 18px;
}

.form-group label {
    display: block;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 6px;
}

.form-control {
    width: 100%;
    padding: 10px 12px;
    background: rgba(255, 255, 255, 0.8);
    border: 1px solid var(--card-border);
    border-bottom: 2px solid #8a8a8a;
    border-radius: 4px;
    font-size: 14px;
    outline: none;
    transition: all 0.2s;
}

.form-control:focus {
    border-bottom-color: var(--accent-color);
    background: #ffffff;
}

/* App Grid */
.hero-banner {
    width: 100%;
    height: 220px;
    background: linear-gradient(135deg, #005da6, #00bcf2);
    border-radius: var(--radius);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    margin-bottom: 32px;
}

.hero-banner h2 { font-size: 28px; margin-bottom: 8px; }
.hero-banner p { opacity: 0.9; font-size: 14px; }

.section-title { font-size: 18px; font-weight: 600; margin-bottom: 16px; }

.grid-apps {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.app-card {
    background: var(--card-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: 0.2s ease;
}

.app-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
}

.app-icon {
    width: 64px;
    height: 64px;
    border-radius: 12px;
    background: #e1e1e1;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}

.app-name { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.app-cat { font-size: 12px; color: var(--text-secondary); margin-bottom: 12px; }

/* Status Widget */
#server-status {
    position: fixed;
    bottom: 16px;
    right: 16px;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border: 1px solid var(--card-border);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    gap: 8px;
}
.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #ff3b30;
}
.status-dot.online { background: #34c759; }
"""
    create_file(os.path.join(root, "assets", "css", "style.css"), style_css)

    # 3. BACKEND SERVER (server/server.js)
    server_js = """
const express = require('express');
const cors = require('cors');
const ngrok = require('@ngrok/ngrok');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

const users = [];

app.get('/api/health', (req, res) => {
    res.json({ status: 'success', message: 'RT Store API Aktif' });
});

app.post('/api/register', (req, res) => {
    const { username, email, password } = req.body;
    if (!username || !email || !password) {
        return res.status(400).json({ status: 'error', message: 'Tüm alanları doldurun.' });
    }
    const exists = users.find(u => u.email === email || u.username === username);
    if (exists) {
        return res.status(400).json({ status: 'error', message: 'Kullanıcı adı veya e-posta zaten kullanımda.' });
    }
    users.push({ username, email, password });
    console.log('[KAYIT]:', username);
    res.json({ status: 'success', message: 'Kayıt başarılı! Yönlendiriliyorsunuz.' });
});

app.post('/api/login', (req, res) => {
    const { usernameOrEmail, password } = req.body;
    const user = users.find(u => (u.username === usernameOrEmail || u.email === usernameOrEmail) && u.password === password);
    if (!user) {
        return res.status(401).json({ status: 'error', message: 'Kullanıcı adı/e-posta veya şifre hatalı.' });
    }
    console.log('[GİRİŞ]:', user.username);
    res.json({ status: 'success', message: 'Giriş başarılı!', username: user.username });
});

app.listen(PORT, async () => {
    console.log('RT Store Backend Portu: ' + PORT);
    try {
        await ngrok.authtoken('3LUnB99ES0TT0R5QPfokIxlnz2n_7beKyZMdHP8sFziwJQJSj');
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'sauciness-aerobics-boxcar.ngrok-free.dev'
        });
        console.log('📱 Ngrok Tüneli Canlıda: ' + listener.url());
    } catch (err) {
        console.error('Ngrok Tünel Hatası:', err.message);
    }
});
"""
    create_file(os.path.join(root, "server", "server.js"), server_js)

    # 4. INDEX.HTML (Karşılama / Mağaza Ana Sayfası)
    index_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RT Store — Microsoft Store</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="sidebar">
        <div>
            <div class="brand">
                <div class="brand-icon">RT</div>
                <span>RT Store</span>
            </div>
            <nav class="nav-links">
                <a href="index.html" class="nav-item active">🏠 Ana Sayfa</a>
                <a href="#" class="nav-item">🎮 Oyunlar</a>
                <a href="#" class="nav-item">📱 Uygulamalar</a>
            </nav>
        </div>
        <div id="user-display" style="font-size:12px; color:var(--text-secondary); padding:0 12px;">Giriş Yapılmadı</div>
    </div>

    <div class="main-wrapper">
        <div class="top-bar">
            <input type="text" class="search-bar" placeholder="Uygulamalar, oyunlar ve daha fazlasını arayın...">
            <div class="auth-buttons" id="auth-nav">
                <a href="login.html" class="btn btn-secondary">Giriş Yap</a>
                <a href="register.html" class="btn btn-primary">Kayıt Ol</a>
            </div>
        </div>

        <div class="content">
            <div class="hero-banner">
                <h2>RT Store'a Hoş Geldiniz</h2>
                <p>En yeni yazılımlar, optimize araçlar ve geliştirici paketleri burada.</p>
            </div>

            <div class="section-title">Öne Çıkan Uygulamalar</div>
            <div class="grid-apps">
                <div class="app-card">
                    <div class="app-icon">⚡</div>
                    <div class="app-name">Ping Optimizer v6</div>
                    <div class="app-cat">Ağ & Araçlar</div>
                    <button class="btn btn-primary" style="width:100%;">İndir</button>
                </div>
                <div class="app-card">
                    <div class="app-icon">🤖</div>
                    <div class="app-name">RT AI Assistant</div>
                    <div class="app-cat">Yapay Zekâ</div>
                    <button class="btn btn-primary" style="width:100%;">İndir</button>
                </div>
                <div class="app-card">
                    <div class="app-icon">🛡️</div>
                    <div class="app-name">RT NetGuard</div>
                    <div class="app-cat">Güvenlik</div>
                    <button class="btn btn-primary" style="width:100%;">İndir</button>
                </div>
            </div>
        </div>
    </div>

    <div id="server-status">
        <div class="status-dot" id="status-dot"></div>
        <span id="status-text">Bağlanıyor...</span>
    </div>

    <script src="assets/js/config.js"></script>
    <script>
        fetch(window.RT_CONFIG.API_URL + '/health')
            .then(res => res.json())
            .then(() => {
                document.getElementById('status-dot').classList.add('online');
                document.getElementById('status-text').innerText = 'Sunucu Aktif';
            })
            .catch(() => {
                document.getElementById('status-text').innerText = 'Sunucu Çevrimdışı';
            });

        const loggedUser = localStorage.getItem('rt_user');
        if(loggedUser) {
            document.getElementById('user-display').innerText = '👤 ' + loggedUser;
            document.getElementById('auth-nav').innerHTML = `<button onclick="logout()" class="btn btn-secondary">Çıkış Yap</button>`;
        }

        function logout() {
            localStorage.removeItem('rt_user');
            location.reload();
        }
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "index.html"), index_html)

    # 5. REGISTER.HTML (Kayıt Olma Sayfası)
    register_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Hesap Oluştur</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body style="align-items:center; justify-content:center;">

    <div class="auth-container">
        <div class="brand-icon" style="margin-bottom:16px;">RT</div>
        <div class="auth-title">Hesap Oluştur</div>
        <div class="auth-subtitle">RT Store hizmetlerine erişmek için kayıt olun</div>

        <form id="registerForm">
            <div class="form-group">
                <label>Kullanıcı Adı</label>
                <input type="text" id="username" class="form-control" required placeholder="ör: guneythedeveloper">
            </div>
            <div class="form-group">
                <label>E-posta Adresi</label>
                <input type="email" id="email" class="form-control" required placeholder="ornek@gmail.com">
            </div>
            <div class="form-group">
                <label>Şifre</label>
                <input type="password" id="password" class="form-control" required placeholder="••••••••">
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%; margin-top:10px;">Kayıt Ol</button>
        </form>
        
        <div style="margin-top:20px; font-size:13px; text-align:center;">
            Zaten hesabınız var mı? <a href="login.html" style="color:var(--accent-color); text-decoration:none; font-weight:600;">Giriş Yapın</a>
        </div>
    </div>

    <script src="assets/js/config.js"></script>
    <script>
        document.getElementById('registerForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const res = await fetch(window.RT_CONFIG.API_URL + '/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const data = await res.json();
                if(res.ok) {
                    alert(data.message);
                    window.location.href = 'login.html';
                } else {
                    alert('Hata: ' + data.message);
                }
            } catch(err) {
                alert('Sunucuya ulaşılamadı! Lütfen sunucunuzun açık olduğunu kontrol edin.');
            }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "register.html"), register_html)

    # 6. LOGIN.HTML (Giriş Yapma Sayfası)
    login_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Giriş Yap</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body style="align-items:center; justify-content:center;">

    <div class="auth-container">
        <div class="brand-icon" style="margin-bottom:16px;">RT</div>
        <div class="auth-title">Oturum Aç</div>
        <div class="auth-subtitle">RT Store hesabınızla devam edin</div>

        <form id="loginForm">
            <div class="form-group">
                <label>Kullanıcı Adı veya E-posta</label>
                <input type="text" id="usernameOrEmail" class="form-control" required placeholder="Kullanıcı adı ya da e-posta">
            </div>
            <div class="form-group">
                <label>Şifre</label>
                <input type="password" id="password" class="form-control" required placeholder="••••••••">
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%; margin-top:10px;">Giriş Yap</button>
        </form>
        
        <div style="margin-top:20px; font-size:13px; text-align:center;">
            Hesabınız yok mu? <a href="register.html" style="color:var(--accent-color); text-decoration:none; font-weight:600;">Hemen Kayıt Olun</a>
        </div>
    </div>

    <script src="assets/js/config.js"></script>
    <script>
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const usernameOrEmail = document.getElementById('usernameOrEmail').value;
            const password = document.getElementById('password').value;

            try {
                const res = await fetch(window.RT_CONFIG.API_URL + '/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ usernameOrEmail, password })
                });
                const data = await res.json();
                if(res.ok) {
                    localStorage.setItem('rt_user', data.username);
                    alert(data.message);
                    window.location.href = 'index.html';
                } else {
                    alert('Hata: ' + data.message);
                }
            } catch(err) {
                alert('Sunucuya ulaşılamadı! Lütfen sunucunuzun açık olduğunu kontrol edin.');
            }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "login.html"), login_html)

    print("\n[+] Tüm Microsoft Store arayüz ve sunucu dosyaları baştan oluşturuldu.")

    # 7. GIT PUSH
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "UI: Microsoft Store Fluent Design entegrasyonu tamamlandi"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[SUCCESS] Kodlar GitHub Pages'e canlıya gönderildi!")
    except Exception as e:
        print(f"[HATA] Git gönderiminde sorun oluştu: {e}")

if __name__ == "__main__":
    main()