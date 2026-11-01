const express = require('express');
const cors = require('cors');
const ngrok = require('@ngrok/ngrok');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Bellek tabanlı geçici kullanıcı veritabanı simülasyonu
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
    res.json({ status: 'success', message: 'Kayıt başarılı.', token: 'mock-jwt-token-' + username });
});

app.post('/api/login', (req, res) => {
    const { usernameOrEmail, password } = req.body;
    const user = users.find(u => (u.username === usernameOrEmail || u.email === usernameOrEmail) && u.password === password);
    if (!user) {
        return res.status(401).json({ status: 'error', message: 'Geçersiz kullanıcı adı veya şifre.' });
    }
    console.log('Kullanıcı giriş yaptı:', user.username);
    res.json({ status: 'success', message: 'Giriş başarılı.', token: 'mock-jwt-token-' + user.username });
});

app.listen(PORT, async () => {
    console.log('RT Store sunucusu ' + PORT + ' portunda çalışıyor.');
    try {
        await ngrok.authtoken('3LUnB99ES0TT0R5QPfokIxlnz2n_7beKyZMdHP8sFziwJQJSj');
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'sauciness-aerobics-boxcar.ngrok-free.dev'
        });
        console.log('Tünel aktif: ' + listener.url());
    } catch (err) {
        console.error('Tünel başlatılamadı:', err.message);
    }
});