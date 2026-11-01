document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value.trim();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                alert('Hata: Girilen şifreler birbiriyle uyuşmuyor.');
                return;
            }

            if (password.length < 8 || password.length > 16) {
                alert('Hata: Şifre 8 ile 16 karakter arasında olmalıdır.');
                return;
            }

            try {
                const response = await fetch('http://localhost:3000/api/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, email, password })
                });
                const result = await response.json();
                alert(result.message || 'İşlem tamamlandı.');
            } catch (error) {
                console.error('Bağlantı Hatası:', error);
                alert('Sunucuyla iletişim kurulamadı.');
            }
        });
    }
});
