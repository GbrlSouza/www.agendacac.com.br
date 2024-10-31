document.getElementById('agendamentoForm').onsubmit = function (event) {
    event.preventDefault();

    const data = document.getElementById('data').value;
    const nome = document.getElementById('nome').value;
    const contato = document.getElementById('contato').value;
    const informacoes = document.getElementById('informacoes').value;

    axios.post('/agendar', { data, nome, contato, informacoes })
        .then(response => {
            alert('Agendamento realizado com sucesso!');
            atualizarCalendario();
        })
        .catch(error => {
            console.error('Erro ao agendar:', error);
        });
};

function atualizarCalendario() {
    axios.get('/calendario')
        .then(response => {
            const calendarioDiv = document.getElementById('calendario');
            calendarioDiv.innerHTML = '';

            response.data.forEach(agendamento => {
                const div = document.createElement('div');
                div.innerHTML = `${agendamento.data}: ${agendamento.nome} (${agendamento.contato}) - ${agendamento.informacoes}`;
                calendarioDiv.appendChild(div);
            });
        })
        .catch(error => {
            console.error('Erro ao carregar calendário:', error);
        });
}

window.onload = atualizarCalendario;
