document.addEventListener('DOMContentLoaded', () => {
    const apiBase = window.RT_CONFIG ? window.RT_CONFIG.API_URL : 'http://localhost:3000/api';

    function showToast(message) {
        let toast = document.createElement('div');
        toast.className = 'rt-toast';
        toast.textContent = message;
        document.body.appendChild(toast);
        setTimeout(() => toast.classList.add('show'), 50);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // Kayıt Formu İşlemleri
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                showToast('Hata: Girilen şifreler uyuşmuyor.');
                return;
            }
            if (password.length < 8 || password.length > 16) {
                showToast('Hata: Şifre 8 ile 16 karakter arasında olmalıdır.');
                return;
            }

            try {
                const res = await fetch(`${apiBase}/register`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const data = await res.json();
                showToast(data.message);
                if (res.ok) {
                    setTimeout(() => window.location.href = 'login.html', 2000);
                }
            } catch (err) {
                showToast('Sunucu bağlantı hatası.');
            }
        });
    }

    // Giriş Formu İşlemleri
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;

            try {
                const res = await fetch(`${apiBase}/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                const data = await res.json();
                showToast(data.message);
                if (res.ok) {
                    localStorage.setItem('rt_user', JSON.stringify(data.user));
                    setTimeout(() => window.location.href = 'index.html', 1500);
                }
            } catch (err) {
                showToast('Sunucu bağlantı hatası.');
            }
        });
    }

    // Uygulama Kataloğunu Yükleme
    const appGrid = document.getElementById('app-grid');
    if (appGrid) {
        fetch(`${apiBase}/apps`)
            .then(res => res.json())
            .then(apps => {
                appGrid.innerHTML = '';
                apps.forEach(app => {
                    const card = document.createElement('div');
                    card.className = 'card';
                    card.innerHTML = `
                        <h3>${app.name}</h3>
                        <p>${app.description}</p>
                        <small>Sürüm: ${app.version} | Kategori: ${app.category}</small>
                        <br><br>
                        <button class="btn-primary" onclick="alert('${app.name} indiriliyor...')">İndir</button>
                    `;
                    appGrid.appendChild(card);
                });
            })
            .catch(() => {
                appGrid.innerHTML = '<p>Uygulamalar yüklenirken bir hata oluştu.</p>';
            });
    }
});
