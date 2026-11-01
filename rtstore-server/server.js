const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const { DatabaseSync } = require("node:sqlite");
const { exec } = require("node:child_process");

const ROOT = path.resolve(__dirname, "..");
const DB_PATH = path.join(__dirname, "rtstore.db");
const PORT = 5000;

const db = new DatabaseSync(DB_PATH);
const server = http.createServer((req, res) => {
    const url = new URL(req.url, `http://localhost:${PORT}`);

    res.setHeader("X-Content-Type-Options", "nosniff");

    if (url.pathname === "/api/health") {
        return sendJson(res, 200, { status: "ok", name: "RT Store" });
    }

    if (url.pathname === "/api/apps") {
        try {
            const apps = db.prepare(`
                SELECT id, name, slug, description, category, version, created_at
                FROM apps
                WHERE is_published = 1
                ORDER BY created_at DESC
            `).all();

            return sendJson(res, 200, apps);
        } catch (error) {
            console.error("Veritabanı sorgu hatası:", error.message);
            return sendJson(res, 500, { error: "Uygulamalar alınamadı." });
        }
    }

    if (req.method !== "GET" && req.method !== "HEAD") {
        return sendJson(res, 405, { error: "Method not allowed" });
    }

    let safePath = decodeURIComponent(url.pathname);
    if (safePath === "/" || safePath === "") safePath = "/index.html";

    // Dosya yolunu proje kök dizinine göre tam ve güvenli bir şekilde birleştiriyoruz
    const filePath = path.join(ROOT, safePath);

    console.log(`[İSTEK] ${url.pathname} -> ${filePath}`);

    fs.readFile(filePath, (error, data) => {
        if (error) {
            console.error(`[HATA] Bulunamadı: ${filePath}`);
            return sendJson(res, 404, { error: "Dosya bulunamadı." });
        }

        const ext = path.extname(filePath).toLowerCase();
        const types = {
            ".html": "text/html; charset=utf-8",
            ".css": "text/css; charset=utf-8",
            ".js": "text/javascript; charset=utf-8",
            ".json": "application/json; charset=utf-8",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".svg": "image/svg+xml",
            ".webp": "image/webp",
            ".ico": "image/x-icon"
        };

        res.writeHead(200, {
            "Content-Type": types[ext] || "application/octet-stream"
        });
        res.end(req.method === "HEAD" ? undefined : data);
    });
});

function sendJson(res, status, data) {
    res.writeHead(status, { "Content-Type": "application/json; charset=utf-8" });
    res.end(JSON.stringify(data));
}

server.listen(PORT, "127.0.0.1", () => {
    console.log(`RT Store sunucusu ${PORT} portunda çalışıyor.`);
    console.log(`Kök Dizin: ${ROOT}`);
    const address = `http://127.0.0.1:${PORT}`;
    setTimeout(() => {
        exec(`start "" "${address}"`);
    }, 700);
});

process.on("SIGINT", () => {
    db.close();
    server.close(() => process.exit(0));
});
