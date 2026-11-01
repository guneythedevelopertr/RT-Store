const express = require('express');
const cors = require('cors');
const path = require('path');
const ngrok = require('@ngrok/ngrok');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Örnek API Uç Noktası
app.get('/api/health', (req, res) => {
    res.json({ status: 'success', message: 'RT Store API aktif ve calisiyor!' });
});

app.listen(PORT, async () => {
    console.log(RT Store sunucusu \ portunda calisiyor...);
    try {
        const listener = await ngrok.forward({
            addr: PORT,
            domain: 'clapped-outrank-triangle.ngrok-free.dev'
        });
        console.log(📱 RT Store dis dunyada yayinda: \);
    } catch (err) {
        console.error('Ngrok tuneli baslatilamadi:', err.message);
    }
});
