const API_BASE_URL = "http://127.0.0.1:5000";

export async function getSummary() {
    const response = await fetch(`${API_BASE_URL}/api/summary`);
    if (!response.ok) {
        throw new Error("Failed to fetch summary");
    }
    return await response.json();
}

export async function getAnalytics() {
    const response = await fetch(`${API_BASE_URL}/api/analytics`);
    if (!response.ok) throw new Error("Failed to fetch analytics");
    return await response.json();
}
 
export async function getDetections() {
    const response = await fetch(`${API_BASE_URL}/api/detections`);
    if (!response.ok) throw new Error("Failed to fetch detections");
    return await response.json();
}