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