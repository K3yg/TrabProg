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
            lin = '<tr id="linha_'+desenhos[i].id+'">' +
            '<td>' + desenhos[i].nome + '</td>' + 
            '<td>' + desenhos[i].data_lancamento + '</td>' + 
            '<td>' +  desenhos[i].criadores + '</td>' +
            '<td>' + desenhos[i].episodios + '</td>' + 
            '<td> <a href=# id="excluir_' + desenhos[i].id + '" ' +
                  'class="excluir_desenho"><img style="widht:30px; height:30px;" src="images/excluir.png" '+
                  'alt="Excluir desenho" title="Excluir desenho"></a>' + 
                '</td>' + 
            '</tr>';
            $('#corpoTabelaDesenhos').append(lin);
    }}

    $(document).on("click", ".excluir_desenho", function() {
      var componente_clicado = $(this).attr('id');  
      var nome_icone = "excluir_";
      var id_desenho = componente_clicado.substring(nome_icone.length);
      $.ajax({
          url: 'http://localhost:5000/excluir_desenho/'+id_desenho,
          type: 'DELETE', 
          dataType: 'json', 
          success: desenhoExcluido, 
          error: erroAoExcluir
      });

      function desenhoExcluido (retorno) {
          if (retorno.resultado == "ok") { 
              $("#linha_" + id_desenho).fadeOut(10, function(){
                  alert("Sucesso!");
              });
          } else {
              alert(retorno.resultado + ":" + retorno.detalhes);
          }            
      }
      function erroAoExcluir (retorno) {
          alert("erro ao excluir dados, verifique o backend: ");
      }
  });

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
