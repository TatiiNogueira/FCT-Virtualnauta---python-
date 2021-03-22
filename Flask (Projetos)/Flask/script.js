                                        //Links que utilizei\\
//https://jsfiddle.net/x51u6aw4/7/
//https://pt.stackoverflow.com/questions/49581/criar-tabela-din%C3%A2mica-em-js-para-utilizar-em-html

//NOTAS:
//appendChild - Siginifica adicionar no fim se o valor indicado por appendChild já existir ele coloca o valor no final
//ou seja muda o de lugar 


//////////////////////////////////////////////////////////////////////
//Linha 20 - Menssagem json - É onde irá ficar os valores que iremos ver da tabela

//Dados para introduzir na tabela
var dados = [];

//Função criar tabela
function CreateTable(){
    //Pedido
    var data = [];
    //Menssagem json
    var message = JSON.parse('{"nome":"Teste"}');
    var req = new XMLHttpRequest();
    //Metodo(GET,POST,...) e o link 
    req.open("GET", "http://127.0.0.1:5000/TodosRegistos");
    req.setRequestHeader("Content-Type", "application/json");
    req.addEventListener("load", function() {
        if (req.status == 200) {
            let user = JSON.parse(req.responseText);
            data = user
            console.log(user)
        } else {
            console.log(req.status)
        }
    });
    req.send(JSON.stringify(message));

    //Criar a tabela
    var novaTabela = document.createElement("table");
    //table.className="gridtable";
    //Criar os Elementos
    var thead = document.createElement("thead");
    var tbody = document.createElement("tbody");
    var headRow = document.createElement("tr");
    //Nome das colunas - Temos de inserir manualmente
    ["Titulo","Grador","Categoria","Descricao","Data","Sala","ImagemID"].forEach(function(el) {
      //Criar Elemento
      var th=document.createElement("th");
      th.appendChild(document.createTextNode(el));
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);
    novaTabela.appendChild(thead); 
    data.forEach(function(el) {
      //Criar Elemento
      var tr = document.createElement("tr");
      for (var o in el) {  
        //Criar Elemento
        var td = document.createElement("td");
        td.appendChild(document.createTextNode(el[o]))
        tr.appendChild(td);
      }
      tbody.appendChild(tr);  
    });
    novaTabela.appendChild(tbody);
    return novaTabela;
}

window.onload=function() {
    //Encontrar a tabela através do id que está no ficheiro Home.html
    document.getElementById("Table").appendChild(CreateTable());
}