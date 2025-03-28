<template>
  <div class="about">
    <h1>Sobre o Projeto</h1>
    <section class="content">
      <h2>Prova de Recrutamento e Seleção - Global Tech Holding</h2>
      <p>
        Este projeto foi desenvolvido como parte da <strong>Prova de Recrutamento e Seleção</strong> da
        Global Tech Holding. O objetivo foi criar uma aplicação web que gerencia uma entidade
        "Pessoa", permitindo ao usuário realizar operações de inclusão, alteração, exclusão e
        pesquisa de dados, tudo isso utilizando tecnologias modernas e seguindo as orientações
        fornecidas.
      </p>

      <h3>Descrição do Projeto</h3>
      <p>
        A aplicação é composta por um backend construído com <strong>Django</strong> e
        <strong>Django REST Framework (DRF)</strong>, utilizando um banco de dados
        <strong>PostgreSQL</strong> para persistência. O frontend foi implementado com
        <strong>Vue.js 3</strong>, atendendo ao requisito de separação entre cliente e servidor e
        utilizando <strong>HTML5</strong> para a interface. Embora a preferência mencionada fosse
        Angular, optei pelo Vue.js devido à sua leveza e facilidade de integração com APIs REST.
      </p>

      <h3>Requisitos Atendidos</h3>
      <ul>
        <li>
          <strong>Interface Web:</strong> Uma tela permite ao usuário informar dados como nome,
          data de nascimento, CPF, sexo, altura e peso, com máscaras para CPF e data.
        </li>
        <li>
          <strong>Botões de Ação:</strong> Inclui botões "Incluir", "Alterar", "Excluir" e
          "Pesquisar", todos integrados ao servidor via chamadas REST. "Alterar" e "Excluir" estão
          disponíveis após a lista ser carregada ou pesquisada.
        </li>
        <li>
          <strong>ID Auto-incrementado:</strong> O campo ID é gerado automaticamente pelo Django.
        </li>
        <li>
          <strong>Arquitetura REST:</strong> As chamadas são feitas em JSON, com um controller
          (`PersonViewSet`) que utiliza uma classe de serviço (`PersonService`) para processar os
          dados. A persistência é feita via ORM do Django.
        </li>
      </ul>

      <h3>Ponto Extra</h3>
      <p>
        Como funcionalidade extra, foi implementado o botão "Peso Ideal" na tela principal. Ao
        selecionar uma pessoa na lista e clicar no botão, o sistema envia uma requisição ao
        servidor, que calcula o peso ideal com base na fórmula fornecida:
      </p>
      <ul>
        <li>Para homens: <code>(72.7 * altura) - 58</code></li>
        <li>Para mulheres: <code>(62.1 * altura) - 44.7</code></li>
      </ul>
      <p>O resultado é exibido em um popup simples no frontend.</p>

      <h3>Tecnologias Utilizadas</h3>
      <ul>
        <li><strong>Backend:</strong> Django, Django REST Framework, PostgreSQL</li>
        <li><strong>Frontend:</strong> Vue.js 3, Vite, Axios</li>
        <li><strong>Ambiente:</strong> Docker, VSCode</li>
      </ul>

      <h3>Considerações Finais</h3>
      <p>
        O projeto foi desenvolvido em um ambiente Dockerizado, com o backend e frontend rodando em
        containers separados, e segue as orientações de prazo (8 horas) e ambiente (VSCode,
        PostgreSQL). Dois vídeos serão gravados conforme solicitado: um demonstrando a aplicação do
        ponto de vista do usuário e outro explicando o código fonte do client e server.
      </p>
    </section>
  </div>
</template>

<style scoped>
.about {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  color: #676c73;
  margin-bottom: 2rem;
}

h2 {
  color: #0f73ff;
  margin-top: 2rem;
}

h3 {
  color: #333;
  margin-top: 1.5rem;
}

p {
  line-height: 1.6;
  color: #555;
}

ul {
  list-style-type: disc;
  padding-left: 20px;
  margin: 1rem 0;
}

li {
  margin-bottom: 0.5rem;
  color: #555;
}

code {
  background-color: #f0f0f0;
  padding: 2px 6px;
  border-radius: 3px;
}

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .content {
    max-width: 800px;
  }
}
</style>