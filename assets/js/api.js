window.RT_API = {
  async getApps() {
    const response = await fetch(`${window.RT_CONFIG.API_BASE_URL}/apps`);
    if (!response.ok) throw new Error("Uygulamalar alınamadı.");
    return response.json();
  }
};
