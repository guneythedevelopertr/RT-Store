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