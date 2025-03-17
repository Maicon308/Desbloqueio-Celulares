function atualizaModelos() {
    var marca = document.getElementById("marca").value;
    fetch(`/obter_modelos/?marca=${marca}`)
        .then(response => response.json())
        .then(data => {
            var modeloSelect = document.getElementById("modelo");
            modeloSelect.innerHTML = "<option value=''>Selecione um modelo</option>";  // Reseta a lista de modelos

            data.modelos.forEach(function(modelo) {
                var option = document.createElement("option");
                option.value = modelo;
                option.textContent = modelo;
                modeloSelect.appendChild(option);
            });
        });
}
