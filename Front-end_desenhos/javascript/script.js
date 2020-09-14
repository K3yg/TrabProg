$( document ).ready(function() {
  $("#link_listar_desenhos").click(function() {
    $.ajax({
      url: 'http://localhost:5000/listar_desenhos',
      method: 'GET',
      dataType: 'json',
      success: listar_desenhos, 
      error: function() {
          alert("erro ao ler dados, verifique o backend");
      }
  });

      function listar_desenhos (desenhos) {
        $('#corpoTabelaDesenhos').empty();
        for (var i in desenhos) { 
            lin = '<tr>' + 
            '<td>' + desenhos[i].nome + '</td>' + 
            '<td>' + desenhos[i].data_lancamento + '</td>' + 
            '<td>' + desenhos[i].criadores + '</td>' +
            '<td>' + desenhos[i].episodios + '</td>' + 
            '</tr>';
            $('#corpoTabelaDesenhos').append(lin);
    }}

     $("#btn_incluir_desenho").click(function(){
      nome = $("#nome").val();
      data_lancamento = $("#data_lancamento").val();
      criadores = $("#criadores").val();
      episodios = $("#episodios").val();
      dados = JSON.stringify({nome : nome, data_lancamento : data_lancamento, criadores : criadores, episodios : episodios});
      $.ajax({
        url: 'http://localhost:5000/incluir_desenho',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: dados,
        success: incluirDesenho,
        error: erroIncluirDesenho
      });

      function incluirDesenho(resposta){
        if (resposta.resultado == "bele"){
          alert("Desenho incluido com sucesso, obrigado!");
          $("#nome_desenho").val("");
          $("#data_lancamento").val("");
          $("#criadores").val("");
          $("#episodios").val("");
        } else {
          alert("Deu ruim!");
        }
      }
      function erroIncluirDesenho(resposta){
        alert("Deu ruim de novo, ve ai as coisa")
      }
    });
})});
