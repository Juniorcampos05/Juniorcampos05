function showMessage(resposta) {
    const messageElement = document.getElementById('message');
    
    if (resposta === 'sim') {
        messageElement.textContent = 'Seja bem vindo ao Elementor Dev  💻';
    } else if (resposta === 'não') {
        messageElement.textContent = 'Obrigado pela sua passagem pelo meu instagram 👍';
    }
    
}
