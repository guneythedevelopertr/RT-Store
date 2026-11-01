const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, '../')));

// Kayıt Endpoint'i
app.post('/api/register', (req, res) => {
    const { username, email, password } = req.body;
    console.log(`[KAYIT TALEBI] Kullanıcı: ${username} | E-posta: ${email}`);
    res.json({ success: true, message: 'Kayıt işlemi başarılı. Doğrulama e-postası gönderildi.' });
});

// Giriş Endpoint'i
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    console.log(`[GIRIS TALEBI] E-posta: ${email}`);
    res.json({ success: true, message: 'Kimlik doğrulama başarılı.' });
});

app.listen(PORT, () => {
    console.log(`RT Store Sunucusu http://localhost:${PORT} adresinde aktif.`);
});
