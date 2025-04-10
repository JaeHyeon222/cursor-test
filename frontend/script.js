document.addEventListener('DOMContentLoaded', () => {
    const promptInput = document.getElementById('prompt');
    const generateBtn = document.getElementById('generate-btn');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error');
    const errorMessage = document.getElementById('error-message');
    const imageSection = document.getElementById('image-section');
    const generatedImage = document.getElementById('generated-image');

    // 현재 페이지의 호스트 IP 가져오기
    const currentHost = window.location.hostname;
    const API_URL = `http://${currentHost}:8000/api/v1/image/generate`;

    generateBtn.addEventListener('click', async () => {
        const prompt = promptInput.value.trim();
        if (!prompt) return;

        // UI 상태 초기화
        loadingDiv.style.display = 'block';
        errorDiv.style.display = 'none';
        imageSection.style.display = 'none';
        generateBtn.disabled = true;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ prompt: prompt }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Failed to generate image');
            }

            const data = await response.json();
            generatedImage.src = data.image_url;
            imageSection.style.display = 'block';
        } catch (error) {
            errorMessage.textContent = error.message;
            errorDiv.style.display = 'block';
        } finally {
            loadingDiv.style.display = 'none';
            generateBtn.disabled = false;
        }
    });
}); 