const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, '../')));

// Örnek Veritabanı Belleği
const db = {
    users: [],
    apps: [
        { id: 1, name: 'RT Optimizer Pro', description: 'Gelişmiş sistem ve ağ hızlandırma aracı.', version: 'v3.2', category: 'Sistem' },
        { id: 2, name: 'RT Security Suite', description: 'Yerel ağ koruması ve güvenlik duvarı yöneticisi.', version: 'v1.0', category: 'Güvenlik' },
        { id: 3, name: 'RT AI Terminal', description: 'Yerel yapay zekâ entegrasyonlu komut istemcisi.', version: 'v2.1', category: 'Yapay Zekâ' }
    ]
};

// Kayıt Endpoint
app.post('/api/register', (req, res) => {
    const { username, email, password } = req.body;
    if (!username || !email || !password) {
        return res.status(400).json({ success: false, message: 'Tüm alanların doldurulması zorunludur.' });
    }
    if (password.length < 8 || password.length > 16) {
        return res.status(400).json({ success: false, message: 'Şifre 8 ile 16 karakter arasında olmalıdır.' });
    }
    
    const existing = db.users.find(u => u.email === email || u.username === username);
    if (existing) {
        return res.status(400).json({ success: false, message: 'Bu e-posta veya kullanıcı adı zaten kullanımda.' });
    }

    db.users.push({ username, email, password, verified: false });
    console.log(`[KAYIT BASARILI] Kullanıcı: ${username} (${email})`);
    res.json({ success: true, message: 'Kayıt başarılı! E-posta adresinize doğrulama bağlantısı gönderildi.' });
});

// Giriş Endpoint
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    const user = db.users.find(u => u.email === email && u.password === password);
    if (!user) {
        return res.status(401).json({ success: false, message: 'Geçersiz e-posta adresi veya şifre.' });
    }
    res.json({ success: true, message: 'Giriş başarılı.', user: { username: user.username, email: user.email } });
});

// Uygulama Listesi Endpoint
app.get('/api/apps', (req, res) => {
    res.json(db.apps);
});

// Geliştirici Başvuru Endpoint
app.post('/api/developer/apply', (req, res) => {
    const { appName, description } = req.body;
    console.log(`[GELİŞTİRİCİ BAŞVURU] Uygulama: ${appName}`);
    res.json({ success: true, message: 'Başvurunuz başarıyla alındı ve inceleme kuyruğuna eklendi.' });
});

app.listen(PORT, () => {
    console.log(`[RT-SERVER] Sunucu http://localhost:${PORT} adresinde aktif.`);
});
