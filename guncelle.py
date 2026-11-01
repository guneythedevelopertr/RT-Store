import os
import subprocess

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"[+ OLUŞTURULDU] {path}")

def main():
    root = os.getcwd()
    print(f"=== RT Store Düzeltme İşlemi Başlatılıyor: {root} ===")

    # 1. API CONFIG
    config_js = """
window.RT_CONFIG = {
    API_URL: 'https://sauciness-aerobics-boxcar.ngrok-free.dev/api'
};
"""
    create_file(os.path.join(root, "assets", "js", "config.js"), config_js)

    # 2. STİLLER (İkon sorunlarını çözen temiz Fluent Design CSS)
    style_css = """
:root {
    --bg-main: #f3f3f3;
    --card-bg: rgba(255, 255, 255, 0.85);
    --card-border: rgba(0, 0, 0, 0.08);
    --accent-color: #0067b8;
    --accent-hover: #005da6;
    --text-primary: #1b1b1b;
    --text-secondary: #5d5d5d;
    --sidebar-bg: rgba(243, 243, 243, 0.9);
    --radius: 12px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    user-select: none;
}

body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    display: flex;
    height: 100vh;
    overflow: hidden;
}

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
    transition: 0.2s ease;
}

.nav-item:hover { background: rgba(0, 0, 0, 0.05); }
.nav-item.active { background: rgba(0, 0, 0, 0.08); font-weight: 600; border-left: 3px solid var(--accent-color); }

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
    background: rgba(243, 243, 243, 0.6);
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
}

.auth-buttons { display: flex; gap: 10px; }

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

.btn-primary { background: var(--accent-color); color: white; }
.btn-primary:hover { background: var(--accent-hover); }
.btn-secondary { background: rgba(0, 0, 0, 0.05); color: var(--text-primary); border: 1px solid var(--card-border); }

.content { padding: 32px; flex: 1; }

.hero-banner {
    width: 100%;
    height: 200px;
    background: linear-gradient(135deg, #005da6, #00bcf2);
    border-radius: var(--radius);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    margin-bottom: 32px;
}
.hero-banner h2 { font-size: 26px; margin-bottom: 8px; }
.hero-banner p { opacity: 0.9; font-size: 14px; }

.section-title { font-size: 18px; font-weight: 600; margin-bottom: 16px; }

.grid-apps {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
}

.app-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: 0.2s;
}
.app-card:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.06); }

.app-icon {
    font-size: 32px;
    margin-bottom: 12px;
}

.app-name { font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.app-cat { font-size: 12px; color: var(--text-secondary); margin-bottom: 14px; }

.auth-container {
    max-width: 400px;
    margin: 40px auto;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 32px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
}

.form-group { margin-bottom: 16px; }
.form-group label { display: block; font-size: 12px; font-weight: 600; margin-bottom: 6px; }
.form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid var(--card-border);
    border-bottom: 2px solid #8a8a8a;
    border-radius: 4px;
    outline: none;
    background: #fff;
}
.form-control:focus { border-bottom-color: var(--accent-color); }

#server-status {
    position: fixed;
    bottom: 16px;
    right: 16px;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid var(--card-border);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 999;
}
.status-dot { width: 8px; height: 8px; border-radius: 50%; background: #ff3b30; }
.status-dot.online { background: #34c759; }
"""
    create_file(os.path.join(root, "assets", "css", "style.css"), style_css)

    # 3. SERVER
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
    res.json({ status: 'success', message: 'API Aktif' });
});

app.post('/api/register', (req, res) => {
    const { username, email, password } = req.body;
    if (!username || !email || !password) {
        return res.status(400).json({ status: 'error', message: 'Tüm alanları doldurun.' });
    }
    if (users.find(u => u.email === email || u.username === username)) {
        return res.status(400).json({ status: 'error', message: 'Bu kullanıcı adı veya e-posta zaten kayıtlı.' });
    }
    users.push({ username, email, password });
    console.log('[KAYIT BAŞARILI]:', username);
    res.json({ status: 'success', message: 'Kayıt başarılı!' });
});

app.post('/api/login', (req, res) => {
    const { usernameOrEmail, password } = req.body;
    const user = users.find(u => (u.username === usernameOrEmail || u.email === usernameOrEmail) && u.password === password);
    if (!user) {
        return res.status(401).json({ status: 'error', message: 'Hatalı kullanıcı adı veya şifre.' });
    }
    console.log('[GİRİŞ BAŞARILI]:', user.username);
    res.json({ status: 'success', message: 'Giriş başarılı!', username: user.username });
});

app.listen(PORT, async () => {
    console.log('Sunucu ' + PORT + ' portunda çalışıyor...');
    try {
        await ngrok.authtoken('3LUnB99ES0TT0R5QPfokIxlnz2n_7beKyZMdHP8sFziwJQJSj');
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'sauciness-aerobics-boxcar.ngrok-free.dev'
        });
        console.log('Tünel aktif: ' + listener.url());
    } catch (err) {
        console.error('Tünel hatası:', err.message);
    }
});
"""
    create_file(os.path.join(root, "server", "server.js"), server_js)

    # 4. INDEX.HTML
    index_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
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
            <input type="text" class="search-bar" placeholder="Mağazada ara...">
            <div class="auth-buttons" id="auth-nav">
                <a href="login.html" class="btn btn-secondary">Giriş Yap</a>
                <a href="register.html" class="btn btn-primary">Kayıt Ol</a>
            </div>
        </div>

        <div class="content">
            <div class="hero-banner">
                <h2>RT Store'a Hoş Geldiniz</h2>
                <p>En yeni araçlar ve performans yazılımları tek tıkla elinizin altında.</p>
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
                document.getElementById('status-text').innerText = 'Sunucu Bağlı';
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

    # 5. REGISTER.HTML
    register_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Kayıt Ol</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body style="align-items:center; justify-content:center;">
    <div class="auth-container" style="width: 100%;">
        <div class="brand-icon" style="margin-bottom:16px;">RT</div>
        <h2 style="margin-bottom:8px;">Hesap Oluştur</h2>
        <p style="font-size:13px; color:var(--text-secondary); margin-bottom:20px;">RT Store ekosistemine katılın</p>
        <form id="regForm">
            <div class="form-group">
                <label>Kullanıcı Adı</label>
                <input type="text" id="username" class="form-control" required>
            </div>
            <div class="form-group">
                <label>E-posta</label>
                <input type="email" id="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label>Şifre</label>
                <input type="password" id="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%; margin-top:10px;">Kayıt Ol</button>
        </form>
        <p style="margin-top:16px; font-size:13px; text-align:center;">Zaten hesabın var mı? <a href="login.html" style="color:var(--accent-color); text-decoration:none;">Giriş Yap</a></p>
    </div>
    <script src="assets/js/config.js"></script>
    <script>
        document.getElementById('regForm').addEventListener('submit', async (e) => {
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
            } catch(e) { alert('Sunucu bağlantı hatası!'); }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "register.html"), register_html)

    # 6. LOGIN.HTML
    login_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RT Store — Giriş Yap</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body style="align-items:center; justify-content:center;">
    <div class="auth-container" style="width: 100%;">
        <div class="brand-icon" style="margin-bottom:16px;">RT</div>
        <h2 style="margin-bottom:8px;">Oturum Aç</h2>
        <p style="font-size:13px; color:var(--text-secondary); margin-bottom:20px;">Hesabınızla giriş yapın</p>
        <form id="loginForm">
            <div class="form-group">
                <label>Kullanıcı Adı veya E-posta</label>
                <input type="text" id="usernameOrEmail" class="form-control" required>
            </div>
            <div class="form-group">
                <label>Şifre</label>
                <input type="password" id="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%; margin-top:10px;">Giriş Yap</button>
        </form>
        <p style="margin-top:16px; font-size:13px; text-align:center;">Hesabın yok mu? <a href="register.html" style="color:var(--accent-color); text-decoration:none;">Kayıt Ol</a></p>
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
            } catch(e) { alert('Sunucu bağlantı hatası!'); }
        });
    </script>
</body>
</html>
"""
    create_file(os.path.join(root, "login.html"), login_html)

    print("\n[+] Tüm dosyalar sıfırdan ve hatasız biçimde güncellendi.")

    # Git İşlemleri
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Fix: Icon rendering ve sunucu baglantisi duzeltildi"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[SUCCESS] GitHub'a başarıyla gönderildi!")
    except Exception as e:
        print(f"[UYARI] Git hatası: {e}")

if __name__ == "__main__":
    main()