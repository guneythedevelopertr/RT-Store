document.addEventListener("DOMContentLoaded", async () => {
    const appList = document.getElementById("app-list");
    const apiMessage = document.getElementById("api-message");

    try {
        const apps = await window.RT_API.getApps();
        if (apps.length === 0) {
            apiMessage.textContent = "Henüz yayınlanmış uygulama bulunmuyor.";
            return;
        }

        appList.innerHTML = "";
        apps.forEach(app => {
            const card = document.createElement("div");
            card.className = "app-card";
            card.innerHTML = `
                <h3>${app.name}</h3>
                <p>${app.description || "Açıklama bulunmuyor."}</p>
                <span style="font-size: 12px; color: var(--blue); font-weight: 600;">Sürüm: ${app.version || "1.0"}</span>
            `;
            appList.appendChild(card);
        });
    } catch (err) {
        apiMessage.textContent = "Uygulamalar yüklenirken bir hata oluştu.";
        console.error(err);
    }
});
