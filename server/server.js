const express = require('express');
const cors = require('cors');
const path = require('path');
const ngrok = require('@ngrok/ngrok');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
    res.json({ status: 'success', message: 'RT Store API aktif ve calisiyor!' });
});

app.listen(PORT, async () => {
    console.log('RT Store sunucusu ' + PORT + ' portunda calisiyor...');
    try {
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'sauciness-aerobics-boxcar.ngrok-free.dev'
        });
        console.log('📱 RT Store dis dunyada yayinda: ' + listener.url());
    } catch (err) {
        console.error('Ngrok tuneli baslatilamadi:', err.message);
    }
});