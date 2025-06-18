document.addEventListener('DOMContentLoaded', async () => {
    let crypto_db = {};

    // Fetch data from backend
    async function fetchCryptoData() {
        const res = await fetch('/api/crypto-data');
        crypto_db = await res.json();
    }
    await fetchCryptoData();

    // Handle side-nav
    document.querySelectorAll('.side-item').forEach(item => {
        item.addEventListener('click', async () => {
            document.querySelectorAll('.side-item').forEach(el => el.classList.remove('active'))
            item.classList.add('active')

            const view = item.dataset.view;
            document.querySelectorAll('.data-view, .chat-area').forEach(el => el.style.display = 'none')

            if (view === 'chat') {
                document.querySelector('.chat-area').style.display = 'flex';
            } else {
                document.querySelector(`#${view}View`).style.display = 'block';
                if (view === 'trends') renderTrendsChart(crypto_db);
                if (view === 'sustainability') renderSustainabilityCards(crypto_db);
                if (view === 'risk') renderRiskMatrix(crypto_db);
            }
        })
    });

    // Handle chat messages
    document.getElementById('sendBtn').addEventListener('click', sendMessage);
    document.getElementById('userInput').addEventListener('keypress', e => {
        if (e.key === 'Enter') sendMessage();
    });

    async function sendMessage() {
        const query = document.getElementById('userInput').value.trim();
        if (!query) return;

        addMessage(query, 'user');
        document.getElementById('userInput').value = '';
        const res = await fetch('/chat', {
            method:'POST',
            headers:{'Content-Type':'application/x-www-form-urlencoded'},
            body:`query=${encodeURIComponent(query)}`
        });
        const data = await res.json();

        addMessage(data.message, 'bot');
        if (data.coinData) {
            display_coin_card(data.coinData);
        }
    }

    function addMessage(text, sender) {
        const message = document.createElement('div');
        message.classList.add('message', `${sender}-message`);
        message.textContent = text;
        document.getElementById('messageContainer').appendChild(message);
        message.scrollIntoView();
    }

    function display_coin_card(coin) {
        const card = document.createElement('div');
        card.classList.add('coin-card');
        card.innerHTML = `
            <div class="coin-header">
                <span>${coin.name}</span> ${coin.recommended ? '⭐ Recommended' : '' }
            </div>
            <div class="metrics">
                <div>📈 Trend: ${coin.price_trend}</div>
                <div>🌱 Sustainability: ${coin.sustainability_score}/10</div>
                <div>💼 Market Cap: ${coin.market_cap}</div>
                <div>⚡ Energy Use: ${coin.energy_use}</div>
            </div>`;
        document.getElementById('messageContainer').appendChild(card);
    }

    function renderTrendsChart(crypto) {
        const ctx = document.getElementById('trendsChart').getContext('2d');
        new Chart(ctx, {
            type:'bar',
            data:{
                labels:Object.keys(crypto),
                datasets:[
                    {
                        label:'Sustainability Score',
                        data:Object.keys(crypto).map(k => crypto[k].sustainability_score * 10),
                        backgroundColor:'rgba(46, 204, 113, 0.7)'
                    }
                ]
            },
            options:{responsive:true, scales:{y:{beginAtZero:true, max:10}}}
        })
    }

    function renderSustainabilityCards(crypto) {
        const container = document.getElementById('sustainabilityCards');
        container.innerHTML = '';
        Object.entries(crypto)
            .sort((a, b) => b[1].sustainability_score - a[1].sustainability_score)
            .forEach(([coin, data]) => {
                const card = document.createElement('div');
                card.classList.add('coin-card');
                card.innerHTML = `
                    <div class="coin-header">
                        <span>${coin}</span> ${data.sustainability_score * 10}/10
                    </div>
                    <div>📈 ${data.price_trend}</div>
                    <div>💼 Market Cap: ${data.market_cap}</div>
                    <div>⚡ Energy: ${data.energy_use}</div>`;
                container.appendChild(card);
            });
    }

    function renderRiskMatrix(crypto) {
        const ctx = document.getElementById('riskChart').getContext('2d');
        new Chart(ctx, {
            type:'scatter',
            data:{datasets:[{
                label:'Cryptocurrencies',
                data:Object.entries(crypto).map(([coin, data]) => ({
                    x: data.sustainability_score * 10,
                    y: data.risk_level==='low'? 3 : data.risk_level==='medium'? 6 : 9,
                    name: coin
                }))
            }]},
            options:{scales:{x:{min:0,max:10},y:{min:0,max:10}},
                plugins:{tooltip:{callbacks:{label:c=>c.raw.name}}}}

        })
    }
});
